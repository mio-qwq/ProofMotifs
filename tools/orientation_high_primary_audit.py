#!/usr/bin/env python3
"""High-primary replay of the production orientation constructor.

The constructor under test receives only (p, coefficient list, supplied u).
Known roots manufacture fixtures and independently audit its returned tensor;
they are not an independent constructor and are never passed to production.
Run from the repository, or pass --repo /absolute/path/to/ProofMotifs.
No files, external services, random choices, or p-sized loops are used.
"""
import argparse
import json
import math
from pathlib import Path
import sys

sys.dont_write_bytecode = True


def poly_mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] = (out[i+j] + x*y) % p
    return out


def from_roots(roots, p):
    f = [1]
    for x in roots:
        f = poly_mul(f, [-x % p, 1], p)
    return f


def uni_value(a, x, p):
    out = 0
    for coefficient in reversed(a):
        out = (out*x + coefficient) % p
    return out


def tensor_value(a, n, x, y, p):
    # Independent nested Horner evaluation of the returned power-basis tensor.
    out = 0
    for i in reversed(range(n)):
        row = uni_value(a[n*i:n*(i+1)], y, p)
        out = (out*x + row) % p
    return out


def replay(module, roots, expected_masks):
    p, u, n = 65537, 3, len(roots)
    f = from_roots(roots, p)
    counters = {"tensor_multiply": 0, "tensor_power": 0, "max_power_bits": 0}
    original_multiply, original_power = module.Tensor.multiply, module.Tensor.power

    def counted_multiply(self, a, b):
        counters["tensor_multiply"] += 1
        return original_multiply(self, a, b)

    def counted_power(self, a, exponent):
        counters["tensor_power"] += 1
        counters["max_power_bits"] = max(counters["max_power_bits"], exponent.bit_length())
        return original_power(self, a, exponent)

    module.Tensor.multiply, module.Tensor.power = counted_multiply, counted_power
    try:
        # This is the ONLY constructor call; no roots/evaluation callback supplied.
        out = module.construct(p, f, u)
    finally:
        module.Tensor.multiply, module.Tensor.power = original_multiply, original_power

    assert out["modulus"] == f
    assert out["digit_levels"] == 16
    assert out["maximum_nonempty_masks"] == expected_masks <= n*(n-1)
    assert counters["max_power_bits"] <= 17
    e = out["orientation"]
    assert len(e) == n*n
    grid = [[tensor_value(e, n, x, y, p) for y in roots] for x in roots]
    assert all(grid[i][i] == 0 for i in range(n))
    assert all(grid[i][j] in (0, 1) for i in range(n) for j in range(n))
    assert all(grid[i][j] + grid[j][i] == 1
               for i in range(n) for j in range(i+1, n))
    rows = [sum(row) for row in grid]
    assert len(set(rows)) > 1 and sum(rows) == n*(n-1)//2
    assert len(out["partial_trace"]) <= n
    assert [uni_value(out["partial_trace"], x, p) for x in roots] == rows
    chosen = [x for x, degree in zip(roots, rows) if degree == out["label"]]
    other = [x for x, degree in zip(roots, rows) if degree != out["label"]]
    assert chosen and other
    expected = from_roots(chosen, p)
    assert out["factor"] == expected
    assert poly_mul(expected, from_roots(other, p), p) == f
    assert out["primary_generator_discovery"] == "NOT performed"
    assert out["primehood"] == "input promise"
    return {"p": p, "N": n, "fixture_roots_not_constructor_input": roots,
            "modulus": f, "u": u, "digit_levels": out["digit_levels"],
            "maximum_nonempty_masks": out["maximum_nonempty_masks"],
            "row_counts": rows, "factor_label": out["label"],
            "factor": expected, "counters": counters}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    sys.path.insert(0, str(args.repo.resolve()/"tools"))
    import orientation_readout

    # Audit-only Lucas certificate: (65537-1)=2^16 is completely factored.
    # This is outside production, whose p is only promised prime.
    assert pow(3, 65536, 65537) == 1
    assert math.gcd(pow(3, 32768, 65537)-1, 65537) == 1
    results = [replay(orientation_readout, [1, 2, 3, 4, 5, 6], 10),
               replay(orientation_readout, [1, 2, 4, 8, 16, 32], 30)]
    print(json.dumps({"status": "PASS", "independence": "independent grid oracle, production constructor under test",
                      "fixtures": results}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

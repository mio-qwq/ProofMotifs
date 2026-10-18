"""Exact normal-character basecases, using standalone F3 arithmetic.

No field enumeration and no general single-orbit sufficiency assertion.
The degree-four exclusion is a polynomial gcd and annihilator certificate.
The degree-five/eight examples are direct normal-character witnesses.
"""
import argparse
import json
from math import gcd
from pathlib import Path

SCOPE = {
    "nonexistence_degrees": [4],
    "existence_degrees": [5, 8],
    "field_enumeration_used": False,
    "all_normal_seeds_connected_claimed": False,
    "single_orbit_full_rank_claimed": False,
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([((a[i] if i < len(a) else 0)
                  + (b[i] if i < len(b) else 0)) % 3
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c * v % 3 for v in a])


def mul(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] = (out[i + j] + v * w) % 3
    return trim(out)


def divrem(a, b):
    require(bool(b), "zero polynomial divisor")
    a = trim(a)
    out = [0] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        shift = len(a) - len(b)
        c = a[-1] * b[-1] % 3
        out[shift] = c
        for j, v in enumerate(b):
            a[shift + j] = (a[shift + j] - c * v) % 3
        a = trim(a)
    return trim(out), a


def power(a, e, modulus):
    out = [1]
    while e:
        if e & 1:
            out = divrem(mul(out, a), modulus)[1]
        a = divrem(mul(a, a), modulus)[1]
        e //= 2
    return out


def xgcd(a, b):
    s0, s1, t0, t1 = [1], [], [], [1]
    while b:
        q, r = divrem(a, b)
        a, b = b, r
        s0, s1 = s1, add(s0, scale(mul(q, s1), 2))
        t0, t1 = t1, add(t0, scale(mul(q, t1), 2))
    c = a[-1] if a else 1
    return scale(a, c), scale(s0, c), scale(t0, c)


def prime_factors(n):
    out, p = [], 2
    while p * p <= n:
        if n % p == 0:
            out.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        out.append(n)
    return out


def rank(columns, m):
    """Column elimination, independent of project field/rank implementations."""
    pivots = {}
    for col in columns:
        a = col + [0] * (m - len(col))
        for j in sorted(pivots):
            if a[j]:
                c = a[j]
                a = [(v - c * w) % 3 for v, w in zip(a, pivots[j])]
        j = next((j for j, v in enumerate(a) if v), None)
        if j is not None:
            pivots[j] = [v * a[j] % 3 for v in a]
    return len(pivots)


def chi(v, q, modulus):
    if not v:
        return 0
    out = power(v, (q - 1) // 2, modulus)
    require(out in ([1], [2]), "character escaped prime field")
    return 1 if out == [1] else -1


def monomial(degree, coefficient=1):
    return [0] * degree + [coefficient]


def degree_four_inputs():
    h = add(monomial(81), [0, 2])
    x40 = monomial(40)
    return [h, add(power([1, 1], 40, h), scale(x40, 2)),
            add(power([2, 1], 40, h), scale(x40, 2))]


def degree_four_certificate():
    inputs = degree_four_inputs()
    d, a, b = xgcd(inputs[0], inputs[1])
    g, c, e = xgcd(d, inputs[2])
    g6 = [1, 0, 1, 0, 1, 0, 1]
    g12 = divrem(g, g6)[0]
    linearized = add(add(monomial(27), monomial(9, 2)),
                     add(monomial(3), [0, 2]))
    return {
        "gcd": g,
        "bezout": [mul(c, a), mul(c, b), e],
        "quotients": [divrem(p, g)[0] for p in inputs],
        "subfield_factor": g6,
        "other_factor": g12,
        "subfield_quotient": divrem(add(monomial(9), [0, 2]), g6)[0],
        "linearized_quotient": divrem(linearized, g12)[0],
        "character_pattern_count": 18,
        "normal_pattern_count": 0,
    }


def witness(m, modulus, y, seed):
    q = 3 ** m
    conjugates = [power(y, 3 ** j, modulus) for j in range(m)]
    inv = power(y, q - 2, modulus)
    return {
        "m": m, "modulus": modulus, "y": y,
        "conjugates": conjugates, "conjugate_rank": rank(conjugates, m),
        "characters": [chi(add(y, [2]), q, modulus), chi(y, q, modulus),
                       chi(add(y, [1]), q, modulus)],
        "a": add([1], inv), "b": add([1], scale(inv, 2)),
        "gamma_seed_exponents": seed,
        "connectivity_index": gcd(gcd(seed[1], seed[2]), (q - 1) // 2),
    }


def build_report():
    return {"schema": 1, "scope": dict(SCOPE),
            "degree_four": degree_four_certificate(),
            "witnesses": [witness(5, [1, 2, 0, 0, 0, 1], [1, 1], [0, 89, 87]),
                          witness(8, [2, 0, 0, 1, 0, 0, 0, 0, 1],
                                  [1, 1, 1, 1], [0, 771, 35])]}


def polynomial(value, limit, name):
    require(isinstance(value, list) and len(value) <= limit
            and all(type(c) is int and c in (0, 1, 2) for c in value)
            and (not value or value[-1] != 0), "invalid polynomial: " + name)


def verify_report(report):
    require(report["schema"] == 1 and report["scope"] == SCOPE, "scope mismatch")
    cert = report["degree_four"]
    for key in ("gcd", "subfield_factor", "other_factor", "subfield_quotient",
                "linearized_quotient"):
        polynomial(cert[key], 82, key)
    for key in ("bezout", "quotients"):
        require(isinstance(cert[key], list) and len(cert[key]) == 3,
                "invalid gcd certificate vector")
        for p in cert[key]:
            polynomial(p, 82, key)
    g = cert["gcd"]
    require(len(g) == 19 and g[-1] == 1, "gcd degree or normalization")
    inputs = degree_four_inputs()
    total = []
    for p, a, q in zip(inputs, cert["bezout"], cert["quotients"]):
        require(mul(g, q) == p, "gcd divisibility failed")
        total = add(total, mul(a, p))
    require(total == g, "gcd Bezout identity failed")
    g6, g12 = cert["subfield_factor"], cert["other_factor"]
    require(len(g6) == 7 and len(g12) == 13 and mul(g6, g12) == g,
            "character-root factorization failed")
    require(mul(g6, cert["subfield_quotient"]) == add(monomial(9), [0, 2]),
            "subfield annihilator failed")
    linearized = add(add(monomial(27), monomial(9, 2)),
                     add(monomial(3), [0, 2]))
    require(mul(g12, cert["linearized_quotient"]) == linearized,
            "linearized annihilator failed")
    require(cert["character_pattern_count"] == 18
            and cert["normal_pattern_count"] == 0, "degree-four count mismatch")
    rows = report["witnesses"]
    require(isinstance(rows, list) and [r["m"] for r in rows] == [5, 8],
            "witness degree scope")
    receipts = []
    for row in rows:
        m, f, y = row["m"], row["modulus"], row["y"]
        q, n, x = 3 ** m, (3 ** m - 1) // 2, [0, 1]
        polynomial(f, m + 1, "modulus")
        polynomial(y, m, "y")
        require(len(f) == m + 1 and f[-1] == 1, "field modulus degree")
        require(power(x, q, f) == x, "Rabin Frobenius identity failed")
        for p in prime_factors(m):
            require(xgcd(f, add(power(x, 3 ** (m // p), f), scale(x, 2)))[0] == [1],
                    "Rabin proper factor exclusion failed")
        require(power(x, q - 1, f) == [1], "primitive order identity failed")
        for p in prime_factors(q - 1):
            require(power(x, (q - 1) // p, f) != [1], "primitive proper order")
        conjugates = [power(y, 3 ** j, f) for j in range(m)]
        require(row["conjugates"] == conjugates, "conjugate basis mismatch")
        require(row["conjugate_rank"] == rank(conjugates, m) == m,
                "normal conjugate rank failed")
        chars = [chi(add(y, [2]), q, f), chi(y, q, f), chi(add(y, [1]), q, f)]
        require(row["characters"] == chars and chars[0] != 0 and len(set(chars)) == 1,
                "three-character pattern failed")
        inv = power(y, q - 2, f)
        a, b = add([1], inv), add([1], scale(inv, 2))
        require(row["a"] == a and row["b"] == b and add(add([1], a), b) == [],
                "seed ratio identity failed")
        require(chi(a, q, f) == chi(b, q, f) == 1, "seed square condition failed")
        seed = row["gamma_seed_exponents"]
        require(isinstance(seed, list) and len(seed) == 3 and seed[0] == 0
                and all(type(v) is int and 0 <= v < n for v in seed)
                and len(set(seed)) == 3, "seed exponent scope failed")
        gamma = power(x, 2, f)
        require(power(gamma, seed[1], f) == a and power(gamma, seed[2], f) == b,
                "seed exponent identity failed")
        index = gcd(gcd(seed[1], seed[2]), n)
        require(row["connectivity_index"] == index == 1, "selected seed connectivity")
        receipts.append({"m": m, "conjugate_rank": m, "characters": chars,
                         "selected_seed_connectivity_index": index})
    return {"verified": True, "degree_four_pattern_count": 18,
            "degree_four_normal_pattern_count": 0, "witnesses": receipts,
            "scope": dict(SCOPE)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    if args.check:
        result = verify_report(json.loads(args.check.read_text()))
    else:
        result = build_report()
        verify_report(result)
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

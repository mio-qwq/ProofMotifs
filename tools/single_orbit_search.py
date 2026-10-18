"""Exact bounded single-orbit searches; no universal existence assertion.

Field elements use base-three coordinates and O(q) power/log lists. Polynomial
witness identities are checked by the pre-existing independent list arithmetic.
"""
import argparse
from collections import Counter
import hashlib
import json
from math import gcd
from pathlib import Path

if __package__:
    from .cyclic_incidence_certificate import (
        _add, _divrem, _mul, _neg, _powmod, _sparse, _xgcd,
        cyclic_orbit_pattern,
    )
else:
    from cyclic_incidence_certificate import (
        _add, _divrem, _mul, _neg, _powmod, _sparse, _xgcd,
        cyclic_orbit_pattern,
    )

MODULI = {
    3: [1, 2, 0, 1], 4: [2, 1, 0, 0, 1],
    5: [1, 2, 0, 0, 0, 1], 6: [2, 1, 0, 0, 0, 0, 1],
    7: [1, 2, 1, 0, 0, 0, 0, 1],
    8: [2, 0, 0, 1, 0, 0, 0, 0, 1],
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def prime_factors(n):
    factors, p = [], 2
    while p * p <= n:
        if n % p == 0:
            factors.append(p)
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


class CompactField:
    """A full nonzero primitive-x cycle certifies the quotient is a field."""
    def __init__(self, m, modulus=None):
        require(m in MODULI, "unsupported bounded degree")
        self.m, self.q = m, 3 ** m
        self.n = (self.q - 1) // 2
        self.modulus = list(MODULI[m] if modulus is None else modulus)
        require(len(self.modulus) == m + 1 and self.modulus[-1] == 1
                and all(type(c) is int and c in (0, 1, 2) for c in self.modulus),
                "invalid field modulus")
        self.weights = [3 ** i for i in range(m)]
        self.powers, self.logs = [], {}
        value = 1
        for exponent in range(self.q - 1):
            require(value != 0 and value not in self.logs,
                    "primitive-x cycle repeats prematurely")
            self.logs[value] = exponent
            self.powers.append(value)
            top = value // self.weights[-1]
            value = (value % self.weights[-1]) * 3
            for i, coefficient in enumerate(self.modulus[:-1]):
                old = value // self.weights[i] % 3
                value += ((old - top * coefficient) % 3 - old) * self.weights[i]
        require(value == 1, "primitive-x cycle does not close")
        self.squares = self.powers[::2]
        self.square_logs = {value: i for i, value in enumerate(self.squares)}

    def add(self, a, b):
        return sum(((a // w + b // w) % 3) * w for w in self.weights)

    def negative_one_minus(self, a):
        return sum(((-(1 if i == 0 else 0) - a // w % 3) % 3) * w
                   for i, w in enumerate(self.weights))

    def trace(self, a):
        if not a:
            return 0
        exponent, result = self.logs[a], 0
        for j in range(self.m):
            result = self.add(result, self.powers[exponent * 3 ** j % (self.q - 1)])
        require(result in (0, 1, 2), "trace escaped prime field")
        return result

    def seed_root_exponents(self, seed):
        _, i, j = seed
        return [k for k in range(self.n)
                if self.negative_one_minus(self.squares[i * k % self.n])
                == self.squares[j * k % self.n]]

    def normalized_orbits(self):
        representatives = set()
        for i, a in enumerate(self.squares):
            b = self.negative_one_minus(a)
            if b not in self.square_logs:
                continue
            j = self.square_logs[b]
            if len({0, i, j}) == 3:
                representatives.add(tuple(cyclic_orbit_pattern((0, i, j), self.n)))
        return sorted(representatives)


def _bit_add(a, b):
    a1, a2 = a
    b1, b2 = b
    az, bz = ~(a1 | a2), ~(b1 | b2)
    return ((a1 & bz) | (az & b1) | (a2 & b2),
            (a2 & bz) | (az & b2) | (a1 & b1))


def _bit_degree(a):
    return (a[0] | a[1]).bit_length() - 1


def _bit_gcd_degree(n, seed):
    """Two bitplanes implement exact F_3 coefficients, not binary arithmetic."""
    a, b = (1 << n, 1), (sum(1 << i for i in seed), 0)
    while _bit_degree(b) >= 0:
        db = _bit_degree(b)
        while _bit_degree(a) >= db:
            da = _bit_degree(a)
            same = bool(a[0] >> da & 1) == bool(b[0] >> db & 1)
            c = (b[1], b[0]) if same else b
            a = _bit_add(a, (c[0] << (da - db), c[1] << (da - db)))
        a, b = b, a
    return _bit_degree(a)


def seed_certificate(field, seed):
    h = [2] + [0] * (field.n - 1) + [1]
    p = _sparse(seed)
    d, a, b = _xgcd(h, p)
    return {"seed": list(seed), "gcd": d,
            "bezout_h": a, "bezout_seed": b,
            "quotient_h": _divrem(h, d)[0],
            "quotient_seed": _divrem(p, d)[0]}


def verify_seed_certificate(field, certificate):
    seed = certificate["seed"]
    require(isinstance(seed, list) and len(seed) == 3
            and all(type(i) is int and 0 <= i < field.n for i in seed)
            and seed == cyclic_orbit_pattern(seed, field.n), "invalid canonical seed")
    require(1 in field.seed_root_exponents(seed), "seed is not an actual edge")
    keys = ("gcd", "bezout_h", "bezout_seed", "quotient_h", "quotient_seed")
    for key in keys:
        value = certificate[key]
        require(isinstance(value, list) and len(value) <= field.n + 1
                and all(type(c) is int and c in (0, 1, 2) for c in value)
                and (not value or value[-1] != 0), "invalid polynomial: " + key)
    d = certificate["gcd"]
    require(d and d[-1] == 1, "gcd is not monic")
    h, p = [2] + [0] * (field.n - 1) + [1], _sparse(seed)
    require(_mul(d, certificate["quotient_h"]) == h, "cyclic divisibility failed")
    require(_mul(d, certificate["quotient_seed"]) == p, "seed divisibility failed")
    require(_add(_mul(certificate["bezout_h"], h),
                 _mul(certificate["bezout_seed"], p)) == d, "Bezout identity failed")
    roots = field.seed_root_exponents(seed)
    require(len(roots) == len(d) - 1, "independent field-root count differs from gcd")
    return {"seed": seed, "gcd_degree": len(d) - 1,
            "row_rank": field.n - len(d) + 1,
            "connectivity_index": gcd(gcd(seed[1], seed[2]), field.n),
            "root_exponents": roots}


def verify_field_polynomial(field):
    """Rabin and primitive-order checks independent of the coordinate recurrence."""
    x, modulus = [0, 1], field.modulus
    require(_powmod(x, field.q, modulus) == x, "Rabin Frobenius identity failed")
    for p in prime_factors(field.m):
        value = _add(_powmod(x, 3 ** (field.m // p), modulus), _neg(x))
        require(_xgcd(modulus, value)[0] == [1], "Rabin proper-factor exclusion failed")
    require(_powmod(x, field.q - 1, modulus) == [1], "primitive order identity failed")
    for p in prime_factors(field.q - 1):
        require(_powmod(x, (field.q - 1) // p, modulus) != [1],
                "x has a proper multiplicative order")


def trace_counterexample(field):
    values = [field.trace(field.squares[34 * t % field.n]) for t in range(field.n)]
    seed, full_edge = [0, 25, 311], [0, 5, 255]
    violations = [t for t in range(field.n)
                  if sum(values[(t + e) % field.n] for e in seed) % 3]
    return {"power": 34, "coefficient": 1, "values": values,
            "seed": seed, "seed_translate_violations": violations,
            "full_edge": full_edge,
            "full_edge_value_sum": sum(values[e] for e in full_edge) % 3}


def build_report():
    fields = []
    for m in range(3, 9):
        field = CompactField(m)
        rows = []
        for seed in field.normalized_orbits():
            degree = _bit_gcd_degree(field.n, seed)
            rows.append({"seed": list(seed), "gcd_degree": degree,
                         "connectivity_index": gcd(gcd(seed[1], seed[2]), field.n)})
            if m >= 7 and degree == m + 1:
                break
        selected = next(row["seed"] for row in rows if row["gcd_degree"] == m + 1)
        fields.append({"m": m, "field_modulus": field.modulus,
                       "subgroup_order": field.n, "complete_orbit_scan": m <= 6,
                       "orbits": rows, "good_seed_certificate": seed_certificate(field, selected)})
    field = CompactField(6)
    return {"schema": 1, "fields": fields,
            "connected_bad_certificate": seed_certificate(field, [0, 25, 311]),
            "nonlinear_trace_witness": trace_counterexample(field)}


def verify_report(report):
    require(report["schema"] == 1, "unknown report schema")
    require([item["m"] for item in report["fields"]] == list(range(3, 9)),
            "wrong bounded degree range")
    summaries = []
    for item in report["fields"]:
        field = CompactField(item["m"], item["field_modulus"])
        verify_field_polynomial(field)
        require(item["subgroup_order"] == field.n, "incorrect subgroup order")
        expected = field.normalized_orbits()
        rows = item["orbits"]
        require(item["complete_orbit_scan"] is (field.m <= 6), "wrong scan completeness flag")
        require([tuple(row["seed"]) for row in rows] == expected[:len(rows)],
                "orbit scan is not the canonical initial segment")
        if item["complete_orbit_scan"]:
            require(len(rows) == len(expected), "complete scan omits an orbit")
        for row in rows:
            seed = row["seed"]
            # Since 3 does not divide N, Z^N-1 has N distinct roots in K.
            # Direct root counting independently checks each bitplane gcd result.
            require(row["gcd_degree"] == len(field.seed_root_exponents(seed)),
                    "orbit gcd-degree/root-count mismatch")
            require(row["connectivity_index"] == gcd(gcd(seed[1], seed[2]), field.n),
                    "incorrect connectivity index")
        good = verify_seed_certificate(field, item["good_seed_certificate"])
        require(good["gcd_degree"] == field.m + 1, "chosen orbit does not force affine kernel")
        require(good["seed"] in [row["seed"] for row in rows], "chosen seed was not searched")
        histogram = Counter((row["connectivity_index"], row["gcd_degree"]) for row in rows)
        summaries.append({"m": field.m, "q": field.q, "N": field.n,
                          "complete_orbit_scan": item["complete_orbit_scan"],
                          "tested_orbits": len(rows), "good_seed": good,
                          "index_nullity_counts": [[index, nullity, count]
                              for (index, nullity), count in sorted(histogram.items())]})
    field = CompactField(6)
    bad = verify_seed_certificate(field, report["connected_bad_certificate"])
    require(bad["seed"] == [0, 25, 311] and bad["connectivity_index"] == 1
            and bad["gcd_degree"] == 13, "incorrect connected counterexample")
    trace = trace_counterexample(field)
    require(report["nonlinear_trace_witness"] == trace, "trace witness mismatch")
    require(trace["seed_translate_violations"] == [] and trace["full_edge_value_sum"] == 1,
            "trace witness does not separate sparse and full constraints")
    require(1 in field.seed_root_exponents(trace["full_edge"]), "separating triple is not an edge")
    canonical = json.dumps(report, sort_keys=True, separators=(",", ":")).encode()
    return {"bounded_degrees": summaries, "connected_bad_seed": bad,
            "nonlinear_witness_verified": True,
            "universal_existence_claim": False,
            "canonical_report_sha256": hashlib.sha256(canonical).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    if args.check:
        value = json.loads(args.check.read_text())
        report = value.get("report", value)
        receipt = verify_report(report)
        if "verification" in value:
            require(value["verification"] == receipt, "saved verification mismatch")
        print(json.dumps(receipt, sort_keys=True, indent=2))
    else:
        report = build_report()
        print(json.dumps({"report": report, "verification": verify_report(report)},
                         sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

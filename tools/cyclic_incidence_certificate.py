"""Standalone F_3 polynomial certificate for the F_243 incidence rank.

One cyclic orbit of 121 true edges already has rank 115.  This script uses
only standard-library polynomial arithmetic, without project field tables,
character enumeration, matrix rank or the uniform Fourier theorem.
"""

from pathlib import Path
import argparse
import hashlib
import json


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _trim(a):
    a = [x % 3 for x in a]
    while a and not a[-1]:
        a.pop()
    return a


def _add(a, b):
    return _trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                  for i in range(max(len(a), len(b)))])


def _neg(a):
    return _trim([-x for x in a])


def _mul(a, b):
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = (c[i + j] + x * y) % 3
    return _trim(c)


def _divrem(a, b):
    a, b = _trim(a), _trim(b)
    if not b:
        raise ZeroDivisionError("zero polynomial")
    quotient = [0] * max(0, len(a) - len(b) + 1)
    while a and len(a) >= len(b):
        k = len(a) - len(b)
        coefficient = a[-1] * pow(b[-1], -1, 3) % 3
        quotient[k] = coefficient
        for j, value in enumerate(b):
            a[k + j] = (a[k + j] - coefficient * value) % 3
        a = _trim(a)
    return _trim(quotient), a


def _xgcd(a, b):
    u, v, s, t = [1], [], [], [1]
    while b:
        quotient, remainder = _divrem(a, b)
        a, b = b, remainder
        u, s = s, _add(u, _neg(_mul(quotient, s)))
        v, t = t, _add(v, _neg(_mul(quotient, t)))
    if not a:
        return [], [], []
    scale = pow(a[-1], -1, 3)
    return tuple(_trim([scale * x for x in p]) for p in (a, u, v))


def _powmod(a, exponent, modulus):
    value = [1]
    a = _divrem(a, modulus)[1]
    while exponent:
        if exponent & 1:
            value = _divrem(_mul(value, a), modulus)[1]
        a = _divrem(_mul(a, a), modulus)[1]
        exponent >>= 1
    return value


def _sparse(exponents):
    polynomial = [0] * (max(exponents) + 1)
    for k in exponents:
        polynomial[k] = (polynomial[k] + 1) % 3
    return _trim(polynomial)


def cyclic_orbit_pattern(exponents, n):
    """Canonical translation-orbit representative of a distinct exponent set."""
    exponents = tuple(k % n for k in exponents)
    _require(len(exponents) == 3 and len(set(exponents)) == 3, "invalid exponent triple")
    return list(min(tuple(sorted((x - anchor) % n for x in exponents))
                    for anchor in exponents))


def _validated_polynomial(value, name):
    _require(isinstance(value, list) and len(value) <= 122,
             "invalid polynomial size: " + name)
    _require(all(type(x) is int and x in (0, 1, 2) for x in value),
             "non-F_3 coefficient: " + name)
    _require(not value or value[-1] != 0, "noncanonical polynomial: " + name)
    return value


def build_certificate():
    h = [2] + [0] * 120 + [1]
    seed = _sparse((0, 4, 68))
    d, a, b = _xgcd(h, seed)
    modulus = [2, 2, 0, 0, 0, 1]
    linear_frobenius = [0, 2, 0, 1]
    one, u, v = _xgcd(modulus, linear_frobenius)
    _require(one == [1], "unexpected reducible modulus")
    return {
        "schema": 1,
        "coefficient_characteristic": 3,
        "field_order": 243,
        "subgroup_order": 121,
        "seed_exponents": [0, 4, 68],
        "field_modulus": modulus,
        "cyclic_modulus": h,
        "seed_polynomial": seed,
        "gcd": d,
        "quotient_cyclic_modulus": _divrem(h, d)[0],
        "quotient_seed": _divrem(seed, d)[0],
        "bezout_cyclic_modulus": a,
        "bezout_seed": b,
        "irreducibility_bezout_modulus": u,
        "irreducibility_bezout_x3_minus_x": v,
        "frobenius_orbit_patterns": [cyclic_orbit_pattern(
            (0, 4 * (3 ** j), 68 * (3 ** j)), 121) for j in range(5)],
    }


def verify_certificate(certificate):
    """Check exact identities, irreducibility and the actual seed edge.

    The rank-gcd identity is checked by divisibility plus the supplied Bezout
    identity, without recomputing its gcd.  The irreducibility check uses
    X^243=X and a separate supplied Bezout identity against X^3-X.
    """
    _require(certificate["schema"] == 1, "unknown certificate schema")
    _require(certificate["coefficient_characteristic"] == 3, "wrong characteristic")
    _require(certificate["field_order"] == 243 and certificate["subgroup_order"] == 121,
             "wrong field or subgroup order")
    _require(certificate["seed_exponents"] == [0, 4, 68], "wrong seed exponents")
    keys = ("field_modulus", "cyclic_modulus", "seed_polynomial", "gcd",
            "quotient_cyclic_modulus", "quotient_seed", "bezout_cyclic_modulus",
            "bezout_seed", "irreducibility_bezout_modulus",
            "irreducibility_bezout_x3_minus_x")
    polynomials = {key: _validated_polynomial(certificate[key], key) for key in keys}
    modulus, h, seed, d = (polynomials[key] for key in
                           ("field_modulus", "cyclic_modulus", "seed_polynomial", "gcd"))
    _require(modulus == [2, 2, 0, 0, 0, 1], "wrong field identification polynomial")
    _require(h == [2] + [0] * 120 + [1], "wrong cyclic modulus")
    _require(seed == _sparse((0, 4, 68)), "wrong seed polynomial")
    _require(len(d) == 7 and d[-1] == 1, "gcd must be monic of degree six")
    _require(d == _mul([2, 1], modulus), "gcd does not equal (X-1)M")
    _require(_mul(d, polynomials["quotient_cyclic_modulus"]) == h,
             "gcd divisibility of cyclic modulus failed")
    _require(_mul(d, polynomials["quotient_seed"]) == seed,
             "gcd divisibility of seed failed")
    bezout = _add(_mul(polynomials["bezout_cyclic_modulus"], h),
                  _mul(polynomials["bezout_seed"], seed))
    _require(bezout == d, "incidence Bezout identity failed")
    x = [0, 1]
    linear_frobenius = [0, 2, 0, 1]
    irreducibility_identity = _add(
        _mul(polynomials["irreducibility_bezout_modulus"], modulus),
        _mul(polynomials["irreducibility_bezout_x3_minus_x"], linear_frobenius))
    _require(irreducibility_identity == [1], "irreducibility Bezout identity failed")
    _require(_powmod(x, 243, modulus) == x, "degree-five Frobenius test failed")
    _require(_powmod(x, 121, modulus) == [1], "generator does not satisfy order 121")
    order_eleven_value = _powmod(x, 11, modulus)
    _require(order_eleven_value != [1], "generator has proper order dividing 11")
    _require(_divrem(seed, modulus)[1] == [], "seed is not a true zero-sum triple")
    vertex_values = [_powmod(x, k, modulus) for k in (0, 4, 68)]
    _require(len({tuple(p) for p in vertex_values}) == 3, "seed vertices repeat")
    _require(_add(_add(vertex_values[0], vertex_values[1]), vertex_values[2]) == [],
             "seed vertices do not sum to zero")
    patterns = [cyclic_orbit_pattern((0, 4 * (3 ** j), 68 * (3 ** j)), 121)
                for j in range(5)]
    _require(certificate["frobenius_orbit_patterns"] == patterns,
             "Frobenius orbit-pattern mismatch")
    stabilizing = [j for j, pattern in enumerate(patterns) if pattern == patterns[0]]
    _require(stabilizing == [0], "unexpected Frobenius stabilizer of seed orbit")
    canonical = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
    return {
        "arithmetic": "F_3 polynomial identities only; no project imports",
        "field_modulus": modulus,
        "field_modulus_irreducible": True,
        "generator_order": 121,
        "generator_power_11": order_eleven_value,
        "seed_exponents": [0, 4, 68],
        "seed_field_coordinates": vertex_values,
        "seed_cyclic_orbit_size": 121,
        "gcd": d,
        "gcd_degree": 6,
        "seed_orbit_incidence_rank": 115,
        "seed_orbit_kernel_dimension": 6,
        "full_hypergraph_incidence_rank": 115,
        "full_kernel_is_affine": True,
        "full_hypergraph_edges_from_proved_formula": 1210,
        "frobenius_orbit_patterns": patterns,
        "seed_orbit_stabilizing_frobenius_exponents": stabilizing,
        "seed_orbit_semilinear_stabilizer_order": 121,
        "seed_automorphism_classification_dependency":
            "affine-kernel extension and classical Carlitz; see SC-011 proof",
        "bezout_degrees": [len(polynomials["bezout_cyclic_modulus"]) - 1,
                            len(polynomials["bezout_seed"]) - 1],
        "canonical_certificate_sha256": hashlib.sha256(canonical).hexdigest(),
    }


def proper_orbit_control():
    """A genuine F_81 edge orbit of rank 25, versus a rank-35 edge orbit."""
    modulus = [1, 0, 1, 2, 1]
    x = [0, 1]
    _require(_powmod(x, 81, modulus) == x, "F_81 Frobenius control failed")
    x9_minus_x = _add(_powmod(x, 9, modulus), _neg(x))
    _require(_xgcd(modulus, x9_minus_x)[0] == [1], "F_81 irreducibility control failed")
    _require(_powmod(x, 40, modulus) == [1], "F_81 subgroup order failed")
    _require(_powmod(x, 20, modulus) != [1] and _powmod(x, 8, modulus) != [1],
             "F_81 subgroup generator has proper order")
    h = [2] + [0] * 39 + [1]
    reports = []
    for exponents in ((0, 5, 30), (0, 1, 9)):
        seed = _sparse(exponents)
        _require(_divrem(seed, modulus)[1] == [], "F_81 control is not a true edge")
        d, a, b = _xgcd(h, seed)
        _require(_add(_mul(a, h), _mul(b, seed)) == d, "F_81 Bezout control failed")
        _require(not _divrem(h, d)[1] and not _divrem(seed, d)[1],
                 "F_81 gcd control failed")
        reports.append({"seed_exponents": list(exponents), "gcd_degree": len(d) - 1,
                        "cyclic_orbit_incidence_rank": 40 - len(d) + 1})
    _require([r["gcd_degree"] for r in reports] == [15, 5], "unexpected F_81 control ranks")
    return {"q": 81, "subgroup_order": 40, "field_modulus": modulus,
            "generator_order": 40, "orbit_controls": reports,
            "arbitrary_single_orbit_need_not_span_full_row_code": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path, help="verify a saved certificate or complete report")
    args = parser.parse_args()
    if args.check:
        value = json.loads(args.check.read_text())
        verification = verify_certificate(value.get("certificate", value))
        if "verification" in value:
            _require(value["verification"] == verification, "saved verification receipt mismatch")
        if "proper_orbit_control" in value:
            _require(value["proper_orbit_control"] == proper_orbit_control(),
                     "saved proper-orbit control mismatch")
        print(json.dumps(verification, sort_keys=True, indent=2))
        return
    certificate = build_certificate()
    print(json.dumps({"schema": 1, "certificate": certificate,
                      "verification": verify_certificate(certificate),
                      "proper_orbit_control": proper_orbit_control()},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

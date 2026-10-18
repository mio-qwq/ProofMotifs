"""Exact arithmetic checks for the written normal-character existence bound.

This checks small factor counts and the two anchors of an induction, not
extension-field elements or every integer in the infinite theorem.
"""
import json
from fractions import Fraction
from math import gcd


def totient(n):
    return sum(gcd(a, n) == 1 for a in range(1, n + 1))


def order_three(n):
    if n == 1:
        return 1
    assert gcd(3, n) == 1
    value, order = 3 % n, 1
    while value != 1:
        value = value * 3 % n
        order += 1
    return order


def factor_data(m):
    n = m
    while n % 3 == 0:
        n //= 3
    factors = []
    theta = Fraction(1)
    for d in range(1, n + 1):
        if n % d:
            continue
        degree = order_three(d)
        count = totient(d) // degree
        assert count * degree == totient(d)
        factors.append({"cyclotomic_index": d, "degree": degree, "count": count})
        theta *= Fraction(3 ** degree - 1, 3 ** degree) ** count
    omega = sum(f["count"] for f in factors)
    q, w = 3 ** m, 2 ** omega
    margin = (q - 3) ** 2 - 36 * (w - 1) ** 2 * q
    return {"m": m, "q": q, "radical_degree": n,
            "irreducible_factor_data": factors, "omega": omega, "W": w,
            "theta": [theta.numerator, theta.denominator],
            "positivity_integer_margin": margin, "criterion_positive": margin > 0}


def main():
    rows = [factor_data(m) for m in range(3, 15)]
    assert [r["omega"] for r in rows] == [1, 3, 2, 2, 2, 5, 1, 4, 3, 3, 5, 4]
    assert [r["m"] for r in rows if r["criterion_positive"]] == [6, 7, 9, 10, 11, 12, 13, 14]
    anchors = []
    for m in (13, 14):
        upper = 2 ** ((m + 2) // 2)
        margin = 3 ** m - (6 * upper + 1) ** 2
        assert margin > 0
        anchors.append({"m": m, "W_upper": upper, "integer_margin": margin})
    print(json.dumps({"finite_criterion_checks": rows, "induction_anchors": anchors,
                      "infinite_range_uses_written_induction": True,
                      "field_element_enumeration_used": False}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

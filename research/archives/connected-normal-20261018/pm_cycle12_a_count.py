#!/usr/bin/env python3
"""Exact arithmetic for the PM-CYCLE12-A maximal-subgroup union bound.

Only stdlib integers/Fraction; does not import ProofMotifs or use field samples.
The infinite step is a separate proof, not an inference from the finite table.
"""
from fractions import Fraction
import json


def factor(n):
    assert n >= 1
    ans = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            ans[p] = ans.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def phi(n):
    result = n
    for p in factor(n):
        result = result // p * (p - 1)
    return result


def order3(n):
    if n == 1:
        return 1
    assert n % 3
    x, k = 3 % n, 1
    while x != 1:
        x, k = x * 3 % n, k + 1
    return k


def distinct_frobenius_factors(m):
    n = m
    while n % 3 == 0:
        n //= 3
    return sum(phi(d) // order3(d)
               for d in range(1, n + 1) if n % d == 0)


def criterion(m):
    q = 3 ** m
    primes = factor((q - 1) // 2)
    r = len(primes)
    omega = distinct_frobenius_factors(m)
    W = 2 ** omega
    sigma = sum((Fraction(1, p * p) for p in primes), Fraction())
    main = q * (1 - sigma) - 3
    error = 6 * (W - 1) + (3 * W - 1) * (4 * r - sigma)
    passed = main > 0 and main * main > error * error * q
    assert omega <= (m + 7) // 3
    assert sigma < Fraction(3, 8)
    assert r <= m - 1
    return {"m": m, "q": q, "N_factors": primes, "omega_F": omega,
            "W_F": W, "r_N": r, "sigma": str(sigma),
            "main": str(main), "error": str(error),
            "squared_margin": str(main * main - error * error * q),
            "criterion_passes": passed}


def uniform_anchor(m):
    q = 3 ** m
    U = 2 ** ((m + 7) // 3)
    main = Fraction(5, 8) * q - 3
    error = (12 * m - 6) * U
    margin = main * main - error * error * q
    assert main > 0 and margin > 0
    return {"m": m, "q": q, "U": U, "main": str(main),
            "error": error, "squared_margin": str(margin)}


def hybrid_degree16():
    # T^16-1: two linear, three quadratic and two quartic factors.
    counts = {}
    for d in [1, 2, 4, 8, 16]:
        degree = order3(d)
        counts[degree] = counts.get(degree, 0) + phi(d) // degree
    assert counts == {1: 2, 2: 3, 4: 2}
    theta = Fraction(1)
    for degree, count in counts.items():
        theta *= (1 - Fraction(1, 3 ** degree)) ** count
    q, rootq, W = 3 ** 16, 3 ** 8, 128
    assert factor((q - 1) // 2) == {2: 5, 5: 1, 17: 1, 41: 1, 193: 1}
    A = theta * Fraction(q - 3 - 6 * (W - 1) * rootq, 4)
    D2 = theta * Fraction(q, 16) + theta * Fraction(15, 16) * (3 * W - 1) * rootq
    rest = sum((Fraction(q - 3, 4 * p * p)
                + 2 * (1 - Fraction(1, 4 * p * p)) * rootq
                for p in [5, 17, 41, 193]), Fraction())
    margin = A - D2 - rest
    assert margin > 0
    return {"m": 16, "Theta": str(theta), "A_lower": str(A),
            "weighted_D2_upper": str(D2), "unweighted_other_upper": str(rest),
            "connected_lower": str(margin)}


if __name__ == "__main__":
    rows = [criterion(m) for m in range(5, 27)]
    failures = [row["m"] for row in rows if not row["criterion_passes"]]
    assert failures == [5, 6, 7, 8, 10, 16]
    anchors = [uniform_anchor(m) for m in [24, 25, 26]]
    print(json.dumps({"finite_rows": rows, "finite_failures": failures,
                      "uniform_anchors": anchors,
                      "hybrid_degree16": hybrid_degree16(),
                      "degree7_prime_order_shortcut": factor((3 ** 7 - 1) // 2) == {1093: 1},
                      "infinite_proof": "See /tmp/pm_cycle12_a_theory.md; +3 induction."},
                     indent=2))

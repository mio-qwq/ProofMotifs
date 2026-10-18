"""Independent exact finite check of the classical Cramer coefficient bound."""
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial, lcm
import json
from feature_repair_independent import echelon, independent_oracle
from feature_repair_boundary import dot


def vertex_integer_coefficients(rows, target):
    n = len(rows[0])
    basis = []
    for row in rows:
        if len(echelon(basis+[row], n)[1]) > len(basis):
            basis.append(row)
    q = len(basis)
    if not q:
        return None
    columns = [[row[j] for row in basis] for j in range(n)]
    for active in combinations(range(n), q):
        eq = [columns[j]+[int(j not in target)] for j in active]
        reduced, pivots = echelon(eq, q)
        if len(pivots) != q:
            continue
        c = [F(0)]*q
        for k, j in enumerate(pivots):
            c[j] = reduced[k][-1]
        w = [dot(c, col) for col in columns]
        if not all(w[j] == 0 if j in target else w[j] >= 1 for j in range(n)):
            continue
        multiplier = lcm(*(t.denominator for t in c))
        ci = [multiplier*t for t in c]
        h = max(1, *(abs(x) for row in rows for x in row))
        assert all(t.denominator == 1 and abs(t) <= factorial(q)*h**(q-1) for t in ci)
        assert all(abs(t) <= factorial(len(rows))*h**(len(rows)-1) for t in ci)
        return ci
    return None


def main():
    counts = []
    for r in (1, 2):
        checked, feasible = 0, 0
        for entries in product((-1, 0, 1), repeat=3*r):
            rows = [list(entries[3*j:3*j+3]) for j in range(r)]
            answer = independent_oracle(rows, [0])
            ci = vertex_integer_coefficients(rows, {0})
            assert (ci is not None) == (answer["kind"] == "selector")
            checked += 1
            feasible += int(ci is not None)
        counts.append({"rows": r, "points": 3, "all_matrices_checked": checked,
                       "feasible_matrices": feasible, "bound_M": factorial(r)})
    tight = [[0, 1, -1], [0, 0, 1]]
    assert vertex_integer_coefficients(tight, {0}) == [F(1), F(2)]
    print(json.dumps({"all_assertions_passed": True, "exhaustive_unit_entry_cases": counts,
                      "tight_R2_H1_example": {"rows": tight, "integer_coefficients": [1, 2],
                                               "bound_M": 2},
                      "qualification": "Bound is for integralized feature rows."}, indent=2))


if __name__ == "__main__":
    main()

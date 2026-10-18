#!/usr/bin/env python3
"""Exact finite feature-repair prototype; no floating-point LP is used.

This is a certificate/testing implementation, not an efficient LP solver.
The oracle enumerates rational basic feasible supports and active sets.
All user-facing mathematics is in /tmp/pm_repair_a.md.
"""

from itertools import combinations, product
from math import factorial
import json
import random
from fractions import Fraction as Rational


class Matrix:
    """Small Fraction-only matrix helper, intentionally independent of CAS/LP."""

    def __init__(self, rows, ncols=None):
        rows = list(rows)
        if rows and not isinstance(rows[0], (list, tuple)):
            rows = [[x] for x in rows]
        self.data = [[Rational(x) for x in row] for row in rows]
        self.rows = len(rows)
        self.cols = len(rows[0]) if rows else (0 if ncols is None else ncols)
        assert all(len(row) == self.cols for row in rows)

    @staticmethod
    def ones(rows, cols):
        return Matrix([[1] * cols for _ in range(rows)], cols)

    @staticmethod
    def vstack(*parts):
        assert parts
        assert all(p.cols == parts[0].cols for p in parts)
        return Matrix([row for p in parts for row in p.data], parts[0].cols)

    @property
    def T(self):
        return Matrix([[self.data[i][j] for i in range(self.rows)] for j in range(self.cols)], self.rows)

    def __iter__(self):
        return (x for row in self.data for x in row)

    def __getitem__(self, item):
        if not isinstance(item, tuple):
            return self.data[item // self.cols][item % self.cols]
        rs, cs = item
        ri = list(range(self.rows))[rs] if isinstance(rs, slice) else rs
        ci = list(range(self.cols))[cs] if isinstance(cs, slice) else cs
        if isinstance(ri, int) and isinstance(ci, int):
            return self.data[ri][ci]
        ri = [ri] if isinstance(ri, int) else list(ri)
        ci = [ci] if isinstance(ci, int) else list(ci)
        return Matrix([[self.data[i][j] for j in ci] for i in ri], len(ci))

    def __setitem__(self, index, value):
        self.data[index // self.cols][index % self.cols] = Rational(value)

    def __eq__(self, other):
        return isinstance(other, Matrix) and (self.rows, self.cols, self.data) == (other.rows, other.cols, other.data)

    def __mul__(self, other):
        assert self.cols == other.rows
        return Matrix([[sum((self.data[i][k] * other.data[k][j] for k in range(self.cols)), Rational(0)) for j in range(other.cols)] for i in range(self.rows)], other.cols)

    def __neg__(self):
        return Matrix([[-x for x in row] for row in self.data], self.cols)

    def row_join(self, other):
        assert self.rows == other.rows
        return Matrix([self.data[i] + other.data[i] for i in range(self.rows)], self.cols + other.cols)

    def col_join(self, other):
        return Matrix.vstack(self, other)

    def rref(self):
        values = [row[:] for row in self.data]
        pivots, rank = [], 0
        for col in range(self.cols):
            pivot = next((i for i in range(rank, self.rows) if values[i][col]), None)
            if pivot is None:
                continue
            values[rank], values[pivot] = values[pivot], values[rank]
            divisor = values[rank][col]
            values[rank] = [x / divisor for x in values[rank]]
            for i in range(self.rows):
                if i == rank:
                    continue
                factor = values[i][col]
                if factor:
                    values[i] = [x - factor * y for x, y in zip(values[i], values[rank])]
            pivots.append(col)
            rank += 1
            if rank == self.rows:
                break
        return Matrix(values, self.cols), tuple(pivots)

    def rank(self):
        return len(self.rref()[1])

    def nullspace(self):
        reduced, pivots = self.rref()
        result = []
        for free in range(self.cols):
            if free in pivots:
                continue
            v = [Rational(0)] * self.cols
            v[free] = Rational(1)
            for i, pivot in enumerate(pivots):
                v[pivot] = -reduced.data[i][free]
            result.append(Matrix(v))
        return result

    def gauss_jordan_solve(self, rhs):
        reduced, pivots = self.row_join(rhs).rref()
        assert pivots == tuple(range(self.cols))
        return Matrix([reduced.data[i][-1] for i in range(self.cols)]), zeros(0, 0)


def zeros(rows, cols):
    return Matrix([[0] * cols for _ in range(rows)], cols)


def solve_unique(columns, rhs):
    """Return the unique rational solution, or None if dependent/inconsistent."""
    if columns.cols == 0:
        return zeros(0, 1) if rhs == zeros(rhs.rows, 1) else None
    if columns.rank() != columns.cols:
        return None
    if columns.row_join(rhs).rank() != columns.cols:
        return None
    answer, params = columns.gauss_jordan_solve(rhs)
    assert params.rows == 0
    return answer


def oracle(A, D):
    """Return ('selector', c) or ('trade', t), exactly verified.

    A has feature rows and Omega columns. D is a sorted set of target indices.
    A selector satisfies A_D^T c=0 and A_O^T c>=1.
    A trade satisfies A t=0, t_O>=0, sum(t_O)=1.
    """
    D = list(D)
    O = [i for i in range(A.cols) if i not in D]
    if not O:
        return "selector", zeros(A.rows, 1)
    AD = A[:, D]
    AO = A[:, O]
    left_null = AD.T.nullspace()
    L = Matrix.vstack(*[v.T for v in left_null]) if left_null else zeros(0, A.rows)
    raw_Q = L * AO
    independent_rows = list(raw_Q.T.rref()[1])
    Q = raw_Q[independent_rows, :]
    L = L[independent_rows, :]
    q = Q.rows
    B = Q.col_join(Matrix.ones(1, len(O)))
    rhs = zeros(q, 1).col_join(Matrix([1]))

    # A nonempty normalized trade polytope has a vertex with at most q+1
    # off-target support points. This step is exact basic-solution enumeration.
    for k in range(1, min(q + 1, len(O)) + 1):
        for support in combinations(range(len(O)), k):
            lam = solve_unique(B[:, list(support)], rhs)
            if lam is None or any(x < 0 for x in lam):
                continue
            outside = zeros(len(O), 1)
            for i, value in zip(support, lam):
                outside[i] = value
            target_basis = list(AD.rref()[1])
            target = solve_unique(AD[:, target_basis], -AO * outside)
            assert target is not None
            t = zeros(A.cols, 1)
            for i, value in zip(O, outside):
                t[i] = value
            for i, value in zip(target_basis, target):
                t[D[i]] = value
            assert A * t == zeros(A.rows, 1)
            assert sum(t[i] for i in O) == 1
            assert all(t[i] >= 0 for i in O)
            assert sum(x != 0 for x in t) <= A.rank() + 1
            return "trade", t

    # Q has independent rows. A feasible selector polyhedron has no lineality
    # and hence has a vertex with q independent tight off-target inequalities.
    for active in combinations(range(len(O)), q):
        y = solve_unique(Q[:, list(active)].T, Matrix.ones(q, 1))
        if y is None or any(x < 1 for x in Q.T * y):
            continue
        c = L.T * y
        w = A.T * c
        assert all(w[i] == 0 for i in D)
        assert all(w[i] >= 1 for i in O)
        return "selector", c
    raise AssertionError("Exact alternative failed")


def stack(base, blocks, chosen):
    return Matrix.vstack(base, *[blocks[j] for j in sorted(chosen)])


def all_subsets(m):
    for k in range(m + 1):
        yield from (frozenset(s) for s in combinations(range(m), k))


def exhaustive_repair(base, blocks, costs, D):
    candidates = sorted(all_subsets(len(blocks)), key=lambda s: (sum(costs[j] for j in s), len(s), tuple(sorted(s))))
    for s in candidates:
        kind, cert = oracle(stack(base, blocks, s), D)
        if kind == "selector":
            return s, sum(costs[j] for j in s), cert
    return None


def adaptive_repair(base, blocks, costs, D):
    """Exact obstruction cuts, with a brute-force minimum-cost master."""
    candidates = sorted(all_subsets(len(blocks)), key=lambda s: (sum(costs[j] for j in s), len(s), tuple(sorted(s))))
    cuts = []
    rejected = set()
    for _ in range(2 ** len(blocks) + 1):
        s = next((s for s in candidates if all(s & cut for cut in cuts)), None)
        if s is None:
            return None, cuts
        kind, cert = oracle(stack(base, blocks, s), D)
        if kind == "selector":
            return (s, sum(costs[j] for j in s), cert), cuts
        assert s not in rejected
        rejected.add(s)
        cut = frozenset(j for j, block in enumerate(blocks) if block * cert != zeros(block.rows, 1))
        assert not (s & cut)
        cuts.append(cut)
        if not cut:
            return None, cuts
    raise AssertionError("Cut method exceeded number of subsets")


def show(vec):
    return [str(x) for x in vec]


def grid_audit():
    """Audit the coordinator's later proposed designed calibration separately."""
    records = []
    for r in range(1, 6):
        omega = list(product((-1, 0, 1), repeat=r))
        exponents = list(product((0, 1, 2), repeat=r))
        target = [i for i, point in enumerate(omega) if 0 in point]
        off = [i for i, point in enumerate(omega) if 0 not in point]
        trade = []
        for point in omega:
            value = 1
            for x in point:
                value *= -2 if x == 0 else 1
            trade.append(value)
        assert all(trade[i] == 1 for i in off)
        annihilated = 0
        for exponent in exponents:
            moment = 0
            for point, weight in zip(omega, trade):
                term = weight
                for x, e in zip(point, exponent):
                    term *= x ** e
                moment += term
            if exponent == (2,) * r:
                assert moment == 2 ** r
            else:
                assert moment == 0
                annihilated += 1
        records.append({"r": r, "points": len(omega), "target_points": len(target), "off_points": len(off), "reduced_monomials_annihilated": annihilated})

    # For r=2 the dictionary is small enough for blind block enumeration.
    r = 2
    omega = list(product((-1, 0, 1), repeat=r))
    exponents = list(product((0, 1, 2), repeat=r))
    def row(exponent):
        return [point[0] ** exponent[0] * point[1] ** exponent[1] for point in omega]
    free = [e for e in exponents if sum(x != 0 for x in e) <= 1]
    optional = [e for e in exponents if e not in free]
    base = Matrix([row(e) for e in free])
    blocks = [Matrix([row(e)]) for e in optional]
    D = [i for i, point in enumerate(omega) if 0 in point]
    found = exhaustive_repair(base, blocks, [1] * len(blocks), D)
    assert found is not None and found[1] == 1
    assert [optional[j] for j in found[0]] == [(2, 2)]
    return {"tensor_moment_checks": records, "r2_selected_monomial": [2, 2], "r2_optimum_unit_cost": found[1]}


def run_tests():
    # Minimal failure of hitting only initial extreme trades.
    base = Matrix([[1, 1, 1]])
    f1 = Matrix([[0, 1, -1]])
    f2 = Matrix([[0, -1, 2]])
    initial_extremes = [Matrix([-1, 1, 0]), Matrix([-1, 0, 1])]
    assert all(f1 * t != Matrix([0]) for t in initial_extremes)
    kind, hidden_trade = oracle(Matrix.vstack(base, f1), [0])
    assert kind == "trade"
    assert hidden_trade == Matrix([-1, Rational(1, 2), Rational(1, 2)])
    assert oracle(Matrix.vstack(base, f2), [0])[0] == "trade"
    result, cuts = adaptive_repair(base, [f1, f2], [1, 1], [0])
    assert result[0] == frozenset({0, 1}) and result[1] == 2
    synergy = {"chosen": sorted(result[0]), "cost": result[1], "selector": show(result[2]), "values": show(stack(base, [f1, f2], result[0]).T * result[2]), "cuts": [sorted(cut) for cut in cuts], "hidden_trade": show(hidden_trade)}

    # Target signs in a trade really must be free, not all nonpositive.
    # D has features 0,1 in the affine line, with off-target feature 2.
    # The only legal affine defect zero at both targets is identically zero.
    signed_target = Matrix([[1, 1, 1], [0, 1, 2]])
    kind, target_trade = oracle(signed_target, [0, 1])
    assert kind == "trade" and target_trade == Matrix([1, -2, 1])

    # Exact set-cover parity, including uncovered universes.
    rng = random.Random(20261018)
    cover_checks = 0
    for _ in range(40):
        n, m = rng.randint(1, 5), rng.randint(1, 5)
        masks = [{i for i in range(n) if rng.randrange(2)} for _ in range(m)]
        costs = [rng.randint(1, 5) for _ in range(m)]
        blocks = [Matrix([[0] + [int(i in mask) for i in range(n)]]) for mask in masks]
        base = Matrix.ones(1, n + 1)
        expected = min((sum(costs[j] for j in s) for s in all_subsets(m) if set().union(*(masks[j] for j in s)) == set(range(n))), default=None)
        exact = exhaustive_repair(base, blocks, costs, [0])
        adaptive, cuts = adaptive_repair(base, blocks, costs, [0])
        assert (None if exact is None else exact[1]) == expected
        assert (None if adaptive is None else adaptive[1]) == expected
        cover_checks += 1

    # Signed rational data: compare adaptive choice to independent full
    # subset enumeration. Multiple targets and vector-valued blocks occur.
    general_checks = 0
    for _ in range(30):
        n, m = rng.randint(2, 5), rng.randint(1, 4)
        D = list(range(rng.randint(1, n - 1)))
        base = Matrix.ones(1, n)
        blocks = [Matrix([[Rational(rng.randint(-2, 2), rng.randint(1, 3)) for _ in range(n)] for _ in range(rng.randint(1, 2))]) for _ in range(m)]
        costs = [rng.randint(1, 5) for _ in range(m)]
        exact = exhaustive_repair(base, blocks, costs, D)
        adaptive, cuts = adaptive_repair(base, blocks, costs, D)
        assert (None if exact is None else exact[1]) == (None if adaptive is None else adaptive[1])
        general_checks += 1

    # A two-dimensional integral example needs a genuinely large coefficient.
    # A single tight row pair gives c=(H,H-1) for q_p=(1,-1),
    # q_q=(-(H-2),H-1), whose determinant is one.
    H = 7
    bound_example = Matrix([[0, 1, -(H - 2)], [0, -1, H - 1]])
    kind, c = oracle(bound_example, [0])
    assert kind == "selector" and c == Matrix([H, H - 1])
    assert max(abs(x) for x in c) <= factorial(2) * H

    output = {"initial_extreme_ray_counterexample": synergy, "signed_target_trade": show(target_trade), "set_cover_instances_checked": cover_checks, "signed_rational_instances_checked": general_checks, "large_coefficient_example": {"H": H, "selector": show(c)}, "later_coordinator_grid_audit": grid_audit(), "all_checks": "PASS"}
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    run_tests()

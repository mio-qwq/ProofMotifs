#!/usr/bin/env python3
"""Exact, dependency-free synthesis and obstruction certificates.

See research/mechanisms/CONSTRUCTION_CONTRACTS.md. This is a small classical
coefficient-matching/interpolation baseline, not a general cancellation solver.
"""
from fractions import Fraction as Q
from itertools import product
from math import lcm
import json


def solve_rational(a, b):
    """Solve a*x=b exactly, setting free variables to zero; return None if false."""
    n = len(a[0])
    rows = [[Q(x) for x in row] + [Q(y)] for row, y in zip(a, b)]
    pivots = []
    for c in range(n):
        k = next((i for i in range(len(pivots), len(rows)) if rows[i][c]), None)
        if k is None:
            continue
        r = len(pivots)
        rows[r], rows[k] = rows[k], rows[r]
        v = rows[r][c]
        rows[r] = [x/v for x in rows[r]]
        for i in range(len(rows)):
            if i != r:
                v = rows[i][c]
                rows[i] = [x-v*y for x, y in zip(rows[i], rows[r])]
        pivots.append(c)
    if any(not any(row[:n]) and row[n] for row in rows):
        return None
    ans = [Q(0)]*n
    for r, c in enumerate(pivots):
        ans[c] = rows[r][n]
    assert all(sum(x*y for x, y in zip(row, ans)) == v for row, v in zip(a, b))
    return ans


def monomials(degree, allowed):
    return [e for e in product(range(degree+1), repeat=4)
            if sum(e) <= degree and all(not e[i] for i in range(4) if i not in allowed)]


def synthesize_square(c):
    """Find W=A(g)+B(h,u)+C(h,v), P affine, W-P*E=(g-h)^2."""
    zero = (0, 0, 0, 0)
    unit = [tuple(int(i == j) for i in range(4)) for j in range(4)]
    phase = dict(zip(unit, (c, -c, 1, -1)))
    target = {(2, 0, 0, 0): 1, (1, 1, 0, 0): -2, (0, 2, 0, 0): 1}
    basis = monomials(2, range(4))
    columns, names = [], []
    for name, allowed in (('A', (0,)), ('B', (1, 2)), ('C', (1, 3))):
        for e in monomials(2, allowed):
            columns.append({e: 1})
            names.append((name, e))
    for e in [zero] + unit:
        columns.append({tuple(x+y for x, y in zip(e, f)): -v for f, v in phase.items()})
        names.append(('P', e))
    matrix = [[col.get(e, 0) for col in columns] for e in basis]
    solution = solve_rational(matrix, [target.get(e, 0) for e in basis])
    assert solution is not None
    scale = lcm(*(x.denominator for x in solution))
    terms = [{'component': name, 'powers': e, 'coefficient': int(v*scale)}
             for (name, e), v in zip(names, solution) if v]

    def evaluate(component, args):
        return sum(t['coefficient'] * product_value(args, t['powers'])
                   for t in terms if t['component'] == component)

    # Independent value-level check of the coefficient identity, including off phase.
    for args in product(range(-2, 3), repeat=4):
        g, h, u, v = args
        w = sum(evaluate(part, args) for part in ('A', 'B', 'C'))
        assert w - evaluate('P', args)*(u-v+c*(g-h)) == scale*(g-h)**2
    labels = range(1, 8)
    support = [s for s in product(labels, repeat=4) if s[2]-s[3]+c*(s[0]-s[1]) == 0]
    weights = [sum(evaluate(part, s) for part in ('A', 'B', 'C')) for s in support]
    assert all(w >= 0 and ((w == 0) == (s[0] == s[1] and s[2] == s[3]))
               for s, w in zip(support, weights))
    return {'phase_coefficient': c, 'matrix_shape': [len(matrix), len(columns)],
            'integer_scale': scale, 'terms': terms, 'M': 7,
            'exact_phase_tuples': len(support), 'max_exponent': max(weights)}


def product_value(args, exponents):
    z = 1
    for x, e in zip(args, exponents):
        z *= x**e
    return z


def trade_check():
    positive = [(1, 2, 3, 1), (2, 1, 1, 3)]
    negative = [(1, 1, 3, 3), (2, 2, 1, 1)]
    assert all(u-v+2*(g-h) == 0 for g, h, u, v in positive+negative)
    assert all(sorted(x[i] for x in positive) == sorted(x[i] for x in negative)
               for i in range(4))
    assert all(g == h and u == v for g, h, u, v in negative)
    assert all(g != h for g, h, u, v in positive)
    # Laurent escape: signed exponent g-h separates target but fails nonnegativity.
    assert [g-h for g, h, u, v in positive] == [-1, 1]
    for m in (1, 2):
        assert all(g == h and u == v for g, h, u, v in product(range(1, m+1), repeat=4)
                   if u-v+2*(g-h) == 0)
    return {'off_target': positive, 'target': negative, 'unary_marginals_equal': True,
            'Laurent_escape_exponents': [-1, 1], 'M_below_3_is_vacuous': True}


def interaction_graphs():
    """Primal/dual certificates for all 64 pair-scope architectures, M>=3."""
    pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    off = [(1, 2, 3, 1), (2, 1, 1, 3)]
    targets = [[(1, 1, 3, 3), (2, 2, 1, 1)],
               [(1, 1, 1, 1), (2, 2, 3, 3)]]
    # (scope set, legal quadratic monomials), one witness per sufficient pattern.
    candidates = [({(0, 1)}, [(1, (0, 0)), (-2, (0, 1)), (1, (1, 1))]),
                  ({(2, 3)}, [(1, (2, 2)), (-2, (2, 3)), (1, (3, 3))]),
                  ({(1, 2), (1, 3)}, [(1, (0, 0)), (-1, (1, 1)), (1, (1, 2)), (-1, (1, 3))]),
                  ({(0, 2), (0, 3)}, [(1, (1, 1)), (-1, (0, 0)), (-1, (0, 2)), (1, (0, 3))]),
                  ({(0, 2), (1, 2)}, [(1, (3, 3)), (-1, (2, 2)), (-4, (0, 2)), (4, (1, 2))]),
                  ({(0, 3), (1, 3)}, [(1, (2, 2)), (-1, (3, 3)), (4, (0, 3)), (-4, (1, 3))])]
    successes, failures = 0, []
    support = [s for s in product(range(1, 8), repeat=4) if s[2]-s[3]+2*(s[0]-s[1]) == 0]
    for bits in product((0, 1), repeat=6):
        edges = {p for p, bit in zip(pairs, bits) if bit}
        found = next((terms for scopes, terms in candidates if scopes <= edges), None)
        if found is not None:
            assert all(i == j or (i, j) in edges for _, (i, j) in found)
            for s in support:
                w = sum(c*s[i]*s[j] for c, (i, j) in found)
                assert w >= 0 and ((w == 0) == (s[0] == s[1] and s[2] == s[3]))
            successes += 1
        else:
            # A pair-feature trade also preserves all unary marginals.
            t = next(t for t in targets if all(
                sorted((s[i], s[j]) for s in off) == sorted((s[i], s[j]) for s in t)
                for i, j in edges))
            assert all(sorted(s[i] for s in off) == sorted(s[i] for s in t) for i in range(4))
            failures.append({'edges': [pairs[i] for i, bit in enumerate(bits) if bit], 'target_trade': t})
    assert successes == 57 and len(failures) == 7
    return {'variable_order': ['g', 'h', 'u', 'v'], 'architectures': 64,
            'quadratic_primal_certificates': successes, 'balanced_trade_obstructions': failures,
            'finite_support_check_M': 7, 'general_scope': 'all M>=3, by written proof'}


def tensor_checks():
    # The fixed reverse-pair obstruction survives at the target sum degree.
    off = [(1, 2, 3, 1), (2, 1, 1, 3)]
    signed = [g-h for g, h, u, v in off]
    shifted = [x+6 for x in signed]
    squares = [(g-h)**2 for g, h, u, v in off]
    assert sum(signed) == 0 and sum(shifted) == 12 and sum(squares) == 2
    # An explicit multi-grading and positive integral scalar collapse.
    weights, c = [(1, 0), (-1, 2), (0, 1)], (1, 1)
    defects = [sum(x*y for x, y in zip(v, c)) for v in weights]
    assert all(x > 0 for x in defects)
    # A dual bad-product certificate, with all multiplicities one.
    bad_weights = [(1, 0), (-1, 1), (0, -1)]
    assert all(sum(v[j] for v in bad_weights) == 0 for j in range(2))
    return {'two_factor_signed_defect': signed, 'two_factor_shifted_degrees_M7': shifted,
            'shifted_target_degree': 12, 'two_factor_square_defects': squares,
            'positive_multigrading': weights, 'positive_separator': c,
            'collapsed_defects': defects, 'bad_multigrading': bad_weights,
            'bad_product_multiplicities': [1, 1, 1],
            'scope': 'explicit primal/dual examples; general equivalence proved in manuscript'}


def mul(a, b):
    """F8 in polynomial-bit basis with modulus t^3+t+1."""
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 8:
            a ^= 11
    return out


def fpow(a, n):
    out = 1
    for _ in range(n):
        out = mul(out, a)
    return out


def fsum(xs):
    out = 0
    for x in xs:
        out ^= x
    return out


def rank8(matrix):
    rows = [list(row) for row in matrix]
    rank = 0
    for c in range(len(rows[0])):
        k = next((i for i in range(rank, len(rows)) if rows[i][c]), None)
        if k is None:
            continue
        rows[rank], rows[k] = rows[k], rows[rank]
        inv = fpow(rows[rank][c], 6)
        rows[rank] = [mul(x, inv) for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank:
                v = rows[i][c]
                rows[i] = [x ^ mul(v, y) for x, y in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def hole_check():
    assert all(mul(a, fpow(a, 6)) == 1 for a in range(1, 8))
    # Independent polynomial irreducibility criterion for a cubic: no F2 root.
    assert all((x**3+x+1) % 2 for x in (0, 1))
    good = [(a, 0) for a in range(4)] + [(0, 1)]
    bad = [(a, 0) for a in range(5)]
    basis = [(i, j) for i in range(4) for j in range(4-i)]
    def evaluation(holes):
        return [[mul(fpow(x, i), fpow(y, j)) for i, j in basis] for x, y in holes]
    assert rank8(evaluation(good)) == 5
    assert rank8(evaluation(bad)) == 4
    def lagrange(i, x):
        num, den = 1, 1
        for j in range(4):
            if j != i:
                num, den = mul(num, x ^ j), mul(den, i ^ j)
        return mul(num, fpow(den, 6))
    def values(point):
        x, y = point
        return [lagrange(i, x) ^ mul(lagrange(i, 0), y) for i in range(4)] + [y]
    identity = [[int(i == j) for j in range(5)] for i in range(5)]
    assert [values(o) for o in good] == identity
    def gram(points):
        vs = [values(p) for p in points]
        return [[fsum(mul(v[i], v[j]) for v in vs) for j in range(5)] for i in range(5)]
    universe = list(product(range(8), repeat=2))
    assert gram([p for p in universe if p not in good]) == identity  # -I=I in F8.
    lines = [[(x, mul(s, x) ^ b) for x in range(8)] for s, b in product(range(8), repeat=2)]
    lines += [[(b, y) for y in range(8)] for b in range(8)]
    assert all(not any(any(row) for row in gram(line)) for line in lines)
    weights = []
    for i in range(5):
        denominator = 1
        for j in range(5):
            if i != j:
                denominator = mul(denominator, i ^ j)
        weights.append(fpow(denominator, 6))
    moments = [fsum(mul(w, fpow(i, k)) for i, w in enumerate(weights)) for k in range(5)]
    assert moments == [0, 0, 0, 0, 1]
    return {'q': 8, 'n': 2, 'd': 3, 'm': 5, 'modulus_bits': 11,
            'good_holes': good, 'bad_holes': bad, 'evaluation_ranks': [5, 4],
            'bad_left_kernel': weights, 'bad_moments_0_through_4': moments,
            'full_affine_lines_checked': len(lines), 'punctured_Gram': identity}


def report():
    return {'status': 'exact_classical_baseline',
            'scope': 'fixed local architectures, not headline theorems or AI causality',
            'unary_obstruction': trade_check(),
            'interaction_graph_classification': interaction_graphs(),
            'tensor_stability': tensor_checks(),
            'coefficient_synthesis': [synthesize_square(c) for c in (2, 3)],
            'hole_geometry': hole_check()}


if __name__ == '__main__':
    print(json.dumps(report(), indent=2, sort_keys=True))

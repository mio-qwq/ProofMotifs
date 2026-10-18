#!/usr/bin/env python3
"""Exact finite feature repair with adaptive trade cuts.

Classical facial separation and finite Benders-style search. The reference
oracle enumerates convex-hull faces and makes no polynomial-time claim.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from math import lcm
from pathlib import Path
import argparse
import json


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), Q(0))


def solve(a, b, n):
    rows = [[Q(x) for x in row] + [Q(y)] for row, y in zip(a, b)]
    pivots = []
    for col in range(n):
        found = next((i for i in range(len(pivots), len(rows)) if rows[i][col]), None)
        if found is None:
            continue
        r = len(pivots)
        rows[r], rows[found] = rows[found], rows[r]
        scale = rows[r][col]
        rows[r] = [x/scale for x in rows[r]]
        for i in range(len(rows)):
            if i != r:
                scale = rows[i][col]
                rows[i] = [x-scale*y for x, y in zip(rows[i], rows[r])]
        pivots.append(col)
    if any(not any(row[:n]) and row[n] for row in rows):
        return None, len(pivots)
    answer = [Q(0)]*n
    for r, col in enumerate(pivots):
        answer[col] = rows[r][n]
    assert all(dot(row, answer) == Q(y) for row, y in zip(a, b))
    return answer, len(pivots)


def matrix(instance, mask):
    rows = list(instance['base_rows'])
    for j, block in enumerate(instance['blocks']):
        if mask >> j & 1:
            rows.extend(block['rows'])
    return [[Q(x) for x in row] for row in rows]


def oracle(instance, mask):
    """Return a verified selector or normalized signed trade, using only rationals."""
    n = len(instance['omega'])
    target = sorted(instance['target_indices'])
    assert target and len(set(target)) == len(target) and all(0 <= i < n for i in target)
    a = matrix(instance, mask)
    assert all(len(row) == n for row in a)
    r = len(a)
    columns = [tuple(row[j] for row in a) for j in range(n)]
    off = [j for j in range(n) if j not in target]
    if not off:
        return {'kind': 'selector', 'coefficients': ['0']*r, 'weights': ['0']*n,
                'faces_examined': 0}
    orthogonal = []
    for j in target:
        v = list(columns[j])
        for u in orthogonal:
            t = dot(v, u)/dot(u, u)
            v = [x-t*y for x, y in zip(v, u)]
        if any(v):
            orthogonal.append(v)
    projected = []
    for j in off:
        v = list(columns[j])
        for u in orthogonal:
            t = dot(v, u)/dot(u, u)
            v = [x-t*y for x, y in zip(v, u)]
        projected.append(v)
    examined = 0
    for size in range(1, min(len(off), r+1)+1):
        for support in combinations(range(len(off)), size):
            examined += 1
            vectors = [projected[i] for i in support]
            kkt = [[dot(v, w) for w in vectors] + [-1] for v in vectors]
            kkt.append([1]*size+[0])
            solution, rank = solve(kkt, [0]*size+[1], size+1)
            if solution is None or rank != size+1 or any(x < 0 for x in solution[:size]):
                continue
            lam = solution[:size]
            p = [sum((t*v[k] for t, v in zip(lam, vectors)), Q(0)) for k in range(r)]
            norm = dot(p, p)
            if any(dot(p, v) < norm for v in projected):
                continue
            if norm:
                c = [x/norm for x in p]
                weights = [dot(c, v) for v in columns]
                scale = lcm(*(x.denominator for x in weights))
                c = [x*scale for x in c]
                weights = [x*scale for x in weights]
                result = {'kind': 'selector', 'coefficients': list(map(str, c)),
                          'weights': list(map(str, weights)), 'faces_examined': examined}
            else:
                trade = [Q(0)]*n
                for i, t in zip(support, lam):
                    trade[off[i]] = t
                rhs = [-dot(row, trade) for row in a]
                target_coeffs, _ = solve([[row[j] for j in target] for row in a], rhs, len(target))
                assert target_coeffs is not None
                for j, t in zip(target, target_coeffs):
                    trade[j] = t
                result = {'kind': 'trade', 'trade': list(map(str, trade)),
                          'faces_examined': examined}
            verify(instance, mask, result)
            return result
    raise AssertionError('Finite-hull closest point must have an affinely independent support')


def verify(instance, mask, certificate):
    a = matrix(instance, mask)
    target = set(instance['target_indices'])
    n = len(instance['omega'])
    if certificate['kind'] == 'selector':
        c = list(map(Q, certificate['coefficients']))
        assert len(c) == len(a)
        w = [sum((c[i]*a[i][j] for i in range(len(a))), Q(0)) for j in range(n)]
        assert w == list(map(Q, certificate['weights']))
        assert all(w[j] == 0 if j in target else w[j] >= 1 for j in range(n))
        assert all(x.denominator == 1 for x in w)
    else:
        assert certificate['kind'] == 'trade'
        z = list(map(Q, certificate['trade']))
        assert len(z) == n and all(dot(row, z) == 0 for row in a)
        assert all(z[j] >= 0 for j in range(n) if j not in target)
        assert sum(z[j] for j in range(n) if j not in target) == 1


def cost(instance, mask):
    return sum((Q(b['cost']) for j, b in enumerate(instance['blocks']) if mask >> j & 1), Q(0))


def optimize(instance):
    p = len(instance['blocks'])
    assert all(Q(b['cost']) >= 0 for b in instance['blocks'])
    full = (1 << p)-1
    full_certificate = oracle(instance, full)
    if full_certificate['kind'] == 'trade':
        return {'status': 'dictionary_impossible', 'full_mask': full,
                'certificate': full_certificate, 'oracle_calls': 1}
    ordered = sorted(range(1 << p), key=lambda m: (cost(instance, m), m))
    cuts, history, master_scans = [], [], 0
    for _ in range(1 << p):
        incumbent = None
        for mask in ordered:
            master_scans += 1
            if all(mask & cut for cut in cuts):
                incumbent = mask
                break
        assert incumbent is not None  # the full mask remains feasible
        cert = oracle(instance, incumbent)
        if cert['kind'] == 'selector':
            return {'status': 'optimal', 'mask': incumbent, 'cost': str(cost(instance, incumbent)),
                    'selected': [b['name'] for j, b in enumerate(instance['blocks']) if incumbent >> j & 1],
                    'certificate': cert, 'history': history,
                    'oracle_calls': len(history)+2, 'master_masks_examined': master_scans}
        z = list(map(Q, cert['trade']))
        cut = sum(1 << j for j, b in enumerate(instance['blocks'])
                  if any(dot(list(map(Q, row)), z) for row in b['rows']))
        assert cut and not incumbent & cut and cut not in cuts
        cuts.append(cut)
        history.append({'mask': incumbent, 'cost': str(cost(instance, incumbent)),
                        'trade': cert, 'mandatory_cut_mask': cut})
    raise AssertionError('Each trade cut excludes its current mask')


def exhaustive(instance):
    calls = 0
    ordered = sorted(range(1 << len(instance['blocks'])), key=lambda m: (cost(instance, m), m))
    for mask in ordered:
        calls += 1
        cert = oracle(instance, mask)
        if cert['kind'] == 'selector':
            return {'status': 'optimal', 'mask': mask, 'cost': str(cost(instance, mask)), 'oracle_calls': calls}
    return {'status': 'dictionary_impossible', 'oracle_calls': calls}


def grid_instance():
    points = list(product((-1, 0, 1), repeat=2))
    monomials = list(product(range(3), repeat=2))
    def row(e):
        return [x**e[0]*y**e[1] for x, y in points]
    return {'id': 'coordinate-zero-union', 'omega': points,
            'target_indices': [j for j, s in enumerate(points) if 0 in s],
            'base_rows': [row(e) for e in monomials if sum(e) <= 1],
            'blocks': [{'name': 'monomial_'+str(e[0])+str(e[1]),
                        'cost': 5 if e == (2, 2) else 1, 'rows': [row(e)]}
                       for e in monomials if sum(e) >= 2]}


def report(panel):
    instances = list(panel['panels'])+[grid_instance()]
    lower = grid_instance()
    lower['id'] = 'coordinate-zero-union-without-top'
    lower['blocks'] = [b for b in lower['blocks'] if b['name'] != 'monomial_22']
    instances.append(lower)
    results = []
    for instance in instances:
        result, baseline = optimize(instance), exhaustive(instance)
        assert result['status'] == baseline['status']
        if result['status'] == 'optimal':
            assert result['cost'] == baseline['cost'] and result['mask'] == baseline['mask']
        results.append({'id': instance['id'], 'adaptive': result, 'exhaustive': baseline})
    return {'scope': 'exact designed calibration, not held-out transfer or speedup claim',
            'oracle': 'rational target-span projection and convex-hull face enumeration',
            'panels': results}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--panel', default=str(Path(__file__).resolve().parents[1]/'research/experiments/feature-repair-panel.json'))
    args = parser.parse_args()
    with open(args.panel) as stream:
        panel = json.load(stream)
    print(json.dumps(report(panel), indent=2, sort_keys=True))

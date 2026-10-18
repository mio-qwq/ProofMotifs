#!/usr/bin/env python3
"""Exact DAG rational-tuple compilation; classical degree/valuation bounds.

An entry is a sum of explicitly labelled edges num(t)/prod q_j(t)^e_j.
Vertices are supplied in topological order. p=0 means Q; otherwise p is a
PROMISED prime. Complexity is output-sensitive in degrees and jet length,
not polynomial in binary-encoded exponents alone. No factoring is needed.
"""
from fractions import Fraction
import argparse
import json


def scalar(x, p):
    if not isinstance(x, (int, str, Fraction)):
        raise ValueError('Exact integer or rational coefficient required')
    q = Fraction(x)
    if not p:
        return q
    if q.denominator % p == 0:
        raise ValueError('Undefined rational specialization at this prime')
    return q.numerator*pow(q.denominator, -1, p) % p


def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def poly(a, p):
    if not a:
        raise ValueError('Polynomial coefficient list must be nonempty')
    return trim([scalar(x, p) for x in a])


def mul(a, b, p, length=None):
    size = len(a)+len(b)-1
    if length is not None:
        size = min(size, length)
    c = [scalar(0, p) for _ in range(size)]
    for i, x in enumerate(a):
        for j, y in enumerate(b[:max(0, size-i)]):
            c[i+j] += x*y
            if p:
                c[i+j] %= p
    return trim(c)


def power(a, k, p, length=None):
    c = [scalar(1, p)]
    while k:
        if k & 1:
            c = mul(c, a, p, length)
        a = mul(a, a, p, length)
        k >>= 1
    return c


def inverse_jet(q, length, p):
    q = poly(q, p)
    if not q[0]:
        raise ValueError('Denominator must be regular at zero')
    inv = pow(q[0], -1, p) if p else 1/q[0]
    out = [inv]
    for k in range(1, length):
        v = -inv*sum((q[i]*out[k-i] for i in range(1, min(k+1, len(q)))), scalar(0, p))
        out.append(v % p if p else v)
    return trim(out)


def normalized(instance):
    p, m, n = instance['p'], instance['vertices'], instance['variables']
    if any(type(x) is not int for x in (p, m, n)) or p < 0 or p == 1 or m < 1 or n < 1:
        raise ValueError('Expected Q or promised prime field and positive dimensions')
    qs = [poly(q, p) for q in instance['denominators']]
    if any(not q[0] for q in qs):
        raise ValueError('All denominators must be units at zero')
    edges = []
    for raw in instance['edges']:
        e = dict(raw)
        if any(type(e[key]) is not int for key in ('src', 'dst', 'var')) or not (0 <= e['src'] < e['dst'] < m and 0 <= e['var'] < n):
            raise ValueError('All edges must follow the common topological order')
        if len(e['exp']) != len(qs) or any(type(k) is not int or k < 0 for k in e['exp']):
            raise ValueError('Expected nonnegative denominator exponents')
        e['num'] = poly(e['num'], p)
        if any(e['num']):
            edges.append(e)
    return p, m, n, qs, edges


def longest(m, edges, weights):
    """Paths may start/end anywhere; empty paths have weight zero."""
    best = [0]*m
    outgoing = [[] for _ in range(m)]
    for e, w in zip(edges, weights):
        outgoing[e['src']].append((e['dst'], w))
    for v in range(m):
        for dst, w in outgoing[v]:
            best[dst] = max(best[dst], best[v]+w)
    return max(best)


def analyze(instance):
    p, m, n, qs, edges = normalized(instance)
    maxima = [longest(m, edges, [e['exp'][j] for e in edges]) for j in range(len(qs))]
    costs = [len(e['num'])-1-sum(k*(len(q)-1) for k, q in zip(e['exp'], qs)) for e in edges]
    excess = longest(m, edges, costs)
    degree = sum(k*(len(q)-1) for k, q in zip(maxima, qs))
    return {'max_exponents': maxima, 'denominator_degree': degree,
            'max_degree_excess': excess, 'jet_length': 1+degree+excess,
            'compiled_dimension': m*(1+degree+excess),
            'nonzero_edges': len(edges), 'prime_is_promised': bool(p)}


def verify_bound(instance, certificate):
    """Recompute DAG bounds; reject understated or altered certificates."""
    expected = analyze(instance)
    if certificate != expected:
        raise ValueError('Incorrect path/degree certificate')
    return True


def entry_jets(instance, length):
    p, m, n, qs, edges = normalized(instance)
    if length < 1:
        raise ValueError('Positive jet length required')
    result = [[[[scalar(0, p)] for _ in range(m)] for _ in range(m)] for _ in range(n)]
    inverses = [inverse_jet(q, length, p) for q in qs]
    for e in edges:
        v = e['num'][:length]
        for q, k in zip(inverses, e['exp']):
            v = mul(v, power(q, k, p, length), p, length)
        old = result[e['var']][e['src']][e['dst']]
        size = max(len(old), len(v))
        total = [(old[j] if j < len(old) else 0)+(v[j] if j < len(v) else 0) for j in range(size)]
        result[e['var']][e['src']][e['dst']] = trim([x % p if p else x for x in total])
    return result


def compile_tuple(instance):
    certificate = analyze(instance)
    length = certificate['jet_length']
    p, m, n, _, _ = normalized(instance)
    jets = entry_jets(instance, length)
    size = m*length
    out = [[[scalar(0, p) for _ in range(size)] for _ in range(size)] for _ in range(n)]
    for var in range(n):
        for u in range(m):
            for v in range(m):
                coeff = jets[var][u][v]
                for a in range(length):
                    for b in range(a+1):
                        if a-b < len(coeff):
                            out[var][u*length+a][v*length+b] = coeff[a-b]
    return certificate, out


def demo():
    # Arrival-vertex denominator reuse: h factors once, not h copies of all.
    panels = []
    for h in (2, 4, 8, 16, 32):
        instance = {'p': 0, 'vertices': h+1, 'variables': 1,
                    'denominators': [[1, -j] for j in range(1, h+1)],
                    'edges': [{'src': u, 'dst': v, 'var': 0, 'num': [1],
                               'exp': [int(j == v) for j in range(1, h+1)]}
                              for u in range(h+1) for v in range(u+1, h+1)]}
        cert = analyze(instance)
        verify_bound(instance, cert)
        panels.append({'h': h, 'paths_0_to_h': 2**(h-1),
                       'path_aware_jet_bound': cert['jet_length'],
                       'naive_repeated_global_denominator_bound': h*h+1})
    return {'classification': 'classical DAG degree bound plus faithful regular representation',
            'panels': panels, 'not_claimed': 'minimal jets, speedup over strongest classical baseline, or new theory'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--demo', action='store_true', required=True)
    parser.parse_args()
    print(json.dumps(demo(), sort_keys=True, indent=2))

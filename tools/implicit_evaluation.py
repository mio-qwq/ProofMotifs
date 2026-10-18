#!/usr/bin/env python3
"""Classical degree-filtered evaluation closure, Q or prime fields.

Input is raw distinct affine points, NOT a monomial dictionary. At most n*m
coordinate products are offered. The output finite multiplication certificate
checks degree completeness for ALL polynomial targets. This is a reference
Buchberger--Moeller-style/evaluation-algebra construction, not a novelty claim.
"""
from fractions import Fraction
from itertools import product
from math import comb, isqrt
import json

CONTRACT = 'explicit affine points; minimum total degree for every value target'


class Field:
    def __init__(self, p=0):
        if type(p) is not int or p < 0 or p == 1 or (p and any(p % i == 0 for i in range(2, isqrt(p)+1))):
            raise ValueError('0 for Q or a prime modulus; no composite field')
        self.p = p

    def parse(self, x):
        if isinstance(x, bool) or isinstance(x, float):
            raise ValueError('No floats or Boolean scalars')
        if self.p:
            if type(x) is not int:
                raise ValueError('Prime-field input uses integers')
            return x % self.p
        return Fraction(x)

    def red(self, x):
        return x % self.p if self.p else x

    def inv(self, x):
        if not x:
            raise ValueError('Division by zero')
        return pow(x, -1, self.p) if self.p else Fraction(1)/x


def parsed_points(points, f):
    if not points or not points[0]:
        raise ValueError('Nonempty points and positive ambient dimension required')
    n = len(points[0])
    if any(len(row) != n for row in points):
        raise ValueError('Ragged points')
    points = [tuple(f.parse(x) for x in row) for row in points]
    if len(set(points)) != len(points):
        raise ValueError('Points must remain distinct over the declared field')
    return points


def dot(a, b, f):
    return f.red(sum(x*y for x, y in zip(a, b)))


def inverse(a, f):
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError('Square matrix required')
    rows = [list(row)+[f.parse(int(i == j)) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        k = next((k for k in range(j, n) if rows[k][j]), None)
        if k is None:
            raise ValueError('Singular evaluation matrix')
        rows[j], rows[k] = rows[k], rows[j]
        u = f.inv(rows[j][j])
        rows[j] = [f.red(x*u) for x in rows[j]]
        for k in range(n):
            if k != j:
                u = rows[k][j]
                rows[k] = [f.red(x-u*y) for x, y in zip(rows[k], rows[j])]
    return [row[n:] for row in rows]


def value(exponent, point, f):
    ans = f.parse(1)
    for x, power in zip(point, exponent):
        ans = f.red(ans*x**power)
    return ans


def construct(points, p=0):
    f = Field(p)
    points = parsed_points(points, f)
    m, n = len(points), len(points[0])
    monomials, columns = [], []
    reducers = []

    def accept(column):
        v = list(column)
        for pivot, row in reducers:
            u = v[pivot]
            v = [f.red(x-u*y) for x, y in zip(v, row)]
        pivot = next((j for j, x in enumerate(v) if x), None)
        if pivot is None:
            return False
        u = f.inv(v[pivot])
        reducers.append((pivot, [f.red(x*u) for x in v]))
        return True

    one = [f.parse(1)]*m
    assert accept(one)
    monomials.append((0,)*n)
    columns.append(one)
    frontier, offers = [0], 0
    while len(columns) < m:
        new = []
        for j in frontier:
            for i in range(n):
                offers += 1
                column = [f.red(h[i]*x) for h, x in zip(points, columns[j])]
                if accept(column):
                    exponent = list(monomials[j])
                    exponent[i] += 1
                    new.append(len(columns))
                    monomials.append(tuple(exponent))
                    columns.append(column)
                if len(columns) == m:
                    break
            if len(columns) == m:
                break
        if not new:
            raise AssertionError('Complete affine-point layer plateau cannot be deficient')
        frontier = new
    assert offers <= n*m
    evaluation = list(map(list, zip(*columns)))
    inv = inverse(evaluation, f)
    degrees = list(map(sum, monomials))
    transitions = []
    for i in range(n):
        matrix = []
        for column in columns:
            v = [f.red(h[i]*x) for h, x in zip(points, column)]
            matrix.append([dot(row, v, f) for row in inv])
        transitions.append(matrix)
    target_degrees, witnesses = [], []
    for i in range(m):
        d = max(degrees[j] for j in range(m) if inv[j][i])
        j = next(j for j in range(m) if degrees[j] == d and inv[j][i])
        target_degrees.append(d)
        witnesses.append({'basis_row': j, 'annihilator': inv[j], 'target_pairing': inv[j][i]})
    d = max(degrees)
    return {'contract': CONTRACT, 'field_modulus': p, 'monomials': monomials,
            'inverse_evaluation': inv, 'multiplication_coordinates': transitions,
            'minimum_common_degree': d, 'cardinal_minimum_degrees': target_degrees,
            'dual_minimality_witnesses': witnesses,
            'hilbert_profile': [sum(e <= k for e in degrees) for k in range(d+1)],
            'observed_coordinate_offers': offers, 'proved_offer_bound': n*m}


def verify(points, certificate, p=0):
    """Check finite filtration/multiplication data, without calling construct."""
    try:
        c = certificate
        if c['contract'] != CONTRACT:
            raise ValueError('Wrong target contract')
        if c['field_modulus'] != p or type(c['field_modulus']) is not int:
            raise ValueError('Certificate cannot change the caller-declared field')
        f = Field(p)
        points = parsed_points(points, f)
        m, n = len(points), len(points[0])
        monomials = c['monomials']
        if len(monomials) != m or any(len(e) != n or any(type(x) is not int or x < 0 for x in e) for e in monomials):
            raise ValueError('Invalid formal monomials')
        degrees = list(map(sum, monomials))
        if min(degrees) != 0 or max(degrees) > m-1:
            raise ValueError('Constant or affine degree bound missing')
        E = [[value(e, h, f) for e in monomials] for h in points]
        inv = [[f.parse(x) for x in row] for row in c['inverse_evaluation']]
        if len(inv) != m or any(len(row) != m for row in inv):
            raise ValueError('Wrong inverse size')
        for i in range(m):
            for j in range(m):
                if dot(E[i], [inv[k][j] for k in range(m)], f) != int(i == j):
                    raise ValueError('Not an inverse evaluation matrix')
        transitions = c['multiplication_coordinates']
        if len(transitions) != n:
            raise ValueError('All coordinate multipliers must be covered')
        for i, matrix in enumerate(transitions):
            if len(matrix) != m:
                raise ValueError('All basis borders must be covered')
            for j, coefficients in enumerate(matrix):
                coefficients = [f.parse(x) for x in coefficients]
                if len(coefficients) != m:
                    raise ValueError('Wrong border size')
                if any(x and degrees[k] > degrees[j]+1 for k, x in enumerate(coefficients)):
                    raise ValueError('Filtration-unsafe representation')
                if any(dot(row, coefficients, f) != f.red(h[i]*row[j]) for row, h in zip(E, points)):
                    raise ValueError('False border identity')
        d = max(degrees)
        actual = [max(degrees[j] for j in range(m) if inv[j][i]) for i in range(m)]
        if type(c['minimum_common_degree']) is not int or any(type(x) is not int for x in c['cardinal_minimum_degrees']):
            raise ValueError('Degree metadata must be integral')
        if c['minimum_common_degree'] != d or c['cardinal_minimum_degrees'] != actual:
            raise ValueError('Wrong minimum degrees')
        if any(type(x) is not int for x in c['hilbert_profile']) or c['hilbert_profile'] != [sum(e <= k for e in degrees) for k in range(d+1)]:
            raise ValueError('Wrong Hilbert profile')
        if type(c['proved_offer_bound']) is not int or c['proved_offer_bound'] != n*m:
            raise ValueError('Wrong theoretical offer bound')
        observed = c['observed_coordinate_offers']
        if type(observed) is not int or not 0 <= observed <= n*m:
            raise ValueError('Malformed offer telemetry (actual execution not replayed here)')
        ws = c['dual_minimality_witnesses']
        if len(ws) != m:
            raise ValueError('Witness count')
        for i, w in enumerate(ws):
            j = w['basis_row']
            if type(j) is not int or not 0 <= j < m or degrees[j] != actual[i] or not inv[j][i]:
                raise ValueError('Wrong dual row')
            if [f.parse(x) for x in w['annihilator']] != inv[j] or f.parse(w['target_pairing']) != inv[j][i]:
                raise ValueError('False dual witness')
        return True, 'all polynomial degrees certified by multiplication closure'
    except (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError) as error:
        return False, str(error)


def jsonable(x):
    if isinstance(x, Fraction):
        return str(x)
    if isinstance(x, dict):
        return {k: jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    return x


def demo():
    cases = []
    raw = [([[0, 0], [1, 0], [0, 1], [1, 1], [2, 3]], 0),
           ([[j]+[0]*19 for j in range(7)], 0),
           ([list(h)+[0]*37 for h in product([0, 1], repeat=3)], 11),
           ([list(h) for h in product([0, 1], repeat=3)], 2),
           ([[0, 0], [0, 1]], 0)]
    for points, p in raw:
        c = construct(points, p)
        assert verify(points, c, p)[0]
        assert verify(jsonable(points), json.loads(json.dumps(jsonable(c))), p)[0]
        m, n, d = len(points), len(points[0]), c['minimum_common_degree']
        cases.append({'m': m, 'n': n, 'p': p, 'points': points, 'certificate': c,
                      'ambient_total_degree_dictionary_size': comb(n+d, d),
                      'all_coordinate_offers_bound': n*m,
                      'prime_field_197_degree_budget': (p-2)//2 if p else None,
                      'legal_197_cardinal_gram': 2*d <= p-2 if p else None})
    return {'status': 'PASS', 'cases': cases,
            'scope': 'classical raw-point implicit grammar discovery; not a sparse/locality optimizer or unread transfer'}


if __name__ == '__main__':
    print(json.dumps(jsonable(demo()), indent=2, sort_keys=True))

#!/usr/bin/env python3
"""Independent deterministic DAG-jet stress panel for PM-SUCCINCT-C.

Run:
  python3 tools/acyclic_jet_independent.py

This persists the exact previous panel's generation order and random draws:
seed 11631, fields Q/F2/F3/F5/F7, sixteen instances per field, and eight
polynomial combinations per instance. The path-expansion and polynomial
arithmetic below do not call production arithmetic or production DP helpers.
Only analyze(), entry_jets(), and parser-facing entry points are under test.
Finite checks supplement, and do not replace, the mathematical proof.
"""

import argparse
import copy
from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import random
import sys


def norm(a, p):
    a = [(x % p if p else Fraction(x)) for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b, p):
    return norm([
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(max(len(a), len(b)))
    ], p)


def mul(a, b, p):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return norm(c, p)


def pw(a, k, p):
    b = [1]
    for _ in range(k):
        b = mul(b, a, p)
    return b


def mm(a, b, p, length):
    m = len(a)
    c = [[[0] for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(m):
                c[i][j] = add(c[i][j], mul(a[i][k], b[k][j], p)[:length], p)
    return c


def expect_value_error(action, description):
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Expected ValueError: ' + description)


def parser_checks(aj):
    """Regression checks for the corrected exact-coefficient input contract."""
    checks = 0
    assert aj.scalar(Fraction(1, 2), 3) == 2
    checks += 1
    assert aj.scalar('1/2', 3) == 2
    checks += 1
    assert aj.scalar(Fraction(1, 2), 0) == Fraction(1, 2)
    checks += 1
    for p in (0, 3):
        expect_value_error(lambda p=p: aj.scalar(0.5, p), 'floating coefficient')
        checks += 1
    expect_value_error(lambda: aj.scalar(Fraction(1, 2), 2), 'undefined bad prime')
    checks += 1

    base = {
        'p': 3, 'vertices': 2, 'variables': 1, 'denominators': [],
        'edges': [{'src': 0, 'dst': 1, 'var': 0,
                   'num': [Fraction(1, 2)], 'exp': []}],
    }
    assert aj.entry_jets(base, 1)[0][0][1] == [2]
    checks += 1
    for key, value in (('p', 3.0), ('vertices', 2.0), ('variables', 1.5),
                       ('vertices', True)):
        instance = copy.deepcopy(base)
        instance[key] = value
        expect_value_error(lambda instance=instance: aj.analyze(instance),
                           'noninteger dimension/characteristic ' + key)
        checks += 1
    for key, value in (('src', 0.0), ('dst', 1.0), ('var', 0.0)):
        instance = copy.deepcopy(base)
        instance['edges'][0][key] = value
        expect_value_error(lambda instance=instance: aj.analyze(instance),
                           'noninteger edge index ' + key)
        checks += 1
    instance = copy.deepcopy(base)
    instance['denominators'] = [[1, 1]]
    instance['edges'][0]['exp'] = [1.0]
    expect_value_error(lambda: aj.analyze(instance), 'noninteger exponent')
    checks += 1
    instance = copy.deepcopy(base)
    instance['p'] = 2
    expect_value_error(lambda: aj.analyze(instance),
                       'undefined bad prime through instance parser')
    checks += 1
    return checks


def stress_panel(aj):
    rng = random.Random(11631)
    instances = 0
    word_checks = 0
    polynomial_checks = 0
    for p in (0, 2, 3, 5, 7):
        for trial in range(16):
            m = rng.choice((2, 3, 4))
            n = 2
            qs = [[1, 1], [1, 2, 1]]
            edges = []
            for i in range(m):
                for j in range(i + 1, m):
                    for var in range(n):
                        for _ in range(rng.randrange(3)):
                            edges.append({
                                'src': i, 'dst': j, 'var': var,
                                'num': [rng.randrange(-2, 3)
                                        for _ in range(rng.randrange(1, 4))],
                                'exp': [rng.randrange(3), rng.randrange(3)],
                            })
            instance = {
                'p': p, 'vertices': m, 'variables': n,
                'denominators': qs, 'edges': edges,
            }
            certificate = aj.analyze(instance)
            length = certificate['jet_length']
            maxima = certificate['max_exponents']
            denominator = [1]
            for q, k in zip(qs, maxima):
                denominator = mul(denominator, pw(q, k, p), p)
            jets = aj.entry_jets(instance, length)
            cleared_words = []
            jet_words = []
            for ell in range(m + 1):
                for word in product(range(n), repeat=ell):
                    exact = [[[0] for _ in range(m)] for _ in range(m)]

                    def paths(start, at, pos, numerator, exponents):
                        if pos == len(word):
                            missing = numerator
                            for q, maximum, k in zip(qs, maxima, exponents):
                                assert maximum >= k
                                missing = mul(missing, pw(q, maximum - k, p), p)
                            exact[start][at] = add(exact[start][at], missing, p)
                            return
                        for edge in edges:
                            if (edge['src'] == at and edge['var'] == word[pos]
                                    and any(norm(edge['num'], p))):
                                paths(start, edge['dst'], pos + 1,
                                      mul(numerator, edge['num'], p),
                                      [a + b for a, b in
                                       zip(exponents, edge['exp'])])

                    for start in range(m):
                        paths(start, start, 0, [1], [0, 0])
                    z = [[[int(i == j)] for j in range(m)] for i in range(m)]
                    for var in word:
                        z = mm(z, jets[var], p, length)
                    for i in range(m):
                        for j in range(m):
                            assert len(exact[i][j]) <= length, (
                                p, instance, certificate, word, i, j, exact[i][j])
                            dz = mul(denominator, z[i][j], p)[:length]
                            assert norm(dz, p) == norm(exact[i][j], p), (
                                p, word, dz, exact[i][j])
                    cleared_words.append(exact)
                    jet_words.append(z)
                    word_checks += 1
            for _ in range(8):
                coefficients = [rng.randrange(-2, 3) for _ in cleared_words]
                left = [[[0] for _ in range(m)] for _ in range(m)]
                right = [[[0] for _ in range(m)] for _ in range(m)]
                for coefficient, a, b in zip(coefficients, cleared_words, jet_words):
                    for i in range(m):
                        for j in range(m):
                            left[i][j] = add(
                                left[i][j], [coefficient * x for x in a[i][j]], p)
                            right[i][j] = add(
                                right[i][j], [coefficient * x for x in b[i][j]], p)
                assert (
                    any(any(x for x in cell) for row in left for cell in row)
                    == any(any(x for x in cell) for row in right for cell in row)
                )
                polynomial_checks += 1
            instances += 1

    assert (instances, word_checks, polynomial_checks) == (80, 1408, 640)
    return {
        'seed': 11631,
        'instances': instances,
        'word_checks': word_checks,
        'random_polynomial_checks': polynomial_checks,
        'fields': [0, 2, 3, 5, 7],
        'parallel_edges': True,
        'shared_non_coprime_denominators': True,
        'result': 'PASS',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', default=str(Path(__file__).resolve().parents[1]))
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    sys.path.insert(0, str(repo))
    from tools import acyclic_jet as aj
    result = stress_panel(aj)
    result['corrected_parser_checks'] = parser_checks(aj)
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()

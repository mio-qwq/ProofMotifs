#!/usr/bin/env python3
"""Exact independent controls for the polynomial-seed operator obstruction."""
from fractions import Fraction as Q
from itertools import product
import json
import importlib.util
from pathlib import Path
import sys


def clean(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a


def add(a, b):
    c = [Q(0)]*max(len(a), len(b))
    for j, x in enumerate(a):
        c[j] += x
    for j, x in enumerate(b):
        c[j] += x
    return clean(c)


def mul(a, b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            c[j+k] += x*y
    return clean(c)


def scaled(a, c):
    return clean([c*x for x in a])


def rank(rows):
    a = [list(map(Q, row)) for row in rows]
    r = 0
    for j in range(len(a[0])):
        pivot = next((k for k in range(r, len(a)) if a[k][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        a[r] = [x/a[r][j] for x in a[r]]
        for k in range(r+1, len(a)):
            a[k] = [x-a[k][j]*y for x, y in zip(a[k], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def word_matrix(seeds, length, d, q=Q(2)):
    """Paths are applied rightmost letter first; T=q^m stays symbolic."""
    count = (d-1)*length+1
    rows = {}
    for word in product(range(len(seeds)), repeat=length):
        paths = [(0, (), Q(1))]
        for letter in reversed(word):
            paths = [(s+a, visits+(s+a,), c*b)
                     for s, visits, c in paths
                     for a, b in seeds[letter].items() if b]
        numerators = {s: [Q(0)] for s in range(length, d*length+1)}
        for s, visits, c in paths:
            assert len(visits) == length and len(set(visits)) == length
            assert all(1 <= r <= d*length for r in visits)
            numerator = [c]
            for r in range(1, d*length+1):
                if r not in visits:
                    numerator = mul(numerator, [-1, q**r])
            assert len(numerator)-1 <= (d-1)*length
            numerators[s] = add(numerators[s], numerator)
        rows[word] = [numerators[s][j] if j < len(numerators[s]) else Q(0)
                      for s in range(length, d*length+1) for j in range(count)]
        assert len(rows[word]) == count**2
    return rows


def monomial_action(word, m, q=Q(2)):
    """For A=J_z, B=J_(z^2), return final degree and exact coefficient."""
    coefficient = Q(1)
    for letter in reversed(word):
        m += 1 if letter == 'A' else 2
        coefficient /= q**m-1
    return m, coefficient


def bivariate_sum(*parts):
    ans = {}
    for part in parts:
        for key, c in part.items():
            ans[key] = ans.get(key, 0)+c
    return {key: c for key, c in ans.items() if c}


def bivariate_mul(a, b):
    ans = {}
    for (i, j), c in a.items():
        for (k, ell), d in b.items():
            key = i+k, j+ell
            ans[key] = ans.get(key, 0)+c*d
    return {key: c for key, c in ans.items() if c}


def cleared_monomial_word(word, total_shift):
    """D_s(T)*word(z^m)/z^(m+s), as an exact polynomial in Z[q,T]."""
    visits, shift = set(), 0
    for letter in reversed(word):
        shift += 1 if letter == 'A' else 2
        visits.add(shift)
    assert shift == total_shift
    ans = {(0, 0): 1}
    for r in range(1, total_shift+1):
        if r not in visits:
            ans = bivariate_mul(ans, {(r, 1): 1, (0, 0): -1})
    return ans


def apply_polynomial(seed, input_poly, q=Q(2)):
    a = mul(seed, input_poly)
    assert a[0] == 0
    return [Q(0)]+[a[j]/(q**j-1) for j in range(1, len(a))]


def main():
    # Universal raw rational certificate over Z[q,T], not numeric evidence:
    # after multiplying by product_(r=1..4)(q^r T-1), the three denominators
    # leave respectively qT-1, q^2T-1 and q^3T-1.
    q = {(1, 0): 1}
    q_plus_one_negative = {(1, 0): -1, (0, 0): -1}
    remainder = bivariate_sum(
        bivariate_mul(q, {(1, 1): 1, (0, 0): -1}),
        bivariate_mul(q_plus_one_negative, {(2, 1): 1, (0, 0): -1}),
        {(3, 1): 1, (0, 0): -1})
    assert remainder == {}

    # Stronger mixed relation BA-qAB=(q-1)A^3, universal over Z[q,T].
    mixed = bivariate_sum(
        cleared_monomial_word('BA', 3),
        bivariate_mul({(1, 0): -1}, cleared_monomial_word('AB', 3)),
        {(1, 0): -1, (0, 0): 1})
    assert mixed == {}

    # C=B+A^2. Expand each C block and verify the full PBW action formula.
    universal_pbw_cases = 0
    for i in range(5):
        for j in range(5):
            s = i+2*j
            numerator = bivariate_sum(*[
                cleared_monomial_word('A'*i+''.join(blocks), s)
                for blocks in product(['B', 'AA'], repeat=j)])
            assert numerator == {(j*j, j): 1}
            universal_pbw_cases += 1

    # Orientation and noncommutativity controls on exact monomial actions.
    for m in range(20):
        terms = [monomial_action(w, m) for w in ['AAB', 'ABA', 'BAA']]
        assert {s for s, _ in terms} == {m+4}
        assert 2*terms[0][1]-3*terms[1][1]+terms[2][1] == 0
    companion = (monomial_action('BBA', 0)[1]-3*monomial_action('BAB', 0)[1]
                 +2*monomial_action('ABB', 0)[1])
    assert companion == Q(2, 1395)

    # Cubic relation embedded in the exact all-path cleared-coefficient matrix.
    cubic = word_matrix([{1: Q(1)}, {2: Q(1)}], 3, 2)
    assert rank(list(cubic.values())) == 7
    assert add(add(scaled(cubic[(0, 0, 1)], 2),
                   scaled(cubic[(0, 1, 0)], -3)), cubic[(1, 0, 0)]) == [0]

    # General non-monomial seeds: 64 length-six words land in <=49 dimensions.
    matrix = word_matrix([{1: Q(1), 2: Q(2)}, {1: Q(3), 2: Q(-1)}], 6, 2)
    general_rank = rank(list(matrix.values()))
    assert len(matrix) == 64 and general_rank <= 49

    # Nonzero unary polynomial seed of order two has strictly increasing orders.
    h, unary_orders = [Q(1)], []
    for k in range(1, 8):
        h = apply_polynomial([0, 0, 3, 1], h)
        order = next(j for j, c in enumerate(h) if c)
        expected = Q(3)**k
        for r in range(1, k+1):
            expected /= 2**(2*r)-1
        assert order == 2*k and h[order] == expected
        unary_orders.append(order)

    # Cross-check the coordinator's generic constructor with independently
    # enumerated path polynomials, never its own symbolic verifier alone.
    root_path = Path(__file__).resolve().with_name('q_polynomial_obstruction.py')
    sys.path.insert(0, str(root_path.parent))
    spec = importlib.util.spec_from_file_location('pm_q_polynomial_root_audit', root_path)
    root = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(root)
    root_panels = []
    for dictionary in [[[0, 1], [0, 0, 1]], [[0, 1, 2], [0, 3, -1]],
                       [[0, 3], [0, -2]], [[0], [0, 1]]]:
        certificate = root.construct(dictionary)
        length, d = certificate['word_length'], certificate['degree_bound']
        seeds = [{j: Q(c) for j, c in enumerate(b) if c} for b in dictionary]
        independent = word_matrix(seeds, length, d)
        total = [Q(0)]*certificate['coordinate_bound']
        for word, coefficient in certificate['terms']:
            total = add(total, scaled(independent[tuple(word)], coefficient))
        assert not any(total)
        assert root.verify_identity(dictionary, certificate['terms'])[0]
        root_panels.append({'length': length, 'terms': len(certificate['terms']),
                            'words_examined': certificate['words_examined'],
                            'coordinate_bound': certificate['coordinate_bound']})
    bad = [(tuple(w), c) for w, c in root.construct([[0, 1], [0, 0, 1]])['terms']]
    bad[0] = bad[0][0], bad[0][1]+1
    assert not root.verify_identity([[0, 1], [0, 0, 1]], bad)[0]

    print(json.dumps({'status': 'PASS',
                      'universal_Z_q_T_cubic_remainder': remainder,
                      'universal_Z_q_T_mixed_relation_remainder': mixed,
                      'universal_Z_q_T_PBW_formula_cases': universal_pbw_cases,
                      'q2_cubic_monomials_checked': 20,
                      'q2_cubic_operator_matrix_rank': 7,
                      'q2_nonmonomial_length6': {'word_count': 64, 'ambient_bound': 49,
                                                'actual_exact_rank': general_rank},
                      'down_up_companion_on_1': str(companion)+'*z^5 (NONZERO)',
                      'root_generic_certificates_independently_checked': root_panels,
                      'root_corrupted_identity_rejected': True,
                      'unary_order2_leading_orders': unary_orders}, indent=2))


if __name__ == '__main__':
    main()

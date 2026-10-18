#!/usr/bin/env python3
"""Exact Q, q=2 seed selection for STRONG rational-coefficient word freeness.

Input rational seeds have zero value at0 and a verified complete split-pole
factorization. This does not factor arbitrary polynomials. General theory is
field-parametric; this executable does NOT use finite-field q of infinite order.
Residual reduction + weighted linear-matroid greedy are classical baselines.
"""
from fractions import Fraction as Q
from itertools import combinations
from math import comb
import json

CONTRACT = 'strong K(z)-word-freeness, not necessity for basic K-faithfulness'


def scalar(x):
    if not isinstance(x, (int, str, Q)) or isinstance(x, bool):
        raise ValueError('Exact rational required')
    return Q(x)


def trim(a):
    a = list(a)
    while len(a) > 1 and not a[-1]:
        a.pop()
    return a or [Q(0)]


def poly(a):
    if not isinstance(a, (list, tuple)) or not a:
        raise ValueError('Nonempty polynomial coefficients required')
    return trim(list(map(scalar, a)))


def add(a, b):
    return trim([(a[j] if j < len(a) else 0)+(b[j] if j < len(b) else 0)
                 for j in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c*x for x in a])


def mul(a, b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def power(a, k):
    out = [Q(1)]
    for _ in range(k):
        out = mul(out, a)
    return out


def exact_div(a, b):
    a = trim(a)
    b = trim(b)
    if not any(b):
        raise ValueError('Zero divisor')
    out = [Q(0)]*max(1, len(a)-len(b)+1)
    while any(a) and len(a) >= len(b):
        j, c = len(a)-len(b), a[-1]/b[-1]
        out[j] += c
        a = add(a, [0]*j+scale(b, -c))
    if any(a):
        raise ValueError('Inexact factorization division')
    return trim(out)


def coordinates(columns, target):
    """Fresh exact linear solve; free coordinates set to zero."""
    rows = [[v[i] for v in columns]+[target[i]] for i in range(len(target))]
    m, pivots = len(columns), []
    for col in range(m):
        p = next((j for j in range(len(pivots), len(rows)) if rows[j][col]), None)
        if p is None:
            continue
        j = len(pivots)
        rows[j], rows[p] = rows[p], rows[j]
        a = rows[j][col]
        rows[j] = [x/a for x in rows[j]]
        for h in range(len(rows)):
            if h != j:
                a = rows[h][col]
                rows[h] = [x-a*y for x, y in zip(rows[h], rows[j])]
        pivots.append(col)
    if any(not any(row[:m]) and row[m] for row in rows):
        return None
    out = [Q(0)]*m
    for i, col in enumerate(pivots):
        out[col] = rows[i][m]
    return out


def valuation_two_integer(a):
    a = abs(a)
    out = 0
    while a % 2 == 0:
        a //= 2
        out += 1
    return out


def orbit(alpha):
    alpha = scalar(alpha)
    if not alpha:
        raise ValueError('Poles must be nonzero')
    j = valuation_two_integer(alpha.numerator)-valuation_two_integer(alpha.denominator)
    return alpha/(Q(2)**j), j


def decompose(seed):
    num, den = poly(seed['num']), poly(seed['den'])
    if not den[0] or num[0]:
        raise ValueError('Seed must be regular and zero at0')
    entries, seen = [], set()
    product_den, declared = [Q(1)], []
    for pole in seed['poles']:
        alpha, order = scalar(pole['alpha']), pole['order']
        if not alpha or alpha in seen or type(order) is not int or order < 1:
            raise ValueError('Distinct nonzero poles and positive integral orders required')
        seen.add(alpha)
        declared.append((alpha, order))
    if sum(k for _, k in declared) != len(den)-1:
        raise ValueError('Declared split degrees do not match the raw denominator')
    for alpha, order in declared:
        product_den = mul(product_den, power([1, -1/alpha], order))
        entries.extend((alpha, k) for k in range(1, order+1))
    if den != scale(product_den, den[0]):
        raise ValueError('Incomplete or incorrect split denominator certificate')
    degree = max(len(den), len(num))-1
    columns, tags = [], []
    for r in range(1, max(0, len(num)-len(den))+1):
        columns.append([0]*r+den)
        tags.append(('poly', r))
    for alpha, k in entries:
        columns.append(add(exact_div(den, power([1, -1/alpha], k)), scale(den, -1)))
        tags.append(('phi', alpha, k))
    columns = [(a+[0]*(degree+1))[:degree+1] for a in columns]
    target = (num+[0]*(degree+1))[:degree+1]
    answer = coordinates(columns, target)
    if answer is None:
        raise ValueError('Partial fraction extraction failed')
    pp, terms = [Q(0)], []
    for tag, c in zip(tags, answer):
        if not c:
            continue
        if tag[0] == 'poly':
            pp += [Q(0)]*max(0, tag[1]+1-len(pp))
            pp[tag[1]] = c
        else:
            terms.append({'alpha': tag[1], 'order': tag[2], 'coefficient': c})
    return {'poly': trim(pp), 'terms': terms}


def residual(dec):
    out = {}
    for term in dec['terms']:
        alpha, _ = orbit(term['alpha'])
        key = (alpha, term['order'])
        out[key] = out.get(key, Q(0))+term['coefficient']
    return {k: v for k, v in out.items() if v}


def combine(decs, coefficients):
    pp, terms = [Q(0)], {}
    for dec, c in zip(decs, coefficients):
        pp = add(pp, scale(dec['poly'], c))
        for term in dec['terms']:
            key = (term['alpha'], term['order'])
            terms[key] = terms.get(key, Q(0))+c*term['coefficient']
    return {'poly': pp, 'terms': [{'alpha': a, 'order': k, 'coefficient': c}
                                for (a, k), c in sorted(terms.items()) if c]}


def telescoper(dec):
    if dec['poly'][0]:
        raise ValueError('Normalized seed decomposition must have zero constant')
    if residual(dec):
        raise ValueError('Nonzero orbit residue blocks rational summation')
    pp = [c/(Q(2)**r-1) if r else Q(0) for r, c in enumerate(dec['poly'])]
    grouped, terms = {}, []
    for term in dec['terms']:
        alpha, j = orbit(term['alpha'])
        key = (alpha, term['order'])
        grouped.setdefault(key, {})[j] = grouped.setdefault(key, {}).get(j, Q(0))+term['coefficient']
    for (alpha, k), coefficients in sorted(grouped.items()):
        running = Q(0)
        for j in range(min(coefficients), max(coefficients)+1):
            running += coefficients.get(j, Q(0))
            if running:
                terms.append({'alpha': alpha*Q(2)**(j+1), 'order': k, 'coefficient': running})
        if running:
            raise ValueError('Unclosed finite chain')
    return {'poly': trim(pp), 'terms': terms}


def shift_difference(dec):
    pp = [c*(Q(2)**r-1) for r, c in enumerate(dec['poly'])]
    terms = []
    for x in dec['terms']:
        terms.extend([dict(x, alpha=x['alpha']/2), dict(x, coefficient=-x['coefficient'])])
    return combine([{'poly': pp, 'terms': terms}], [Q(1)])


def synthesize(seeds, target):
    if type(target) is not int or target < 0:
        raise ValueError('Nonnegative target rank required')
    costs = [scalar(x['cost']) for x in seeds]
    if any(x < 0 for x in costs):
        raise ValueError('Nonnegative costs required')
    decs = [decompose(x) for x in seeds]
    rs = [residual(x) for x in decs]
    rows = sorted(set().union(*(set(x) for x in rs))) if rs else []
    columns = [[x.get(row, Q(0)) for row in rows] for x in rs]
    basis, accepted = [], []
    for i in sorted(range(len(seeds)), key=lambda j: (costs[j], j)):
        if coordinates([columns[j] for j in basis], columns[i]) is None:
            basis.append(i)
            if len(accepted) < target:
                accepted.append(i)
    repairs = []
    for i in range(len(seeds)):
        cs = coordinates([columns[j] for j in basis], columns[i])
        coeff = [Q(0)]*len(seeds)
        coeff[i] += 1
        for j, c in zip(basis, cs):
            coeff[j] -= c
        defect = combine(decs, coeff)
        anti = telescoper(defect)
        if shift_difference(anti) != defect:
            raise AssertionError('Telescoper identity')
        repairs.append({'seed': i, 'basis_coordinates': cs, 'telescoper': anti})
    return {'contract': CONTRACT,
            'status': 'selected' if len(basis) >= target else 'strong_rank_insufficient',
            'target_rank': target, 'quotient_rank': len(basis), 'basis': basis,
            'selected': accepted if len(basis) >= target else [],
            'cost': sum((costs[i] for i in accepted), Q(0)) if len(basis) >= target else None,
            'rows': rows, 'columns': columns, 'decompositions': decs, 'repairs': repairs}


def seed_from_parts(name, cost, pp, terms):
    den, poles = [Q(1)], {}
    for a, k, c in terms:
        if type(k) is not int or k < 1 or not scalar(a):
            raise ValueError('Nonzero pole and positive integral order required')
        if c:
            a = scalar(a)
            poles[a] = max(k, poles.get(a, 0))
    for a, k in sorted(poles.items()):
        den = mul(den, power([1, -1/a], k))
    num = mul(poly(pp), den)
    for a, k, c in terms:
        if not c:
            continue
        num = add(num, scale(add(exact_div(den, power([1, -1/scalar(a)], k)), scale(den, -1)), scalar(c)))
    return {'name': name, 'cost': cost, 'num': num, 'den': den,
            'poles': [{'alpha': a, 'order': k} for a, k in sorted(poles.items())]}


def verify(seeds, target, certificate):
    """Recheck input, rank/greedy decisions and raw rational telescoper identities.

    Does not call synthesize(). Linear solve/polynomial primitives are shared;
    an independent executable comparison is provided separately.
    """
    try:
        if certificate['contract'] != CONTRACT:
            raise ValueError('Incorrect certificate contract')
        if type(target) is not int or target < 0 or certificate['target_rank'] != target:
            raise ValueError('Target rank')
        costs = [scalar(x['cost']) for x in seeds]
        if any(c < 0 for c in costs):
            raise ValueError('Negative cost')
        decs = [decompose(x) for x in seeds]
        rs = [residual(x) for x in decs]
        rows = sorted(set().union(*(set(x) for x in rs))) if rs else []
        columns = [[x.get(row, Q(0)) for row in rows] for x in rs]
        for key, expected in [('rows', rows), ('columns', columns), ('decompositions', decs)]:
            if jsonable(certificate[key]) != jsonable(expected):
                raise ValueError('False '+key)
        basis = []
        for i in sorted(range(len(seeds)), key=lambda j: (costs[j], j)):
            if coordinates([columns[j] for j in basis], columns[i]) is None:
                basis.append(i)
        ok = len(basis) >= target
        if certificate['basis'] != basis or certificate['quotient_rank'] != len(basis):
            raise ValueError('False quotient rank or basis')
        if certificate['status'] != ('selected' if ok else 'strong_rank_insufficient'):
            raise ValueError('Incorrect strong-contract status')
        selected = basis[:target] if ok else []
        if certificate['selected'] != selected:
            raise ValueError('Not the minimum-cost greedy selection')
        if ok and scalar(certificate['cost']) != sum((costs[j] for j in selected), Q(0)):
            raise ValueError('Incorrect cost')
        if not ok and certificate['cost'] is not None:
            raise ValueError('Spurious feasible cost')
        if len(certificate['repairs']) != len(seeds):
            raise ValueError('Missing repair certificate')
        for i, repair in enumerate(certificate['repairs']):
            if repair['seed'] != i:
                raise ValueError('Repair index')
            cs = list(map(scalar, repair['basis_coordinates']))
            if len(cs) != len(basis) or any(sum((cs[k]*columns[j][h] for k, j in enumerate(basis)), Q(0)) != columns[i][h] for h in range(len(rows))):
                raise ValueError('Repair quotient coordinates')
            target_num, target_den = poly(seeds[i]['num']), poly(seeds[i]['den'])
            for j, c in zip(basis, cs):
                target_num = add(mul(target_num, poly(seeds[j]['den'])), scale(mul(poly(seeds[j]['num']), target_den), -c))
                target_den = mul(target_den, poly(seeds[j]['den']))
            anti = repair['telescoper']
            if poly(anti['poly'])[0]:
                raise ValueError('Telescoper normalization')
            rational = seed_from_parts('certificate', 0, anti['poly'],
                                       [(x['alpha'], x['order'], scalar(x['coefficient'])) for x in anti['terms']])
            a, b = rational['num'], rational['den']
            aq = [x*Q(2)**r for r, x in enumerate(a)]
            bq = [x*Q(2)**r for r, x in enumerate(b)]
            left = mul(add(mul(aq, b), scale(mul(a, bq), -1)), target_den)
            right = mul(target_num, mul(b, bq))
            if left != right:
                raise ValueError('False raw rational telescoper identity')
        return True, 'accepted'
    except (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError) as error:
        return False, str(error)


def demo():
    seeds = [seed_from_parts('same-orbit-expensive', 9, [0], [(3, 1, 1)]),
             seed_from_parts('same-orbit-cheap', 2, [0], [(6, 1, 1)]),
             seed_from_parts('exact-difference', 0, [0], [(3, 1, 1), (6, 1, -1)]),
             seed_from_parts('different-order', 3, [0], [(3, 2, 1)]),
             seed_from_parts('mixed-orbits', 4, [0], [(3, 1, 1), (5, 1, 1)]),
             seed_from_parts('independent-fifth', 7, [0], [(5, 1, 1)]),
             seed_from_parts('exact-polynomial', 0, [0, 1], [])]
    out = synthesize(seeds, 3)
    assert out['selected'] == [1, 3, 4] and out['cost'] == 9
    assert verify(seeds, 3, out)[0], verify(seeds, 3, out)
    trials = []
    for r in range(5):
        candidate = synthesize(seeds, r)
        assert verify(seeds, r, candidate)[0]
        feasible = []
        for chosen in combinations(range(len(seeds)), r):
            cols = [out['columns'][i] for i in chosen]
            independent = all(coordinates(cols[:j], cols[j]) is None for j in range(len(cols)))
            if independent:
                feasible.append(sum(scalar(seeds[i]['cost']) for i in chosen))
        assert (candidate['status'] == 'selected') == bool(feasible)
        if feasible:
            assert candidate['cost'] == min(feasible)
        trials.append({'r': r, 'feasible_subsets': len(feasible), 'minimum_cost': min(feasible) if feasible else None})
    return {'example': out, 'same_input_exhaustive_control': trials,
            'classification': 'classical rational q-residues + minimum-weight linear matroid; strong contract only',
            'not_claimed': 'finite prefix or finite matrix hitting point, new theory, or held-out success'}


def jsonable(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    return x


if __name__ == '__main__':
    print(json.dumps(jsonable(demo()), sort_keys=True, indent=2))

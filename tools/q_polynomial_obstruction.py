#!/usr/bin/env python3
"""Symbolic all-input operator identities for polynomial seeds over Q, q=2.

Each word is represented by shift bands of polynomials in T=2^m after
clearing a common denominator. This certifies all formal series, not sampled
monomials. Reference rank solves are classical; no novelty/speedup claim.
"""
from fractions import Fraction as Q
from itertools import islice, product
import json
if __package__:
    from . import q_seed_synthesis as qs
else:
    import q_seed_synthesis as qs


def normalized(seeds):
    seeds = [qs.poly(b) for b in seeds]
    if any(b[0] for b in seeds):
        raise ValueError('Polynomial seeds must vanish at0')
    return seeds


def denominator(degree):
    out = [Q(1)]
    for r in range(1, degree+1):
        out = qs.mul(out, [Q(-1), Q(2)**r])
    return out


def word_array(seeds, word):
    seeds = normalized(seeds)
    d = max([1]+[len(b)-1 for b in seeds])
    current, old_den = {0: [Q(1)]}, [Q(1)]
    for length, letter in enumerate(reversed(word), 1):
        if type(letter) is not int or not 0 <= letter < len(seeds):
            raise ValueError('Invalid word letter')
        new_den, new = denominator(d*length), {}
        extra = qs.exact_div(new_den, old_den)
        for shift, num in current.items():
            for r in range(1, len(seeds[letter])):
                coefficient = seeds[letter][r]
                if not coefficient:
                    continue
                s = shift+r
                term = qs.exact_div(qs.mul(num, extra), [-1, Q(2)**s])
                new[s] = qs.add(new.get(s, [Q(0)]), qs.scale(term, coefficient))
        current, old_den = new, new_den
    return current, old_den, d


def verify_identity(seeds, terms):
    """Verify a nonzero free polynomial is a zero OPERATOR symbolically."""
    try:
        seeds = normalized(seeds)
        if not terms:
            raise ValueError('Nonempty identity required')
        polynomial = {}
        for word, coefficient in terms:
            word, coefficient = tuple(word), qs.scalar(coefficient)
            polynomial[word] = polynomial.get(word, Q(0))+coefficient
        polynomial = {w: c for w, c in polynomial.items() if c}
        if not polynomial:
            raise ValueError('Free polynomial is zero')
        max_length = max(map(len, polynomial))
        d = max([1]+[len(b)-1 for b in seeds])
        common = denominator(d*max_length)
        total = {}
        for word, c in polynomial.items():
            bands, den, _ = word_array(seeds, word)
            extra = qs.exact_div(common, den)
            for shift, num in bands.items():
                total[shift] = qs.add(total.get(shift, [Q(0)]), qs.scale(qs.mul(num, extra), c))
        if any(any(num) for num in total.values()):
            raise ValueError('Nonzero operator numerator')
        return True, 'all-input rational-band identity'
    except (ValueError, TypeError, IndexError, ZeroDivisionError) as error:
        return False, str(error)


def construct(seeds):
    seeds = normalized(seeds)
    n = len(seeds)
    if n < 2:
        raise ValueError('At least two polynomial letters required')
    d = max([1]+[len(b)-1 for b in seeds])
    length = 1
    while n**length <= ((d-1)*length+1)**2:
        length += 1
    size = ((d-1)*length+1)**2
    basis, columns = [], []
    for word in islice(product(range(n), repeat=length), size+1):
        bands, _, _ = word_array(seeds, word)
        column = []
        for shift in range(length, d*length+1):
            num = bands.get(shift, [Q(0)])
            if len(num) > (d-1)*length+1:
                raise AssertionError('Degree budget')
            column.extend((num+[Q(0)]*((d-1)*length+1))[:(d-1)*length+1])
        cs = qs.coordinates(columns, column)
        if cs is not None:
            terms = [(w, -c) for w, c in zip(basis, cs) if c]+[(word, Q(1))]
            assert verify_identity(seeds, terms)[0]
            return {'word_length': length, 'degree_bound': d, 'coordinate_bound': size,
                    'words_examined': len(basis)+1, 'terms': terms,
                    'contract': 'zero operator on all Q[[z]], q=2, not just value on1'}
        basis.append(word)
        columns.append(column)
    raise AssertionError('Dimension pigeonhole')


def demo():
    seeds = [[0, 1], [0, 0, 1]]
    # A=J_z, B=J_(z^2); composition is rightmost first.
    explicit = [((1, 0), 1), ((0, 1), -2), ((0, 0, 0), -1)]
    cubic = [((0, 0, 1), 2), ((0, 1, 0), -3), ((1, 0, 0), 1)]
    assert verify_identity(seeds, explicit)[0]
    assert verify_identity(seeds, cubic)[0]
    # The other superficially matching down-up relation is NOT an identity.
    wrong = [((1, 1, 0), 1), ((1, 0, 1), -3), ((0, 1, 1), 2)]
    assert not verify_identity(seeds, wrong)[0]
    panels = []
    for dictionary in [seeds, [[0, 1, 1], [0, 2, -1]], [[0, 3], [0, -2]], [[0], [0, 1]]]:
        panels.append(construct(dictionary))
    return {'classification': 'polynomial seed grammar cannot encode a free algebra on two or more letters',
            'explicit_BA_minus_2AB_minus_A3': explicit, 'homogeneous_cubic': cubic,
            'false_companion_relation_rejected': True, 'generic_symbolic_certificates': panels,
            'not_claimed': 'arbitrary rational seeds fail, or a new theorem of quantum algebra'}


if __name__ == '__main__':
    print(json.dumps(qs.jsonable(demo()), sort_keys=True, indent=2))

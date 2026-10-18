#!/usr/bin/env python3
"""Independent exact controls for PM-Q-C; final cross-audit imports the constructor.

Q rational identities use cross multiplication of polynomial pairs. Positive
characteristic uses the genuine infinite-order q=t in F_3(t), never a numeric
finite-field element. Finite jets below are controls, not infinite proofs.
"""

from fractions import Fraction as Q
from itertools import combinations, product
from math import comb
from random import Random
import json
import importlib.util
from copy import deepcopy
from pathlib import Path


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a) or (Q(0),)


def padd(a, b):
    c = [Q(0)] * max(len(a), len(b))
    for j, v in enumerate(a):
        c[j] += v
    for j, v in enumerate(b):
        c[j] += v
    return trim(c)


def pscale(a, c):
    return trim([v*c for v in a])


def pmul(a, b):
    c = [Q(0)] * (len(a)+len(b)-1)
    for j, x in enumerate(a):
        for k, y in enumerate(b):
            c[j+k] += x*y
    return trim(c)


def ppow(a, n):
    r = (Q(1),)
    for _ in range(n):
        r = pmul(r, a)
    return r


def radd(a, b):
    return padd(pmul(a[0], b[1]), pmul(b[0], a[1])), pmul(a[1], b[1])


def rscale(a, c):
    return pscale(a[0], c), a[1]


def rshift(a, q=Q(2)):
    return tuple(c*q**j for j, c in enumerate(a[0])), tuple(c*q**j for j, c in enumerate(a[1]))


def req(a, b):
    return pmul(a[0], b[1]) == pmul(b[0], a[1])


ZERO = ((Q(0),), (Q(1),))


def phi(alpha, order):
    den = ppow((Q(1), -1/Q(alpha)), order)
    return padd((Q(1),), pscale(den, -1)), den


def rat_of_terms(terms, poly=None):
    ans = (trim(poly or [Q(0)]), (Q(1),))
    for (alpha, order), coefficient in terms.items():
        ans = radd(ans, rscale(phi(alpha, order), coefficient))
    return ans


def orbit(alpha):
    """alpha=odd-core * 2**exponent; signed core is canonical."""
    alpha = Q(alpha)
    assert alpha
    n, d, exponent = alpha.numerator, alpha.denominator, 0
    while n % 2 == 0:
        n //= 2
        exponent += 1
    while d % 2 == 0:
        d //= 2
        exponent -= 1
    return Q(n, d), exponent


def residues(terms):
    ans = {}
    for (alpha, order), c in terms.items():
        core, _ = orbit(alpha)
        key = core, order
        ans[key] = ans.get(key, Q(0)) + c
    return {key: c for key, c in ans.items() if c}


def antiterms(terms):
    """Return finite-support normalized-pole certificate iff residues vanish."""
    if residues(terms):
        return None
    blocks = {}
    for (alpha, order), c in terms.items():
        core, j = orbit(alpha)
        block = blocks.setdefault((core, order), {})
        block[j] = block.get(j, Q(0)) + c
    ans = {}
    for (core, order), block in blocks.items():
        running = Q(0)
        for j in range(min(block), max(block)+1):
            if running:
                ans[core*Q(2)**j, order] = running
            running += block.get(j, Q(0))
        assert running == 0
    return ans


def rank(rows):
    if not rows:
        return 0
    a = [list(row) for row in rows]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j] != 0), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = a[r][j]
        a[r] = [x/v for x in a[r]]
        for i in range(len(a)):
            if i != r:
                v = a[i][j]
                a[i] = [x-v*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def jet(rational, count):
    num, den = rational
    assert den[0]
    a = []
    for j in range(count):
        value = num[j] if j < len(num) else Q(0)
        value -= sum(den[k]*a[j-k] for k in range(1, min(j, len(den)-1)+1))
        a.append(value/den[0])
    return a


def word_jets(seed_jets, max_length, count, q):
    zero, one = q-q, q/q
    words = {(): [one]+[zero]*(count-1)}
    for length in range(1, max_length+1):
        for w in product(range(len(seed_jets)), repeat=length):
            b, h = seed_jets[w[0]], words[w[1:]]
            coefficient = [sum((b[k]*h[j-k] for k in range(j+1)), zero) for j in range(count)]
            words[w] = [zero]+[coefficient[j]/(q**j-one) for j in range(1, count)]
    return words


# A separate implementation of the coefficient field F_3(t).
P = 3


def mt(a):
    a = [x % P for x in a]
    while len(a) > 1 and not a[-1]:
        a.pop()
    return tuple(a) or (0,)


def ma(a, b):
    c = [0]*max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return mt(c)


def mm(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return mt(c)


def ms(a, c):
    return mt([x*c for x in a])


def md(a, b):
    a = list(mt(a))
    b = mt(b)
    assert b != (0,)
    quotient = [0]*max(1, len(a)-len(b)+1)
    while tuple(a) != (0,) and len(a) >= len(b):
        j = len(a)-len(b)
        v = a[-1]*pow(b[-1], -1, P) % P
        quotient[j] = v
        for k, c in enumerate(b):
            a[j+k] = (a[j+k]-v*c) % P
        a = list(mt(a))
    return mt(quotient), mt(a)


def mg(a, b):
    while b != (0,):
        a, b = b, md(a, b)[1]
    return ms(a, pow(a[-1], -1, P))


class FpT:
    def __init__(self, num=0, den=(1,)):
        if isinstance(num, FpT):
            self.num, self.den = num.num, num.den
            return
        num = (num,) if isinstance(num, int) else num
        num, den = mt(num), mt(den)
        assert den != (0,)
        g = mg(num, den)
        num, den = md(num, g)[0], md(den, g)[0]
        v = pow(den[-1], -1, P)
        self.num, self.den = ms(num, v), ms(den, v)

    def __add__(self, other):
        other = FpT(other)
        return FpT(ma(mm(self.num, other.den), mm(other.num, self.den)), mm(self.den, other.den))

    __radd__ = __add__

    def __neg__(self):
        return FpT(ms(self.num, -1), self.den)

    def __sub__(self, other):
        return self + -FpT(other)

    def __rsub__(self, other):
        return FpT(other) + -self

    def __mul__(self, other):
        other = FpT(other)
        return FpT(mm(self.num, other.num), mm(self.den, other.den))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = FpT(other)
        assert other.num != (0,)
        return FpT(mm(self.num, other.den), mm(self.den, other.num))

    def __rtruediv__(self, other):
        return FpT(other)/self

    def __pow__(self, n):
        ans = FpT(1)
        for _ in range(n):
            ans *= self
        return ans

    def __eq__(self, other):
        other = FpT(other)
        return self.num == other.num and self.den == other.den

    def __repr__(self):
        return f"FpT({self.num}/{self.den})"


def main():
    checks = {}
    # High-order poles and gaps: verify certificate as a full rational identity.
    terms = {(Q(1, 8), 3): Q(1), (Q(1, 2), 3): Q(-5), (Q(2), 3): Q(4)}
    poly = [Q(0), Q(7), Q(0), Q(5)]
    gterms = antiterms(terms)
    gpoly = [Q(0), Q(7), Q(0), Q(5, 7)]
    b, g = rat_of_terms(terms, poly), rat_of_terms(gterms, gpoly)
    assert req(radd(rshift(g), rscale(g, -1)), b)
    checks['gapped_repeated_pole_certificate'] = {'order': 3, 'nonzero_g_poles': len(gterms)}

    # Two distinct locations in one orbit are dependent; a different order is not.
    same = {(Q(1), 1): Q(1), (Q(2), 1): Q(-1)}
    assert residues(same) == {}
    assert req(radd(rshift(phi(2, 1)), rscale(phi(2, 1), -1)), rat_of_terms(same))
    assert residues({(Q(1), 1): Q(1), (Q(1), 2): Q(-1)}) != {}
    checks['same_orbit_vs_order'] = 'PASS'

    # Positive polynomial b=z gives a rational relation but a K-free unary orbit.
    words = word_jets([[Q(0), Q(1)]+[Q(0)]*7], 6, 9, Q(2))
    for length in range(1, 7):
        denom = 1
        for s in range(1, length+1):
            denom *= 2**s-1
        expected = [Q(0)]*9
        expected[length] = Q(1, denom)
        assert words[(0,)*length] == expected
    assert rank(list(words.values())) == 7
    checks['polynomial_strong_vs_base_field_boundary'] = {'residue_rank': 0, 'unary_word_jet_rank': 7}

    # Independently generated positive controls; exact full rational identities.
    rng = Random(610031)
    for _ in range(80):
        gterms = {}
        for _ in range(5):
            core = rng.choice([Q(1), Q(3), Q(-5, 7)])
            j, k = rng.randrange(-2, 3), rng.randrange(1, 4)
            key = core*Q(2)**j, k
            gterms[key] = gterms.get(key, Q(0))+rng.randrange(-3, 4)
        bterms = {}
        for (alpha, k), c in gterms.items():
            bterms[alpha/2, k] = bterms.get((alpha/2, k), Q(0))+c
            bterms[alpha, k] = bterms.get((alpha, k), Q(0))-c
        assert residues(bterms) == {}
        certificate = rat_of_terms(antiterms(bterms))
        assert req(radd(rshift(certificate), rscale(certificate, -1)), rat_of_terms(bterms))
        # Adding an isolated orbit/order obstruction must be detected.
        bterms[Q(11), 4] = Q(1)
        assert residues(bterms)[Q(11), 4] == 1
        assert antiterms(bterms) is None
    checks['random_exact_rational_identity_controls'] = 80

    # Weighted matroid selection checked against exhaustive subsets, including
    # zero vectors, negative costs, ties and infeasible target ranks.
    panels = 0
    for _ in range(120):
        m, d = 7, 4
        vectors = [[Q(rng.randrange(-2, 3)) for _ in range(d)] for _ in range(m)]
        vectors[0] = [Q(0)]*d
        costs = [rng.randrange(-5, 9) for _ in range(m)]
        for target in range(6):
            chosen = []
            for j in sorted(range(m), key=lambda j: (costs[j], j)):
                if len(chosen) == target:
                    break
                if rank([vectors[i] for i in chosen+[j]]) > len(chosen):
                    chosen.append(j)
            feasible = [s for s in combinations(range(m), target) if rank([vectors[i] for i in s]) == target]
            assert (len(chosen) == target) == bool(feasible)
            if feasible:
                assert sum(costs[i] for i in chosen) == min(sum(costs[i] for i in s) for s in feasible)
            panels += 1
    checks['greedy_vs_exhaustive_exact_r_target_panels'] = panels

    # Full word controls over Q: seven words, two independent pole orbits.
    count = 11
    words = word_jets([jet(phi(1, 1), count), jet(phi(3, 1), count)], 2, count, Q(2))
    assert rank(list(words.values())) == 7
    checks['Q_q2_two_orbit_length2_jet_rank'] = 7

    # Genuine positive-characteristic coefficient field and infinite-order q.
    t = FpT((0, 1))
    count = 10
    b1 = [FpT(0)]+[FpT(1)]*(count-1)
    b2 = [FpT(int(j > 0 and j % P == 0)) for j in range(count)]
    words = word_jets([b1, b2], 2, count, t)
    h1, h2 = words[(0,)], words[(1,)]
    frobenius = [FpT(0)]*count
    for j in range((count-1)//P+1):
        frobenius[P*j] = h1[j]**P
    assert frobenius == h2
    char_rank = rank(list(words.values()))
    assert char_rank == 7
    checks['F3_t_qt_charp_control'] = {'length2_jet_rank': char_rank, 'h_letter2_equals_h_letter1_cubed_through_jet': count,
                                    'seed_orders': [1, 3], 'interpretation': 'algebraic dependence is not linear word dependence'}

    # A finite-order shift does not have an inverse on positive series.
    assert Q(-1)**2-1 == 0
    checks['finite_order_negative_control'] = 'q=-1: z^2 lies in kernel; Delta^-1 on zK[[z]] does not exist'
    # A non-split rational input is simply outside a split-pole implementation.
    checks['nonsplit_contract_control'] = 'z/(1+z^2) over Q has no rational poles; reject, do not report residue rank zero'

    # Root implementation cross-audit. Build raw rational inputs independently,
    # then verify every extracted decomposition and dependency witness by FULL
    # raw-rational cross multiplication (not its normalized-term checker).
    root_path = str(Path(__file__).resolve().with_name('q_seed_synthesis.py'))
    spec = importlib.util.spec_from_file_location('pm_q_root_audit', root_path)
    root = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(root)

    def root_dec_rat(dec):
        terms = {(Q(x['alpha']), x['order']): Q(x['coefficient']) for x in dec['terms']}
        return rat_of_terms(terms, list(map(Q, dec['poly'])))

    def raw_seed(terms, pp, cost, scalar=Q(1)):
        poles = {}
        for alpha, order in terms:
            poles[alpha] = max(order, poles.get(alpha, 0))
        den = (Q(1),)
        for alpha, order in poles.items():
            den = pmul(den, ppow((Q(1), -1/alpha), order))
        num = pmul(pp, den)
        for (alpha, order), c in terms.items():
            complement = (Q(1),)
            for beta, multiplicity in poles.items():
                complement = pmul(complement, ppow((Q(1), -1/beta), multiplicity-(order if beta == alpha else 0)))
            num = padd(num, pscale(padd(complement, pscale(den, -1)), c))
        return {'num': pscale(num, scalar), 'den': pscale(den, scalar), 'cost': cost,
                'poles': [{'alpha': a, 'order': k} for a, k in poles.items()]}

    audited_seed_count = 0
    audited_witness_count = 0
    for panel in range(40):
        seeds = []
        for i in range(7):
            terms = {}
            for _ in range(4):
                alpha = rng.choice([Q(1), Q(3), Q(-5, 7)])*Q(2)**rng.randrange(-2, 3)
                k = rng.randrange(1, 4)
                terms[alpha, k] = terms.get((alpha, k), Q(0))+rng.randrange(-2, 3)
            pp = [Q(0)]+[Q(rng.randrange(-3, 4)) for _ in range(rng.randrange(4))]
            seeds.append(raw_seed(terms, pp, rng.randrange(9), Q(rng.choice([-3, 1, 5]))))
        answer = root.synthesize(seeds, panel % 5)
        raw = [(tuple(map(Q, s['num'])), tuple(map(Q, s['den']))) for s in seeds]
        for j, dec in enumerate(answer['decompositions']):
            assert req(root_dec_rat(dec), raw[j])
            audited_seed_count += 1
        for repair in answer['repairs']:
            rhs = raw[repair['seed']]
            for j, c in zip(answer['basis'], repair['basis_coordinates']):
                rhs = radd(rhs, rscale(raw[j], -c))
            g = root_dec_rat(repair['telescoper'])
            assert req(radd(rshift(g), rscale(g, -1)), rhs)
            audited_witness_count += 1
        target = answer['target_rank']
        feasible = [s for s in combinations(range(7), target)
                    if rank([answer['columns'][j] for j in s]) == target]
        assert (answer['status'] == 'selected') == bool(feasible)
        if feasible:
            assert answer['cost'] == min(sum(Q(seeds[j]['cost']) for j in s) for s in feasible)

    controls = [
        {'num': [0, 1], 'den': [1, 0, 1], 'poles': [], 'cost': 0},
        {'num': [0, 1], 'den': [1, -1], 'poles': [], 'cost': 0},
        {'num': [0, 1], 'den': [1, -1], 'poles': [{'alpha': 2, 'order': 1}], 'cost': 0},
        {'num': [0, 1], 'den': [1, -1], 'poles': [{'alpha': 1, 'order': 2}], 'cost': 0},
        {'num': [0, 1], 'den': [1, -1], 'poles': [{'alpha': 1, 'order': 1}, {'alpha': 1, 'order': 1}], 'cost': 0},
        {'num': [0, 1], 'den': [1, -1], 'poles': [{'alpha': 0, 'order': 1}], 'cost': 0},
        {'num': [0, 1], 'den': [1, -1], 'poles': [{'alpha': 1, 'order': True}], 'cost': 0},
        {'num': [0, 1], 'den': [1, -1], 'poles': [{'alpha': 1, 'order': 1}], 'cost': -1},
        {'num': [0, 1], 'den': [1, -1], 'poles': [{'alpha': 1, 'order': 1}], 'cost': True},
        {'num': [0, 1], 'den': [0, 1], 'poles': [], 'cost': 0},
        {'num': [1], 'den': [1], 'poles': [], 'cost': 0},
        {'num': [0, 0.5], 'den': [1], 'poles': [], 'cost': 0},
    ]
    for seed in controls:
        try:
            root.synthesize([seed], 1)
        except (ValueError, TypeError, ZeroDivisionError):
            pass
        else:
            raise AssertionError(f'invalid input accepted: {seed}')
    assert root.synthesize([], 0)['status'] == 'selected'
    assert root.synthesize([], 1)['status'] == 'strong_rank_insufficient'
    zero_uncancelled = raw_seed({(Q(1), 3): Q(0)}, [Q(0)], 0)
    assert root.synthesize([zero_uncancelled], 1)['quotient_rank'] == 0
    checks['root_cross_audit'] = {'raw_decompositions_checked': audited_seed_count,
                                'full_rational_dependency_witnesses_checked': audited_witness_count,
                                'invalid_inputs_rejected': len(controls),
                                'zero_and_empty_inputs': 'PASS',
                                'selection_exhaustive_panels': 40}

    # Second snapshot: standalone certificate verification and regressions for
    # both hardening observations. Trap expansion before testing huge invalid
    # orders, so a regression fails immediately instead of allocating memory.
    original_power = root.power
    def forbidden_power(*args):
        raise AssertionError('Expansion occurred before declared degree rejection')
    root.power = forbidden_power
    try:
        try:
            root.decompose({'num': [0, 1], 'den': [1, -1], 'cost': 0,
                            'poles': [{'alpha': 1, 'order': 10**100}]})
        except ValueError:
            pass
        else:
            raise AssertionError('Huge invalid declared order accepted')
    finally:
        root.power = original_power
    try:
        root.telescoper({'poly': [Q(1)], 'terms': []})
    except ValueError:
        pass
    else:
        raise AssertionError('Nonzero helper constant silently discarded')
    for bad_order in [True, 0, -1, Q(1, 2)]:
        try:
            root.seed_from_parts('bad', 0, [0], [(1, bad_order, 1)])
        except ValueError:
            pass
        else:
            raise AssertionError('Invalid helper order accepted')

    seeds = [raw_seed({(Q(1), 1): Q(1)}, [Q(0)], 2),
             raw_seed({(Q(2), 1): Q(1)}, [Q(0)], 1),
             raw_seed({(Q(1), 2): Q(1)}, [Q(0)], 3),
             raw_seed({}, [Q(0), Q(1)], 0)]
    certificate = root.synthesize(seeds, 2)
    assert root.verify(seeds, 2, certificate)[0]
    json_seeds = json.loads(json.dumps(root.jsonable(seeds)))
    json_certificate = json.loads(json.dumps(root.jsonable(certificate)))
    assert root.verify(json_seeds, 2, json_certificate)[0]
    corruptions = []
    for key, value in [('cost', certificate['cost']+1),
                       ('quotient_rank', certificate['quotient_rank']+1),
                       ('status', 'strong_rank_insufficient'),
                       ('basis', []), ('selected', [])]:
        corrupted = deepcopy(certificate)
        corrupted[key] = value
        corruptions.append((key, corrupted))
    corrupted = deepcopy(certificate)
    corrupted['columns'][0][0] += 1
    corruptions.append(('columns', corrupted))
    corrupted = deepcopy(certificate)
    corrupted['decompositions'][0]['terms'][0]['coefficient'] += 1
    corruptions.append(('decomposition', corrupted))
    corrupted = deepcopy(certificate)
    corrupted['repairs'][0]['basis_coordinates'][0] += 1
    corruptions.append(('quotient coordinates', corrupted))
    corrupted = deepcopy(certificate)
    corrupted['repairs'][0]['telescoper']['terms'][0]['coefficient'] += 1
    corruptions.append(('rational telescoper', corrupted))
    corrupted = deepcopy(certificate)
    corrupted['repairs'][1]['telescoper']['poly'] = [Q(0), Q(1)]
    corruptions.append(('polynomial telescoper', corrupted))
    for name, corrupted in corruptions:
        assert not root.verify(seeds, 2, corrupted)[0], f'False {name} accepted'
    empty_certificate = root.synthesize([], 0)
    assert root.verify([], 0, empty_certificate)[0]
    assert root.verify([], 1, root.synthesize([], 1))[0]

    # These are narrower metadata/canonicalization probes. An added constant is
    # still a mathematically valid antidifference; acceptance is not unsound.
    relabeled = deepcopy(certificate)
    relabeled['contract'] = 'incorrect broader basic-faithfulness interpretation'
    shifted_constant = deepcopy(certificate)
    shifted_constant['repairs'][0]['telescoper']['poly'][0] += Q(1)
    assert not root.verify(seeds, 2, relabeled)[0], 'Misleading contract metadata accepted'
    assert not root.verify(seeds, 2, shifted_constant)[0], 'Noncanonical constant accepted'
    checks['root_verify_and_hardening'] = {
        'huge_invalid_order_rejected_before_power': True,
        'nonzero_helper_constant_rejected': True,
        'bad_helper_orders_rejected': 4,
        'valid_and_JSON_roundtrip_accepted': True,
        'mathematically_invalid_certificates_rejected': len(corruptions),
        'empty_feasible_and_infeasible_certificates_accepted': True,
        'misleading_contract_label_rejected': not root.verify(seeds, 2, relabeled)[0],
        'added_antidifference_constant_rejected': not root.verify(seeds, 2, shifted_constant)[0],
    }
    print(json.dumps({'status': 'PASS', 'checks': checks}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()

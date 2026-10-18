"""Deterministic exact experiments; JSON goes to stdout. Not a proof assistant."""
import json
from itertools import product
from math import comb
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cancellation import Field, order, carry_free, standard_fields


def exhaustive_pairs(f: Field) -> dict:
    vectors = list(product(range(f.q), repeat=f.q))
    moments = {mu: f.moments(mu) for mu in vectors}
    orders = {mu: order(moments[mu]) for mu in vectors}
    tested = equal = jumps = zero = 0
    for mu in vectors:
        for nu in vectors:
            conv = f.convolution(mu, nu)
            actual = moments[conv]
            assert actual == f.moment_product(moments[mu], moments[nu])
            r, s, t = orders[mu], orders[nu], orders[conv]
            if r is not None and s is not None:
                assert t is None or t >= r + s
                assert (t == r + s) == carry_free(r, s, f.p)
                if t is None:
                    zero += 1
                elif t == r + s:
                    equal += 1
                else:
                    jumps += 1
            tested += 1
    return dict(q=f.q, modulus=list(f.modulus), weight_vectors=len(vectors),
                ordered_pairs=tested, nonzero_factor_equal=equal,
                nonzero_factor_finite_jump=jumps, nonzero_factor_zero_product=zero)


def saturated_directions(f: Field) -> dict:
    tested = independent = dependent = 0
    for d in range(f.degree + 2):
        for directions in product(range(f.q), repeat=d):
            w = f.span(directions)
            mu = f.saturated(directions)
            expected = tuple(int(x in w) for x in range(f.q)) if len(w) == f.p ** d else (0,) * f.q
            assert mu == expected
            m = f.moments(mu)
            if len(w) == f.p ** d:
                assert order(m) == len(w) - 1
                c = f.derivative_constant(w)
                assert m[len(w) - 1] == c
                sign = f.neg[1] if d % 2 else 1
                assert c == f.mul[sign][f.pow(f.moore_det(directions), f.p - 1)]
                independent += 1
            else:
                assert order(m) is None
                assert f.moore_det(directions) == 0
                dependent += 1
            tested += 1
    return dict(q=f.q, max_direction_length=f.degree + 1,
                direction_tuples=tested, independent=independent, dependent=dependent)


def main() -> None:
    fields = standard_fields()
    report = {'schema': 1, 'arithmetic': 'exact finite fields', 'randomized': False,
              'pair_experiments': [exhaustive_pairs(f) for f in fields[:3]],
              'saturated_experiments': [saturated_directions(f) for f in fields]}
    f = fields[2]
    a, b = f.difference(1), f.difference(2)
    report['F4_witness'] = dict(modulus=list(f.modulus),
        mu=list(a), nu=list(b), mu_moments=list(f.moments(a)),
        nu_moments=list(f.moments(b)), product=list(f.convolution(a,b)),
        product_moments=list(f.moments(f.convolution(a,b))),
        self_product=list(f.convolution(a,a)))
    checked = 0
    for p in (2, 3, 5, 7):
        for r in range(100):
            for s in range(100):
                assert carry_free(r, s, p) == (comb(r+s, r) % p != 0)
                checked += 1
    report['lucas_checks'] = checked
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()

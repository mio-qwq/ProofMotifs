"""Exact small-field checks for the SC-009 multiplicative-Fourier proof."""
from pathlib import Path
import json
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cancellation import Field


def spectrum_report(f: Field) -> dict:
    if f.p != 3 or f.degree < 2:
        raise ValueError('a characteristic-three field with q>3 is required')
    squares = {f.mul[x][x] for x in range(1, f.q)}
    n = len(squares)
    relation = sorted(a for a in squares
                      if f.neg[f.add[1][a]] in squares)
    admissible = []
    failing_witnesses = {}
    for k in range(n):
        witness = None
        for a in relation:
            b = f.neg[f.add[1][a]]
            value = f.add[f.add[1][f.pow(a, k)]][f.pow(b, k)]
            if value:
                witness = (a, b, value)
                break
        if witness is None:
            admissible.append(k)
        else:
            failing_witnesses[str(k)] = list(witness)
    expected = [0] + [3**j for j in range(f.degree)]
    eta = 1 if f.pow(f.neg[1], (f.q-1)//2) == 1 else -1
    expected_relation_size = (f.q-2-3*eta)//4
    nonsquare_square_successes = []
    for s in range(1, f.q):
        if f.pow(s, (f.q-1)//2) == f.neg[1]:
            t = f.add[f.mul[s][s]][1]
            if t and t in squares:
                nonsquare_square_successes.append(s)
    return dict(q=f.q, degree=f.degree, modulus=list(f.modulus),
                square_subgroup_size=n, relation_size=len(relation),
                expected_relation_size=expected_relation_size,
                admissible_exponents=admissible,
                expected_affine_exponents=expected,
                spectrum_matches=admissible == expected,
                order_two_exponent=(n//2 if n % 2 == 0 else None),
                order_two_failure=(failing_witnesses.get(str(n//2))
                                   if n % 2 == 0 else None),
                nonsquare_s_with_square_s2_plus_1=len(nonsquare_square_successes),
                arithmetic='exact shared finite-field tables',
                limitations='finite sanity check, not the uniform Fourier proof')


def main() -> None:
    fields = [Field(3, (1, 2, 0, 1)), Field(3, (2, 0, 1, 0, 1)),
              Field(3, (1, 2, 0, 0, 0, 1))]
    print(json.dumps(dict(schema=1, randomized=False,
                          reports=[spectrum_report(f) for f in fields]),
                     sort_keys=True, indent=2))


if __name__ == '__main__':
    main()

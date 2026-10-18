"""Independent exact controls for PM-MIX-B; standard library only."""
from fractions import Fraction


def apply_seed(v, seed, q, n):
    out = [Fraction(0) for _ in range(n + 1)]
    for m, coefficient in enumerate(v):
        for r, a in seed.items():
            if m + r <= n:
                out[m + r] += coefficient * a / (q ** (m + r) - 1)
    return out


def word(v, letters, seeds, q, n):
    for letter in reversed(letters):
        v = apply_seed(v, seeds[letter], q, n)
    return v


def add_terms(v, terms, seeds, q, n):
    out = [Fraction(0) for _ in range(n + 1)]
    for a, letters in terms:
        w = word(v, letters, seeds, q, n)
        out = [x + a * y for x, y in zip(out, w)]
    return out


count = 0
for q in map(Fraction, (2, 3, -2)):
    for r in (1, 2, 3):
        for a in map(Fraction, (1, -2)):
            for lam in map(Fraction, (0, 1, -1, 2)):
                n = 22
                eigenvalue = q ** r
                # u=a*z^r, u/(1-lam*u)=sum_(j>=1)lam^(j-1)*u^j.
                seeds = {
                    "A": {r: a},
                    "B": {r * j: lam ** (j - 1) * a ** j
                          for j in range(1, n // r + 1)},
                }
                terms = [(1, "AB"), (-eigenvalue, "BA"),
                         (eigenvalue - 1, "BB"),
                         (lam * (eigenvalue - 1), "BAB")]
                for m in range(6):
                    v = [Fraction(0) for _ in range(n + 1)]
                    v[m] = 1
                    assert not any(add_terms(v, terms, seeds, q, n))
                    count += 1

# Negative control: deleting the cubic term is not an operator identity.
q, n = Fraction(2), 12
seeds = {"A": {1: Fraction(1)},
         "B": {j: Fraction(1) for j in range(1, n + 1)}}
v = [Fraction(1)] + [Fraction(0)] * n
drop = add_terms(v, [(1, "AB"), (-q, "BA"), (q - 1, "BB")],
                 seeds, q, n)
assert drop[3] == Fraction(-1, 21)
assert drop[0] == drop[1] == drop[2] == 0

# Positive control: each generator alone has nonzero, distinct-order powers.
for letter in ("A", "B"):
    for k in range(1, 10):
        result = word(v, letter * k, seeds, q, n)
        denominator = 1
        for j in range(1, k + 1):
            denominator *= q ** j - 1
        assert next(i for i, x in enumerate(result) if x) == k
        assert result[k] == 1 / denominator

# Independent band-level telescoping control: a universal rational identity
# is proved in the note; here it is evaluated exactly, not fitted by rank.
for q in map(Fraction, (2, 3, -2)):
    for m in range(7):
        for s in range(2, 20):
            u = {j: 1 / (q ** (m + j) - 1) for j in range(1, s)}
            left = u[s - 1] - q * u[1]
            right = (1 - q) * (sum(u.values()) +
                    sum(u[j] * u[j + 1] for j in range(1, s - 1)))
            assert left == right

print(f"PASS: {count} exact generalized monomial-action controls")
print("PASS: omitted-cubic control has leading coefficient -1/21 at z^3")
print("PASS: unary faithful-leading-term controls for A and B")
print("PASS: 378 exact coefficient telescoping controls")

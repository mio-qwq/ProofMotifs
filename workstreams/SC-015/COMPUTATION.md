# SC-015 normal-character basecase certificates

This computation supplies necessary basecases for the normal-character
existence theorem. It does not assert that a normal-character seed is connected
or generates the complete incidence row code. The two displayed seeds happen
to be connected, as individually verified.

## Scope and arithmetic

`tools/normal_pattern_certificate.py` imports only the Python standard library.
It uses ordinary coefficient-list arithmetic in F3, extended Euclidean
identities, direct field powering, Rabin irreducibility and primitive-order
tests, and column elimination on Frobenius conjugates. It does not import the
older project field, cyclic-gcd, or rank code and does not enumerate a field.
It is not proof-assistant formalization or human review. Historical originality
is not claimed for the algorithms or the basecases.

The exploratory discovery checked degree four completely and stopped at the
first witnesses in degrees five and eight. It checked no other degrees.
The committed certificate instead proves the degree-four obstruction by
polynomial identities and directly verifies the two positive witnesses.
No selected-seed row-code gcd is required or claimed in this certificate.

## Degree-four exclusion

All polynomials below lie in F3[Y]. The exact gcd is

```
G = gcd(Y^81-Y, (Y-1)^40-Y^40, (Y+1)^40-Y^40)
  = Y^18+Y^10+2Y^6+2Y^4+2.
G6  = Y^6+Y^4+Y^2+1.
G12 = Y^12+2Y^10+2Y^4+Y^2+2.
G = G6*G12.
```

The JSON certificate gives all three divisibility quotients and a three-input
Bezout identity, proving this is exactly the gcd. Since Y^81-Y is separable and
splits in F81, there are exactly eighteen roots. They are exactly the elements
with equal, nonzero quadratic characters at y-1, y, y+1: the character is the
fortieth power; zero cannot be shared by the three distinct arguments.

The certificate further gives exact quotients proving

```
G6 divides Y^9-Y;
G12 divides L(Y)=Y^27-Y^9+Y^3-Y.
```

The first six roots lie in F9 and have conjugate rank at most two. The remaining
twelve satisfy `(sigma-1)(sigma^2+1)y=0`, with `sigma(y)=y^3`, and have conjugate
rank at most three. Thus none is normal over F3. This exclusion does not depend
on a selected coordinate presentation of F81.

An earlier attempted single annihilator L for all eighteen roots failed:
the six subfield roots require their separate factor. The final certificate
uses the factorization above and checks both mechanisms.

## Positive degree-five and degree-eight witnesses

Elements are coefficient lists in ascending powers of X. Integer encodings in
the table mean the corresponding base-three digits. Both field presentations
have primitive X and gamma=X^2.

| m | Field modulus | y | a=(y+1)/y | b=(y-1)/y | gamma seed exponents |
|---|---|---|---:|---:|---|
| 5 | X^5+2X+1 | 1+X | 211 | 151 | [0,89,87] |
| 8 | X^8+X^3+2 | 1+X+X^2+X^3 | 1721 | 1224 | [0,771,35] |

The conjugate encodings are respectively

```
m5: [4,28,165,180,228], rank 5;
m8: [40,922,2525,612,4143,4914,5444,1811], rank 8.
```

The verifier recomputes these conjugates and their full coordinate rank, rather
than trusting the rank in the report. In both cases all three characters are
-1, and the ratios a,b are therefore nonzero squares. Their sum with 1 is zero.
Exact exponent identities and gcd computations give connectivity indices
`gcd(89,87,121)=1` and `gcd(771,35,3280)=1` for these two selected seeds.

## Actual verification commands

Run from the repository root:

```
python tools/normal_pattern_certificate.py > /tmp/pm-cycle11-normal-pattern-certificate.json
python tools/normal_pattern_certificate.py --check /tmp/pm-cycle11-normal-pattern-certificate.json
python -m unittest tests.test_normal_pattern_certificate -v
```

The first command generates deterministic JSON and internally verifies it.
The second verifies a supplied certificate, including the explicit scope
restrictions. Negative tests damage the gcd, Bezout coefficients, annihilator
quotients, field modulus, conjugate basis/rank, character values, seed ratios,
seed exponents, connectivity index, reported counts and theorem scope.
The scoped test module contains nine tests. See the cycle command log for the
actual combined project-suite result; no unexecuted global-suite count is
asserted here.

## Next mathematical operation

Combine these two positive basecases and the degree-four exclusion with a
separately proved general normal-character bound. Then keep the digit-weight
scope explicit: normality eliminates nonzero linearized cubic obstacles but
does not resolve arbitrary higher-weight frequencies, connectivity, or the
one-good-orbit question.

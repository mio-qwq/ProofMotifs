# PM-CYCLE11-E: adversarial normality and spectral audit

Date: 18 October 2026. Read-only repository assignment. No repository edits,
commits, or pushes. Independence: the initial counting calculation was derived
before reading A's note; small-field coordinate arithmetic was written without
project imports, power/log tables, or another agent's normality checker.

## Verdict

Accept the proposed normal/three-character counting inequality and the existence
classification for m>=3: a normal y with equal nonzero chi(y-1), chi(y),
chi(y+1) exists exactly when m>=5. The classification does not assert
multiplicative connectivity or full incidence rank. Accept the additional
exclusion of the quartic (2+2) frequency family for these normal-filter seeds.

## Counting calculation, independently checked

Let H=T^m-1, theta=product over DISTINCT irreducible P of
(1-3^(-deg P)), and W=2^(number of DISTINCT P). The Frobenius module K is
cyclic even if 3 divides m: its minimal polynomial is H, since a nonzero
linearized polynomial arising from a degree<m annihilator has ordinary degree
<3^m and cannot vanish on all of K. The minimal polynomial has full dimension,
so the cyclic-vector criterion applies.

Under CRT, each module factor is R/(P^e), and normality is the condition of
lying outside the ideal (P) in EVERY factor. Additive orthogonality gives
constant Fourier coefficient 1-3^(-deg P), with 3^(deg P)-1 nontrivial
coefficients each -3^(-deg P). Thus the global normality indicator Omega has
trivial coefficient theta and nontrivial Fourier l1 norm theta(W-1).
No eigenbasis, squarefree H, or semisimple Frobenius has been assumed.

For distinct a,b, the exact quadratic-character sum is
sum_x chi((x-a)(x-b))=-1. For every nontrivial additive character psi, complete
the square with c=(a+b)/2, d=(a-b)/2 and parametrize the conic
z^2=x^2-d^2 by x=(v+d^2/v)/2, v!=0. It follows exactly that

 sum_x chi((x-a)(x-b)) psi(x)
   = psi(c) sum_(v!=0) psi((v+d^2/v)/2).

Both coefficients in the last ordinary Kloosterman sum are nonzero, so its
absolute value is at most 2 sqrt(q), q=3^m. Primary source actually read:
Keith Conrad, *On Weil's proof of the bound for Kloosterman sums*, Journal of
Number Theory 97 (2002), author-hosted PDF
https://kconrad.math.uconn.edu/articles/kloosterman.pdf . Theorem 3 on printed
page 4 and the proof extending through page 5 were visually inspected. This is
a FIELD character estimate, not an integer-modulus estimate.

Away from 0,+1,-1, the equality-of-signs indicator is

 (1 + chi(y(y-1)) + chi(y(y+1)) + chi((y-1)(y+1)))/4.

Its boundary values are not always zero: in even degree they can be 1/2.
However Omega vanishes at every element of F3 for m>1, so weighted summation
over the entire field is exact without an error term. Each quadratic gives
lower bound -theta-2 theta(W-1)sqrt(q). Hence the count is at least

 theta/4 [q-3-6(W-1)sqrt(q)].

This independently agrees with A's formula, later read in
/tmp/pm_cycle11_a_normal_character.md. The sufficient positivity condition
(q-3)^2>36(W-1)^2 q also requires q>3, satisfied throughout m>=3.

## Degree coverage

At most two linear factors occur, every other distinct factor costs at least
two degrees. Thus #P<=floor((m+2)/2). A's two-parity induction from m=13,14
using sqrt(q)>6*2^floor((m+2)/2)+1 is correct. Incrementing m by two multiplies
the left side by 3 and the exponential bound by 2. All m>=13 are covered.
The exact factor counts for m6,7,9,10,11,12 are 2,2,1,4,3,3; they give strict
positivity. The needed orders are ord_7(3)=6, ord_5(3)=4, ord_11(3)=5;
repeated powers for m divisible by 3 do not change the distinct factors.

m=3 is impossible because the constant frequency N=13=1+3+9 gives trace(y)=0
for every valid filtered y. Normality prohibits this nonzero relation.

m=4 has an exact polynomial obstruction. D's independently coded symbolic gcd
is the degree-18 polynomial

 G=Y18+Y10+2Y6+2Y4+2=G6*G12,
 G6=Y6+Y4+Y2+1,
 G12=Y12+2Y10+2Y4+Y2+2.

It is the gcd of Y81-Y with the two differences of 40th powers expressing
the equality of chi(y),chi(y-1),chi(y+1). None of 0,+1,-1 is a common root.
Direct polynomial divisions give G6 | Y9-Y and
G12 | Y27-Y9+Y3-Y. Thus every filtered y is annihilated by a nonzero
Frobenius polynomial of degree 2 or 3, both less than 4, and cannot be normal.
The multiplicative factorization and both divisions were independently
rechecked using the pre-existing project's elementary polynomial arithmetic;
the finite census below uses wholly independent arithmetic.

tools/normal_pattern_independent_check.py implements coordinate polynomial products,
reduction, exponentiation and Gaussian elimination over F3 from scratch. It
imports no project code and no CAS. Direct no-zero-divisor checks certify the
two small quotient fields. Actual command:

 python tools/normal_pattern_independent_check.py

The exhaustive results are:

 m3: 27 elements, normal18, filtered6, intersection0; all filtered ranks2.
 m4: 81 elements, normal32, filtered18, intersection0; filtered rank counts
     rank1:2, rank2:8, rank3:8.

For m4, twelve filtered elements satisfy the degree-three relation above;
the other six lie in F9. This agrees with D's polynomial proof.

The proposed m5,m8 witnesses were also read in D's independent polynomial
checker. They verify normal rank, identical nonzero characters, irreducibility,
and seed connectivity, without relying on a general existence assumption.
These two cases complete the stated m>=5 classification.

## Simultaneous cubic avoidance and the quartic boundary

If normal y satisfies the character filter, a=1+1/y and b=1-1/y give a valid
square seed. For a three-Frobenius-power exponent, the SC014 identity turns
badness into a relation of three normal conjugates. The relation vanishes
only if all three indices coincide modulo m; that case is an affine
Frobenius frequency, which must remain. Thus the ONE seed excludes every
nonaffine frequency having that cubic representation. This is simultaneous
avoidance, not an exchange of universal and existential quantifiers.

For a quartic exponent with repeated indices (r,r,s,s), expansion gives

 P_k(a)=-h^k [1+(F^r y-F^s y)^2], h=a-1.

If the bracket vanished, z=F^r y-F^s y would satisfy z^2=-1, hence F^2 z=z.
Consequently

 F^(r+2)y - F^(s+2)y - F^r y + F^s y = 0.

Normality forces the positive multiset {r+2,s} and negative multiset
{s+2,r} to agree modulo m: each coefficient difference lies between -2 and 2,
so zero modulo 3 forces an integer difference of zero. A matching yields
r=s or m divides 2. The former gives z=0 and the latter is impossible for
m>=3. Hence the (2+2) quartic family is excluded. Four identical indices or
a (3+1) multiplicity reduce to the already excluded quadratic family.
The (2+1+1) and four-distinct families are not settled by this argument.

Normality alone still does not imply multiplicative generation by a,b.
The reported m8 normal-filter disconnected seed with a quartic root is
consistent with every accepted statement, and forbids calling this a solution
to PM-QUESTION-0001. Human peer review, Lean verification and historical
priority remain unestablished.

## Final manuscript and degree-eight counterexample follow-up

Read final workstreams/SC-015/RESULTS.md, including PM-THEOREM-0019 and
PM-THEOREM-0020. Accept both as stated. The additional displayed factorization
for a (2+1+1) repetition is correct: the six pair terms are
x^2+2xu+2xv+uv=(x-u)(x-v). This is a simplification, not an exclusion.

Independently extended tools/normal_pattern_independent_check.py with a targeted m8
case, reusing its own generic coordinate multiplication and exponentiation.
No B arithmetic or project code was called, and no m8 field scan was used.
Rabin irreducibility checks X^(3^8)=X and gcd(f,X^(3^4)-X)=1; primitive-X
checks use the exact prime divisors 2,5,41 of 6560. All passed under
f=X^8+X^3+2.

The supplied y=4863 has conjugates
4863,5384,4109,6146,4227,2754,3736,4501. Direct coordinate elimination gives
rank 8 and determinant 2. The three characters of y-1,y,y+1 are all -1.
The identities a*y=y+1, b*y=y-1 hold for a=4783,b=2761, as do
a=gamma^76, b=gamma^2368, gamma=X^2. The support gcd with N=3280 is 4.
The seed is valid and disconnected, not a counterexample to a proposed
connected-normal theorem.

For k=820=1+9+81+729, the targeted independent arithmetic gives
a^k=b^k=1 and quartic Q(y)=2=-1. This is a genuine nonaffine frequency:
its Frobenius orbit modulo 3280 is {820,2460}, disjoint from 0 and the
eight powers of three. For the actual square edge {1,81,164}, coordinate
addition gives zero and all three entries are nonzero squares. The absolute
trace of u^820 is [2,1,2], with sum 2. The trace function therefore violates
a full edge while annihilating every scaled seed edge by the exact seed
frequency identity.

Normality implies F3(y)=K. Since y=(a-1)^(-1), F3(a)=K, so H=<a,b> has
field span K. Its index is four; the previously accepted component theorem
therefore gives sparse kernel dimension at least 4*(8+1)=36, versus full
dimension 9. No exact sparse dimension is asserted. This is an accepted
boundary counterexample showing that normality and low-weight exclusions
alone do not imply connectivity or full row-code generation.

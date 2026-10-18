# PM-CYCLE10-E independent adversarial verdict

Question: audit the proposed low ternary weight frequency exclusions,
linearized bad-seed parametrization, and degree-13 counterexample.
Allowed scope: repository read-only, /tmp notes and independent code only.
No project imports, shared edits, remote writes, or full-field enumeration.

## Verdict

ACCEPT the identities, square filter, dimension formula, sufficient subfield
criterion, sixfold-normalization argument, low-fiber exclusions, and the
degree-13 connected bad seed, with the scope qualifications below. The
degree-13 nullity is proved at least 27, not exactly 27. The original
existence of some good seed in every degree remains unresolved.

## 1. Algebraic identities, including collisions

Let a,b be distinct nonzero squares with 1+a+b=0 and neither equal 1.
Put h=a-1, so a=1+h and b=1-h in characteristic three. For nonnegative
r,s, put R=3^r,S=3^s. Then

  1+(1+h)^(R+S)+(1-h)^(R+S)=-h^(R+S).

The expansion is a product of two Frobenius binomials; it remains valid
when r=s. Since h is nonzero, no such frequency is bad for a valid seed.

For three terms R,S,T the constant terms cancel and the odd elementary
symmetric terms cancel, leaving

  P_(R+S+T)=-(h^(R+S)+h^(R+T)+h^(S+T))
            =-h^(R+S+T)(y^R+y^S+y^T), y=h^(-1).

This also holds with repeated r,s,t. In particular r=s=t makes the right
side zero identically and the frequency is affine; it must not be called
an extra frequency. Also a non-repeated triple can give the constant
frequency modulo N, e.g. m=3 and (r,s,t)=(0,1,2). The identities are
integer-exponent polynomial identities; only evaluation on S permits
reduction modulo N=(3^m-1)/2.

The map y -> a=(y+1)/y, b=(y-1)/y is a bijection between valid normalized
parameters and y not in {0,1,-1} satisfying

  chi(y-1)=chi(y)=chi(y+1).

Indeed these nonzero character equalities are exactly chi(a)=chi(b)=1.
The exclusion of 0,1,-1 removes undefined or zero entries. Distinctness
of all three entries follows: any coincidence gives a=b=1 in
characteristic three, impossible because h=1/y is nonzero.

## 2. Dimension and subfield criterion, including 3 dividing m

Let F be Frobenius, H(T)=T^m-1, G(T)=T^r+T^s+T^t with repeated terms
combined in F3[T], and D=gcd(H,G), chosen monic. Bezout gives
D=A H+B G. Since H(F)=0, ker G(F) is contained in ker D(F); G=D G1 gives
the reverse containment.

The coordinator supplied a fully self-contained replacement for the
normal-basis proof; I independently checked it and accept it. Write
L_D(Y)=sum D_i Y^(3^i), c=deg D. Since D divides H and H(0)=-1,
D(0) is nonzero. Therefore L_D has degree 3^c, nonzero constant derivative,
and exactly 3^c distinct roots in the algebraic closure. Linearized
composition corresponds to multiplication of the coefficient polynomials
over F3. H=D H1 implies L_H=L_H1 composed with L_D, so all roots of L_D
are roots of L_H=Y^(3^m)-Y and belong to K. The root space thus has
F3 dimension c. This argument needs neither separability of H(T) nor a
diagonalization of Frobenius; 3 dividing m is harmless.

If D divides T^d-1 for a proper divisor d of m, then G(F)-kernel lies in
ker(F^d-I)=F_(3^d). All corresponding a,b lie in this subfield, so
the generated multiplicative subgroup lies in F_(3^d)^*, a proper
subgroup of S. Such a seed is disconnected. This is a sufficient
subfield-containment criterion, not a claim that every proper kernel is
a subfield. The degree-13 example specifically has a four-dimensional
kernel not contained in any proper subfield.

All three-term kernels contain F3 because G(1)=0, so the square-filtered
bad parameter count is at most 3^c-3. One cannot infer existence of a
single seed avoiding every remaining frequency from individual bounds.

## 3. Sixfold normalization and differential fibers

On valid a, the maps s(a)=-1-a and t(a)=1/a preserve the valid set and
generate S3. The first permutes a,b. The second replaces the seed by
its normalization at a, multiplying its power sum by a^(-e). Hence
both preserve B_k for every positive integer lift e of k.

The action is free. Transposition fixed points are 1 or +/-1, all
excluded from the valid set; three-cycle fixed points solve
a^2+a+1=(a-1)^2=0 and are also excluded. Thus each nonempty B_k has
at least six elements, and its cardinality is divisible by six.

If e>0 is even, P_e=0 is exactly
  (a+1)^e+a^e=-1.
The unrestricted fiber always contains x=1, which is inadmissible.
If that fiber has at most six roots, at most five can be valid, forcing
B_k empty. A global c=-1 differential uniformity bound <=6 suffices,
but a bound for this specific fiber is enough.

If e>0 is odd, P_e=0 is exactly
  (a+1)^e-a^e=1.
The unrestricted fiber contains 0,-1,1, all inadmissible. A fiber bound
of eight leaves at most five valid roots, again forcing B_k empty.
Parity is that of the chosen integer lift; unrestricted differential
equations cannot be swapped merely because two lifts agree on S.
No external uniformity theorem was imported in this review.

For c>=2 an additional exact elementary identity is available. Set
Q=3^(c-1). Frobenius invariance gives B_(3^c-3)=B_(Q-1), and direct
expansion with b=-1-a gives

  ab (1+a^(Q-1)+b^(Q-1))=(a-1)(a^Q-a).

Thus B_(3^c-3) is exactly the valid parameters a in
F_(3^gcd(m,c-1)); it has size at most 3^gcd(m,c-1)-3. Every connected
seed avoids it unless m divides c-1. In the latter case the frequency
is constant modulo N and is not extra. The c=1 case gives exponent
zero and should be handled separately rather than using the identity.

## 4. Degree-13 counterexample independently verified

Independent implementation: tools/linearized_seed_independent_check.py. This code uses
ordinary ascending coefficient lists, its own multiplication and long
division, its own Rabin irreducibility search, its own Gaussian elimination,
and its own character, trace and modular-power calculations. No imports
from project or B arithmetic. Run with Python without -O (assertions).

I independently searched sparse degree-13 moduli and found the same
irreducible polynomial f=X^13+2X+1. Since 13 is prime, the Rabin check
gcd(f,X^3-X)=1 and X^(3^13)=X modulo f proves irreducibility. Trial
division through floor(sqrt(797161)) proves N=797161 prime.

For G=1+T+T^4 the ordinary gcd with T^13-1 is G itself, degree four.
Independently constructed linear-map matrix gives kernel basis, in
ascending base-three coefficient encoding,

  [1,300,732,19719].

All 81 linear combinations were checked to satisfy y+y^3+y^81=0.
Exactly 78 survive y not in F3, and all 78 pass the square filter.
This exhaustive 81-element kernel calculation is not an enumeration of K.

For the particular y=X^2+X^3+X^9=19719, the independent calculation gives

  a=2X^5+2X^11+X^12=886221,
  b=2+X^5+X^11+2X^12=1240274.

Verified: a=(y+1)/y; b=(y-1)/y; a,b are nonidentity squares;
1+a+b=0; 1+a^85+b^85=0; all three entries distinct. Since N is prime,
a alone generates S, so the seed is connected.

The 3-cyclotomic orbit of 85 modulo N has 13 distinct elements and is
disjoint from {0} union the 13-element orbit of 1. Consequently these
27 forced cyclic roots prove seed-kernel dimension at least 27; the
complete square hypergraph has dimension 14 by SC-009. This is a strict
failure, without any claim that the lower bound is exact.

The explicit nonlinear witness is f(u)=Tr_(K/F3)(u^85). Every translated
seed equation vanishes by trace linearity and the single identity
1+a^85+b^85=0. No need to enumerate N translates. Independently checked
the genuine omitted edge

  {1,1+X+X^3+X^4,1+2X+2X^3+2X^4}, encoded {1,112,223}.

Its three entries are distinct nonzero squares, sum zero, and f takes
values (1,1,0), with sum 2. Thus f cannot lie in the full incidence
kernel, in particular cannot be an affine restriction. This is a direct
separator even without invoking cyclic diagonalization for non-affinity.

The example disproves 'every connected seed is good in odd degree'.
It does not disprove 'there exists a good seed in each degree', and it
does not establish historical originality. No Lean or human review.

Handoff: accept the exact identities and counterexample, preserve the
checker plus its actual output, and retain the original existence question
as open. Do not spend effort computing the exact degree-13 nullity unless
it becomes necessary for a subsequent theorem.

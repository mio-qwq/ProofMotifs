# PM-CYCLE11-B: quartic Frobenius obstructions

Independent derivation and coordinate check, 18 October 2026. Read-only input
was SC-014/RESULTS.md and ROADMAP.md. No repository edits or pushes by B.
The algebra below is classical polarization/Frobenius algebra; no historical
priority, human review, or formal-verification assertion is made.

## 1. Exact quadratic reduction

Let K=F_(3^m), S=(K*)^2, and E={1,a,b} a valid distinct square zero-sum
seed. Put h=a-1 and y=h^(-1); then a=1+h, b=1-h, and
a=(y+1)/y, b=(y-1)/y. Let A_i=3^(r_i), i=1,2,3,4, and k=sum A_i.
Occurrences are indexed separately, so repeated r_i are allowed. Expanding
the two products shows that their odd-size terms cancel, their constant
terms together with the initial 1 sum to zero, and each positive even-size
term has coefficient 2=-1. Consequently

    P_k(a)=1+a^k+b^k
          =-sum_(i<j) h^(A_i+A_j)-h^k
          =-h^k (1+Q(y)),
    Q(y)=sum_(i<j) y^(A_i+A_j).

For the last equality, each two-element subset is paired with its complement;
this remains valid for repeated A_i because the subsets are indexed. Thus
the exact bad-parameter condition is Q(y)=-1, y outside F_3, together with
chi(y-1)=chi(y)=chi(y+1). Exponents can subsequently be reduced modulo N
on S; this does not authorize calling an affine/constant collision extra.

Q is an F_3-quadratic map K -> K. It is generally K-valued, not one scalar
quadratic form. Its polar form is

    B(y,z)=sum_(i<j) (F^r_i(y) F^r_j(z)+F^r_i(z) F^r_j(y)).

For c in F_3,

    Q(y+c)=Q(y)+3c sum_i F^r_i(y)+6c^2=Q(y).

Also Q(-y)=Q(y), and Q(Fy)=F(Q(y)). The quadratic map therefore descends
to K/F_3; the square-filtered bad set is invariant under the same six
normalizations y -> epsilon*y+c used in SC-014. Unlike the cubic case,
normal-basis linear independence does not directly exclude Q(y)=-1.

## 2. Multiplicity patterns

All indices below are read modulo m; equal residues must first be grouped.

* Three equal indices: k=3*3^r+3^s=3^(r+1)+3^s, so SC-014's quadratic
  exclusion applies. Four equal indices have the same reduction. Directly,
  Q=0 for either pattern.
* Pattern r,r,s,s: writing x=F^r(y), z=F^s(y), one obtains
  Q=x^2+xz+z^2=(x-z)^2.
* Pattern r,r,s,t: Q=(F^r(y)-F^s(y))(F^r(y)-F^t(y)).
* Four distinct indices retain the full e_2 quadratic expression.

The two-two pattern is impossible for every seed if m is odd, since -1 is
then a nonsquare in K. In even degree the unfiltered solvability is also
explicit. For j=s-r not zero modulo m, d=gcd(j,m), ell=m/d, choose
iota in F_9 with iota^2=-1. The equation is equivalent, after applying an
invertible Frobenius map, to (1-F^j)x=+/-iota. The image of 1-F^j is exactly
the relative-trace-zero subspace for K/F_(3^d). Therefore solutions exist iff
Tr_(K/F_(3^d))(iota)=0. If d is odd, ell is even and the alternating sum of
the Frobenius conjugates of iota vanishes; if d is even, the trace equals
ell*iota and vanishes exactly when 3 divides ell. Each sign then has 3^d
solutions, before applying the square filter. This is the standard additive
Hilbert-90/linearized difference criterion, not a new method.

## 3. Normality excludes the entire two-two pattern

Assume m>=3 and y is normal over F_3. For r != s modulo m, suppose
z=F^r(y)-F^s(y) obeys z^2=-1. Then z belongs to F_9, hence F^2(z)=z.
This gives the linear relation

    F^(r+2)y - F^(s+2)y - F^r y + F^s y = 0.

Since the m conjugates of y are independent, the positive index multiset
{r+2,s} must equal the negative multiset {s+2,r} modulo m. Each coefficient
has multiplicity at most two, so no coefficient of size three can disappear
in characteristic three. One matching would force r=s; the other forces
2=0 modulo m. Both are excluded. For r=s one has Q=0 immediately. Thus
no two-two quartic frequency annihilates a seed arising from normal y, in
either parity. Together with the triple-repetition reduction, only the
two-one-one and four-distinct quartic patterns need further study for normal y.

## 4. Exact normal, square-filtered, disconnected bad seed

Use K=F_3[X]/(X^8+X^3+2), q=6561, N=3280, gamma=X^2. Ascending base-three
integer encodings are used. Take

    y=4863 = X+2X^5+2X^7,
    a=4783 = 1+X+2X^4+X^5+2X^7,
    b=2761 = 1+2X+X^4+2X^5+X^7.

The independent checker performs ordinary coordinate polynomial products
and reductions, with no ProofMotifs imports. It verifies a complete length
6560 primitive-X cycle. Thus every nonzero residue in the quotient is a unit,
which proves that this quotient is a field and X is primitive. It checks

    a*y=y+1, b*y=y-1, 1+a+b=0,
    a^N=b^N=1, chi(y-1)=chi(y)=chi(y+1)=-1.

The normal conjugates, as coordinate encodings, are

    4863,5384,4109,6146,4227,2754,3736,4501.

Their 8x8 F_3 coordinate determinant is 2, hence y is normal. Moreover
a=gamma^76 and b=gamma^2368. The exact support index is

    gcd(76,2368,3280)=4.

This seed has four components. Normality implies that y generates the whole
field, and K=F_3(a) since y=1/(a-1). SC-013 therefore gives sparse-kernel
dimension at least 4*(8+1)=36, versus full-square dimension 9. The separate
existing bitplane gcd happens to yield exactly 36, but that equality is not
needed for this certificate and is not supplied as an independent proof here.

For the genuine four-distinct frequency

    k=1+9+81+729=820,

the checker verifies Q(y)=2=-1 and a^k=b^k=1. The Frobenius frequency orbit
is {820,2460}, disjoint from {0,1,3,...,3^7} modulo N. This is an actual
extra frequency, not a low-digitweight presentation of an affine mode.

An explicit separating function is f(u)=Tr_(K/F3)(u^820). For every t in S,

    sum_(u in tE) f(u)
      =Tr(t^820*(1+a^820+b^820))=0.

Thus the identity covers all 3280 sparse scaled edges without enumerating
their equations individually. The true square edge gamma^[0,2,1672] is
{1,81,164}; its f-values are {2,1,2}, with sum 2. It follows that f is not an
affine restriction and the sparse code is insufficient. This example proves
that normality plus the square filter does not guarantee a good orbit or
connectivity. It does NOT refute sufficiency of normality PLUS connectivity;
the index-four disconnectedness is essential to the stated conclusion.

## 5. Actual commands and unsuccessful branch

Primary reproducible command:

    python tools/normal_quartic_boundary.py

Exit status 0. Frozen structured output is
`research/experiments/normal-quartic-boundary.json`. Source is
`tools/normal_quartic_boundary.py`. Only standard-library modules are used.

Exploration used the existing CompactField implementation to identify the
degree-eight witness. Targeted counter-searches additionally tested connected,
normal, square-filtered parameters for quartic-frequency witnesses in degrees
9,10,11, using primitive moduli X^9+2X^4+1, X^10+X^3+X+2, and X^11+2X^2+1.
No connected normal witness was found; degree ten had connected quartic bad
seeds whose y were nonnormal. Those searches were exploratory, not preserved
as research certificates, and are not evidence of a general theorem. Search
was stopped at the coordinator's direction. The actual deliverable is the
proved exact reduction, multiplicity refinements, and independently checked
degree-eight boundary example, not a new degree table.

Next mathematical operation: study the two-one-one product equation and the
four-distinct K-valued quadratic equation under both normality and support
connectivity. Normal-basis independence alone controls linearized operators,
not quadratic products; a successful cubic sieve does not settle every
nonaffine frequency or PM-QUESTION-0001.

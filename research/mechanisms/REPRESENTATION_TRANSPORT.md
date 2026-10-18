# Generating representations and safely transporting cancellation

19 October 2026, Asia/Singapore. This closes the bounded mixed-q-seed gate
and returns to the macro question of auxiliary-object discovery. Results are
manual proofs with independent AI views and exact arithmetic controls, not
Lean, human review, historical novelty, or a successful unread transfer.

Two operations are made explicit: a rational change of generators can carry
an old relation into a new-looking higher-degree cancellation; and a polynomial
evaluation dictionary can be generated from raw points, not merely optimized
after someone supplies it. Both have direct classical baselines. Neither
establishes a missing universal mathematical instrument or an AI causal claim.

## 1. PM-MIX0001: the rational seed does not remove operator relations

Let K be any field, q in K* of infinite multiplicative order, r>=1, a in K*,
u=a*z^r, Q=q^r, and c in K. On ALL K[[z]], with rightmost composition first,
define sigma f(z)=f(qz), Delta=sigma-1, and

    J_b(f)=sum_(k>=1) [z^k](bf)/(q^k-1) * z^k.

Put A=J_u, B=J_(u/(1-cu)). Then

    AB-QBA+(Q-1)B^2+c(Q-1)BAB=0.                         (1)

Consequently these two operators do not faithfully encode the free
K-algebra on two letters. The free polynomial in (1) is nonzero because
the distinct word AB has coefficient1, in every allowed characteristic.
In particular u=z,c=1 answers the preceding project question negatively.
Strong residue rank1 was not used as a necessary condition for this conclusion.

### Complete proof without inverting an integration operator

Let Z=M_u, multiplication by u. On z^m, with t=q^(m+r),

    (ZA-QAZ)(z^m)
      = a^2[1/(t-1)-Q/(Qt-1)] z^(m+2r)
      = (Q-1)A^2(z^m).

Every denominator is nonzero. Every output coefficient uses finitely many
input coefficients, so this is an identity on all formal series. Put
S=1-cZ, a genuine invertible multiplication operator with inverse M_(1/(1-cu)).
Then B=A S^-1 and BS=A. Calling the left side of (1) P,

    P S = A^2-BA+cB[QAZ+(Q-1)A^2]
        = A^2-BA+cBZA
        = A^2-BS A = 0.

Compose with S^-1 on the right to obtain P=0. No division by c occurs, so
c=0 is included (then B=A). No inverse of A or B is used: they raise order
and are NOT invertible endomorphisms of all K[[z]]. The Jackson derivative
has constants in its kernel; formal fraction-ring heuristics alone would
not resolve those domain/boundary issues.

Each nonzero generator alone is faithful: if b has leading order s>=1,
J_b^k(1) has order ks with nonzero leading coefficient. Thus the joint failure
is not explained by either unary generator being zero or algebraic.
For u=z,c=1, deleting the cubic correction leaves a nonzero leading
coefficient -1/((q^2-1)(q^3-1)) at z^3 on1; at q=2 it is -1/21.
No complete relation ideal, minimal identity length, or general rational-
alphabet obstruction is asserted.

## 2. PM-MIX0002: a universal finite transport certificate

The algebraic step holds in any unital associative algebra over a commutative
coefficient ring, with central Q,c, whenever

    R0=ZA-QAZ-(Q-1)A^2=0,   R1=B(1-cZ)-A=0,

and S=1-cZ is a unit. It needs no infinite-order assumption until the
specific formal integration realization is instantiated. Over the FREE
algebra Z[Q,c]<A,B,Z>, define H=A+(Q-1)B+c(Q-1)BA. Exact expansion gives

    P S = H R1 - R1 A - c B R0.                          (2)

This is a constant-size ideal-membership certificate, not a renamed kernel
condition or a search over infinitely many words. tools/resolvent_certificate.py
checks it with exact integer polynomial coefficients. Its verify_identity
checks the supplied algebraic equality ONLY: it does not validate the field,
infer that P is nonzero, identify a canonical theorem, or prove S invertible.
The canonical demonstration separately verifies P!=0; the application above
supplies R0=R1=0 and the actual unit. Zero identities are valid inputs to
a generic equality checker, not certificates of nonfaithfulness.

The unit condition cannot simply be dropped. Over Q take Q=2,c=1,A=0,
B=Z=1. Then R0=R1=0 and PS=0, but S=0 and P=1. In our application the
unit is established algebraically by positive z-adic order, not guessed from
an invertible finite truncation. Relation construction uses a constant number
of free-polynomial rewrites; applying the rational-seed operators to an N-jet
can separately be done by prefix sums in O(N) field operations for r=1.

### Exact established-method comparison

Díaz–Pariguan, arXiv:0804.0183v2 (23Jun2009), §3 Definition4 and Theorem6,
already gives the q-meromorphic Weyl relation yx-qxy=x^2 and its Jackson
integral representation. With x=(q-1)J_z and y=M_z this is our base relation.
Their analytic representation uses real 0<q<1; the coefficient proof here
justifies our all-field/formal-series scope. The retrieved version's integral
result is Theorem6, NOT Theorem7. Lopes2023 Example3.1 explicitly changes
y to y+(q-1)^-1 x to identify the quantum plane. Bell–Rogalski2012 has a
free-subalgebra criterion for specified fraction generators with additional
hypotheses, not for every pair in an Ore division ring. These facts strengthen
classical coverage, not historical originality for the eliminated cubic.

The bounded rational-seed gate is CLOSED. Do not follow it with another
neighboring seed scan, a full-presentation search, or constant optimization.

## 3. PM-IMPLICIT0001: discover an optimal evaluation representation from points

Input: m>=1 distinct explicit points h_1,...,h_m in K^n, n>=1, over any
effective field K with exact operations/equality. The grammar is ordinary
commutative polynomials, with TOTAL DEGREE as cost. No monomial dictionary,
degree bound, separating linear form, generic position, or factorization
oracle is supplied. Write v(f)=(f(h_j))_j, V_d=v(K[x]_<=d), V_-1=0,
and D_i=diag(h_(1,i),...,h_(m,i)).

There is a construction using at most nm coordinate-product candidates and
O(nm^3) field operations that returns m monomials b_1=1,...,b_m such that

    V_d = span{v(b_j):deg b_j<=d}                         (3)

for EVERY d. It returns the exact d*=min{d:V_d=K^m}<=m-1 and an inverse
evaluation matrix C=E^-1, E_(i,j)=b_j(h_i). For every value target y!=0,

    N(y)=sum_j (Cy)_j b_j,
    minimum possible degree = max{deg b_j:(Cy)_j!=0}.     (4)

Thus N(e_i) are simultaneously individually degree-minimal cardinal
polynomials, not merely a family with an optimal maximum degree. N(0)=0.
This does not optimize support, circuit size, locality or coefficient height.

### Constructive proof and pruning invariant

Start with b_1=1, and frontier {b_1}. Multiply each newly retained degree-d
monomial by all n coordinates. Form a candidate evaluation as D_i v(b),
reduce it by incremental exact elimination against all previously accepted
vectors, and retain the original monomial iff its vector is independent.
Only newly accepted monomials get expanded in the next degree layer.
Complete each layer unless full rank m is reached; only that full-rank event
permits early stopping within a layer.

Inductively (3) holds at every completed layer, because

    V_(d+1)=V_d+sum_i D_i V_d
            =V_d+sum_i D_i span(new degree-d frontier).

The products of older basis members already lie in V_d, having been offered
earlier. Thus the new frontier suffices. The kernel of evaluation is an
IDEAL: v(p)=v(q) implies v(x_i p)=v(x_i q). This is the load-bearing
multiplication congruence behind the pruning; arbitrary linear readouts do
not have it. For example L(1)=e1,L(x)=0,L(x^2)=e2 is linear but would lose
the degree-two direction if x were discarded and never expanded.

A complete-layer plateau would make V_d stable under every D_i. Since it
contains1, it would then contain every polynomial evaluation. Distinct points
make those evaluations span K^m: for each pair i!=j choose a coordinate
ell(i,j) where they differ; the product over j!=i of

    (x_ell(i,j)-h_(j,ell(i,j))) /
    (h_(i,ell(i,j))-h_(j,ell(i,j)))

is cardinal at h_i and has degree<=m-1. This proof works even when m>|K|,
where a single injective linear form is impossible. Hence a deficient true
plateau cannot occur and d*<=m-1. A single rejected candidate is not a plateau.
Each of at most m accepted vectors is expanded n times, proving the nm bound;
each incremental reduction costs O(m^2) field operations. Matrix inversion
costs O(m^3). Only accepted exponent labels need materializing.

Finally E is invertible, and (3) says y in V_d iff (Cy)_j=0 for all basis
degrees>d. This proves (4), including optimality among ALL polynomials.

## 4. PM-IMPLICIT0002: finite certificates for all degrees, not just sampled terms

The constructor returns actual monomials, C and the coordinate border table

    T_i(:,j)=C D_i E(:,j).

A separate verifier evaluates the monomials from raw points, checks EC=I,
the constant basis member, every border identity E T_i(:,j)=D_i E(:,j), and

    T_i(k,j)=0 whenever deg b_k>deg b_j+1.                (5)

These FINITE checks prove (3) by induction on the degree of every monomial;
the reverse inclusion follows from the actual degrees of b_j. The verifier
need not trust the discovery queue or enumerate all low-degree monomials.

For any infeasible degree budget d and target y, select a row j of C with
deg b_j>d and (Cy)_j!=0. Then lambda=row_j(C) annihilates every V_d but
lambda*y!=0. This is an exact lower-degree impossibility certificate. The
cardinal witnesses use y=e_i. For infeasibility of surjectivity itself at
d<d*, any C row with degree>d suffices.

The base construction can work with O(m^2+nm) field storage and a shared
m-monomial/m^2-coefficient output. Our reference materializes every border
coordinate, so its certificate/output and working storage use O(nm^2)
fields. Verification remains O(nm^3) field operations. Rational bit growth,
input/label encodings and the primitive field arithmetic cost are separate;
the Q/prime-field prototype's exact prime validation also costs separately.
No speedup against modern BM implementations is claimed.

## 5. PM-IMPLICIT0003: rejected divisors are not automatically a monomial ideal

Take H={(0,0),(1,1),(2,2),(3,3),(0,1)} over Q. If xy is processed before
both squares, 1,x,y,xy are independent, while x^2=xy and y^2=xy-x+y on H.
Both squares are rejected. Pruning ALL their multiples then falsely stops
at rank4; x^2 y supplies a fifth direction. Exact degree ranks are1,3,4,5.
No admissible multiplicative term order puts xy before both squares.

Our frontier method still expands xy's coordinate products: rejecting a
different divisor does not suppress them. BM's stronger leading-monomial
pruning needs its admissible order. Neither that staircase property nor a
canonical Gröbner basis is promised by our arbitrary within-degree ordering.

## 6. Return to source197 and the actual macro gap

Over a finite field of size q, within PM-CONSTRUCTION-0002's exact square
output/total-degree contract, the raw hole set admits its cardinal punctured
Gram construction iff 2d*<=q-2. If so the discovered cardinal polynomials
give full-line Gram0 and punctured Gram -I_m. If not, an inverse row at a
degree above floor((q-2)/2) certifies nonsurjectivity in that budget and
therefore excludes every legal polynomial vector realizing the prescribed
square punctured-Gram target (not every polynomial).
This is not impossibility outside that architecture, a rectangular-output
classification, or validation of the source's incidence/headline theorem.

The operation is already classical: Möller–Buchberger1982 constructs an
interpolation basis from points with degree refinements; Abbott–Bigatti–
Kreuzer–Robbiano2000 AlgorithmC and its separator variant explicitly provide
the matching evaluation/border mechanism. Thus “only a supplied dictionary
can be handled by old tools” is too broad. The finite algebra congruence and
degree filtration explain a genuine implicit-generation case.

This does not generate the phase/local scopes of107 or the sharing/bilinear
architecture of157 from arbitrary statements. Nor does it supply their
positivity, characteristic or composition hypotheses. The role of the target
observable and allowed grammar remains essential; there is no single faithful
scalar cancellation order covering these mechanisms.

Next: freeze a genuinely unread external target and the available input/cost
contract BEFORE its statement/proof is used for transfer. Compare this
classical implicit-generation operation with the strongest same-input baseline;
record absence of the multiplication congruence as a failed transfer if that
is what occurs. Do not continue toy point panels or q-seed variants. No unread
transfer has been attempted or succeeded in the present checkpoint. PM-H1..H5
remain OPEN; stronger classical coverage is a substantive research outcome.

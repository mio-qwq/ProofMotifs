# PM-IMPLICIT-A: dictionary-free degree-minimal finite-point interpolation

## Nine-field scoped ledger

1. **TASK ID:** PM-IMPLICIT-A.
2. **RESEARCH QUESTION:** From m distinct explicit points H in K^n alone,
   construct a total-degree-minimal polynomial evaluation basis/cardinal map
   without enumerating all monomials below a degree bound or receiving a
   candidate dictionary. Decide whether multiplication closure permits sound
   pruning, polynomial field-operation cost, and a minimality witness.
3. **KNOWN ASSUMPTIONS:** K is an effective field with exact field operations,
   inversion of nonzero elements, and equality tests; m,n>=1; the input points
   are pairwise distinct; total degree is the filtration. All characteristics
   are allowed. Complexity below is field-operation complexity, not a hidden
   bit-complexity claim for arbitrary effective fields.
4. **AVAILABLE EVIDENCE:** I read AGENTS.md and RESEARCH_PROGRAM.md in the
   earlier scoped task, and now read the relevant source197 statement and
   proof in research/mechanisms/CONSTRUCTION_CONTRACTS.md. Its square punctured
   Gram contract is equivalent to surjectivity of the degree-bounded hole
   evaluation map. The present algorithm supplies that surjectivity decision
   and interpolation from the points alone. No current B/C child note was
   inspected.
5. **EXPECTED OUTPUT:** A complete constructive proof, field time/space and
   certificate bounds, explicit use of the evaluation ideal, and limitations;
   classical Buchberger--Moller/evaluation-code coverage is the anticipated
   literature baseline, not an originality claim.
6. **ALLOWED SCOPE:** Repository read-only; only own /tmp note/code written;
   no Git commands, child delegation, original-paper lookup, field scan, or
   external communication. The only task communication was an interim update
   to the coordinator. No project file was changed.
7. **INDEPENDENCE REQUIREMENT:** The construction/proof was derived before
   receiving other proposals. No other current child note or proposal was
   read. The explicitly requested model configuration continues as supplied;
   this process has no independent facility to verify the actual backend
   model/reasoning setting.
8. **STOP CONDITIONS:** One bounded complete proof and fixed exact sanity
   controls; no small-field enumeration, optimization of constants, or new
   neighboring research stream. This proof closes the assigned question.
9. **HANDOFF:** /tmp/pm-implicit-a.md contains the proof and limits;
   /tmp/pm-implicit-a.py contains a dependency-free exact implementation and
   fixed controls. No formal proof assistant or independent adversarial review
   is claimed. The coordinator handles primary-source comparison/integration.

## Main constructive statement: PM-IMPLICIT-A-001

Write H=(h_1,...,h_m), and let

    ev: K[x_1,...,x_n] -> K^m,
    ev(p) = (p(h_1),...,p(h_m))^t.

Let P_d be the polynomials of total degree at most d, set V_d=ev(P_d),
and set V_-1={0}. From H alone one can construct m monomials
B=(b_1=1,b_2,...,b_m), their evaluations, and the inverse C of their square
evaluation matrix E=(b_j(h_a))_(a,j), such that

    V_d = span{ev(b_j): deg(b_j)<=d}                       (F)

for every integer d. Thus B is a filtration-adapted monomial evaluation
basis, not merely an arbitrary basis of K^m.

The construction examines at most nm monomial candidates, not all monomials
in a prescribed degree simplex. It takes O(nm^3) exact field operations and
O(m^2+nm) stored field elements (including the input), together with
O(nm log(m+1)) bits for optional explicit exponent vectors. A parent-index /
coordinate-label DAG uses only O(m log(nm+1)) bits until exponent vectors are
requested. Equality tests are polynomially bounded by the same operations.
The largest selected degree is

    d_* = min{d: ev(P_d)=K^m} <= m-1.

The cardinal polynomials

    ell_a(x) = sum_j C_(j,a) b_j(x)

have ell_a(h_b)=delta_(a,b). Each ell_a individually has the smallest total
degree of any polynomial with those cardinal evaluations, not merely a
minimal common maximum degree. More generally

    N(y) = sum_j (Cy)_j b_j

is a degree-minimal interpolant of every y in K^m. Its degree is the largest
deg(b_j) for which (Cy)_j is nonzero, with the zero polynomial convention
when y=0.

## Algorithm: multiply only the newly accepted frontier

Let D_i=diag(h_(1,i),...,h_(m,i)). Start with B=[1], its evaluation vector
v=(1,...,1)^t, and frontier F=[1]. Maintain incremental Gaussian elimination
on the accepted evaluation vectors.

At degree d, the frontier consists exactly of the monomials newly accepted
with degree d. For every b in the frontier and every i=1,...,n:

1. Form v= D_i ev(b), using m scalar multiplications. This is the evaluation
   of the candidate monomial x_i b. No expanded candidate dictionary exists.
2. Reduce v against the current accepted evaluation vectors. If dependent,
   discard it and never expand this particular candidate.
3. If independent, accept the candidate, retain its evaluation, its parent
   pointer and coordinate i, and put it in the next frontier.

Finish this layer, replace the frontier by the newly accepted monomials,
and continue. Stop immediately when rank reaches m. Finally invert E.

An exponent tuple need only be formed for an accepted candidate. A rejected
candidate is represented during reduction by (parent index,i), so copying an
n-entry exponent tuple for each of nm rejected candidates is unnecessary.

## Proof of sound pruning and exact degree profile

The exact multiplication rule is

    ev(x_i p) = D_i ev(p).                                (M)

Therefore

    V_(d+1) = V_d + sum_i D_i V_d.                        (R)

Initially V_0 is the one-dimensional span of ev(1). Suppose that at the
start of layer d the accepted monomials of degree <=d are a basis of V_d.
If an accepted monomial b has degree <d, then each product x_i b was already
considered in an earlier layer; whether accepted or rejected, its evaluation
lies in V_d. Thus in (R) only products of the current degree-d frontier can
enlarge the span. Incremental elimination of precisely these products
therefore produces a basis of V_(d+1). This proves (F) inductively, including
all rejected monomials and all monomials that were never generated.

Equivalently, every rejected relation

    ev(c) = sum_j alpha_j ev(b_j)

has deg(b_j)<=deg(c). Multiplication by x_i preserves the relation by (M),
and all right-hand products are either already represented or generated by
accepted frontiers in the relevant next layer. Repeated multiplication cannot
reintroduce a lost evaluation direction. This is why pruning is rigorous;
an independence test in an unrelated linear feature space would not suffice.

No layer with rank <m can have an empty next frontier. Such a layer would
give V_(d+1)=V_d, hence D_i V_d subset V_d for every i. Since 1 is present,
induction would put the evaluation of every monomial into V_d. But ev is onto:
for every ordered pair a!=b choose a coordinate i(a,b) with
h_(a,i)!=h_(b,i), and the polynomial

    product_(b!=a)
      (x_(i(a,b))-h_(b,i(a,b))) /
      (h_(a,i(a,b))-h_(b,i(a,b)))

is cardinal at h_a. Its degree is at most m-1. This argument works over
every field, including small finite fields; it does not assume that one
linear coordinate separates all the points, pass to an extension field, or
expand that product into a monomial dictionary.

Consequently every unfinished layer increases rank, termination occurs with
m basis vectors by degree m-1, and the selected degree counts equal dim V_d.
This also proves the stronger sorted-degree optimality: for any evaluation
basis of polynomials, the number of members with degree <=d is at most
dim V_d. The greedy basis attains equality for every d simultaneously.

## Interpolation, minimality, and dual negative certificates

Invertibility of E gives ev(N(y))=E C y=y. By (F),

    y is in V_d  iff  (Cy)_j=0 whenever deg(b_j)>d.        (D)

Therefore N(y) has minimum possible degree. Applying this to y=e_a proves
individual degree-minimality of every cardinal polynomial and common
maximum-degree optimality d_*.

If degree d is insufficient for a prescribed y, choose j with deg(b_j)>d
and (Cy)_j!=0. The row

    lambda^t = row_j(C)

is an exact separating certificate:

    lambda^t ev(p)=0 for every p in P_d,
    lambda^t y=(Cy)_j != 0.

For a bare failure of surjectivity at any d<d_*, choose any row j with
deg(b_j)>d. That row is nonzero and annihilates all V_d. In particular a
row indexed by a top-degree selected monomial certifies that d_*-1 is too
small. All rows indexed by degree>d form a basis of the annihilator of V_d.
For m=1, d_*=0 and V_-1={0}; there is no nonnegative smaller degree to test.

Thus both positive constructions and negative certificates concern *every*
degree-bounded polynomial, not only the examined candidates.

## Compact independent certificate verification

The output monomial list B and cardinal coefficient matrix C already contain
enough data for a polynomial-time verifier; no list of rejected candidates
or all low-degree monomials need be retained. The verifier:

1. Evaluates the at most m supplied monomials at H, obtaining E, verifies
   b_1=1, and verifies E C=I_m.
2. For each supplied b_j of degree <d_* and each coordinate i, forms
   w=D_i ev(b_j), computes c=Cw, and checks

       c_k=0 whenever deg(b_k)>deg(b_j)+1.                 (BORDER)

3. Uses the desired row of C as the dual certificate and checks the indicated
   nonzero target pairing when a particular y is specified.

(BORDER), together with b_1=1, proves by induction that every degree-d
monomial evaluates into span B_(<=d) for d<=d_*. The reverse inclusion is
automatic from the actual monomial degrees. Thus these checks independently
establish (F), cardinality and the global minimality witness, rather than
merely trusting the constructor's frontier log. They cost O(nm^3) field
operations and O(m^2+nm) field storage. The supplied certificate itself is
O(m^2) field elements plus the m monomial descriptions. If explicit border
coordinates are desired, they occupy O(nm^2) additional output fields and
can be streamed; they are not needed for the stated working-space bound.

## Complexity accounting

Each accepted monomial is expanded at most once and generates n candidates,
so there are at most nm candidates overall. Incremental Gaussian reduction
uses at most m pivot eliminations on a length-m vector per candidate: O(m^2)
field operations, with one inversion only when a vector is accepted. Thus
generation/reduction costs O(nm^3). Inverting E costs O(m^3), already within
that bound since n>=1. Reconstructing exponent vectors from accepted parent
pointers uses O(nm) integer word operations; all exponents are <=m-1.

The input occupies nm field entries, accepted/echelon evaluation vectors
O(m^2), and the inverse/cardinal coefficients O(m^2). A candidate and frontier
require O(m) additional entries. Output cardinal polynomials share the same
m-monomial dictionary, with an m-by-m coefficient matrix; no exponential
expanded support occurs. Preprocessing a new target y after construction
costs O(m^2) field operations. Bit growth of rational coefficients and the
cost of field arithmetic/equality are separate and are not bounded merely
by counting field operations. Outputting all cardinal coefficients already
permits Theta(m^2) field entries in the worst case.

## Load-bearing ideal / congruence condition and boundaries

The kernel I(H)=ker(ev) is an ideal, since evaluation is an algebra map into
K^m with componentwise multiplication. Hence ev(p)=ev(q) implies
ev(x_i p)=ev(x_i q). The diagonal coordinate operators commute, and the
constant vector is cyclic for their algebra because the coordinates separate
the given points. These properties, not just finite feature rank, justify
closure and pruning. Equivalently K[x]/I(H) is the finite reduced algebra K^m.

For a simple failure control without the ideal condition, take a mere linear
feature map L:K[x]->K^2 with L(1)=e_1, L(x)=0, and L(x^2)=e_2. Discarding x
as dependent and never expanding it misses the degree-2 direction. No operator
D can satisfy L(xp)=D L(p) for all p: it would give D L(x)=0=L(x^2), a
contradiction. This works in every characteristic and isolates the missing
multiplication congruence.

Distinctness is essential for surjectivity onto *labelled* K^m. Duplicate
points force an annihilator e_a-e_b at every degree. If duplicates are allowed,
the same closure algorithm saturates at the number of distinct points rather
than m; that is a genuine obstruction, not a long plateau requiring more
monomials. The assigned task assumes duplicates absent. Distinctness can be
checked separately with O(nm^2) field equality tests if required.

The algorithm does not optimize monomial support, coefficient bit size, an
arbitrary weighted feature cost, or a non-degree-compatible grammar. The
accepted monomial set need not be advertised as a Groebner staircase/order
ideal under the arbitrary within-layer order used here; filtration adaptation
and the evaluation ideal are sufficient. A term-order-specific version can
impose additional classical staircase structure, but it is not needed for
the claimed theorem. This result does not remove the source197 assumptions
on the finite field, line cancellation degree, or square output dimension.

## Actual exact controls

Created only /tmp/pm-implicit-a.py using apply_patch; ran

    python /tmp/pm-implicit-a.py

The dependency-free implementation uses fractions.Fraction over Q and exact
modular arithmetic for one *fixed* F2 point set. It constructs the basis,
inverts E, independently evaluates supplied monomials, verifies E C=I,
checks all needed border inclusions, and checks the lower-degree annihilator.
There was no field enumeration, random search, numerical rank, or exhaustive
monomial scan. Output:

    singleton over Q: PASS; ranks=[1], minimum_degree=0, candidates=0
    duplicate coordinate functions over Q: PASS; ranks=[1, 2, 3, 4], minimum_degree=3, candidates=5
    five explicit non-Cartesian F2 points: PASS; ranks=[1, 4, 5], minimum_degree=2, candidates=5
    fifteen irrelevant coordinates over Q: PASS; ranks=[1, 2, 3, 4], minimum_degree=3, candidates=48
    non-Cartesian Q points: PASS; ranks=[1, 3, 5], minimum_degree=2, candidates=6

The second test has duplicated coordinate *functions* on distinct points,
not duplicate points; it stresses safe pruning. The F2 set contains five
explicit points of F2^3, not the whole space or a classified sample. The many
irrelevant-coordinate control verifies that coordinates may vanish identically
on H without blocking later useful multiplication directions. These controls
supplement the field-general proof, not replace it.

## Literature and program limits

No original paper was looked up or read in this independent task, as requested.
Buchberger--Moller, finite quotient-algebra border methods, evaluation codes,
and finite-dimensional reachable/Krylov spaces are the expected classical
baselines for the coordinator to check. There is no absence-of-search or
historical novelty claim. This gives a positive implicit-generation operation
with exact primal/dual degree certificates under an explicitly load-bearing
algebra congruence. It does not by itself establish PM-H4/H5, unseen transfer,
or a missing general mathematical instrument.

# PM-SYNTH-C: independent prior-art and boundary audit

Date: 2026-10-18. Scope: read-only ProofMotifs. No repository writes, Git operations,
external messages, paid actions, ParallelSearch calls, or subagents. This note and
the small exact counterexample checker are the only written files, under /tmp.

## Result

There is a useful bounded *engineering* problem: jointly choose a representation
from a frozen small dictionary, construct typed certificates, and retain failures
and resource costs. None of the three inspected calibration certificates requires
a new general cancellation theorem. Exact finite-dimensional synthesis is already
linear algebra; polynomial multiplier synthesis is NulLA/Macaulay linear algebra;
positive local weight synthesis is a facial-set/linear-programming problem.

The two new source-specific obstructions supplied by researcher A are correct
under their intended hypotheses. Their general principles are classical. The
107 obstruction is a particularly clean application of facial-set duality. It
can justify a restricted interaction requirement, but cannot establish a need for
a new mathematical tool or a universal minimum degree across representations.

## Inputs actually inspected

Local: AGENTS.md, RESEARCH_PROGRAM.md, CANCELLATION_TOOL_AUDIT_20261018.md,
UNIFICATION_BOUNDARIES.md, AI_PROOF_EVIDENCE_20261018.md, and
research/corpus/openai_math_sources_20261018.json.

Original source files were independently fetched at openai/math revision
1581d4cbdd69a0faf34b2089614fe2a814316a6a:

- B07, 03-pairing.tex, blob f77a972f6e99d6c7f312c802b7a5b8b59de5a184.
- B18, FiniteProjection.lean, blob 585d246122aebba1c7fec25f180c2fab16e0c92c.
- B19, SquareWeights.lean, blob 2592d0adba3c73d7d8925262e8e2568c79656c1d.
- B21, 02-geometry.tex, blob 615530e1f2e5052afd794b3e0719ce1c28553d23.

These are source inspections, not builds or headline-theorem certification.

## Primary-source coverage

1. Uwe Schauz, *Algebraically Solvable Problems*, EJC 15 (2008), R10,
   https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1r10/pdf .
   Inspected Lemma 1.4(iv), Theorems 3.2–3.3 and the polynomial-modification
   discussion. The coefficient formula expresses a specified leading coefficient
   by weighted evaluations on an integral grid. For a finite field grid the
   normalizer is -1. Distinct field nodes make the denominators invertible;
   arbitrary rings require the integral-grid hypotheses/localization.
   Retrieval: turn148view0, turn150view2, turn150view5.

2. Nira Dyn and Michael Floater, *Multivariate polynomial interpolation on lower
   sets*, JAT 177 (2014), 34–42, DOI 10.1016/j.jat.2013.09.008.
   Independently inspected the authors' MAIA2013 slides, pp. 4–7:
   https://pages.cs.wisc.edu/~deboor/MAIA2013/slides/floater.pdf .
   They state unique interpolation in the lower-set monomial space and its
   Newton expansion; the slides trace the basic result to Kuntzmann (1959).
   Their displayed setting is real, so the finite-field extension is justified
   separately by the nonzero triangular diagonal, not attributed wholesale to
   an analytic interpolation theorem. Retrieval: turn152view1; publication
   metadata and DOI independently verified at the author's institution,
   https://cris.tau.ac.il/en/publications/multivariate-polynomial-interpolation-on-lower-sets/
   (turn161view1).

3. De Loera, Lee, Malkin and Margulies, *Hilbert's Nullstellensatz and an
   Algorithm for Proving Combinatorial Infeasibility*, arXiv:0801.3788v1,
   https://arxiv.org/pdf/0801.3788 . Inspected §2 and §3.1–3.2. Fixed-degree
   multipliers in 1=sum beta_i f_i are found by linear equations in their
   coefficients. Completeness for refuting polynomial infeasibility refers to
   the algebraic closure; finite-field-only feasibility needs the equations
   x_j^q-x_j. Lemma 3.2 permits certificates over the base field. Theorem 3.5's
   invariant/orbit compression preserves existence when char(K) does not divide
   the symmetry-group order. Without that condition the compressed search is
   sound, but its converse is unavailable. Retrieval: turn142view1,
   turn143view3, turn143view4.

4. Rauh, Kahle and Ay, *Support Sets in Exponential Families and Oriented
   Matroid Theory*, arXiv:0906.5462v2,
   https://arxiv.org/pdf/0906.5462 . Definition 6 calls F facial when a linear
   functional is zero on its columns and at least one on all other columns.
   Lemma 7 characterizes this exactly by signed kernel vectors: one sign's
   support lies in F if and only if the other sign's support does. Thus an
   equal-marginal trade is already the complete kind of obstruction needed
   for finite additive-weight selection. The hypotheses are a finite real
   configuration and a constant vector in the row span. Retrieval: turn154view0.

5. Aryaman Maithani, *Splitting the difference: Computations of the Reynolds
   operator in classical invariant theory*, arXiv:2412.18841v2,
   https://arxiv.org/html/2412.18841v2 . Definition 4.1 and Theorem 4.2 specify
   a linear equivariant splitting, with existence for linearly reductive groups.
   Example 4.3 gives the F2 swap of x,y: no equivariant projection exists,
   since it would send x+y to both x+y and 2 pi(x)=0. The finite-group average
   requires invertible group order. Retrieval: turn147view1, turn148view2.

6. Gosper (1978), *Decision procedure for indefinite hypergeometric summation*,
   pp. 40–41, https://sites.math.rutgers.edu/~zeilberg/akherim/gosper1978.pdf ;
   Zeilberger (1991), *The Method of Creative Telescoping*, §§4–5,
   https://sites.math.rutgers.edu/~zeilberg/mamarimY/Zeilberger_y1991_p195.pdf .
   The first decides hypergeometric antidifference existence within its class.
   The second synthesizes recurrence and rational certificate simultaneously
   over a rational-function ground field. This is established cancellation
   discovery, not only checking a supplied witness. Retrieval: turn150view0–1,
   turn156view0–1.

7. Koutschan, *Creative Telescoping for Holonomic Functions*, arXiv:1307.4554v1,
   https://arxiv.org/pdf/1307.4554 . §4 explicitly retains boundary terms;
   variable summation endpoints require corrections. §5.3 gives systematic
   support growth for Chyzak's construction; §5.4's denominator/degree guesses
   are expressly heuristic. Holonomic representation is an input assumption;
   these termination statements cannot simply be transferred to modular
   group actions. Retrieval: turn142view4, turn143view6, turn156view2.

8. Berlekamp, McEliece and van Tilborg (1978), *On the inherent intractability
   of certain coding problems*, DOI 10.1109/TIT.1978.1055873. The authors'
   institutional publication page supplies the primary abstract:
   https://research.tue.nl/en/publications/on-the-inherent-intractability-of-certain-coding-problems/ .
   General decoding is NP-complete. This obstructs a blanket efficient
   minimum-support linear-certificate promise, by the direct syndrome
   decoding reduction stated below. Retrieval: turn147view3, turn148view3.

## Source-specific reductions, independently checked

### 197: annihilation and interpolation are different obligations

For univariate P of degree at most q-1 over a field containing F_q,

    sum_(t in F_q) P(t) = -[X^(q-1)]P.

This follows either from the coefficient formula with derivative of X^q-X
equal to -1 or directly from power sums. Restricting a multivariate polynomial
to a full affine line proves B07's vanishing at degree at most q-2.

For a specified hole set H with |H|=m, put E=ev_H:P_d→K^m. A vector polynomial
f=(f_1,...,f_m) of coordinate degree at most d has hole matrix X whose rows
lie in im(E). If its hole Gram is X X^T=I_m, X is invertible, so E is
surjective. Conversely surjectivity supplies the indicator interpolants,
making X=I_m. Under 2d<q-1, the whole-space and every full-line Gram vanish,
so the retained Gram is -I_m. This is an exact necessary-and-sufficient
interpolation test within this *square* vector-output architecture.

For q=8,n=2,d=3,m=5, five points on a line have evaluation rank at most 4.
The lower set with indices {(0,0),(1,0),(2,0),(3,0),(0,1)} has rank 5 by
Newton triangularity. Counts and degree alone cannot decide the construction.
The test is standard poised interpolation. It is useful as a negative instance,
not a new general theory. Discovering H or a regular retained line family is a
separate combinatorial search; the certificate does not solve it.

### 107: fixed support, allowed locality, and positive weights

Write e=u-v+2(g-h), W=g^2+hu-h^2-hv. Direct expansion gives

    W=(g-h)^2+h e.

Given e, a prescribed square, and the allowed monomial scopes {g},{h,u},{h,v},
finding the displayed identity is bounded syzygy/linear coefficient solving.
Checking W>=0 and its exact zero locus on e=0 uses ordered integer labels;
it is not a finite-field positivity statement. Fourier averaging requires a
primitive root of the declared order; label bounds then turn e=0 modulo L
into e=0 over the integers. These are separate proof obligations.

For M>=3, the two off-target branches (1,2,3,1),(2,1,1,3) and two target
branches (1,1,3,3),(2,2,1,1) all satisfy e=0 and have identical coordinate
marginals. Every unary sum A(g)+H(h)+B(u)+C(v) has equal total on the two
pairs. If it is zero on targets and nonnegative on the phase support, it
must be zero on both off-target branches. This proves A's obstruction.

Using one-hot unary features, this is literally a signed kernel vector
violating Rauh–Kahle–Ay Lemma 7. Arbitrary finite local-feature versions
are already facial-set linear programs with dual trades. The concrete
source-specific degree-two optimum remains a valid restricted conclusion:
degree<=1 polynomials are unary; B19 supplies a quadratic solution.

### 157: the raw certificate is a bounded polynomial consequence

Once each of the six functional equations is evaluated on the other incident
witness, a constant-multiplier sum cancels the paired shared-vector values
and the symmetric bilinear terms. Its value is the inconsistent constant 1
over F2. At this expanded level Gaussian elimination discovers it.

Starting from unevaluated coordinate equations, multiply sharing equations
by the corresponding u-coordinate and functional equations by witness
coordinates. With symmetry built into the parameterization, these use
multiplier degree at most one. Thus a low-degree NulLA/Macaulay baseline
can discover the local contradiction. If symmetry is instead supplied as
separate variables/relations, its multiplier degrees must also be counted.
Neither this observation nor a finite coordinate run discovers the complete
tensor/frame/entropy construction or proves a dimension-uniform family by
itself.

Explicitly in characteristic two, let the row F_ij=u_j U_i+a+T(x_ij,.)
encode the functional constraint, S_ik=U_i x_ik+U_k x_ki the sharing vector,
and E_ij=a(x_ij)+a(x_ji)+1 the edge scalar. Then the polynomial identity is

    1 = sum_(ordered distinct i,j,k) F_ij(x_ik)
        + sum_j u_j(S_ik) + sum_(edges ij) E_ij.

The two directed T terms at each vertex cancel by symmetry. The sharing
summands cancel the uU terms, the E terms cancel the a terms, and three
constants leave one. This explicitly proves multiplier degree at most one
when symmetry is encoded directly. If U,u,T,a are fixed numeric input data,
the original constraints are already affine linear in the witnesses, so ordinary
Gaussian elimination is a complete feasibility baseline.

## Independent adversarial tests and limitations

1. **Two Fourier selectors defeat an unqualified minimum-degree claim.**
   If the allowed method can introduce independent phases g-h and u-v,
   two ordinary root-of-unity filters select the diagonal with no polynomial
   weight. Therefore the degree-two lower bound requires a fixed single
   phase e, fixed tensor-leg scopes, and a declared cost for additional
   selectors. It is not a representation-independent necessity theorem.

2. **The square interpolation architecture matters.** If the output dimension
   r differs from |H|, surjectivity onto K^H is no longer necessary. Over
   characteristic two, the constant evaluation space on three holes has
   dimension one and admits Gram I_1. On two holes the same dimension-one
   space has Gram identically zero. Hence even rank>=r is insufficient in
   rectangular variants: the restricted bilinear form is essential.

3. **The uniform line-Gram degree threshold has a scalar exception.**
   In characteristic two, sum f(t)^2=(sum f(t))^2. For a single coordinate,
   degree d<=q-2 already gives zero diagonal Gram even if 2d>=q-1.
   For at least two coordinates and unrestricted polynomials, products of
   monomials of complementary degrees can reach q-1. Do not promote the
   sufficient threshold to a necessary statement without output dimension
   and quantifiers.

4. **Symmetry in 157 is essential.** An exact F2 counterexample has
   X=F2^2, V=F2^3, a=(0,1), T=[[0,0],[1,0]]. With V coordinates
   (e12,e23,e31), use Ui columns

       U1=(e12,e31), U2=(e23,e12), U3=(e31,e23),
       u1=(1,1,0), u2=(0,1,1), u3=(1,0,1).

   Orient 1→2→3→1, give each outgoing witness (1,0) and incoming witness
   (0,1). All maps are injective and all hole identities hold, yielding a
   triangle. The checker verifies every functional equality on all four X
   vectors (24 checks). If characteristic two is removed instead, even
   X=V=F3, Ui=id, ui=a=id, T=0, witness 2 at every endpoint gives a triangle.

5. **Reynolds unification loses the modular examples.** The additive F_q
   line-sum operator N satisfies N^2=qN=0 in characteristic p. It is not
   a normalized projection. Also X^(p^r)-1=(X-1)^(p^r), so a characteristic-p
   field has no nontrivial p-power root of unity. Fourier diagonalization
   of that additive p-group into scalar characters cannot reproduce its
   modular cancellation. The correct augmentation/radical structure must
   remain explicit. Symmetry compression without nonmodularity can miss
   existing certificates (NulLA Theorem 3.5's exact boundary).

6. **Sparse optimality is stronger than linear feasibility.** Over F2,
   asking for a certificate c of support at most s in a generic dictionary
   with evaluation matrix A and target b asks whether Ac=b has a Hamming
   weight-at-most-s solution: syndrome decoding. General dense Gaussian
   feasibility is polynomial, but this sparse promise includes an
   NP-complete problem. Restrictions or heuristic labels are required.

Exact checker: /tmp/pm_synth_c_boundary.py. Executed with Python; all assertions
passed. This is finite checking of explicit counterexamples, not a proof of
any general positive algorithm.

## Follow-up: independently audited interaction repair statement

Fix M>=3, S={(g,h,u,v) in [M]^4:u-v+2(g-h)=0}, and
D={(x,x,y,y):x,y in [M]}. All weights here are real valued. Require W>=0 on S
and W=0 exactly on D. Assume arbitrary unary terms are free.

**Single pair.** A single additional arbitrary pair function can work if and
only if its pair is {g,h} or {u,v}. Sufficiency is (g-h)^2 or (u-v)^2.
For a cross pair, restricting to D tests every possible pair of its arguments,
so W|D=0 forces that pair function to be a sum of two unary functions.
It can be absorbed into the unary terms; the previous balanced trade then
rules it out. In particular, even an arbitrary nonlinear cross pair is
insufficient. This independently validates the coordinator's proposed repair.

**Complete cross-pair graph version.** If the allowed added pairs are confined
to the four cross pairs {gu,gv,hu,hv}, a weight exists if and only if their
bipartite graph contains two incident edges. For a star at h the source weight
g^2-h^2+hu-hv works; for a star at g use h^2-g^2-gu+gv. For a star at u use
v^2-u^2-4ug+4uh, equal on S to (u-v)^2. For a star at v use
u^2-v^2+4vg-4vh, also equal on S to (u-v)^2. These are nonnegative and vanish
exactly on D.

Conversely, a cross graph without incident edges is contained in one of the
two perfect matchings. The earlier off-target pair versus targets
(1,1,3,3),(2,2,1,1) preserves both gu and hv marginals. The same off-target
pair versus targets (1,1,1,1),(2,2,3,3) preserves both gv and hu marginals.
Each trade therefore rules out every additive function of its matching's pair
features, including arbitrary unary terms. This proves the classification.

Thus source scopes {hu,hv}, with unary g, are exactly the minimal cross-only
repair architecture. Degree two is optimal in this architecture because degree
at most one is unary. Both statements depend on keeping the single support
equation S and counting additional Fourier selectors as changes of the method.
This is an instance-specific application of the established facial-set
criterion, not a new general theorem about cancellation discovery.

## Independent implementation audit

Read tools/construction_contracts.py in full and executed
`python tools/construction_contracts.py` read-only. All assertions passed.

- The 15-by-20 rational system includes every monomial of total degree at most
  two; an affine multiplier times the linear phase creates no omitted higher
  term. The c=2 solution is the source weight. The c=3 solution is
  W=3g^2-3h^2+2hu-2hv, P=2h, with W-Pe=3(g-h)^2. Both agree with symbolic
  expansion. The M=7 supports have respectively 147 and 107 tuples; maximum
  surviving exponents are 9 and 12. These are finite checks accompanying the
  exact coefficient identity, not a general synthesis performance result.
- The 64 interaction architectures have 57 primal quadratic certificates and
  seven trade obstructions. This matches an independent count: any internal
  edge suffices (48 graphs); among the 16 cross-only graphs exactly seven are
  matchings (empty, four singletons, two perfect matchings), leaving nine
  successes. The code's four star formulas and two pair-preserving trades
  match the proof above. Infinite M>=3 scope comes from that proof, not from
  the finite M=7 loop.
- Independently reimplemented F8 multiplication as bit-polynomial convolution
  and reduction, with inverses found by brute search rather than powers.
  Used an independently coded span-rank routine and independently solved the
  five indicator interpolation systems instead of using the code's displayed
  Lagrange formula. Reproduced ranks [5,4], barycentric vector [2,6,5,7,6],
  moments [0,0,0,0,1], punctured Gram I5, and zero Gram on all 72 distinct affine
  lines. The cubic t^3+t+1 has no F2 root and is therefore irreducible.

The complete independent replay source is preserved as
`/tmp/pm_synth_c_gf8_check.py`. After persistence it was executed with
`python /tmp/pm_synth_c_gf8_check.py` and reproduced all the preceding values.
It imports no primary construction code and additionally checks all five
cardinal evaluation vectors explicitly. It is suitable for a separate exact
CI replay step; the coordinator owns any repository copy and CI integration.

No correctness contradiction was found. Acceptance is for the exact local
baseline computations and the explicitly bounded architecture conclusions.
The integrated mathematical note remains to be read separately; this is not
historical novelty certification, Lean verification, or validation of any
upstream headline theorem.

Also read and executed tools/triangle_contracts.py. Its ranks (8,9) in
characteristic two, (9,9) in odd characteristics and after the relevant grammar
constraints are removed, and (8,8) for even edge parity agree with the scalar
system. The new no-hole control is valid: X=F2^2,V=F2^4, a=(1,1),T=I2,u_i=0,
U_i(e1)=e1,U_i(e2)=e_(i+2). All three maps are distinct and injective, T is
symmetric and nondegenerate, and T(x,x)=a(x). Functional constraints force both
witnesses to (1,1); these fail sharing for different i and also fail edge parity.
There are 48 witness pairs and zero holes. This refutes a positive-density
conclusion from those local algebraic hypotheses. The odd-characteristic
triangle does not preserve u_i U_i=0, which is not an assumption of the original
triangle lemma; do not claim it preserves the complete raw-frame construction.

## Follow-up: all-powers stability and strict separation

The coordinator's proposed finite integral grading lemma is correct. Let S be
finite, D a subset, w:S→Z^k with w(d)=0 for d in D, and n range over positive
integers. Then

    for every n and s_1,...,s_n in S,
    sum_i w(s_i)=0 iff every s_i lies in D

is equivalent to existence of c in Z^k with c·w(s)>0 for every s outside D.
If S\D is empty, handle the vacuous case explicitly. Otherwise failure of a
strict separator is exactly a nonzero nonnegative real relation on the finite
off-target weight vectors. Rational data permit a rational relation, and
clearing denominators produces an obstructing multiset. Conversely such a
separator rules out every multiset containing an off-target. Rational strict
separation can itself be cleared to integral c. In dimension one this is
equivalent to all off-target weights having the same strict sign.

The real-cone alternative is the original result of P. Gordan, *Ueber die
Auflösung linearer Gleichungen mit reellen Coefficienten*, Math. Ann. 6 (1873),
23–28, DOI 10.1007/BF01442864. Publisher metadata was checked at
https://link.springer.com/article/10.1007/BF01442864 and the original scan read
at https://scispace.com/pdf/ueber-die-auflosung-linearer-gleichungen-mit-reellen-4fjlz4l0s4.pdf .
Its first page states the equivalence between no nonnegative nonzero homogeneous
solution and deriving a linear combination with all coefficients strictly
positive. Retrieval: turn164view1, turn168view0. The finite rational grading
corollary is thus a classical separation consequence, not a new general theorem.

Both restrictions have explicit failures. For real weights {1,-sqrt(2)}, no
nonempty integer multiset sums to zero, yet no common positive linear functional
exists. For the infinite integral weight set {(1,n):n in Z} union {(0,-1)},
there is likewise no nonempty zero-sum multiset, but a common strict separator
would require its second coefficient both zero and negative. Finite rational
data must be retained.

A shifted middle coefficient is an ordinary-polynomial local escape from
constant-degree selection: w=g-h+(M-1) lies in [0,2M-2] and selecting coefficient
M-1 picks the diagonal on the source phase support. Its centered defect g-h
takes opposite values on the two exposed off-target branches, so it fails
all-powers additive stability. Nonnegative defect with degree-zero target is
therefore a substantive stability contract; it is not a restriction forced by
the existence of any one-shot polynomial coefficient selector.

## Final integrated-statement audit

Read research/mechanisms/CONSTRUCTION_CONTRACTS.md in full after the coordinator
wrote it. All four propositions, their hypotheses and proofs, and the claimed
computation outputs were independently checked. No mathematical correctness
objection remains.

- PM-CONSTRUCTION-0001: the graph iff criterion, all four stars, matching
  trades, count 57/7, fixed-contract degree optimum and explicit escapes are
  correct. The code's 15-by-20 coefficient synthesis faithfully instantiates
  the prescribed-square baseline.
- PM-CONSTRUCTION-0002: the iff uses the necessary square output matrix
  correctly; 2d<=q-2 suffices in every finite field. The general same-budget
  H-plus/H-minus example, explicit cardinal functions and barycentric dual
  obstruction are valid for n>=2,d>=1 under the stated bound. The F8 evidence
  matches independent arithmetic and interpolation.
- PM-CONSTRUCTION-0003: the characteristic-two parity conclusion and the
  constant-row six-evaluation completeness proof are correct. The two row
  cancellation transpositions generate S3; equal plus-edge coefficients
  impose 2w=0. The raw multiplier identity, no-hole richness control and the
  restrictions on the odd-characteristic example are accurately separated.
- PM-CONSTRUCTION-0004: the finite integral multigrading equivalence, rational
  separation/denominator argument, scalar sign corollary and product failures
  of shifted/signed defects are correct, including the empty off-target case.

Requested only two notational precision changes: explicitly call k a field in
0003 and write D subset Omega in 0004. The coordinator also intends to add the
infinite integral boundary and original Gordan citation recorded above. These
do not repair a false theorem; they make the already intended scope explicit.
The source, baseline, calibration and non-novelty limitations are appropriately
stated. Acceptance remains a mathematical/code review by an AI researcher,
not formal verification, historical priority certification or source headline
verification. All repository inspection remained read-only.

## Concrete falsification protocol

Freeze a bounded synthesis class before further calibration: an exact scalar
field, operator/feature dictionaries, maximal polynomial degree D, certificate
degree, allowed tensor-leg scopes, admissible phase count/period, and a cost
measure. Include every representation choice in the input and account for it.

Baseline each component with its strongest existing algorithm: interpolation
and moment nullspaces; facial-set LP and dual trades; bounded NulLA; ordinary
Fourier selection with multiple filters; and a summation package on its supported
input class. A solver that only receives a hand-picked square, phase, or evaluated
six-equation contradiction has been given the principal representation clue.

The immediate test panel is:

- q=8 degree-3 five-collinear versus the five-point lower set;
- degree q-1 line sums, whose residual is -1 for X^(q-1);
- 107's M=3 unary impossibility versus allowed pair interactions;
- M=2, where the phase already selects the diagonal;
- nonprimitive zeta=1 with M=4 and branch (2,1,1,4): W=0 but e=-1;
- primitive period 5 without label bounds, branch (10,5,1,16): W=0,e=-5;
- the two explicit triangle counterexamples above;
- a generic sparse affine system known to require a large support.

Every promised completeness result should reproduce the baseline's yes/no
outcome within the frozen class and reject the damaged hypotheses. If a proposed
method has identical feasible certificates, merely reroutes them through a larger
kernel, and shows no resource or transfer gain, retire the new-tool claim.
If it finds a representation or a compact uniform family certificate with a proved
bound that the baseline was not supplied, that is the residual research target;
label known synthesis, instance-specific extension, and historical novelty
separately. These exposed examples remain calibration, never held-out transfer.

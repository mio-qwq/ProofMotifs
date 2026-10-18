# PM-IMPLICIT-C — independent adversarial gate

## 1. TASK ID

PM-IMPLICIT-C, task-scoped researcher `/root/mixed_seed_c_ultra`. Requested
configuration GPT-6.1 Sol Ultra; actual model/effort metadata not independently
exposed. No human review or formal-assistant compilation is claimed.

## 2. RESEARCH QUESTION

From raw m distinct points H subset K^n, discover an evaluation basis and
degree-minimal cardinal polynomials, without a prelisted monomial dictionary
or enumeration of every ambient monomial up to the final degree. Challenge
degree pruning, plateau stopping, finite-field separation and resource claims.

**Verdict:** a degree-layered coordinate-product span algorithm works, in
polynomially many field operations, over every effective field. However,
arbitrary degree-only ordering does **not** justify pruning all multiples of
rejected monomials. A five-point counterexample below is decisive.
The positive construction is directly classical Buchberger–Möller territory,
not evidence of a missing general interpolation tool.

## 3. KNOWN ASSUMPTIONS

n,m>=1; H=(h_1,...,h_m) consists of pairwise distinct points of K^n. K has
exact effective arithmetic, division by nonzero elements, and decidable zero
tests. Bounds below count field operations/equality tests, not a uniform bit
complexity across arbitrary effective fields. Points are supplied explicitly.

Let ev(f)=(f(h_1),...,f(h_m)), and let V_d=ev(K[x]_<=d), with V_-1=0.
Coordinate multiplication is the known diagonal operator
D_i(v)_j=h_(j,i)v_j. The optimum common degree is

    d*=min{d: V_d=K^m}.

The algorithm below actually supplies a minimum-total-degree polynomial
representative for every evaluation target separately, so each cardinal
coordinate is simultaneously degree-minimal. This implies both optimal
maximum coordinate degree and optimal sum of coordinate degrees. These
objectives should still be distinguished from minimum sum of basis-monomial
degrees or minimum monomial support/circuit size.

## 4. AVAILABLE EVIDENCE / CLASSICAL BASELINE

Read AGENTS.md in full and the controlling research/RESEARCH_PROGRAM.md
(full in the preceding task, current leading sections reread). For source197,
read research/mechanisms/CONSTRUCTION_CONTRACTS.md through the full
PM-CONSTRUCTION-0002 theorem/proof/boundaries. Its local hole problem is
surjectivity of degree-bounded evaluation, not validation of the source's
headline or incidence construction. No current `/tmp/pm-implicit-a` or `b`
notes were opened, and no Git operation was used.

One bounded structural search found the original author-hosted paper:

H. M. Möller and B. Buchberger, *The Construction of Multivariate Polynomials
with Pre-assigned Zeros*, EUROCAM1982, LNCS144, pp.24–31.
<https://www3.risc.jku.at/people/buchberger/papers/1982-04-00-A.pdf>

The author bibliography identifies the 1982 venue; do not substitute a later
digitization/index date. The author-hosted PDF has nine scanned manuscript
pages, all read visually, including references. Algorithm2 (manuscript pp.3–4)
generates interpolation terms through evaluation and border candidates rather
than a supplied dictionary, with ideal-compatible pruning; its correctness is
proved on p.5. The paper states O(n^2 m^3) arithmetical operations on p.4.
Sections5–6, pp.7–8, adapt the term selection to total degree. Identity(9)
ensures selected terms up to degree d represent every degree<=d polynomial
modulo the point ideal, yielding a unisolvent degree-controlled interpolation
space. Thus the essential raw-point/implicit-feature operation is already
present in the primary source. Our simpler evaluation-vector field-operation
count below is not a claimed improvement over modern BM implementations.

No historical novelty or exhaustive literature claim is made.

## 5. EXPECTED OUTPUT / INDEPENDENT PROOF AND COUNTEREXAMPLES

### PM-IMPLICIT-C-1: small-field-safe separation and finite degree bound

For each ordered pair i!=j choose a coordinate ell(i,j) with
h_(i,ell)!=h_(j,ell). Then

    L_i(x)=product_(j!=i)
           (x_ell(i,j)-h_(j,ell(i,j))) /
           (h_(i,ell(i,j))-h_(j,ell(i,j)))

is cardinal on H and has total degree<=m-1. Every denominator is genuinely
nonzero. Hence evaluation of all polynomials is onto and d*<=m-1. This works
in every characteristic and does not require a linear form separating H.

For example no linear form is injective on the four points F_2^2, since its
image has at most two values; nevertheless 1,x,y,xy is an evaluation basis
and d*=2. An assumption that a generic linear form separates the input would
silently exclude this legitimate field/input.

### PM-IMPLICIT-C-2: safe degree-frontier discovery

Start with B_0={1}. At the end of layer d retain all previously accepted
monomial representatives and let W_d consist of newly accepted degree-d
monomials, whose evaluations form a complement of V_(d-1) in V_d. Generate
the next candidates only by x_i*b for b in W_d, i=1,...,n. Evaluate these as
D_i ev(b), and keep exactly those that increase the cumulative span. Complete
the layer, or stop as soon as rank m is reached. Crucially, do not suppress a
candidate merely because some other divisor was rejected.

**Invariant and proof.** The retained monomials of degree<=d evaluate to a
basis of V_d. Indeed

    V_(d+1)=V_d+sum_i D_i V_d
           =V_d+sum_i D_i span(ev(W_d)),

because D_i V_(d-1) subset V_d. Therefore coordinate products of the newest
frontier, together with the old span, generate exactly the next degree
filtration. Exact incremental elimination preserves precisely that span.
This induction justifies discarding dependent vectors; it does not assert
that the rejected monomials form a monomial ideal.

If a complete layer gives V_(d+1)=V_d, then V_d is stable under **all** D_i
and contains1. Hence it contains every monomial evaluation, and therefore is
K^m by PM-IMPLICIT-C-1. Thus a true complete-layer plateau of rank<m cannot
occur on valid input. A rejection of one coordinate product, or no growth in
an unfinished queue prefix, is not such a plateau.

### PM-IMPLICIT-C-3: exact degree optimality and cardinal maps

Let B be the final m retained monomials and let E_(j,b)=b(h_j). E is invertible.
For any target v, the unique interpolant p_v=sum_b (E^-1 v)_b b satisfies

    deg(p_v)<=d iff v belongs to V_d.

For the forward implication use evaluation. For the reverse implication,
B_<=d already evaluates to a basis of V_d, and uniqueness in the full B basis
forces all coefficients on degree>d terms to be zero. Thus p_v has the least
possible ordinary formal total degree among every polynomial interpolating v.
Set v to each standard coordinate vector to obtain the cardinal maps. This
also proves d* is minimal, rather than merely an upper bound from termination.

Degree-layer greedy additionally minimizes the sum of degrees of an evaluation
monomial basis: for every d it takes exactly dim V_d independent terms of
degree<=d, the largest number any independent family can contain there.
No shortest circuit, sparsest polynomial or optimal coefficient-height claim
follows.

### PM-IMPLICIT-C-4: explicit invalid divisibility-pruning example

Over Q take

    H={(0,0),(1,1),(2,2),(3,3),(0,1)}.

At degree2, suppose xy is processed before x^2,y^2. The evaluations of
1,x,y,xy are independent. On H,

    x^2=xy,                  y^2=xy-x+y.

So both squares are rejected. If the algorithm now prunes **all multiples**
of these rejected monomials, only 1,x,y,xy remain and it falsely stops at
rank4<5. But x^2*y has a new evaluation: on the four diagonal points it is
t^3, adding the missing Vandermonde direction. The actual degree ranks are

    dim V_0,V_1,V_2,V_3 = 1,3,4,5.

No admissible multiplicative monomial order puts xy before both squares.
BM's leading-term pruning has an ordering hypothesis; arbitrary degree ties
do not inherit it. Our safe vector-frontier method processes the retained
xy's coordinate products regardless of rejected divisors and therefore works.

### Additional adversarial boundaries

* Premature rejection: H={(0,0),(0,1)}. The x candidate is zero/dependent,
  but y is new and rank2. Stopping after x is wrong.
* Degree loss under arbitrary acceptance order: on H={0,1,2} in Q, the
  evaluations of 1,x^2,x^3 are independent, but they have maximum degree3
  while optimum is2. Indeed x=(3/2)x^2-(1/2)x^3 on H. Rejecting a low-degree
  vector because of previously retained high-degree vectors loses the degree
  invariant.
* Distinct points are essential: duplicate rows prevent surjective evaluation
  onto separately indexed coordinates. Validate distinctness or quotient
  duplicate input points explicitly.
* Formal polynomial degree, reduced polynomial-function degree, and supplied
  expression degree differ. For example x^2=x as functions on F_2, but the
  formal expressions have degrees2 and1. The proof tracks actual formal
  monomial representatives and their degree filtration, not a degree label
  inherited from an unreduced expression or a finite-field function table.

## 6. ALLOWED SCOPE / COST / ACTUAL CHECKS

Repo read-only; own files only `/tmp/pm-implicit-c.md` and
`/tmp/pm_implicit_c_checker.py`. No child agents, Git operations, outbound
messages outside the research team, or current competing child-note reads.

At most m independent evaluation vectors are ever retained. Expand each
retained vector at most once under each of n coordinate multipliers, for at
most nm product candidates (plus the initial1). Vector formation costs
O(nm^2) field operations; incremental elimination costs O(nm^3); final matrix
inversion costs O(m^3). There are at most m-1 nontrivial degree layers.
This does not enumerate all binomial(n+d,d) ambient monomials.

Basis exponents have degree<=m-1. An explicit cardinal polynomial uses at
most m basis monomials; all cardinal coordinates use at most m^2 coefficients
with shared basis labels. Exact coefficient bit growth, input encoding,
exponent-vector copying and arbitrary-field arithmetic costs are separate.

Actual commands included read-only rg/sed discovery, the primary web query and
visual reading of all nine PDF pages, and:

    python /tmp/pm_implicit_c_checker.py

The dependency-free exact checker independently implements degree-frontier
generation. It passed every nonempty subset of F_2^3 (255 cases), comparing
each degree rank against an exhaustive tiny-case oracle; full F_3^2 with
optimum4; seven rational collinear points with optimum6; mixed hole geometry;
and all negative examples above. Exhaustive monomial enumeration occurs
**only in that bounded regression oracle**, not in the discovery algorithm.
These finite checks support, but do not replace, the arbitrary-field proof.

## 7. INDEPENDENCE REQUIREMENT / REVIEW STATUS

The positive filtration proof, complexity analysis, separator argument and
objective clarification were sent before reading coordinator code or any
other child's proposal. The five-point non-ideal-pruning counterexample was
also independently constructed and sent. The original BM paper was then read
as the classical comparison. No current child a/b notes were inspected.

The coordinator subsequently supplied code for a specifically requested audit;
see the completed audit below.

## 8. STOP CONDITIONS

Bounded theorem/adversarial/primary-source gate complete. Do not turn this into
unlimited geometry classification or claim a new interpolation theory.
For source197 this solves the supplied raw-hole, fixed-coordinate,
total-degree interpolation obligation; it does not discover the surrounding
representation grammar, regular incidence, tensor construction or headline
theorem. No held-out transfer or AI causal conclusion follows.

## 9. HANDOFF

Accept the raw-point coordinate-frontier algorithm with degree-safe complete
layers and all-coordinate expansion. Reject arbitrary divisor pruning unless
an admissible term-order/leading-term argument is supplied. Include the
five-point rational counterexample in tests. Keep exact field-operation
complexity distinct from bit complexity and preserve actual formal degrees.
Recognize BM1982 as a direct existing baseline. Proceed only to bounded
coordinator code review if requested, then return to the macro gap.

### Completed coordinator proof/code audit

Read complete files, read-only, at these actual SHA256 hashes:

    tools/implicit_evaluation.py
      1632a9e1aa312b2eae36e03a10a802554b0cd0a95597d11722c3a5e95ede03dc
    tests/test_implicit_evaluation.py
      48c0b2423d23eaaaab3501103fa5945e3612ed56a18a96d63fb0af14b674f080

The implementation uses exact Q or prime-field arithmetic, validates distinct
points, and expands complete degree frontiers without divisor pruning. The
only early stop is full rank. Its final certificate includes the actual
monomials, inverse evaluation matrix, and all n*m coordinate-border expansions.

**Independent verifier proof:** let F_d be the span of the supplied basis
monomials of actual degree<=d. Actual evaluation gives F_d subset V_d.
The constant is present, and the checked border expansions show
D_i F_d subset F_(d+1) for every coordinate i. Induction on monomial degree
gives V_d subset F_d. Hence F_d=V_d at every degree, without replaying the
constructor. Invertibility then establishes all target interpolants and their
minimum degrees. A selected nonzero inverse row at the target's top degree
annihilates V_(d-1) and pairs nontrivially with the target, a valid lower-bound
certificate. The proof is not merely finite ranks at a sampled cutoff.

Commands run with PYTHONDONTWRITEBYTECODE=1 and python -B to avoid repo caches:

    python -B -m unittest discover -s tests -p 'test_implicit_evaluation.py' -v

All six unit tests passed. A separate inline runpy program loaded my independent
checker and the root source, and crosschecked root construct/verify/optimum for
all255 nonempty subsets of F_2^3 against my exhaustive tiny-case oracle.
The five-point nonideal-pruning case also passed with Hilbert profile1,3,4,5.

No core mathematical or arithmetic defect found. Two minor public-schema
boundaries were tested and reported to the coordinator:

* `hilbert_profile[0]=True` passes because BooleanTrue compares equal to1;
  exact integer type checking would clarify a strict JSON schema.
* `observed_coordinate_offers` and `proved_offer_bound` are not checked by
  verify, even if set to -100. These must be explicitly construction telemetry,
  not independently verified execution claims. Checking the claimed bound
  equals n*m is easy; certifying an actual offer count requires replay or
  an execution log. The algorithmic bound itself has the structural proof.

The root prototype stores a full O(nm^2) border table. No streaming-memory,
uniform bit-complexity, or novelty claim is accepted. The implementation's
Q/F_p restriction is narrower than the mathematical arbitrary-effective-field
theorem. Subsequent edits require their own disclosed hashes; this audit is
scoped to the exact versions above.

### Final narrow regression / resolutions

The coordinator subsequently hardened only the schema/reference boundaries.
Read the complete latest source and tests again, with final SHA256:

    tools/implicit_evaluation.py
      a158f77cbacd533e1bf454d9f1e04ae38815e066fcd57a615f51335d420d1b20
    tests/test_implicit_evaluation.py
      b0abe961b92b5e8194b7da3cc560cb7a188eb831c1144e1fc14804794cfad356

All seven unit tests passed, including the new five-point rejected-divisors
regression. Independently reran the full255 nonempty F_2^3 subset crosscheck
against my separate degree oracle; every constructor/verifier/optimum check
passed. The five-point cardinal degrees were also checked individually as
3,3,3,3,1.

All reported schema issues are resolved at these versions: Hilbert-profile
entries require strict int; the proved bound requires strict int equal to n*m;
observed offers require strict int in0..n*m. Explicit negative checks rejected
Boolean entries, negative values and counts above n*m. The observed count is
still deliberately telemetry, not a replayed execution certificate; the error
message states that limitation. Q integer inversion now returns exact
Fraction(1)/x; verified inv(2)=Fraction(1,2). Every demo now includes its raw
points, and its included certificate reverified against those points.

Commands used python -B / PYTHONDONTWRITEBYTECODE=1 for coordinator imports and
unit tests. My independent checker was rerun successfully unchanged: it does
not import the coordinator API and needed no compatibility edits. No new
research, Git operation, repo edit or child task was undertaken. Final audit
accepted; bounded child task complete.

### Final integrated-prose review

At the coordinator's final narrow request, read the consolidated
research/mechanisms/REPRESENTATION_TRANSPORT.md completely, without new
research, code edits, Git operations or other child-note reads. Review scope
includes the mathematical prose itself, not only the previously audited code.
The reviewed consolidated file had243 lines and SHA256
1ada265c5d9a1fbfd8330aa8f16d1c4c86c566fded61a2ee35b8ea4b05264933.

The generalized mixed-seed theorem was checked for u=a*z^r, a!=0, Q=q^r:
the monomial calculation has the required factor a^2 and denominators
t-1,Qt-1 with t=q^(m+r); the eliminated relation has Q-1 and c(Q-1)
with no missing a or r factor. S=1-c*M_u is a genuine formal-series unit;
the abstract ideal-membership identity and its counterexample without a unit
are correct. No inverse of an integration operator is smuggled into the proof.

The raw-point theorem, every-target degree optimality, frontier induction,
complete-closure plateau rule, arbitrary-field pairwise separators, candidate
bound and field-operation/output costs were checked. The finite border
certificate really proves the entire degree filtration by induction, not
only a finite sampled rank assertion. The source197 equivalence within the
square-output/ordinary-degree cutoff is mathematically correct. No historical
novelty, uniform bit-complexity, headline validation or held-out-transfer
overreach was found.

One prose correction was reported in section6: an inverse row at excessive
degree does NOT literally "exclude every legal polynomial in that budget"
(zero and many legal polynomials remain). It certifies nonsurjectivity, hence
excludes every legal polynomial VECTOR realizing the prescribed square
punctured-Gram target; alternatively it excludes a specific cardinal target
whose dual pairing is nonzero. The core theorem is unaffected. Acceptance
of that sentence is conditional on this target-qualified wording correction.

No further mathematical, algorithmic or source comparison work was undertaken.
Final consolidated-main-proof review complete; stop.

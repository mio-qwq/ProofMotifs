# Succinct cancellation certificates and uniform finite-jet interfaces

Date: 19 October 2026 (Asia/Singapore). Status: proved scoped propositions,
classical reproduction/source-derived synthesis, exact implementation controls,
and one preserved **failed** pre-proof transfer. Not a new universal tool,
capability experiment, historical originality result, human review or Lean proof.

## Why this continuation belongs to the macro program

The preceding finite-dictionary optimizer assumes all candidate features are
already supplied. This continuation asks whether a compact structure can
*generate* a sufficient test representation without listing exponentially many
words or paths. This advances PM-H4/H5 at a precise interface, not by treating
every equality as a kernel. It also exposes a distinct question: certifying
one supplied object is not the same as constructing one map that works for
every object of bounded complexity.

The preregistered target and operation are in
`research/experiments/succinct-transfer-protocol.json`. Its public freeze commit
is `2b8dd9e15462030b944fa220b8587e81a8e1e60f`. The statement-level decision was
saved in `succinct-statement-decision.md` before proof access was released.
The title-targeted external source was family116, not a representative sample.
No model-training holdout claim is possible.

## 1. Reachable-space generation: exact classical baseline

**PM-SUCCINCT0001.** Let K be a field, lambda a row of length r, gamma a column
of length r, and A_i explicit r-by-r matrices for a finite alphabet. Define
c(w)=lambda A_w gamma, with A_empty=I. There is an exact actual-word reachable
basis B with at most r rows. If its rank is d>0, its words can have length at
most d-1. Either some basis word is a nonzero witness, or local equations

\[
 \lambda=\alpha B,\qquad BA_i=C_iB\ (\text{every }i),\qquad B\gamma=0
\]

certify that every coefficient c(w) vanishes. These equations alone suffice
for zero soundness; independence and provenance certify the additional
exact-basis/rank claim, not zero soundness.

Proof. Generate lambda, then offer each accepted row times every A_i to
incremental exact elimination, retaining only independent successors and a
parent/letter annotation. Each addition increases dimension. At termination
the span contains lambda and is invariant, so it contains every lambda A_w;
all retained rows are themselves reachable, proving equality. Let R_t be the
span of words of length at most t. A plateau R_t=R_(t+1) implies invariance
and finality. Starting from dimension one when lambda is nonzero, there are
at most d-1 strict increases. Thus R_(d-1) is final and provides the stated
word bound. The local equations give lambda A_w=alpha C_w B by induction.
Annihilation proves zero; otherwise a reachable basis row gives a witness.
For lambda=0 use the empty basis. A shift on r states, with lambda at the
first state and gamma at the last, has its first witness at r-1, so the
bound is sharp. This proof works in every characteristic.

Generation uses O((n+1)r^3) field operations and O((n+1)r^2) certificate
scalars. For prime fields the field must be specified; for Q the rational
input height and elimination growth count. A common input denominator makes
all words of length <=r integer products divided by its <=r+1 power;
bounded-order minors then bound coordinate bit lengths polynomially. This
gives a polynomial bit implementation, not a generic guarantee for every
unnormalized program. See independent A2a for the full height argument.

The executable checker in `tools/reachable_series.py` deliberately replays
each basis word separately and verifies rank by separate full elimination;
its stronger verification can cost O(r^4+nr^3), even though synthesis is
cubic in field operations. Its primality checker is trial division for the
small test primes, **not** a polynomial-in-log-p arbitrary-prime implementation.
Layered width W and explicit length L use separate prefix spaces, at cost
O(nLW^3); width alone does not bound witness length. These distinctions are
part of the contract, not implementation footnotes.

Primary match: Kiefer2020, Algorithms1–2, Propositions2.1–2.2 and §3 explicitly
give this construction, bound and intertwining summary. CAV2011 §2.1/Fig.1
gives its dual and cubic implementation. Raz–Shpilka2005 §2/Theorem4 supplies
the noncommutative ABP counterpart, explicitly white-box in §1.1. Thus this
is reproduction/certificate packaging, not a missing theorem.

### Access and composition obstructions

**PM-SUCCINCT0002.** A deterministic tester using only scalar word-coefficient
queries, with a promise of r=D+1 states, needs n^D queries in the worst case
to distinguish zero from all singleton length-D series. Proof: each word u
has a D+1-state labelled chain supported at u alone. On the all-zero query
transcript, any unqueried u remains indistinguishable from zero. This is a
restricted oracle lower bound, **not** a matrix-hitting-point lower bound.

Scalar evaluation is an even different interface: xy-yx has nonzero formal
coefficients over every field but is zero at every commuting scalar pair.
A one-seed invariant summary also cannot be rewired arbitrarily: retain the
embedding B and certify every incoming boundary row and every new transition.
Changing the terminal column can undo a scalar cancellation. For instance
(1,-1)(1,1)^T=0, but (1,-1)(1,0)^T=1. Direct sums and synchronized Kronecker
products preserve the appropriate equations; they do not give bounded cost
under indefinitely many products. See independent A4 for full interfaces.

## 2. Frozen external test: a failed transfer, not a failed theorem

Family116's selected theorem takes **only** p,n,s and outputs one matrix tuple
over F_p for all size-bounded formulas and all coefficient extensions of F_p.
The frozen operation instead takes a particular formula's explicit transition
matrices and constructs input-dependent words. Even a polynomial formula-to-
ABP conversion cannot consume a formula absent from the target input.

This input/quantifier mismatch was recorded before reading the proof. It
remains the transfer verdict. A compatible local lemma is not headline success.
The proof's formula-specific matrices serve as witnesses to a universal size
bound, not as generator inputs. We have not refuted the target theorem.

### What the released proof actually does

| Operation | Input/structure | Certificate or first surviving term | Boundary |
| --- | --- | --- | --- |
| Independent word-series encoding | Infinite-order multiplicative shift, rational poles in disjoint shift orbits | Minimal relation plus two uncancellable endpoint poles proves injectivity | Finite-order shift/overlapping orbits do not supply this argument |
| Uniform order control | Invertible regular fundamental matrix H, rational shift system of degree <=nu | Casoratian leading Vandermonde and unit-minor invariance bound ord(uHv) by nu*binom(m,2) | Infinite-order shift, constant endpoints and regular invertibility are essential |
| Finite coefficient descent | Known common denominator D, regular at zero, and cleared degree <E | Nonzero cleared polynomial survives E-jet; regular representation is faithful | Without a degree/valuation budget, truncation can erase nonzero terms |

The source uses b_i=z/(1-(1+t)^i z) and sigma(z)=tz. Transcendental t makes
t^a distinct for different integers a, in every characteristic. Its q-integral
operators divide coefficients by t^r-1, not by r. This avoids the ordinary
derivative's positive-characteristic collapse. The source's proof is read and
independently challenged, but no formal compilation/headline certification or
historical priority conclusion is made here.

Two mechanisms are genuinely different: (i) interior pole cancellations are
allowed while two boundary poles obstruct an exact difference; (ii) many early
series coefficients may cancel, but a Casoratian bounds their possible delay.
The latter directly addresses a first-surviving-term question. A general
explanation of AI success does not follow from finding it in this proof.

Necessary-hypothesis counterexamples for the order bound:

- Without H invertible over K[[z]], take scalar H=z^M, A=tau^M, nu=0.
- If tau has finite order q, take H=I+z^(qM) E_12 and A=I. Constant endpoints
  select z^(qM), violating every claimed nu=0 order bound. For tau=1 any M works.
- For ordinary differentiation in characteristic p, H=I+z^p E_12 satisfies
  H'=0 but has a nonzero component of order p. The infinite-order shift avoids
  precisely this degeneracy; it cannot be simulated by a finite-field element
  of supposedly infinite order.

These are algebraic controls of a source argument, not a new theorem of ours.
The source cites rational q-summation, hyperlogarithm independence, multiplicity
estimates and Wronskians. Independent review found additional q-multiplicity
literature (Bertrand2010/2012), requiring exact comparison before any novelty
claim. The retrieved Bertrand author file is January2007 slides, **not** the
journal article. Moura2003 and that full journal comparison remain unaudited.

## 3. Path-aware finite-jet compiler: source-derived general synthesis

**PM-SUCCINCT0003 (proved upper bound).** Let V_1,...,V_n be h-by-h rational
matrices over K(t), all supported on a supplied common DAG. Each nonzero
labelled edge e contributes

\[
 a_e(t)\big/\prod_{j=1}^{J}q_j(t)^{e_{ej}},\qquad q_j(0)\ne0,
\]

where a_e is nonzero and the exponents are nonnegative integers. Sums of
parallel labelled edges are allowed. Include empty paths at every vertex and
all choices of variable label/parallel term in every path maximum. Define

\[
 M_j=\max_P\sum_{e\in P}e_{ej},\quad D=\prod_jq_j^{M_j},\quad
 c_e=\deg a_e-\sum_je_{ej}\deg q_j,
\]
\[
 L=\max\bigl(0,\max_P\sum_{e\in P}c_e\bigr),\qquad
 E=1+\deg D+L.
\]

For **every** noncommutative polynomial f with coefficients in **any** constant
field extension K'/K, with t still a fresh indeterminate over K', each entry
of D f(V) is a polynomial of degree <E. Reducing entries of
V modulo t^E and taking their multiplication matrices on K[t]/(t^E) gives a
tuple T of hE-by-hE base-field matrices with

\[
 f(V)=0\quad\Longleftrightarrow\quad f(T)=0.
\]

This preserves evaluation at the supplied tuple. It does **not** say every
nonzero free polynomial has nonzero evaluation there; the tuple may satisfy
many identities. No word encoding or formula-size multiplicity bound is
inferred from this compiler alone.

Proof. Every word-entry summand follows a labelled DAG path of length <h.
For a path P its denominator exponents s_j satisfy s_j<=M_j, so multiplying
by D leaves the polynomial

\[
 \prod_{e\in P}a_e\prod_jq_j^{M_j-s_j}.
\]

Its degree is deg D+sum_(e in P)c_e, at most E-1. Empty paths account for
the constant word. Linear combinations over K' cannot increase degree, even
when large cancellations occur. No coprimality, irreducibility or absence of
shared factors is assumed. The nonzero constant term makes D a unit in the
power-series ring and every E-jet ring. A nonzero polynomial of degree <E
cannot have zero E-jet; hence f(V) and its reduced matrix have the same
zero/nonzero status. The regular representation of K'[t]/(t^E) is an injective
unital algebra map: multiplication by a, applied to1, recovers a. Entrywise
block substitution therefore preserves evaluation and is compatible with
scalar extension. This proves both directions.

Construction: topologically order the common DAG. Longest-path dynamic
programs for each nonnegative exponent weight and once for the signed degree
cost compute M_j,L without enumerating paths; allow start/stop at every vertex
and empty path value0. Cost O((J+1)(|V|+|E_graph|)) integer operations, plus
polynomial degree/jet arithmetic and dense output. The compiler is polynomial
in expanded degrees and E/output length. If exponents are binary encoded, E
can be exponentially large in their bit length; no input-only polynomial-time
claim is made. The upper bound depends on the supplied edge presentation;
it is not a minimal denominator, minimal dimension or optimal jet theorem.

### Parametric cost control and failures

On the complete increasing DAG on0,...,h, assign denominator 1-jt to every
edge arriving at j and numerator1. A path uses each arrival at most once, so
M_j=1, deg D=h, L=0 and E=h+1. There are 2^(h-1) paths from0 to h. An explicit
naive denominator-per-matrix bound would reuse G=prod_j(1-jt) on each of at
most h steps, yielding G^h and E_naive=h^2+1. This is a proved reduction in
that **naive sufficient resource bound**, not a speedup over the best classical
DAG-aware algorithm, a claim of minimal E, or a performance measurement.

A global common DAG is a composition contract: joining fragments with a new
cycle invalidates it. For V=[t], any proposed fixed E loses f(V)=t^E from f=x^E.
For V=[1/(1-t)], f=(x-1)^E likewise starts at order E. Regularity alone is not
enough. Even on a DAG, too short a jet fails: let V_x=(1-t)^(-1)E_01 and
V_y=E_01. Then (x-y)(V)=t/(1-t) E_01 is nonzero but its1-jet is zero; our
bound gives E=2. Characteristic-sensitive zeros/degrees must be normalized in
the specified field before computing the bounds.

This generalizes the released source's increasing-index denominator reuse and
faithful descent, using classical path arithmetic and local-ring algebra.
It was proposed **after** proof exposure: a source-derived synthesis, not a
successful frozen unseen transfer and not historically new mathematics.

## 4. Exact boundary beyond DAGs: finite evaluation algebra

**PM-SUCCINCT0004.** Suppose V_i belong to Mat_h(K(t)) and are regular at0.
Let A=K<V_1,...,V_n> be the *unital K-algebra*, not the K(t)-algebra. There
exists a single finite E such that reduction modulo t^E preserves the
zero/nonzero status of every polynomial evaluation f(V) iff dim_K A is finite.
The same E then works for coefficients in every constant-field extension.
Here scalar extension means K(t) maps to K'(t) with the formal parameter t
transcendental over K'; it does not make that parameter a coefficient constant.

Necessity: reduction is K-linear into Mat_h(K[t]/(t^E)), of dimension h^2 E.
If it is injective on every evaluation, it is injective on A, so A has finite
dimension. Sufficiency: on a finite-dimensional A the kernels of the E-jet
maps form a descending sequence. Their intersection is zero because a
nonzero regular rational function has a finite order at0. The descending
sequence eventually stabilizes; its stable value is the intersection, hence
zero. This argument does NOT make one observed plateau a stopping rule:
the kernels can stay equal for many consecutive E before decreasing again.

### Constructive certificate and resource budget

Supply finitely many rational matrices B_j, coefficients a_j in K and constant
coefficients C_jik in K such that

\[
 I=\sum_j a_jB_j,\qquad B_jV_i=\sum_k C_{jik}B_k.
\]

Their span contains A by induction on words. Supply also a polynomial D_0
with D_0(0)!=0 such that D_0 B_j is polynomial, every entry of degree <E.
Every f(V) is then in that span, and D_0f(V) has degree <E. The same unit/
regular-representation argument proves faithful E-jets. Independent rows or
actual-word provenance are unnecessary for this sound upper certificate,
but required to certify an exact generated-algebra dimension.

This is a compact checkable replacement for an enumerated table of every
polynomial evaluation. It detects why the DAG condition is sufficient rather
than necessary: other finite evaluation algebras also admit the compilation.
It is classical finite-dimensional algebra and invariant-span reasoning, not
a priority claim for a new algebraic theorem.

Under a supplied promise dim_K A<=D, there is a bounded construction. Let a
common polynomial delta, with delta(0)!=0, clear all V_i, write P_i=delta V_i,
and put b=max(deg delta, max degree of entries of P_i). Generate actual word
matrices from I, accepting a word only when it is K-linearly independent of
the current list. Test dependence by clearing denominators and comparing
polynomial coefficients over K. If closure occurs after d<=D accepted words,
their maximum length is <=d-1, by retained parent pointers (or the ordinary
word-span plateau argument). Multiplication by delta^(d-1) clears all these
basis matrices, with every entry of degree <=(d-1)b. Therefore

\[
 E=1+(d-1)b
\]

is a certified sufficient jet length. If D+1 independent word matrices appear,
report only that the supplied dimension budget is exceeded; do not report
infinity or continue without a stopping bound. Polynomial coefficient arrays
have O(h^2 Db) coordinates, up to zero/constant boundary adjustments; the
number of basis offers is O(nD). Exact linear algebra, word multiplication
and dense hE output thus cost polynomially many field operations in explicit
n,h,D,b. Expanded-degree/output and rational-bit caveats still apply. No
unpromised polynomial-time finiteness decision is inferred from this search.

For scalar extension, clear the finite basis's denominators and form its
polynomial coefficient matrix over K. A nonzero d-by-d minor stays nonzero
over every extension K'/K, so the basis remains independent and spans the
generated K'-algebra. The certificate equations and degree bounds also persist.
This proves the extension assertion without assuming that a K-linear kernel
statement automatically covers arbitrary extension coefficients.

### Exact failures distinguishing the interfaces

- V=[t] has infinite K-algebra and no faithful fixed jet; over K(t) its
  ambient scalar vector space has dimension1. Using K(t)-linear dependence
  would therefore certify the wrong object.
- The cyclic nonconstant tuple V=[[1,t],[0,0]] is idempotent, so its K-algebra
  has dimension2 and fixed jets exist. Cycles alone do not imply failure.
- V=t^M E_12 has algebra span{I,V}, of dimension2 for M>=1, but its smallest
  faithful jet length is M+1. Thus algebra dimension alone gives no bound
  independent of coefficient degree; a single jet-rank plateau proves nothing.
- Individual generator algebraicity is not enough: V_1=t E_12 and V_2=E_21
  both square to0, but (V_1V_2)^k=t^k E_11 gives infinitely many K-independent
  evaluations. Full joint right-generator closure is essential.

These examples give concrete reasons to preserve the scalar ring, degree
budget and composition interface. The theorem extends a source-derived DAG
operation to an exact finite-algebra criterion; it does not discover a faithful
auxiliary map from an arbitrary problem statement or establish a new theory.

## 5. Evidence and next mathematical operation

`tools/reachable_series.py` contains exact synthesis and a separately coded
certificate checker. Its deterministic report includes384 seeded models,
all4096 two-state/two-letter F2 inputs, genuine +1/-1 path cancellation,
field-rank change and11 malformed certificates. A97-state F2 representation
of (x+y)^96 has2^96 nonzero word coefficients, but only195 candidate rows are
offered; the large word table is **not** expanded. This is the established
reachable-space advantage over full expansion, not a new baseline improvement.

`tools/acyclic_jet.py` implements the path bounds and regular representation;
its tests compare with independently written rational-polynomial arithmetic,
including noncoprime factors, signed edge costs, characteristic controls and
insufficient jets. Three actual scoped GPT-6.1-Sol/Ultra tasks provided two
independent mathematical views and separate source/adversarial review; root
accepted the proofs and corrected an identified rational-to-Fp parser bug.
This is AI review and exact computation, not human or formal verification.

The current evidence favors a more specific operational program: choose a
representation that is faithful and cheaply truncatable, prove a resource
budget for the first survivor, and preserve that budget under composition.
The main remaining difficulty is finding the faithful auxiliary map from
the problem's actual input. Neither feature selection nor reachable closure
nor the DAG compiler performs that discovery in general.

Next concrete operation: compare the explicit all-characteristic shift-order
bound against the full q-difference multiplicity literature (not titles or
slides alone), then formulate a bounded operator-family synthesis task with
specified input, legal maps and equal-information classical baseline. Freeze
a second genuinely unread target only after this gate. Do not call family116
unread again, relabel its source-derived compiler as pre-proof prediction,
or revert to small-field scans. PM-H1–H5 remain open.

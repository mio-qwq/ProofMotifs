# Costed representation repair: exact certificates and a discovery baseline

Date: 19 October 2026 (Asia/Singapore). This continues the missing-cancellation-tool program.
The operation now chooses optional features from a finite dictionary; it does
not receive a prescribed residual square or its coefficients. General theory
is classical facial separation, sparse feature selection and Benders-style
feasibility cuts. This is an exact reference construction, not a new universal
method, a historical-priority claim, or an explanation of AI capability.

## PM-REPAIR-0001: feasibility, obstruction and composition

Let Omega be a finite nonempty index set, D a nonempty subset, and O=Omega-D.
Feature matrices have rational entries and columns indexed by Omega. A0 is
always available; optional row blocks B1,...,Bp have nonnegative rational
costs. For J subset [p], let A_J vertically stack A0 and its selected blocks.
A legal selector has the form W=c^t A_J and must satisfy

\[
 W_d=0\quad(d\in D),\qquad W_o\ge1\quad(o\in O).
\]

Exactly one of the following exists:

1. Such a rational c, which can be scaled to give integer evaluated weights.
2. A rational trade z with A_J z=0, z_o>=0, and sum_(o in O)z_o=1;
   its coefficients on D are unrestricted in sign.

**Proof.** Quotient the feature-column space by the span of target columns.
Equivalently project orthogonally off that span; rational input gives rational
projected columns b_o. If zero lies in conv{b_o}, its rational convex
coefficients lift to a trade after solving for target coefficients. If zero
does not lie there, strict separation gives a functional vanishing on the
target span and positive on every off-target column. Rational perturbation
and scaling give W_o>=1. A trade and selector cannot coexist: their pairing
would be zero by A_J z=0 but at least one by positivity and normalization.
If O is empty, the zero selector works and trade normalization is impossible.
QED. This is homogeneous/conical separation in explicit input form. It is
literally an ordinary convex-polytope facial-set criterion when the constant
row is in the available row span. Without that hypothesis the distinction
matters: A=(1,2), D={first column} has a polytope vertex there, but no linear
weight can vanish on its first column and be positive on its second.
Adding a constant row changes the allowed representation; it is not WLOG.

Clear denominators of the **evaluated weights**, not just c: rational features
may leave fractional weights even with integral c. The resulting integral
W vanishes on D and is positive elsewhere, so every independent product has
total weight zero exactly when every factor lies in D. This is the precise
composition contract from PM-CONSTRUCTION-0004. Product supports constrained
by additional coupling need separate treatment.

## PM-REPAIR-0002: complete minimum-cost repair with adaptive trade cuts

First test the full dictionary A_[p]. If it has a trade, that same trade
annihilates every smaller stack: no repair exists. If feasible, maintain
mandatory cuts indexed by previously found trades. For a current failing J
with trade z, define

\[
 K(z)=\{j:B_jz\ne0\}.
\]

Every feasible repair J* must intersect K(z). Indeed if no selected block
breaks z, then A_(J*)z=0 and the same trade rules out its selector. Add
sum_(j in K(z))x_j>=1 to a binary master problem with objective
sum cost_j x_j. Choose a cheapest mask satisfying all current cuts and test
it with the exact feasibility alternative; repeat until feasible.

**Correctness and optimality.** All cuts are necessary for every feasible
repair. Each failing incumbent misses its new cut, so it is never revisited.
The full mask remains possible once the initial feasibility test passes;
in particular each cut is nonempty. There are at most 2^p incumbent checks,
plus the full-stack check. On first success the master cost is a global lower
bound, attained by its certified selector, proving exact optimality. The
record of trades and cuts plus the final primal certificate is independently
checkable. A generic exact binary master and exact rational LP suffice;
neither novel optimization theory nor a polynomial-time optimum is claimed.

**Existence is easier than optimality.** Without a cost objective, one full-stack
feasibility test solves the dictionary-existence question. Repeated subset
search is justified by cost or other declared restrictions, not existence.

**Cost boundary / set-cover reduction.** Given a finite universe U and sets S_j,
let Omega={d} union U, D={d}, A0 be the constant row, and B_j the one-row
indicator of S_j, zero at d. A selected family has a selector exactly when
it covers U: summing its indicator rows works in one direction; an uncovered
u has the same selected column as d, which forbids W_u>=1 in the other.
Thus weighted set cover is a special case, even for one binary row per block
and a singleton target. Minimum repair is NP-hard. With rational input the
decision problem is in NP (a mask plus a polynomial-bit rational feasible
point, by standard rational linear-system bounds), hence NP-complete. We do
not import approximation constants or promise an efficient sparse solver.

## PM-REPAIR-0003: breaking the original extreme trades is insufficient

It is incorrect to enumerate only the original extreme obstruction rays and
then select blocks that individually break every ray. Their images under the
new blocks can cancel, leaving a surviving combination.

For Omega=(d,p,q), D={d}, A0=(1,1,1), the original pointed trade cone has rays
r1=(-1,1,0), r2=(-1,0,1). Adding B=(0,1,-1) breaks each ray individually,
but B(r1+r2)=0. The normalized trade (-1,1/2,1/2) still rules out any positive
selector. This is the same obstruction that makes a signed single-copy
defect fail under products, now inside the representation-selection step.

The failure persists for whole categorical one-hot blocks. Take

\[
 A0=\begin{pmatrix}1&0&1&0\\0&1&0&1\end{pmatrix},\quad
 B=\begin{pmatrix}1&0&0&1\\0&1&1&0\end{pmatrix},\quad D=\{d1,d2\}.
\]

The old rays (-1,0,1,0) and (0,-1,0,1) have opposite nonzero B-images;
their sum survives both matrices. In the augmented representation, the new
trade (-1/2,-1/2,1/2,1/2) is still an obstruction. Thus this is not an artifact
of allowing a signed scalar feature. Current-matrix circuits or the entire
current cone must be rechecked; static initial-ray hitting is unsound.

## PM-REPAIR-0004: a sharp higher-degree target, without a supplied square

For every r>=1 work on the **ordinary rational grid** Omega={-1,0,1}^r;
this is not a field of characteristic three. Let D be its coordinate-zero
union, the points where some coordinate vanishes. Any real polynomial W
vanishing on D and strictly positive on O={-1,1}^r has total degree at least
2r. The product of coordinate squares attains this bound.

**Exact obstruction and proof.** Put b(-1)=1,b(0)=-2,b(1)=1 and
z(s)=2^(-r) product_i b(s_i). On O all z(s)=2^(-r)>0 and their sum is one;
on D the signs are unrestricted. The univariate moments of degrees 0,1,2
are 0,0,2. Tensoring shows that every monomial of total degree below 2r is
annihilated: some coordinate exponent is 0 or 1. It follows that no such
polynomial can be a positive zero-target selector, by pairing with z.
The degree-2r polynomial product_i x_i^2 is zero on D and one on O. QED.

There is a stronger mandatory-feature statement. Reduce every polynomial
modulo x_i^3-x_i to exponents in {0,1,2}, without increasing degree. Evaluation
on the ternary grid is an isomorphism for this reduced space. Vanishing on
each zero-coordinate slice forces every surviving monomial to contain every
variable. On O its sign average therefore equals exactly the coefficient
of x_1^2...x_r^2, which must be positive. Thus that feature is compulsory in
the reduced-monomial dictionary; adding arbitrarily many other features in
that dictionary cannot replace it. The argument is classical tensor finite
differences / coefficient interpolation, not a newly discovered degree theory.

This family was designed and analyzed by the coordinator before its input
file was frozen. It is a new calibration application in this project, **not**
a previously unread external target, a blinded test, or evidence of AI-specific
discovery. The optimizer is supplied all monomials in the finite dictionary,
but not the required residual or its coefficients. Its output chooses the
necessary feature. The point and dictionary counts each grow as 3^r, and
the dense evaluation matrix has 9^r entries;
there is no general efficient high-order discovery claim.

## Reference algorithm and actual evidence

Input protocol: research/experiments/feature-repair-panel.json, SHA256
80e6bc9a1b7e342b304f27539e9a0128846c1c636af775061bb5775d6cfd8ab9.
It was saved before primary optimizer execution, with its designed-calibration
status explicit. It freezes feature blocks, costs, targets, baseline and
failure panels. It does not preregister an external held-out experiment.

tools/feature_repair.py implements exact rational arithmetic. For each fixed
stack it projects off the target-column span, enumerates affinely independent
convex-hull supports and solves the rational minimum-norm KKT equations. A
candidate p is accepted only after checking p.b_o>=p.p for every off column.
If p=0, recover a normalized trade; otherwise p/(p.p) supplies a selector.
This test is globally valid since it is the supporting condition for the
closest point. A finite hull has an affine-independent closest-point support,
so enumeration terminates. This is an exponential reference oracle, not a new
LP algorithm; production implementations should use existing exact LP methods.

The binary master in this reference also enumerates masks. Its cost is
accounted separately from oracle calls. Compare it to exhaustive mask search
using the **identical** oracle and input information:

| Designed panel | Exact result | Adaptive oracle calls, including full precheck | Exhaustive calls |
| --- | --- | --- | --- |
| Signed obstruction plus repair row | Both features required, cost3 | 4 | 4 |
| Categorical old-ray shortcut | Full dictionary impossible | 1 | 2 |
| Weighted cover | Blocks b,c,d; cost5 | 7 | 12 |
| Two-dimensional zero-coordinate union | Chooses x^2 y^2 alone; cost5 | 15 | 33 |
| Same grid dictionary without that feature | Impossible | 1 | 32 |

These are exact counts on these frozen panels, not asymptotic or wall-clock
speed claims. The adaptive method can have worse overhead on other inputs.
Costs are declared feature-block costs, not the full cost of mathematical
discovery, model inference, table generation or auxiliary-object invention.

Every stored trade and selector has a direct exact validator. Independent
review uses a different rational Fourier–Motzkin/Farkas oracle rather than
importing the Gram-projection implementation. Exact JSON reports, actual
commands and review decisions are recorded in the checkpoint.

An independent researcher also froze a different univariate sparse-monomial
calibration before its optimizer ran. Its optimum costs4, increases to9 under
its feature-deletion control, and is impossible in an odd-only dictionary.
Adaptive and exhaustive oracle counts are equal there (20 and142 respectively),
so there is **no measured search advantage** on that additional panel. The
separate input, discovery implementation and optimizer-free certificate
checker are saved, including180 exact cuts. This is designed calibration too.

## PM-REPAIR-0005: an explicit complete bounded-MILP baseline

Rowwise clear denominators of the entire dictionary matrix, preserving each
row's block membership, so its R rows have integer entries bounded by H>=1.
This rescaling preserves every attainable function and every block cost.
For R>=1 let M=R! H^(R-1). Every feasible mask has a selector with **integer
coefficients relative to these integralized rows**, all of absolute value at
most M. It is not the same coefficient bound for the original rational rows:
if row i was multiplied by L_i, its original coefficient is L_i times the
bounded new coefficient.

**Proof.** Choose q independent available feature rows. If O is empty the
zero selector suffices. Otherwise the feasible coefficient polyhedron on
these q rows has no line: a direction and its negative in its recession cone
would annihilate every state column, contradicting row independence. A
nonempty pointed polyhedron has a vertex. Choose q independent active
constraints at that vertex; their coefficient matrix C is integer with
entries bounded by H and right side in {0,1}. By Cramer's rule, multiplying
the vertex by |det C| gives integral coefficients, remains zero on targets
and has every off-target weight at least |det C|>=1. Each numerator is
bounded by q!H^(q-1), by expanding along the right-side column. Set unused
coefficients to zero. As q<=R, this is at most M. QED.

Consequently a conventional mixed-integer linear program is complete: one
binary x_j per block, one integer coefficient per integralized row, target
equalities and off-target inequalities as before, and coefficient bounds
-M x_j<=c_i<=M x_j for each optional row in block j; base coefficients have
bound M. Minimize the same declared block cost. Its feasible masks are
exactly the original feasible masks. R=0 is trivial: a nonempty O is
impossible; otherwise the zero selector works.

The bit length of M is O(R log R+R log H), polynomial in the explicit rational
input after rowwise least-common-multiple clearing. This supplies a concrete
input-matched existing-tool baseline, not an arbitrary coefficient cutoff,
a new MILP theorem, or a polynomial-time optimizer. Sparse normalized trades
also have polynomial-bit certificates: project off the target span, choose
at most rank(A)-rank(A_D)+1 affine-independent off-target columns whose convex
hull contains zero, then at most rank(A_D) target columns to lift the
relation. The unique rational solves on these supports are bounded by
ordinary determinants; total support is at most rank(A)+1. Global minimum
cost still requires the binary-master lower-bound verification.

## Prior art and the narrower remaining question

1. Rauh–Kahle–Ay, [arXiv:0906.5462v2](https://arxiv.org/pdf/0906.5462),
   Definition6/Lemma7: facial sets and signed dependencies give fixed-stack
   feasibility when the constant row is available. All frozen panels satisfy
   this hypothesis. The general theorem above uses homogeneous separation;
   its normalized target-free-sign trade must not silently add a constant.
2. Hooker–Ottosson, *Logic-based Benders decomposition*, Mathematical
   Programming96 (2003),33–60, [DOI](https://doi.org/10.1007/s10107-003-0375-9):
   inference-based valid cuts and finite master search already supply the
   correctness pattern of adaptive repair. The independent audit read the
   [author-hosted manuscript](https://johnhooker.tepper.cmu.edu/benders2.pdf),
   section5 Theorems1–2; this is not a new Benders principle.
3. Bradley–Mangasarian–Street, *Feature Selection via Mathematical Programming*,
   INFORMS Journal on Computing10(2) (1998),209–217,
   [DOI](https://doi.org/10.1287/ijoc.10.2.209): their original abstract explicitly
   optimizes features of separating planes. Its discrimination problem differs
   from our exact target face, but sparse representation selection is not new.
4. Christandl–Fawzi–Ta–Zuiddam, *Larger Corner-Free Sets from Combinatorial
   Degenerations*, ITCS2022, [original paper](https://doi.org/10.4230/LIPIcs.ITCS.2022.48),
   Definition21 and section2.3 equation(1): integer local weights with zero
   target and positive complement are an existing combinatorial-degeneration
   contract, and the paper explicitly constructs them by integer programming.
   Its objective selects retained diagonal vertices under fixed readouts;
   ours fixes D and pays for optional blocks. This direct overlap is stronger
   prior-art evidence than a general claim that Gaussian elimination exists.

Existing methods therefore already discover some composition-compatible
cancellation weights and optimize some representation choices. The present
work does not prove a missing operation beyond those methods. A useful future
instrument would need additional structural compression, a better justified
dictionary/auxiliary-object discovery step, or a proved cost/transfer gain on
a frozen unread target. Merely renaming sparse separation would not provide it.
PM-H1..H5 remain open; these findings update PM-H4/H5 with exact boundaries
and a reproducible established-method baseline.

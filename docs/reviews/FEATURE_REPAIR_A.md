# PM-REPAIR-A: exact finite feature repair and its limitations

Date: 18 October 2026 research window. Task-scoped independent researcher.
Repository read-only; only `/tmp/pm_repair_a*` written. Read `AGENTS.md`,
`research/RESEARCH_PROGRAM.md`, and
`research/mechanisms/CONSTRUCTION_CONTRACTS.md` completely. The initial proposal
was sent before receiving other proposals. Section 9 is a separately labeled
audit of a later coordinator-supplied target. No historical novelty, held-out
transfer, human review, or formal verification claim is made.

### Task ledger (all nine required fields)

| Field | Record |
| --- | --- |
| TASK ID | PM-REPAIR-A |
| RESEARCH QUESTION | Exact representation/feature repair for finite positive zero-target selectors, with additive independent-product stability, beyond a supplied coefficient system. |
| KNOWN ASSUMPTIONS | Finite rational feature matrices, fixed nonempty target set, optional legal row blocks with declared nonnegative rational costs; no new-tool premise. Existing all-product scalar-collapse/facial/Gordan baselines supplied. |
| AVAILABLE EVIDENCE | The three required repository instruction/contract files, original primary-source web texts listed in Section 8, exact standard-library Fraction experiments. |
| EXPECTED OUTPUT | One precise useful theorem/algorithm/obstruction, complete proofs, sharp failures, explicit cost, existing-tool comparison, exact replay code. |
| ALLOWED SCOPE | Repository read-only; only `/tmp/pm_repair_a*` edited via apply_patch; primary-source browsing allowed; no Git, external correspondence, payments, or subagents. |
| INDEPENDENCE REQUIREMENT | Initial proposal sent before any other proposal was received; later coordinator target and implementation reviews distinguished in Sections 9 and 11. |
| STOP CONDITIONS | Stop once a precise proposal and its scope, prior art, tests, and boundaries are saved; no historical novelty claim. |
| HANDOFF | `/tmp/pm_repair_a.md`, `/tmp/pm_repair_a.py`, and `/tmp/pm_repair_a_cross.py`; coordinator owns integration and acceptance. |

Configuration provenance: controller assignment explicitly specifies
`gpt-6.1-sol` with `ultra` reasoning. This is assignment metadata, not an
inference from the quality of the work. No separate tool-reported runtime
model identifier was exposed to this researcher; the coordinator can audit
its actual spawn parameters.

## 1. Executive conclusion and proposed instrument

For an explicitly supplied finite feature dictionary, representation repair is
an exact **weighted block-support optimization problem over a polyhedron**.
Existing exact LP plus mixed-integer/feature-selection methods already supply
the operation. A useful checkable synthesis is:

1. Given a selected block set, produce either an integral nonnegative scalar
   selector with exactly the desired zero set, or a sparse rational trade.
2. Use each trade to identify a mandatory choice among still-available blocks.
3. Solve the resulting minimum-cost hitting-set master, generate a new trade
   when its candidate fails, and stop with an optimal repair and selector.

The formulation genuinely chooses blocks rather than merely solving a supplied
coefficient system. It gives no general polynomial-time improvement: deciding
whether *some* repair exists is one LP, but minimum-cost repair is NP-complete
even for binary scalar features. A finite polynomial-encoding MILP is an
input-parity existing-tool baseline.

The essential warning is that **hitting only the initial circuits/extreme
trades is not sound**. New equalities can preserve a positive combination of
old extreme trades even when they destroy each generator individually. A
three-point exact counterexample appears in Section 6.

Suggested internal classification: mathematical synthesis/operational
specification using established separation and support optimization, with
source-specific counterexamples and a designed calibration theorem. Not a new
universal cancellation instrument.

## 2. Exact contract

Let `Omega` be a finite explicitly enumerated set of `N` states, and let
`D` be a nonempty subset. Put `O = Omega \ D`. The input comprises rational
matrices

\[
A_0\in\mathbb Q^{r_0\times N},\qquad
A_j\in\mathbb Q^{r_j\times N}\quad(1\leq j\leq m),
\]

and nonnegative rational block costs `k_j`. Columns are state evaluations;
rows are legal scalar features. `A_0` is always available. For a selected set
`S`, let `A^S` be the vertical stack of `A_0` and the `A_j`, `j in S`.

A successful repair admits a coefficient vector `c` such that

\[
(A_D^S)^t c=0,\qquad (A_O^S)^t c\geq\mathbf1. \tag{P_S}
\]

Finite strict positivity can always be rescaled to this normalization. The
objective is to minimize `sum_{j in S} k_j`. The resulting scalar defect is
`W(s)=c^t A^S(s)`. Affine facial language is equivalent to this contract when
a constant feature is legally available. Without a legal intercept, use the
central zero-selector contract `(P_S)` as written; silently adding a constant
would change the resource model.

The pool is fixed and legal by hypothesis. This does **not** design a phase,
invent an arbitrary feature, or discover the admissible dictionary. If any
function were legal at unit cost, `1_O` would make repair trivial. Costs of
generating/evaluating features, degree, coefficient height, periods, dimension,
and product placement must be recorded separately when they matter.

## 3. PM-REPAIR-A.1: exact oracle, sparse obstruction, and product stability

For each `S`, precisely one of these two certificates exists:

* Selector `(P_S)` with rational `c`, hence after legal rescaling an integral
  scalar-valued `W`.
* Normalized rational trade

\[
A^S t=0,\qquad t_s\geq0\ (s\in O),\qquad
\sum_{s\in O}t_s=1. \tag{T_S}
\]

The target coefficients `t_d`, `d in D`, are **unrestricted in sign**.
Let `r=rank A^S`, `d=rank A_D^S`, and `q=r-d`. A trade can be chosen with
at most `q+1` off-target support points and at most `d` target support points,
hence at most `r+1` total support points. These bounds also hold when the
matrix has dependent rows/columns.

### Proof of the alternative

Work in the rational quotient of the feature space by
`span{A^S(d): d in D}`. Write `v_s` for the image of the off-target column
`A^S(s)`. A legal selector is a linear functional on the quotient strictly
positive on every `v_s`. If `0` is outside the finite convex hull of the
`v_s`, a strict separating functional exists. Rationality permits a rational
one; scale its finite positive minimum to at least one and pull it back.
If `0` belongs to that convex hull, rational linear feasibility supplies
nonnegative rational `lambda_s` summing to one with
`sum lambda_s v_s=0`. Thus `sum lambda_s A^S(s)` lies in the target column
span; negate a rational target-span representation to obtain `(T_S)`.
These cases exclude one another because pairing `(P_S)` with `(T_S)` gives

\[
0=c^t A^S t=\sum_{s\in O}t_s W(s)\geq1.
\]

For sparsity, the quotient span has dimension `q`. A minimal positive
convex representation of zero uses at most `q+1` columns: if a representation
uses more, the lifted columns `(v_s,1)` are dependent; perturb its positive
coefficients in that dependence until one becomes zero. Repeat. Represent
the resulting target-span vector in a basis of at most `d` target columns.
All calculations can be rational, proving the stated bound. Equivalently,
write each target variable as a difference of two nonnegative variables and
take a basic feasible solution of the normalized rational system.

If `O` is empty, take `W=0`, and the trade normalization is impossible.

### Composition guarantee

After clearing rational denominators, `W:Omega -> Z_{>=0}` is zero exactly
on `D`. For every `n>=1` and every independent tuple in `Omega^n`,

\[
\sum_{i=1}^n W(s_i)=0\quad\Longleftrightarrow\quad s_i\in D\quad\forall i.
\]

This is direct positivity, not a new collapse theorem. `W` remains a linear
combination of the selected legal readouts; local additive decomposition is
preserved. This guarantee concerns additive products on full independent
support. Coupled product support, coefficient targets other than zero,
characteristic-dependent cancellation, and evaluation-cost optimality are
different contracts.

### Cost

A rational LP feasibility oracle has polynomial bit complexity in the
explicit matrix encoding; both certificates have polynomial bit length.
Checking either one costs `O(R_S N)` rational operations, or less with sparse
columns/trades. Discovering a sparse trade need not enumerate all circuits.
The prototype in `/tmp/pm_repair_a.py` deliberately does not implement a
polynomial LP algorithm: it uses Fraction-only elimination and enumerates
basic supports. Its trade search considers at most

\[
\sum_{i=1}^{\min(q+1,|O|)}\binom{|O|}{i}
\]

supports, and its selector search at most `binom(|O|,q)` active sets, with
polynomial-size rational elimination per set. This is an exact replay/testing
baseline, not an efficiency claim.

## 4. PM-REPAIR-A.2: exact repair cuts and optimality

Let `T_0` be all rational trades satisfying `(T_emptyset)`. For each such
trade define the block set

\[
B(t)=\{j:A_jt\ne0\}.
\]

A block selection is a successful repair if and only if it hits `B(t)` for
every `t in T_0`. Consequently each observed trade supplies a valid exact
constraint

\[
\sum_{j\in B(t)} z_j\geq1,\qquad z_j\in\{0,1\}. \tag{C_t}
\]

### Proof

If a successful selection `S` misses `B(t)`, then the same `t` annihilates
all selected blocks and the base, contradicting Section 3. Conversely, if
`S` fails, its rational oracle trade belongs to `T_0` and has
`A_jt=0` for every `j in S`; hence `S` misses its set `B(t)`.

### Exact algorithm

Start with no trade constraints. Minimize `sum k_j z_j` over the binary
master. Query the exact oracle at its selected set. On success return that
set and selector. On failure append `(C_t)` and repeat. If `B(t)` is empty,
the full dictionary cannot repair the representation. If the master becomes
infeasible, no successful repair exists.

All actual repairs satisfy every generated cut, so each master optimum is
a lower bound on the true optimum. When its candidate succeeds, it attains
that lower bound and is globally optimal. A failed candidate violates its
new cut and is never revisited. There are only `2^m` selections, hence at
most `2^m` oracle evaluations. Although `T_0` may be infinite, its incidence
patterns `B(t)` range over at most `2^m` subsets.

Evaluating a cut costs `O(R_all |supp(t)|)` rational operations. This does
not bound the integer-master effort polynomially. Direct enumeration costs
at most `2^m` fixed-system LP solves and is the simplest safe worst-case
baseline. An adaptive implementation can prune many sets, but no general
runtime advantage has been proved here. An optimality audit must include
the exact master solution/proof or exhaustive coverage of cheaper choices;
a selector alone certifies feasibility, not minimum cost.

An unconstrained existence check is easier still: query the full stack once.
Monotonicity proves that this single LP decides whether any selection works.

## 5. PM-REPAIR-A.3: explicit existing-tool MILP with a safe finite bound

Clear denominators **within each feature row** using positive integer
multipliers. This preserves legality, block support, and the set of possible
defects. Let the resulting integer full stack have `R>=1` rows and entries
bounded in absolute value by `H>=1`. Define

\[
M=R!H^{R-1}.
\]

Every feasible selected architecture has an integral selector coefficient
vector in the scaled row coordinates with every coordinate bounded by `M`
and all off-target values at least one. Thus the following finite MILP has
exactly the desired optimum:

\[
\begin{aligned}
\min\quad &\sum_j k_jz_j\\
\text{subject to}\quad&A_D^t c=0,\quad A_O^t c\geq\mathbf1,\\
&-M\leq c_{0,\ell}\leq M,\\
&-Mz_j\leq c_{j,\ell}\leq Mz_j\quad(j\geq1),\\
&z_j\in\{0,1\}.
\end{aligned}
\]

Continuous `c` suffices; making it integral is also exact. The bit length
of `M` is `O(R log R + R log H)`. Rowwise denominator clearing gives an
`H` of polynomial encoding length in the original rational input. This
large bound is a correctness device, not a numerical recommendation.

### Proof of the bound

For a feasible selected stack, choose a basis of its feature rows, a subset
of original rows, of size `r<=R`. Every legal defect has a representation
on this row basis. The feasible coefficient polyhedron is

`P={c: c.A_D=0, c.A_O>=1}`.

It has no lineality, since the row basis is independent on all columns.
For completeness, start at any feasible point. If the currently tight
constraints, including target equalities, have rank less than `r`, choose
a nonzero direction orthogonal to them. Some other column has nonzero
pairing with this direction, because all columns span the row-coordinate
space. Orient the direction to decrease one slack inequality and move until
the first new inequality becomes tight. It is independent of the old tight
ones. Repeat until there are `r` independent active constraints. Their
integer `r by r` matrix has nonzero determinant, and RHS entries are zero
or one. Cramer's rule gives coefficients `det_i/det`. Each numerator has
absolute value at most `r! H^{r-1}`. Multiplying the coefficient vector by
`|det|` gives an integral feasible vector with coordinates
`sign(det) det_i`, still bounded by `r!H^{r-1}<=M`. Embed zeros on discarded
feature rows. For `O` empty the zero vector suffices; `r=0` cannot be
feasible when `O` is nonempty.

This proof also provides a polynomial-size NP witness. No unjustified
user-chosen big-M is necessary. Small arbitrary coefficient bounds would
change the problem: even the two-dimensional columns `(1,-1)` and
`(-(H-2),H-1)` force a normalized vertex selector `(H,H-1)`.

## 6. PM-REPAIR-A.4: complexity and sharp failure controls

### Weighted set cover is an exact special case

Given a universe `U` and subsets `F_j` with costs `k_j`, let
`Omega={d} union U`, `D={d}`, and let the free feature be the constant one.
Block `j` has one binary feature `f_j(d)=0`,
`f_j(u)=1_{u in F_j}`. If selected sets cover `U`, their sum is a legal
nonnegative selector. If a point `u` is uncovered, its selected feature
column equals the target column, so every defect zero at `d` is also zero
at `u`. Therefore the optimum repair cost equals the optimum cover cost.

Decision repair is in NP by the bounded integral certificate of Section 5;
set cover proves NP-hardness even for these binary scalar rows. Thus it is
NP-complete. This is an explicit reduction, not a claim that these complexity
facts are historically new. The nonnegative binary subclass can use ordinary
weighted set-cover methods. Signed general dictionaries have complementarities
absent from this direct coverage interpretation.

### Initial extreme trades are insufficient

Take `Omega={d,p,q}`, `D={d}`, base row `(1,1,1)`, and one optional row

\[
f=(0,1,-1).
\]

The initial normalized trade polytope has extreme points
`t_p=(-1,1,0)` and `t_q=(-1,0,1)`. The optional row breaks each:
`f.t_p=1`, `f.t_q=-1`. Thus a static hitting set of just these initial
extremes declares the block sufficient. But the trade

\[
\tfrac12t_p+\tfrac12t_q=(-1,1/2,1/2)
\]

annihilates both base and optional row. No scalar multiple of `f` is
strictly positive at both off-target points. This is already the smallest
nontrivial convex-cancellation configuration: one target, two off-target
points, one signed scalar block.

Add a second row `g=(0,-1,2)`. Neither row alone works, but
`3f+2g=(0,1,1)` does. With unit block costs the optimum is two. The
prototype's adaptive cuts are `{f,g}`, then `{g}`, then `{f}`, and it returns
coefficients `(base,f,g)=(0,3,2)`. This is a concrete reason not to infer
submodular coverage or greedy approximation guarantees for arbitrary signed
dictionaries.

### Target signs cannot be restricted

Let target feature locations on an affine line be `0,1`, and the off-target
location be `2`, with base matrix

\[
A=\begin{pmatrix}1&1&1\\0&1&2\end{pmatrix}.
\]

A legal affine defect zero at both target points is identically zero, so
selection is impossible. The normalized trade is `(1,-2,1)`, containing
a **positive** target coefficient. The convex hull of the off-target point
does not meet the convex hull of the target points. Therefore merely looking
for an equality of nonnegative off-target and nonnegative target mixtures
misses this obstruction. The correct quotient is by the **linear span of
target columns**, and target trade coefficients are free-signed.

## 7. Exact replay evidence

Run `python3 /tmp/pm_repair_a.py`. It uses only the Python standard library,
`fractions.Fraction`, an independently written small rational matrix helper,
and combinatorial enumeration. No floating-point LP or unverified decimal
tolerance is used. Current exact assertions pass:

* Three-point initial-extreme failure, hidden trade, two-block synergy,
  globally optimal cost two, and selector values `(0,1,1)`.
* Signed-target obstruction `(1,-2,1)`.
* 40 deterministic random binary set-cover instances with exact optimum
  agreement between direct covers, full subset enumeration, and adaptive cuts.
* 30 deterministic random signed rational dictionaries, including multiple
  targets and vector blocks, with adaptive/full-enumeration optimum agreement.
* The large coefficient example, returning `(7,6)` when `H=7`.
* Later coordinator target moment checks for `r=1,...,5`, and a complete
  `r=2` block search selecting only exponent `(2,2)` at optimum unit cost one.

These checks corroborate proofs and implementation behavior on small inputs;
they are not a complexity benchmark, held-out transfer, or proof of all cases.

## 8. Prior-art pins and the new-tool gate

The closest baseline is not only an LP with a representation supplied by
hand. Sparse linear feature selection and mixed-integer support optimization
already address the extra block-choice step.

1. Rauh, Kahle, Ay, *Support Sets in Exponential Families and Oriented Matroid
   Theory*, arXiv:0906.5462v2, Definition 6 and Lemma 7, pp. 5-6, give the
   facial-set/kernel-sign characterization. Their Lemmas 11-12 discuss
   sign-consistent circuit decomposition. The feature/trade oracle above is
   a rational separation specialization, not a new alternative.
   Original text inspected: https://arxiv.org/pdf/0906.5462 and
   https://arxiv.org/html/0906.5462v2 .
2. Bradley, Mangasarian, Street, *Feature Selection via Mathematical
   Programming*, INFORMS J. Computing 10(2), 209-217 (1998),
   https://doi.org/10.1287/ijoc.10.2.209 . Original publisher abstract inspected:
   it explicitly optimizes the feature count in a separating hyperplane using
   linear constraints and gives an exact equilibrium-constraint formulation.
   This is close operational prior art; no assertion here identifies their
   entire model with grouped target-equality repair.
3. Amaldi and Kann, *On the approximability of minimizing nonzero variables
   or unsatisfied relations in linear systems*, Theoret. Comput. Sci. 209,
   237-260 (1998), https://doi.org/10.1016/S0304-3975(97)00115-1 . Primary
   predecessor ECCC TR96-015 explicitly studies minimum-nonzero-variable
   solutions of linear relations and feature-minimum linear classifiers:
   https://eccc.weizmann.ac.il/report/1996/015/ and its original PDF
   https://eccc.weizmann.ac.il/report/1996/015/download . The report page and
   author bibliography were inspected; PDF extraction has damaged encoding.
   Do not import uninspected quantitative inapproximability constants.
4. Benders, *Partitioning procedures for solving mixed-variables programming
   problems*, Numer. Math. 4, 238-252 (1962),
   https://doi.org/10.1007/BF01386316 . Publisher metadata inspected, full
   article subscription-limited. The adaptive procedure here is transparently
   a feasibility-cut/implicit-hitting-set scheme, not a claimed new
   decomposition method.
5. Karp, *Reducibility Among Combinatorial Problems* (1972),
   https://www.cs.umd.edu/~gasarch/BLOGPAPERS/Karp.pdf , original reprint
   retrieved, is the set-cover complexity baseline. The task-specific
   cost-preserving reduction is fully proved above, so it does not depend on
   treating a secondary summary as evidence for this exact repair model.

Recommended PM-H4/H5 resolution for the present input model: the needed
operation has an exact established-method implementation; a missing new-tool
claim does not survive this gate. A proposed specialized repair method must
beat the full feature-selection/MILP baseline at the **same dictionary,
costs, matrix access, and certificate requirements**, not just beat a solver
given fewer inputs. The still-open operational issue is constructing a useful
legal dictionary economically, or exploiting an explicitly proved structure
to improve runtime/cost/generalization. No such improvement is proved here.

## 9. Separately labeled review of the later coordinator calibration

This target was supplied by the coordinator after the independent initial
proposal above; it is not independently originated or externally held out.

### PM-REPAIR-A.5: mandatory top feature on a ternary grid

For integer `r>=1`, let

\[
\Omega=\{-1,0,1\}^r,\qquad
D=\{x:\prod_i x_i=0\},\qquad O=\{-1,1\}^r.
\]

Any real polynomial zero on `D` and strictly positive on `O` has ordinary
total degree at least `2r`. The product `prod_i x_i^2` attains degree `2r`
and is an integral selector. More strongly, reduce its evaluation function
modulo `x_i^3-x_i`, obtaining the unique polynomial

\[
\overline W=\sum_{e\in\{0,1,2\}^r}c_e x^e.
\]

Then `c_e=0` if any `e_i=0`, and

\[
c_{(2,\ldots,2)}=2^{-r}\sum_{\epsilon\in\{-1,1\}^r}W(\epsilon)>0. \tag{*}
\]

Consequently the exact top feature `x_1^2...x_r^2` is mandatory in the
reduced-monomial dictionary, not merely some feature of degree `2r`. If each
optional block is one reduced monomial and the constant/unary features are
free, repair is possible precisely when the top feature is available, and
selecting that block alone suffices. For nonnegative costs its block cost is
the optimum (zero-cost superfluous blocks may be included).

### Proof by reduction and sign averaging

Reducing a monomial with `x_i^k=x_i^{k-2}` for `k>=3` on the grid never
increases total degree. The reduced monomials form a basis of all functions
on the grid: this follows by tensoring the three-point invertible Vandermonde
matrix, or repeated univariate interpolation. Setting `x_i=0` leaves exactly
the reduced monomials with `e_i=0`; vanishing on that coordinate hyperplane
and basis independence force all those coefficients zero. Thus every
remaining exponent lies in `{1,2}^r`. Its sign-cube average vanishes whenever
one exponent is one. The only survivor is the all-two exponent, proving
`(*)`. A polynomial below degree `2r` could not have that coefficient after
degree-nonincreasing reduction, a contradiction.

### Independent dual proof by a tensor trade

Put `b(-1)=1`, `b(0)=-2`, `b(1)=1`, and

\[
t(x)=2^{-r}\prod_{i=1}^r b(x_i).
\]

Every off-target entry is `2^{-r}` and sums to one. The one-coordinate
moments satisfy `sum b=0` and `sum a b(a)=0`. Therefore any ordinary monomial
of total degree below `2r` has a coordinate of exponent zero or one and is
annihilated by `t`. In fact `t` annihilates every reduced monomial except
the all-two one, where the pairing is one. This is an exact certificate
against every lower-degree polynomial, not a numerical search.

The target coefficients of `t` alternate in sign. For `r=2`, the central
target point has a positive coefficient, making the free-sign warning in
Section 6 operational. Positivity on *all* off-target points is essential:
`prod_i x_i` has degree `r`, the right zero set, and both signs. The grid's
intermediate zero nodes are essential: if the domain were only `{±1}^r`,
then `D` would be empty and the constant selector would suffice.

### Existing-method baseline and explicit cost

This is a tensor finite-difference/interpolation obstruction, not evidence
that a new polynomial-certificate tool is needed. Alon's original
*Combinatorial Nullstellensatz*, Theorem 1.1, Lemma 2.1, and their proof
explicitly use degree-nonincreasing Cartesian-grid reduction and grid
interpolation; original text inspected:
https://www.tau.ac.il/~nogaa/PDFS/null2.pdf . The displayed coefficient
identity also follows directly by tensor Lagrange interpolation; no external
theorem is required to verify the proof here.

An explicit full grid/dictionary has `N=3^r` states and `3^r` monomials,
so the dense evaluation input has `9^r` entries. Computing the factored
trade or top selector takes `O(r3^r)` arithmetic to list evaluations and
`O(r)` to describe symbolically. A dense verifier checks `O(9^r)` pairings;
the tensor moment proof verifies symbolically with `O(r)` identities. This
is a meaningful **structured certificate compression**, but standard tensor
finite differences/interpolation supply exactly the same compression. A
claim of representation-search improvement cannot charge the proposed tool
only the symbolic factored input while charging its baseline the dense
dictionary. The complete `r=2` search and `r<=5` exact moments are designed
calibration, not held-out transfer.

## 10. Handoff and stop boundary

Deliverables: `/tmp/pm_repair_a.md`, `/tmp/pm_repair_a.py`, and
`/tmp/pm_repair_a_cross.py`.
The initial proposal, source proximity, exact proof, sharp counterexamples,
prototype checks, and later target audit are complete for coordinator review.
No repo edits, Git operations, external messages, spending, subagents,
unread-target claim, or formal-verification claim were made. Stop here unless
the coordinator requests a specific adversarial review.

## 11. Separately labeled final integrated-proof/code cross-review

After the independent proposal and Section 9 audit, the coordinator requested
a final audit of `research/mechanisms/FEATURE_REPAIR.md` and
`tools/feature_repair.py`. Both were read in full. No mathematical error was
found in PM-REPAIR-0001 through PM-REPAIR-0004 or in the primary oracle's
completeness argument.

The primary oracle computes a rational orthogonal projection off the target
column span, then enumerates affinely independent supports of the closest
point in the off-target convex hull. Its KKT matrix is nonsingular precisely
for affine independence; the nonnegative barycentric coefficients and global
`p.b_o >= p.p` check certify the true closest point. If its norm is nonzero,
`p/(p.p)` is a strict normalized selector; if zero, the rational barycentric
coefficients lift to the required target-free-sign trade. Every closest point
has such a support of at most ambient dimension plus one. Dependent features,
duplicate columns, and empty feature stacks do not invalidate this argument.
The code separately verifies all returned certificates exactly.

I reran `python3 tools/feature_repair.py` read-only from the repository. All
five panel outputs match the integrated table, including costs, selected
blocks, impossible panels, and oracle-call counts. No output was redirected
into the repository.

The independent cross-review script `/tmp/pm_repair_a_cross.py` loads the
primary implementation without running its main program or producing Python
bytecode, then compares it with my different quotient/basic-support/active-set
oracle. Exact result: **336 fixed-stack comparisons PASS on 80 separately
generated deterministic integer dictionaries**. Cases include empty feature
stacks, empty optional blocks, all-target domains, dependent rows, zero-cost
blocks, and multiple target columns. This is supplemental implementation
evidence, not formal verification or an exhaustive theorem.

Two small reporting cautions were sent to the coordinator:

1. Trades, cuts, and a final selector prove optimality only after the binary
   master lower bound is independently checked, for example by verifying that
   every cheaper mask violates a stored cut. The published algorithm's exact
   master enumeration does supply this obligation; a validator should retain
   it instead of checking just the final primal certificate.
2. A full `r`-variable grid and reduced dictionary each have cardinality `3^r`,
   but their dense evaluation matrix contains `9^r` entries. Symbolic tensor
   certificates must be compared against equally structured baselines.

The coordinator's categorical one-hot counterexample is also correct: its
two original target-matching trades have opposite nonzero new-block images,
and their normalized sum annihilates both full blocks. It strengthens the
signed-scalar initial-extreme warning independently of the small signed
example in Section 6. This audit is an AI mathematical/code review, not a
human specialist review.

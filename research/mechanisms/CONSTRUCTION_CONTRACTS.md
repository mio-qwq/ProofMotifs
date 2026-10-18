# Constructing cancellation while preserving the required operation

Date: 18 October 2026. These are source-specific mathematical results and
classical synthesis baselines for PM-H4/H5. They do not establish a new universal
tool, AI-specific enrichment, a causal explanation, historical priority, or the
headline claims of the source manuscripts. All three source families were
already inspected calibration examples; none is a held-out transfer.

## What has become operational

An annihilator identifies contributions that vanish. A useful construction must
also produce the required residual **using the allowed readouts**, and remain
valid under the operation for which the residual is needed. Those obligations
can be decided in the following restricted models. The exact tests supply
primal constructions or dual obstructions, rather than a renamed kernel.

| Obligation | Exact input that cannot be dropped | Construction or obstruction | Existing baseline |
| --- | --- | --- | --- |
| 197: prescribed punctured Gram | Actual hole evaluations, coordinate-degree bound, output dimension equal to hole count | Cardinal interpolation or a nonzero evaluation dependence | Newton/Lagrange interpolation, evaluation codes |
| 107: nonnegative zero-degree selector | Fixed integer phase, local readouts, target at degree zero | Quadratic local weights or a balanced feature trade | Facial sets, linear separation, coefficient matching |
| 157: triangle parity consequence | Field characteristic, sharing identities, symmetric contractions, plus-observable | Six-row certificate; absent outside this grammar in odd characteristic | Linear algebra; degree-one NulLA certificate |
| Repeated additive selection | Integral grading and all tensor powers, not a single coefficient test | Positive scalar collapse or an explicit bad multiset | Rational convex separation / theorem of alternatives |

The first three mechanisms cannot simply be identified by one cancellation
order. In 197 the degree cutoff annihilates full lines, while deletion produces
the residual. In 107 a character filter first imposes a phase and a polynomial
grading then selects its zero set. In 157 symmetry and characteristic two
cancel six contractions; the residual is a parity relation. Mean-zero and
involution controls in UNIFICATION_BOUNDARIES.md remain different-order cases.

## PM-CONSTRUCTION-0001: complete pair-interaction criterion for the fixed phase

Fix an integer M>=3, let

\[
 S=\{(g,h,u,v)\in[M]^4:u-v+2(g-h)=0\},\qquad
 D=\{(x,x,y,y):x,y\in[M]\}.
\]

Choose a graph G on the four variables. An allowed real weight is a sum of
arbitrary unary functions and arbitrary functions on the edges of G. Require
W>=0 on S and W=0 on S exactly on D. Such a weight exists **if and only if**
G contains either gh or uv, or two incident cross edges between {g,h} and
{u,v}. Every feasible graph has a quadratic integer weight. Of the 64 graphs,
57 are feasible and 7 impossible, for every M>=3.

**Sufficiency.** An internal edge gh or uv permits its squared difference.
For the four possible cross-edge stars, respectively centered at h,g,u,v, use

\[
\begin{array}{c|l|l}
\text{center}&W& W\text{ on }S\\\hline
h&g^2-h^2+hu-hv&(g-h)^2\\
g&h^2-g^2-gu+gv&(g-h)^2\\
u&v^2-u^2-4ug+4uh&(u-v)^2\\
v&u^2-v^2+4vg-4vh&(u-v)^2.
\end{array}
\]

The phase equation proves the last column by substitution. The squares vanish
exactly on D within S, and all displayed terms are legal.

**Necessity.** A graph without an internal edge or adjacent cross edges is a
matching in K_(2,2), hence contained in one of its two perfect matchings.
Both off-target points

\[
 p=(1,2,3,1),\quad p'=(2,1,1,3)
\]

belong to S. Against the target pair (1,1,3,3),(2,2,1,1), their multisets of
gu readouts and hv readouts agree, as do all unary readouts. Against the target
pair (1,1,1,1),(2,2,3,3), their multisets of gv readouts and hu readouts agree.
Consequently every weight in either matching architecture has
W(p)+W(p')=0. Nonnegativity forces both weights to zero, contradicting exact
selection. This rules out arbitrary functions, not just low-degree polynomials.
There are 1+4+2=7 such graphs. QED.

In the source architecture the only cross edges are hu,hv, and both are
necessary. Degree at most one yields only unary functions and is impossible;
degree two is sufficient. This is a sharp result **within this fixed contract**.
For M=1,2 the phase already implies D, so the obstruction is vacuous.

**Exact discovery baseline.** Given the phase E, the three legal scopes
{g},{h,u},{h,v} and the prescribed residual (g-h)^2, assign unknown coefficients
to all local degree-at-most-two monomials and an affine P. Matching coefficients
in W-P E=(g-h)^2 gives a 15-by-20 rational system. Exact elimination recovers
the source W with P=h. This is discovery conditional on the chosen phase,
scopes and residual; those inputs were not discovered by the solver.
The controlled perturbation E=u-v+3(g-h) gives, after clearing denominators,
W=3g^2-3h^2+2hu-2hv and P=2h, with W-P E=3(g-h)^2. This is a calibration
perturbation, not a preregistered unseen target or a complexity improvement.

**Essential escapes.** The signed Laurent weight g-h already isolates D at
coefficient zero on S. The ordinary nonnegative weight g-h+M-1 does the same
at coefficient M-1. Two separate Fourier phases g-h and u-v also select D.
Thus the theorem is not a representation-independent lower bound on filters.
These alternatives change the coefficient target, positivity of the defect,
or phase budget. Their behavior under repeated products differs below.

## PM-CONSTRUCTION-0002: hole geometry is necessary and sufficient locally

Let Q be a finite field of size q, n>=1, d>=0, 2d<=q-2, H subset Q^n with
|H|=m>0, and P_d the space of formal polynomials of total degree at most d.
There is a vector polynomial f:Q^n->Q^m with each coordinate in P_d such that

\[
 \sum_{z\notin H}f(z)f(z)^t=-I_m
\]

if and only if ev_H:P_d->Q^H is onto. Every full affine line disjoint from H
then has zero Gram sum for this f. This does not assert that a regular
high-girth family of such lines exists.

**Proof.** Each product f_i f_j has degree at most q-2. For 0<=k<q-1,
sum_(t in Q)t^k=0, including k=0 because q=0 in Q. Restrict to a line and
then partition the affine space into parallel lines; every full Gram sum is
zero. Thus the required punctured identity is equivalent to XX^t=I_m for the
square matrix X of hole columns f(h). Such X is invertible, so its rows span
Q^H and ev_H is onto. Conversely surjectivity supplies the m cardinal
polynomials, making X=I_m and giving both assertions. QED.

For a parametric same-budget obstruction, take n>=2, d>=1 and m=d+2.
Choose distinct a_0=0,a_1=1,...,a_(d+1) in Q; the bound supplies enough nodes.
Five points below are the d=3 instance of the following general construction:

\[
 H_+=\{(a_i,0):0\le i\le d\}\cup\{(0,1)\},\quad
 H_-=\{(a_i,0):0\le i\le d+1\},
\]

with other coordinates zero. If L_i is the degree-d univariate cardinal
polynomial on a_0,...,a_d, the coordinates
L_i(X)-L_i(0)Y and Y are cardinal on H_+, with degree at most d.
For H_- restriction to its line has rank exactly d+1<m, so the construction
is impossible. More explicitly the nonzero weights

\[
 b_i=\left(\prod_{j\ne i}(a_i-a_j)\right)^{-1}
\]

annihilate every restricted degree-at-most-d polynomial. This follows by
comparing the leading coefficient in interpolation on d+2 nodes. It is a
dual certificate against **every** permitted vector polynomial.

For Q=F2[t]/(t^3+t+1), n=2,d=3,m=5, use bit-encoded nodes 0,1,2,3,4.
The bad dependence is [2,6,5,7,6]; its moments of degrees 0 through 4 are
[0,0,0,0,1]. Evaluation ranks are 5 and 4. Exact computation independently
checks the cardinal values, the punctured I_5 (since -1=1), and all 72 full
affine-line Gram sums. This finite check corroborates the parametric proof.

**Boundary.** Output dimension equal to |H| is essential. In characteristic two
constant evaluations on two holes have rank one but Gram always zero; constants
on three holes can give Gram I_1 without surjectivity onto all three hole
coordinates. For rectangular output neither surjectivity nor rank alone is
the general criterion: the restricted bilinear form matters. The degree bound
here is sufficient, not claimed necessary for every output architecture.

## PM-CONSTRUCTION-0003: the exact triangle certificate and its limits

Let k be a field of characteristic two, X,V vector spaces, a in X*, T symmetric
bilinear, and arbitrary linear U_i:X->V and u_i in V*, for i=1,2,3.
For each directed incidence suppose witnesses x_ij satisfy

\[
 U_i x_{ij}=U_j x_{ji},\qquad
 u_jU_i=a+T(x_{ij},-).
\]

Then c_ij=a(x_ij)+a(x_ji) obeys c_12+c_23+c_31=0. In particular all three
cannot equal one. Injectivity and T(x,x)=a(x) are unnecessary for this local
lemma; no claim removes them from the larger source construction.

**Proof.** Evaluate each of the six directed functional identities on x_ik,
where i,j,k are distinct. For fixed j the two left sides cancel by sharing
on {i,k}; for fixed i the two T terms cancel by symmetry. The six a terms
are precisely the three c's. QED.

There is also an exact completeness statement in the **six-evaluation grammar**.
Write its rows as L_(j;ik)-B_(i;jk)-A_(i;k)=0, identify
L_(j;ik)=L_(j;ki) and B_(i;jk)=B_(i;kj), and allow constant row weights.
All combinations eliminating L,B and depending only on the three plus-edge
observables form a one-dimensional space in characteristic two and the zero
space in any other characteristic. Indeed cancellation requires
w_ijk+w_kji=w_ijk+w_ikj=0. These transpositions generate S3, so weights are
one parameter times permutation sign. Equal coefficients on A_(i;k),A_(k;i)
then force 2w=0. This proves both claims, not merely sample ranks.

The raw polynomial equations are already covered by a degree-one NulLA
certificate. In characteristic two put F_ij=u_jU_i+a+T(x_ij,-),
S_ik=U_ix_ik+U_kx_ki, E_ij=a(x_ij)+a(x_ji)+1. With symmetric T built into
its coordinates,

\[
 1=\sum_{i,j,k\ distinct}F_{ij}(x_{ik})
   +\sum_j u_j(S_{ik})+\sum_{\{i,j\}}E_{ij},
\]

where in the middle sum {i,k} is the complement of j. Expansion cancels all
sharing, bilinear and a terms and leaves 3=1. Multipliers of raw scalar
equations have degree at most one. If symmetry is instead an extra variable
relation, its multipliers must be counted separately. Fixing U,u,T makes the
hole equations affine in the witnesses, where ordinary elimination suffices.

**Actual failure controls.** In odd characteristic the local interface admits
U_i=id,u_i=a=id,T=0,x_ij=1/2, giving a triangle. This does not retain extra
frame self-annihilation or diagonal identities. In characteristic two a
nonsymmetric T admits an injective triangle; full vector data and exact
checks are in CONSTRUCTION_B.md and triangle_contracts.py. That control cannot
retain T(x,x)=a(x) over F2, since polarization would imply symmetry.

**Cancellation does not supply richness.** A stronger countermodel retains
even distinct injective maps, symmetric nondegenerate T, T(x,x)=a(x), and
u_iU_i=0, yet has no holes: take X=F2^2,V=F2^4,T=I_2,a=(1,1), all u_i=0,
U_i(e1)=e1,U_i(e2)=e_(i+1), i=1,2,3. The functional identities force both
witnesses to (1,1); their a-values sum to zero. Thus no positive density of
holes follows from this local algebra. In particular no uniform four-hole
supersaturation follows from the six-term cancellation alone. A's alternative
a=(1,0) also gives an empty relation with T=I_2, but does **not** retain the
diagonal identity; the stronger version here uses the corrected a=(1,1).
The source's frame laws/gradient realization and distribution hypotheses
remain separate, substantial obligations. This is not a counterexample to
the source's full theorem.

## PM-CONSTRUCTION-0004: stability under all additive products

Let Omega be finite, D subset Omega nonempty, and w:Omega->Z^r with w(d)=0 for d in D.
Call this grading stable if, for every n>=1,

\[
 \sum_{i=1}^n w(s_i)=0\quad\Longleftrightarrow\quad s_i\in D\ (\text{all }i).
\]

It is stable if and only if there is an integral linear functional c with
c.w(s)>0 for every s outside D. Thus a stable finite integral multigrading
can always collapse to a nonnegative scalar defect with the same zero set.
Linear collapse preserves an additive decomposition into legal local readouts.

**Proof.** Remove D and let A have the remaining integer weight vectors as
columns. A bad product is exactly a nonzero nonnegative integral vector z
with Az=0; target factors may be omitted. Such a vector exists if and only
if 0 belongs to the convex hull of the columns: normalize z in one direction;
in the other, rational feasibility of this integer system gives rational
convex coefficients and clearing denominators gives z. If 0 is outside the
finite convex hull, strict separation gives a real c positive on every column.
Finite strict inequalities admit a rational perturbation of c; clearing its
denominators makes c integral. Conversely positive c rules out any bad sum.
If Omega=D the empty strict system is vacuous and c=0 works. QED.

For scalar integer defects, stability means every off-target defect has the
same strict sign, allowing a global sign reversal. Positive p and negative
q would otherwise give a bad product with -q copies of p and p copies of q.
Integrality matters: the real defects 1,-sqrt(2) have no nonzero nonnegative
integral relation but cannot be made both positive by a scalar functional.
Finiteness matters too: the integral weights {(1,n):n in Z} together with
(0,-1) admit no nonempty zero-sum multiset, but positivity on every (1,n)
forces the separator's second coordinate to zero, contradicting positivity
on (0,-1). Full independent support Omega^n matters; coupled product supports
can exclude the bad multiset.

In 107 the two off-target branches p,p' above have Laurent defects -1,+1.
Their product returns to zero. The shifted ordinary-polynomial alternative
has degrees M-2,M, whose sum is the two-target degree 2(M-1). It therefore
also fails all-product selection. The quadratic defect is nonnegative and
zero exactly on D, so it is stable for independent products of the filtered
support S. This is a local product theorem; it does not establish any tensor
rank, asymptotic complexity, or headline application. Extra selectors can
work one factor at a time; their placement and period costs must be counted.

## Prior art, algorithm and remaining gap

These results refine the **input requirements** for a proposed instrument.
They do not show that existing mathematics lacks these operations. In
particular:

- Rauh–Kahle–Ay, *Support Sets in Exponential Families and Oriented Matroid
  Theory*, [arXiv:0906.5462v2](https://arxiv.org/pdf/0906.5462), Definition 6
  and Lemma 7, gives the facial-set/signed-dependence criterion. With columns
  equal to local one-hot features and a constant coordinate, positive local
  selection is exactly a facial-set problem. The matching trades above are
  explicit applications.
- P. Gordan, *Ueber die Auflösung linearer Gleichungen mit reellen Coefficienten*,
  Math. Ann. 6 (1873), 23–28, [DOI 10.1007/BF01442864](https://doi.org/10.1007/BF01442864),
  states the strict homogeneous alternative on page 23; a public scan was
  inspected in the independent audit. The product-stability lemma uses this
  classical alternative plus rationality, not a new theorem of alternatives.
- De Loera–Lee–Malkin–Margulies, [arXiv:0801.3788v1](https://arxiv.org/pdf/0801.3788v1),
  section 2, already discovers bounded-degree polynomial certificates by
  coefficient matching. Section 3.2 Theorem 3.5 requires characteristic not
  dividing the group order for completeness of its orbit compression. One
  cannot average over S3 in characteristic two to justify completeness;
  the full matrix and the direct six-row proof remain valid.
- Lower-set Newton and univariate Lagrange interpolation already construct
  the needed cardinal functions. The upstream 197 pairing explicitly credits
  Dyn–Floater. The finite-field extension follows from a nonzero triangular
  evaluation diagonal. Read source-specific comparisons in CONSTRUCTION_A.md
  and the independent prior-art audit in CONSTRUCTION_ADVERSARIAL.md.

For a frozen finite certificate grammar, form columns m f_i for every allowed
multiplier m and solve for the desired residual's coefficient vector. If no
solution exists, elimination returns a dual functional vanishing on those
columns but not on the residual. This certifies failure of that grammar,
not impossibility of every mathematical proof or existence of an actual
countermodel. Dense elimination costs O(R C min(R,C)) field operations for an
R-by-C matrix; dimension and coefficient bit sizes can grow rapidly. Exact
LP/separation is the relevant ordered-positivity baseline. Minimum-support
optimization is a stronger problem and is not promised by feasibility.

The remaining concrete operation is **choosing and repairing a representation
under its actual composition and resource constraints**, instead of supplying
the phase, square, hole geometry and contraction grammar by hand. This is an
operational research target, not a proved gap beyond existing algorithms.
Next compare representation-search cost with fixed exact LP/NulLA baselines,
then freeze a previously unread target before testing any transfer. The 64
graphs and c=3 perturbation here are transparent calibration, not unseen data.

## Source pins and verification scope

Primary files at openai/math revision 1581d4cbdd69a0faf34b2089614fe2a814316a6a:
B07 03-pairing.tex, blob f77a972f6e99d6c7f312c802b7a5b8b59de5a184;
B18 FiniteProjection.lean, blob 585d246122aebba1c7fec25f180c2fab16e0c92c;
B19 SquareWeights.lean, blob 2592d0adba3c73d7d8925262e8e2568c79656c1d;
B21 02-geometry.tex, blob 615530e1f2e5052afd794b3e0719ce1c28553d23.
Full paths/links are in research/corpus/openai_math_sources_20261018.json.
The comparison records object/action, observable, certificate, first residual,
construction step, baseline and failed hypothesis in CONSTRUCTION_A/B.md.
Those source reads are not fresh Lean compilation or full headline audits.

Exact replay commands and outputs:

```sh
python3 tools/construction_contracts.py
python3 tools/triangle_contracts.py
python3 tools/construction_boundary_check.py
python3 tools/construction_independent_field.py
```

Corresponding JSON is in research/experiments. The primary implementation
recovers weights by coefficient matching and checks all 64 interaction scopes;
the separate boundary implementation uses different explicit triangle data.
The independent field implementation uses polynomial-bit convolution, brute
inverse search, span rank and newly solved interpolation systems rather than
importing the primary arithmetic or Lagrange construction.
Independent algebraic views, adversarial review and coordinator acceptance
are documented separately. These are AI reviews, not human peer review.
There is no new FORMAL_VERIFIED claim or historical-new-tool claim.

# PM-SYNTH-A — construction information that cancellation does not supply

Date: 2026-10-18. Task-scoped independent initial mathematical proposal for ProofMotifs. Repository inspection was read-only. This note concerns the local polynomial-pairing construction in family 197 and the local Fourier/ordinary-polynomial projection in family 107. It does not validate either upstream headline, compile Lean, establish historical novelty, or constitute a held-out application.

## 1. Precise outcome

The strongest common conclusion found is a **restricted no-go**, rather than a new universal cancellation theorem. Knowing a scalar averaging action and the class of observables that it kills does not determine whether the *required constrained residual construction* is possible.

Two exact obstructions make the missing input concrete:

* **197 interpolation geometry.** Fix the same field, dimension, polynomial-degree budget, line-sum annihilator and number of holes. A set of `d+2` holes in an index simplex admits the prescribed punctured Gram residual, while `d+2` collinear holes do not. The latter has a nonzero explicit barycentric evaluation dependence. This obstructs every vector polynomial of the allowed degree, not merely the source's particular interpolation algorithm.
* **107 local interactions.** Fix the same bounded labels, Fourier phase and desired matching branches. No sum of arbitrary unary weights can be zero on all desired branches, nonnegative on the Fourier support, and positive on an undesired surviving branch. An exact two-branch marginal trade proves this. The source's access to the interactions `hu` and `hv` permits a quadratic square certificate. Degree two is minimal in this nonnegative, zero-target-degree ansatz.

The qualification in the second bullet is essential: if signed Laurent exponents and extraction of an interior coefficient are allowed, the unary linear weight `g-h` already separates the desired branches. Thus the interaction obstruction concerns the ordinary-polynomial/degree-zero degeneration requirement, not every possible exact coefficient filter.

These are sharp input requirements for an operational instrument: preserve the hole evaluation geometry and the permitted local readouts, and specify whether the requested operation is a degeneration to degree zero or an arbitrary coefficient projection. The underlying rank, interpolation, finite-Fourier and convex-separation mathematics is established. Historical novelty of this precise comparison is unresolved, and no new mathematical principle is claimed.

## 2. Primary-source inspection and common template

All upstream paths below were fetched at the manifest's pinned revision
`1581d4cbdd69a0faf34b2089614fe2a814316a6a` of `openai/math` on 2026-10-18. Original-source content was inspected, not inferred solely from the repository's research notes.

* 197: `preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/build/sections/03-pairing.tex` (manifest B07, complete, 106 lines); `lean/OAI/RingTheory/DirectFiniteness/Pairing.lean` (B06, complete, 289 lines); `lean/docs/197.md` (B09, complete).
* 107: `lean/OAI/LinearAlgebra/MatrixMultiplication/AuxiliarySeparation/Separation/Fourier.lean` (B17, complete); `FiniteProjection.lean` in the same directory (B18, complete); `SquareWeights.lean` there (B19, complete); additionally `NoWrap.lean` there (complete, outside the preexisting B17–B19 records); `lean/docs/107.md` (B20, complete).

Canonical source URL prefix: `https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/` followed by the exact path above. The source files' content was returned by `github.fetch`. Their existence and local arguments are evidence about those statements, not successful compilation or a full dependency audit.

| Template field | Family 197: punctured polynomial pairing | Family 107: finite projection plus square weights |
| --- | --- | --- |
| Object/action | Functions on `Q^n`, where `Q` has `q` elements, restricted to a full affine `Q`-line `a+tb`; sum over every `t in Q`. The source's pairing proposition chooses characteristic two. | A finite family of branches with integer labels `(g,h,u,v)` in `1,...,M`; multiply a branch by `zeta^(r E)`, average over `r=0,...,L-1`, with `E=u-v+2(g-h)`, `L=5M`, `zeta` a primitive `L`th root in `C`. Then extract a polynomial coefficient. |
| Observable class | Polynomial entries of `x_v x_v^T`, each of total degree at most `2d`; source chooses `d=(q-2)/2`, hence `2d=q-2`. On any line they become univariate polynomials of degree below `q-1`. | Arbitrary complex branch coefficients times Fourier characters; after the phase filter, a branch has the ordinary polynomial degree supplied by an additive sum of weights on three allowed tensor legs. |
| Synthesized certificate | Lower-set Newton interpolation produces `f_o` of degree at most `d`, cardinal on all of `S_d`, for holes `o in O subset S_d`. Put `x_v=(f_o(v))_o`. Products have the line-sum degree budget, and the hole Gram contribution is `I`. | Weights `A(g)=g^2`, `B(h,u)=hu-h^2`, `C(h,v)=-hv` satisfy `A+B+C=(g-h)^2+hE`. The normalized primitive-root average enforces `L|E`; the label bound gives `|E|<=3(M-1)<L`, hence `E=0`; there the total weight is a nonnegative square. |
| First structurally surviving term | For a line polynomial of degree at most `q-1`, its sum is minus its coefficient of `t^(q-1)`; the degree `q-1` monomial is the first permitted survivor. The source stays strictly below it. The nonzero residual `-I` is then produced by deleting holes, not by a surviving positive-degree term of the full sum. On the whole `Q^n`, the first total degree capable of a nonzero monomial sum is `n(q-1)`, a distinct threshold. | The Fourier filter retains precisely `E=0` under no wrap. Among those branches, degree zero retains exactly `g=h,u=v`. For `M>=3`, the first permitted undesired degree is one, realized by `|g-h|=1` and `u-v=-2(g-h)`. Arbitrary coefficients can cancel even these permitted terms, so no aggregate coefficient is asserted nonzero. |
| Actual construction choice | Choose the *index simplex*, not an arbitrary hole set of the same size. Interpolate on all of `S_d` even when only `O` is deleted. This supplies a cardinal evaluation map within the degree budget. | Choose a phase visible to all necessary labels and choose weights respecting the allowed leg readouts `g`, `(h,u)`, `(h,v)`. The cross interactions make the residual weight a square. Individual leg weights may be negative; the total is nonnegative after Fourier projection. |
| Strongest relevant existing tools | Finite-field power sums plus lower-set Newton interpolation; in coding language, the evaluation code's coordinatewise square lies in degree `2d`, and full-line incidence vectors annihilate that square code. The manuscript itself cites lower-set interpolation and related coding constructions, while proving the needed facts directly. | Character orthogonality/Reynolds projection, no-aliasing bounds, and a diagonal torus degeneration exposed by a nonnegative support weight. For synthesis under a specified local readout, convex separation or marginal-trade obstructions are the appropriate existing baseline. This note proves the needed finite criterion below and does not claim it as new. |
| Failed hypothesis | Degree `q-1` permits a nonzero line sum; cardinal interpolation is impossible at the allowed degree on an overloaded line; if a regular retained-line family has degree `D` nonzero in the coefficient field, local zero sums contradict a nonzero global Gram residual. | A nonprimitive root or loss of no-wrap can retain a forbidden phase. Unary local readouts cannot supply the required nonnegative weight. Allowing signed Laurent degrees removes that particular obstruction, so the type of coefficient operation cannot be suppressed. |

The source's headline scope is much larger. In 197, incidence regularity, girth, packing, group embeddings and the reverse-product defect remain separate obligations. The scope file explicitly describes a detailed group with odd-prime torsion, and must not be silently used to certify the catalogue's stronger torsion-free heading. In 107, tensor, spectral/growth and arithmetic-complexity bridges remain separate obligations. No conclusion about an exponent or practical matrix multiplication follows from the local projection alone.

## 3. The 197 geometric obstruction, parametrically

All polynomials here are formal polynomials over a finite field `Q`; total degree means ordinary polynomial degree. Write `P_d` for the polynomials in `n` variables of total degree at most `d` and `A=Q^n`.

### A197-1. Exact local feasibility criterion

Assume `n>=1`, `m=|O|`, `O subset A`, and `2d<=q-2`. There is a vector polynomial

`x:A -> Q^m`, each of whose components is the evaluation of an element of `P_d`,

such that

`sum_(v in A\O) x_v x_v^T = -I_m`

if and only if the evaluation map `ev_O:P_d -> Q^O` is surjective. When it exists, the same `x` automatically satisfies

`sum_(v in ell) x_v x_v^T = 0`

for every full affine line `ell` in `A`, including every full line contained in `A\O`.

**Proof.** Each entry of `x_v x_v^T` is a polynomial of total degree at most `2d<=q-2`. On a full line its sum is zero by the finite-field power-sum identity. Partitioning `A` into parallel lines also gives zero for its full-space sum.

If `ev_O` is surjective, choose a polynomial of degree at most `d` for each coordinate function on `O`. Their evaluation columns at the holes are the standard coordinate vectors, so the hole Gram sum is `I_m`; subtract from the full-space zero sum.

Conversely, let `X` be the `m` by `m` matrix whose columns are the `x_o`, with holes indexed in any order. Full-space cancellation and the prescribed complement identity imply `XX^T=I_m`. Hence `X` is invertible over the field. Its rows are evaluations of degree-at-most-`d` polynomials, so the image of `ev_O` contains a basis of `Q^O`. Thus it is surjective. QED.

This criterion is ordinary evaluation-code/rank algebra; it is included to identify the exact constraint, not advertised as a new instrument.

### A197-2. Sharp collinear obstruction

Let `r<=q` distinct holes lie on an affine line, and suppose `r>=d+2`. Then `ev_O` is not surjective, so A197-1's prescribed residual is impossible at degree `d`.

More precisely, evaluation of `P_d` on `r` distinct collinear points has rank exactly `min(r,d+1)` when `d<q`. The restriction is a univariate polynomial of degree at most `d`, giving the upper bound. Conversely, choose an affine linear coordinate `lambda` on the ambient space whose restriction to that line is its parameter. The polynomials `1,lambda,...,lambda^d` yield the Vandermonde lower bound. If a larger hole set contains these `r` points, a dependence among these columns extends by zeros to a dependence on all its holes.

An explicit dependence for `r=d+2` points with line parameters `a_0,...,a_(d+1)` is

`w_i = 1 / product_(j!=i)(a_i-a_j)`.

All entries `w_i` are nonzero and

`sum_i w_i a_i^k=0  (0<=k<=d)`,

`sum_i w_i a_i^(d+1)=1`.

**Proof of the certificate.** Lagrange interpolation on these `d+2` nodes writes the polynomial `T^k` (`k<=d+1`) as a sum of its node values times the degree-`d+1` Lagrange cardinal polynomials. Their leading coefficients are precisely `w_i`. Compare the coefficient of `T^(d+1)`. Any ambient polynomial of total degree at most `d` restricts to a linear combination of the first `d+1` monomials, giving the stated dependence. For any candidate matrix of hole columns, `Xw=0`; an invertible `X`, and hence `XX^T=I`, is impossible. QED.

The bound is sharp for collinear holes: if `r<=d+1`, univariate Lagrange interpolation in `lambda` supplies cardinal polynomials of degree `r-1<=d`.

### A197-3. Same profile, opposite feasibility: explicit parameter family

Let `n>=2`, `d>=1`, and `2d<=q-2`. Enumerate distinct elements with `a_0=0,a_1=1`, and set `m=d+2`. All displayed points below have remaining coordinates zero.

Good holes:

`O_+ = {(a_i,0):0<=i<=d} union {(0,1)}`.

Bad holes:

`O_- = {(a_i,0):0<=i<=d+1}`.

They have the same cardinality `m`; the field, affine ambient space, action, observable degree cutoff, component degree budget and requested residual are identical.

For `O_+`, let `L_i(X)` be the degree-`d` univariate Lagrange cardinal polynomials on `a_0,...,a_d`. The explicit components

`f_i(X,Y)=L_i(X)-L_i(0)Y  (0<=i<=d)`,

`f_*(X,Y)=Y`

have degree at most `d` and are cardinal on `O_+`. Thus A197-1 constructs the residual and all full-line identities. Also `O_+` lies in the source's index simplex `S_d`: the axis points have indices `(i,0)` with `i<=d`, and `(0,1)` has index `(0,1)`.

For `O_-`, A197-2 gives evaluation rank exactly `d+1<m`, so the residual is impossible for *every* allowed polynomial vector map.

**Concrete source-compatible instance.** Take

`Q=F_2[t]/(t^3+t+1)`, `q=8`, `n=2`, `d=3`, `m=5`.

Use the bit encoding `a_0=0,a_1=1,a_2=t,a_3=t+1,a_4=t^2`; addition is xor and multiplication is reduced modulo `t^3+t+1`.

`O_+={(0,0),(1,0),(t,0),(t+1,0),(0,1)}`,

`O_-={(0,0),(1,0),(t,0),(t+1,0),(t^2,0)}`.

For the bad nodes, the barycentric dependence is the bit vector

`w=[2,6,5,7,6]=[t,t^2+t,t^2+1,t^2+t+1,t^2+t]`.

Its moments at powers `0,1,2,3` are all zero, and the power-four moment is one. Hence the bad evaluation rank is exactly four. For the good holes, the preceding `L_i-Y` construction gives five independent coordinate values while preserving component degree at most three and product degree at most six.

These facts concern the local punctured Gram construction. Neither hole set here is asserted to satisfy the additional size, regular-incidence or girth hypotheses of the full manuscript proposition.

### A197-4. Scalar incidence compatibility

If retained points each lie on exactly `D` retained full lines, and matrices `W_v` satisfy every retained-line sum zero and `sum_V W_v=-I_m` with `m>0`, summing the line equations gives

`0=sum_lines sum_(v in line)W_v=D sum_V W_v=-D I_m`.

Over a field this forces `D=0` as a scalar. In the characteristic-two source, `D=ell+1` for an odd prime `ell`, so this requirement holds. It is independent of the interpolation obstruction above.

## 4. The 107 locality obstruction, parametrically

Fix an integer `M>=1`. Let

`S_M={(g,h,u,v) in {1,...,M}^4 : E=u-v+2(g-h)=0}`,

`D_M={(g,g,u,u):g,u in {1,...,M}}`.

The source's constant-term ordinary-polynomial certificate asks for an integer-valued weight `W` such that

`W=0 on D_M`, and `W>0 on S_M\D_M`.

In particular it is nonnegative on `S_M`. The integers can be replaced by rational weights and a positive common denominator clearing; the no-go below holds for arbitrary real weights.

### A107-1. Arbitrary unary nonnegative weights cannot separate

Let

`W(g,h,u,v)=A(g)+H(h)+B(u)+C(v)`

for completely arbitrary real functions of one label. If `W=0` on `D_M` and `W>=0` on `S_M`, then `W=0` on *all* of `S_M`.

**Proof by an exact trade.** For any `s=(g,h,u,v) in S_M`, its reversal

`s^R=(h,g,v,u)`

also lies in `S_M`, because its phase is `-E(s)`. Set

`d_1=(g,g,u,u)`, `d_2=(h,h,v,v)`.

These are desired branches. In each of the four individual coordinate positions, the multiset of labels of `s,s^R` equals the corresponding multiset for `d_1,d_2`. Therefore every additive unary weight satisfies

`W(s)+W(s^R)=W(d_1)+W(d_2)=0`.

Both left terms are nonnegative, so both are zero. This holds for every `s`. QED.

For `M>=3`, `S_M\D_M` is nonempty. The explicit balanced trade is

`s_1=(1,2,3,1)`, `s_2=(2,1,1,3)`,

`d_1=(1,1,3,3)`, `d_2=(2,2,1,1)`.

Both wrong branches have phase zero. Their unary feature sum equals that of the two target branches, ruling out strict positivity. This is an algebraic obstruction valid for arbitrary unary functions, not a finite search over a polynomial ansatz.

For `M<=2`, the off-target set is empty: a nonzero `g-h` gives `|2(g-h)|>=2` but `|u-v|<=1`. Thus that small case provides no counterexample to the theorem or its sharpness.

### A107-2. The source's interactions suffice; symbolic degree two is minimal

Allow the leg readouts `g`, `(h,u)`, `(h,v)`, as in the source. Define

`A(g)=g^2`, `B(h,u)=hu-h^2`, `C(h,v)=-hv`.

Then, identically over the integers,

`W=A+B+C=(g-h)^2+hE`.

On `S_M` this is `(g-h)^2>=0`. It is zero exactly when `g=h`; the phase equation then forces `u=v`. Thus it gives the source's desired nonnegative, degree-zero certificate for every `M`.

Now restrict `A,B,C` to polynomials of total degree at most `r` in their respective allowed variables. If `r<=1`, their sum is unary affine: collect the two occurrences of the linear `h` term into `H(h)`. A107-1 rules out separation when `M>=3`. At `r=2` the displayed source certificate works. Therefore **two is the minimum symbolic total degree within this specified nonnegative local-leg ansatz**, even when coefficients may depend on `M`. The stronger arbitrary-unary theorem also shows that high-degree unary polynomials do not repair the missing interactions.

The square need not be interpreted as cancellation of arbitrary high moments. It is a positive support weight modulo an independently imposed phase relation. The Fourier sum supplies exact vanishing of unwanted phases; the square supplies a different operation, identification of a zero-weight face.

### A107-3. A necessary boundary: signed coefficient projection escapes

If nonnegative degrees and extraction of degree zero are not required, set

`W_0(g,h,u,v)=g-h`.

This is unary and linear. On `S_M`, `W_0=0` if and only if `g=h,u=v`. Therefore the Laurent polynomial

`sum_(s in S_M) c_s t^(g-h)`

has constant coefficient exactly `sum_(s in D_M)c_s`. If an ordinary polynomial is required but an interior coefficient is permitted, multiply by `t^(M-1)` and extract coefficient `M-1`. Its degree is at most `2(M-1)`; using the phase bounds makes a smaller range possible. This is a correct local filtering observation, not a conclusion about the complexity or tensor rank of the surrounding construction.

Thus A107-1 does not show that the source's interactions or quadratic degree are necessary for every exact filter. It shows they are necessary for the source-type **nonnegative weight with the desired terms at degree zero** under the specified local readouts. Whether an interior-coefficient alternative preserves the surrounding construction's useful quantitative bounds remains an independent question.

### A107-4. Fourier and degree boundaries from the original formulas

With a primitive `L`th root `zeta` in `C`,

`(1/L) sum_(r=0)^(L-1) zeta^(rE) = 1_(L|E)`.

This follows by summing the geometric progression when `zeta^E!=1`, and primitiveness gives `zeta^E=1 iff L|E`. For all labels in `1,...,M`, `|E|<=3(M-1)<5M=L`, so divisibility is equivalent to `E=0`.

The failure examples can affect even the final degree-zero test:

* With allowed labels `M=4`, the branch `(g,h,u,v)=(2,1,1,4)` has `E=-1` and `W=0`. A true primitive twentieth root removes it. The nonprimitive root `zeta=1` keeps it and its zero-degree weight, creating a false survivor.
* If the label bound is dropped, take `M=1`, hence `L=5`, and `(g,h,u,v)=(6,1,1,36)`. Then `E=-25` and `W=0`. A primitive fifth-root average keeps this nonzero phase, and degree-zero extraction keeps the wrong branch. All labels here are positive, but they violate the bound `<=M`.

On the valid phase-zero support, the exact weight is a square. The source proves the valid coarse bound `(M-1)^2`; using all four label bounds also gives the elementary sharper local bound

`|g-h|<=floor((M-1)/2)`, hence `W<=floor((M-1)/2)^2`.

No matrix-multiplication consequence of that local refinement is claimed.

## 5. Existing operational baseline: readouts, faces and trade certificates

The following is the ordinary finite convex-separation criterion, stated to expose the exact input a solver needs. It is not a proposed new theorem, and replacing a specialist method by generic linear programming is not itself new mathematics.

Let `S` be a finite support, `D` a nonempty desired subset, and let `phi:S -> Q^N` encode the permitted local readouts. Coordinates can be one-hot indicators of each local label configuration. A legal additive weight is `W(s)=w dot phi(s)`; add a constant coordinate if needed.

**A-LOC (known criterion).** There is a rational legal weight with `W(d)=0` for every `d in D` and `W(s)>0` for every `s in S\D` if and only if there is no nonzero nonnegative rational vector `(beta_s)_(s in S\D)` and rational scalars `(alpha_d)_(d in D)` with

`sum_(s outside D) beta_s phi(s) = sum_(d in D) alpha_d phi(d)`.

With a constant coordinate, the total coefficients on the two sides coincide. The `alpha_d` need not be nonnegative; a stronger positive trade is often available, as in A107-1.

**Proof.** Let `U=span_Q{phi(d):d in D}` and project features to the real quotient `R^N/U_R`. A weight vanishing on all desired features is a linear functional on this quotient. If such a functional is strictly positive on every projected off-target feature, pairing it with the displayed relation contradicts nonzero nonnegative `beta`.

Conversely, normalize a hypothetical nonnegative relation by `sum beta=1`. Its existence says exactly that zero belongs to the convex hull of the finitely many projected off-target features. If there is no relation, that compact convex hull excludes zero. Let `p` be its point nearest zero in an arbitrary Euclidean structure. For every point `x` of the hull, minimality along the segment from `p` to `x` gives `p dot x >= ||p||^2>0`. Thus the functional `p dot -` is positive on every off-target feature and annihilates `U` after lifting to its orthogonal complement. Since all features are rational, the homogeneous equalities defining `U` admit a rational basis, and rational points are dense in their solution subspace. A sufficiently close rational approximation preserves the finitely many strict inequalities. Conversely, a real normalized relation in the rational linear equalities and nonnegative inequalities has a rational solution: take a minimal support solution, eliminate dependent columns until its positive columns are affinely independent, and solve that full-rank rational system. Hence the rational and real formulations agree. QED.

This criterion supplies either a finite legal weight or an exact obstruction once the local readouts are fixed. The important operation is not just computing a kernel: changing the readouts changes which branch configurations share marginals, and can change an impossible nonnegative degeneration into a possible one. In the unary 107 model the four tuples above give an exact trade. The actual `hu,hv` interactions distinguish it; the square formula is a concise symbolic witness for the enriched readouts.

For 197, the analogous obstruction is an evaluation *circuit* rather than an ordered positive trade: a nonzero dependence among hole columns blocks interpolation at the required degree. The field's characteristic and the relevant vector-space geometry must be preserved. It would be unsound to apply real positivity or a semisimple averaging theorem to this modular evaluation problem without a proved bridge.

One simple algebraic warning sharpens the last point. On all functions on a finite additive group of order `q` in characteristic dividing `q`, the unnormalized orbit sum `T` satisfies `T^2=qT=0` and is nonzero. The normalized characteristic-zero Fourier projector `P` satisfies `P^2=P` and is nonzero. An algebra homomorphism cannot carry the first operator to the second: it would force both `P^2=0` and `P^2=P`. Thus a purported operator-preserving identification of these two averages is impossible. This does not prevent a more informative comparison; it forbids dropping the coefficient/normalization data.

## 6. What this rules out, and the next mathematical operation

The no-go is relative to a specified information loss and certificate class. It does not prove that a universal synthesis system is impossible. It proves that a system which retains only action/observable annihilation data and aggregate size/degree information cannot correctly decide these constrained constructions. In 197, A197-3 gives opposite answers with that profile held fixed. In 107, the phase, bounded labels and desired branches stay fixed while changing from unary readouts to the actual interacting leg readouts changes infeasibility into feasibility.

A credible candidate instrument should accept at least:

1. the coefficient field/ring and the precise averaging or coefficient operation;
2. a costed grammar of permitted auxiliary polynomials and local readouts;
3. the desired residual or desired branch support;
4. the degree/positivity budgets and all no-wrap hypotheses;
5. exact failure witnesses, including evaluation circuits and marginal trades.

The most useful next operation is to test a **minimal interaction augmentation procedure** on the already-seen 107 calibration: start with unary readouts, return the four-tuple trade, identify which allowed pair readout breaks it, and synthesize a valid weight while accounting for polynomial degree and the final allowed coefficient operation. Baseline this against direct polynomial identities and the known face-separation criterion. Do not label this calibration held out. A second operation is to prove or refute whether the signed linear interior-coefficient alternative preserves the required tensor/complexity bridge; the local identity alone does not answer it.

For a genuinely held-out test, the coordinator must freeze an unexposed target and the local access/cost model before attempting it. Success would require constructing a correct useful certificate or returning a valid obstruction under that same model, compared with the strongest existing domain method. This note itself contains no held-out transfer.

## 7. Verification and command record

* Read-only repository commands: `pwd`; `rg --files` for AGENTS/program/evidence/manifest/audit/boundaries; `cat` of those files; targeted `rg -n` for the two families and their source-specific mechanisms.
* Primary retrieval: `github.fetch` with the pinned canonical blob URLs listed in section 2. The initial batched retrieval printed duplicated structured content and was truncated; the dependent 107 files and 197 Lean/scope files were then fetched individually and their source text inspected. A repository-wide recursive tree fetch failed with `Transport closed` and supplied no evidence; it was not used to support any claim.
* Exact local arithmetic command: a standalone standard-library Python heredoc implemented xor addition and multiplication reduced by binary polynomial `0b1011`, inverted the five barycentric denominators, and printed nodes `[0,1,2,3,4]`, weights `[2,6,5,7,6]`, moments `0,0,0,0,1` for powers `0,...,4`. It exited zero. This independently checks the displayed bad-hole dependence, not the whole proof or a headline theorem.
* The coordinating researcher was informed of both proposed obstructions, the explicit `F_8` certificate, and the signed-Laurent escape before this note was finished. Independent adversarial review and the coordinator's planned exact standard-library certificates remain separate from this author's proof pass.
* No Lean compilation, external correspondence, paid tools, repository writes, Git operations or pushes were performed by this subtask. This note was created only under `/tmp` using `apply_patch`.

Correctness status: complete elementary proofs supplied above, pending independent adversarial assessment. Formal-verification status: not formalized or compiled. Historical-novelty status: unresolved; the component tools are classical. Contribution status: a precise construction-sensitive obstruction analysis for the two calibration mechanisms, not a new universal theorem.

## 8. Independent cross-review of the relayed PM-SYNTH-B local identity

The coordinator relayed the following local data from an independently working researcher. This section checks those data as stated; the underlying family-157 source assumptions were not independently re-audited in this subtask.

Let `k` be a field of characteristic two, `X,V` vector spaces, `a:X->k` linear, `T:X times X->k` symmetric bilinear, `U_i:X->V` linear and `u_i:V->k` linear for `i=1,2,3`. For every ordered distinct pair assume a witness `x_ij in X` satisfying

`U_i x_ij=U_j x_ji`,

`u_j composed U_i = a + T(x_ij,-)`.

Then

`a(x_12)+a(x_21)+a(x_13)+a(x_31)+a(x_23)+a(x_32)=0`.

**Independent proof.** Evaluate the two functional equations indexed `(1,3)` and `(2,3)` respectively at `x_12` and `x_21`. Their left sides coincide by the shared-image identity for edge12. Thus

`a(x_12)+a(x_21)=T(x_13,x_12)+T(x_23,x_21)`.

Evaluate the equations indexed `(1,2)` and `(3,2)` at `x_13` and `x_31`, obtaining

`a(x_13)+a(x_31)=T(x_12,x_13)+T(x_32,x_31)`.

Finally use `(2,1)` and `(3,1)` at `x_23` and `x_32`:

`a(x_23)+a(x_32)=T(x_21,x_23)+T(x_31,x_32)`.

Add the three equations. Symmetry pairs the six right-hand terms; each pair sums to zero in characteristic two. No injectivity or nondegeneracy was used. In particular, the three edge observables cannot all equal one, because `1+1+1=1` in characteristic two. QED.

The relayed constant model is correct for this local law: `X=V=F_2`, `a=id`, `T(x,y)=xy`, `U_i=id`, `u_i=0`. The functional equation forces `x_ij=1` for every ordered pair; shared images hold; all edge observables are zero. If vertices must be distinct pairs `(U_i,u_i)`, however, this particular repeated-label model alone does not meet that additional hypothesis.

A stronger countermodel handles distinct injective maps and a nondegenerate symmetric form. Set `X=F_2^2`, `V=F_2^4`, `a(x_1,x_2)=x_1`, `T(x,y)=x_1y_1+x_2y_2`, and `u_i=0`. Define distinct injective maps by

`U_i(e_1)=e_1`, `U_i(e_2)=e_(i+1)` for `i=1,2,3`.

The equation `0=a+T(x_ij,-)` forces every witness to equal `e_1`. Their images all equal `e_1`, so the shared-image condition holds. Nevertheless every edge observable is `a(e_1)+a(e_1)=0`. Thus these local conditions, even supplemented by those stated injectivity/distinctness/nondegeneracy properties, do not force the richness needed for any global supersaturation conclusion. This does not refute source-specific additional hypotheses not supplied to this reviewer.

Review decision: accept the relayed local six-evaluation cancellation; accept that injectivity is unnecessary for that identity; accept the local counterexample with the distinctness qualification above. No headline or global richness conclusion follows from this local check.

## 9. Task ledger and handoff

* **Task ID:** PM-SYNTH-A.
* **Research question:** Can a common operational instrument be proved for the 197 and 107 constructions beyond annihilator language; otherwise, which omitted construction inputs provably block it?
* **Known assumptions:** Finite-field ordinary degree and the source line-sum threshold for 197; complex normalized primitive-root Fourier averaging, bounded integer labels, allowed leg readouts and a nonnegative degree-zero filter for 107. No uninspected headline dependency is assumed proved.
* **Available evidence:** Governing AGENTS/program; evidence manifest and audit; original pinned source text listed in section 2; exact `F_8` barycentric moment computation; relayed independent PM-SYNTH-B local statement.
* **Expected output:** Same-template source comparison, complete proofs or counterexamples, explicit boundaries, scratch note and next operation.
* **Allowed scope:** Read-only ProofMotifs and primary-source retrieval; only `/tmp/pm_synth_a*` files edited, via `apply_patch`; no Git, push, paid calls or external communications.
* **Independence:** Core proposal developed independently before coordinator feedback; no further agents spawned. PM-SYNTH-B review was a later separately labeled cross-review of a relayed statement.
* **Failed hypothesis preserved:** Unary interactions are not necessary for unrestricted coefficient extraction: signed linear `g-h` is an escape. The no-go is restricted to nonnegative weights with desired branches at degree zero. Likewise the bad-hole obstruction is restricted to the stated component degree budget, not all polynomial or nonpolynomial constructions.
* **Stop conditions respected:** No claim of novelty from a missed search; no promotion of source lemmas to upstream headlines; no forced universal theorem; no enumeration substituted for a proof.
* **Handoff:** Coordinator plans independent standard-library certificates and tampering checks, and repository integration under its own ownership. Exact next mathematical operation: specify the final permitted coefficient operation and test minimal local-readout augmentation against the direct polynomial/face-separation baseline; separately determine whether the signed linear alternative preserves the surrounding 107 bridge. New targets must be frozen and exposure-audited before being called held out.

## 10. Follow-up independent audit: tensor stability of integral gradings

The coordinator later proposed the following lemma for independent checking. This section is a new proof pass after the initial proposal; it should not be described as part of the author's independent initial derivation. The lemma is accepted with the hypotheses and boundaries below. It is a standard rational-cone/separation fact, not a historical-novelty claim.

### A-TENS. Exact tensor-stability criterion

Let `Omega` be a finite set, `D` a nonempty subset, and `w:Omega -> Z^r` a vector-valued grading with `w(d)=0` for every `d in D`. The following are equivalent:

1. For every integer `n>=1` and every tuple `(s_1,...,s_n) in Omega^n`, one has `sum_i w(s_i)=0` if and only if every `s_i` lies in `D`.
2. There is no nonzero tuple of nonnegative integer multiplicities `(m_s)_(s in Omega\D)` with `sum_s m_s w(s)=0`.
3. Zero does not belong to `conv_R{w(s):s in Omega\D}`; the convex hull of the empty set is taken to be empty.
4. There is a vector `c in Z^r` such that `c dot w(s)>0` for every `s in Omega\D`.

**Proof, (1) iff (2).** A bad tuple with zero total grading can have all its entries in `D` deleted without changing its total. At least one off-target entry remains. Its repetition counts give the nonnegative integer relation in (2). Conversely, expand any such relation into a tuple containing each off-target branch its specified number of times. Its length is positive and its total grading is zero although none of its entries is desired. The implication “all desired implies sum zero” uses only `w(D)=0`.

**Proof, (2) iff (3).** An integer relation can be divided by its positive total multiplicity to give a convex combination equal to zero. Conversely, suppose zero lies in the finite convex hull. Choose a convex representation with the fewest nonzero coefficients. Its support vectors are affinely independent: otherwise an affine dependence could be added or subtracted in a small amount until some positive coefficient becomes zero, contradicting minimality. There are therefore at most `r+1` support vectors. The barycentric coefficients solve the full-column-rank rational linear system formed by these integer vectors together with the equation that the coefficients sum to one. Select a nonsingular square submatrix; ordinary exact elimination or Cramer's rule shows that the unique coefficients are rational. Clearing a common positive denominator produces a nonzero nonnegative integer relation. This is the step that needs rational/integral weights.

**Proof, (3) implies (4).** If there are no off-target branches, take `c=0` and the condition is vacuous. Otherwise let `K` be the compact convex hull of the off-target vectors. Zero is outside `K`. Let `p in K` minimize Euclidean distance to zero. Then `p!=0`. For every `x in K`, the segment from `p` to `x` lies in `K`; differentiating squared distance along that segment at its initial endpoint gives

`p dot x >= ||p||^2>0`.

Thus `p` strictly separates every off-target vector from zero. There are only finitely many inequalities, so sufficiently close rational approximations to `p` preserve all of them. Multiply such a rational vector by a common positive denominator to obtain the required integer `c`.

**Proof, (4) implies (1).** If a tuple contains an off-target branch, the dot product of its total grading with `c` is a sum of nonnegative integers with at least one positive term; it is strictly positive. Its vector total cannot be zero. A tuple consisting only of desired branches has total zero. QED.

Consequently, every finite integral vector grading with this exact independent-tensor stability can be replaced by a single integral grading `h(s)=c dot w(s)` that is zero on desired branches and strictly positive on all other branches. If the original grading is additive across permitted local readouts, this linear scalarization preserves that locality. It need not preserve a useful quantitative degree bound: the separating integer vector can have large entries. Existence of a positive scalarization is not an optimal-cost algorithm or a new convex-separation theorem.

When the criterion fails, a bad relation needs at most `r+1` distinct off-target grading vectors, by the minimal-support argument above. This bounds the number of *types* in an obstruction, not the tensor length: denominator clearing can require large multiplicities.

### Scalar boundary and exact 107 consequence

For `r=1` and a nonempty off-target set, the criterion is equivalent to all off-target integer weights being strictly positive, or all being strictly negative. A zero off-target weight fails at tensor length one. If positive weight `a` and negative weight `-b` occur, with `a,b>0`, then `b/gcd(a,b)` copies of the first and `a/gcd(a,b)` of the second give a bad zero-sum tuple.

In the valid 107 phase support `S_M`, take `D=D_M` and the signed linear grading `w_0=g-h`. For `M>=3`, the two off-target branches

`(1,2,3,1)` and `(2,1,1,3)`

have grades `-1` and `+1`. Thus their twofold independent tensor product has grade zero and is falsely retained by a single total constant-coefficient extraction. If the ordinary-polynomial shift `w_0+(M-1)` is used instead, desired single branches have grade `M-1`, while this wrong pair has total grade `2(M-1)`, exactly the target degree for the twofold product. The shift therefore does not repair independent-tensor stability.

The source's square grading `(g-h)^2`, in contrast, is zero precisely on desired phase-zero branches and positive elsewhere. A-TENS immediately proves stability under every independent tensor power. This resolves one concrete reason why nonnegative degree-zero filtering carries information that a signed Laurent coefficient projection lacks.

This conclusion requires the product support to include the independent tuples in `S_M^n`. Further coupling, synchronization or an additional filter might exclude the bad tuple. The lemma does not by itself certify which product model the surrounding 107 tensor/complexity argument uses. Also, the statement is structural support exclusion: arbitrary branch coefficients might cancel some survivors, and no numerical nonvanishing of an aggregate coefficient is asserted.

For `M<=2`, `S_M=D_M`, so the criterion is vacuous, consistent with the earlier small-label boundary.

### Rationality, finiteness and empty-off-target boundaries

* **Rational weights suffice.** The entire theorem holds for `w:Omega->Q^r`: multiply all finitely many weights by a common positive denominator. Integer exponents are the natural source application.
* **Arbitrary real weights defeat necessity.** Let `Omega={d,p,n}`, `D={d}`, and scalar weights `w(d)=0`, `w(p)=1`, `w(n)=-sqrt(2)`. Every integer multiset has total zero only if it contains no `p` or `n`, because `a-b sqrt(2)=0` with nonnegative integers forces `a=b=0`. Thus condition (1) holds. Nevertheless no scalar `c`, even real, is positive on both off-target weights. Zero is in their real convex hull, but the unique convex relation uses irrational coefficients and cannot be cleared to integer multiplicities. This shows exactly where the rationality hypothesis enters.
* **Finiteness matters.** Let the off-target integral vectors in `Z^2` be all `(k,1)` for integers `k`, together with `(1,0)`, and include one desired zero vector. There is no nonempty zero-sum off-target multiset: its second coordinate is positive if any `(k,1)` occurs, and otherwise its first coordinate is positive. But any linear functional positive on every `(k,1)` must have first coefficient zero; it then vanishes on `(1,0)`. Thus condition (1) can hold for an infinite integral support with no strict separator. The finite-hull compactness hypothesis cannot be dropped without replacement.
* **All branches desired.** If `Omega=D`, every grading is zero by hypothesis, condition (1) holds, the off-target relation is absent, the convex hull is empty, and condition (4) is vacuous with `c=0`. It is unnecessary to exclude this case. If there are off-target branches but their weights are all zero, all equivalent properties fail at length one.

Follow-up handoff: accept the coordinator's lemma as stated for finite integral/rational gradings. Its immediate value is an exact distinction between tensor-stable zero-face degeneration and a one-shot signed coefficient slice. Any claim about the surrounding 107 application must still check the actual product support and quantitative cost model. Historical novelty and formal verification remain unclaimed.

# PM-SYNTH-B: a source-pinned triangle certificate and its construction obstruction

Date: 2026-10-18. Independent initial mathematical view; task PM-SYNTH-B. Read-only inspection of `/workspace/scratch/415407b3c01b/ProofMotifs` and pinned primary sources. Only this report and `/tmp/pm_synth_b_checks.py` were written, using apply_patch. No Git operations, repository modifications, external communications, or further delegation. This is local mathematical checking, not a build or validation of the headline Hadwiger manuscript.

Task ledger: RESEARCH QUESTION — identify a useful cancellation certificate operation and its actual required construction inputs, particularly in family 157; compare to established mathematics and 197/107. KNOWN ASSUMPTIONS — only the pinned local source equations and explicitly stated fields, symmetries, observable relations and laws; no correctness or novelty of upstream headlines assumed. AVAILABLE EVIDENCE — AGENTS/program, AI_PROOF_EVIDENCE_20261018.md, pinned source manifest, primary source reads listed below. EXPECTED OUTPUT — full local derivation, exact negative controls, classical baseline, next testable operation. ALLOWED SCOPE — read-only repository/source inspection and own `/tmp/pm_synth_b*` files; no Git, repository edits, external messages/payments or further spawn. INDEPENDENCE — initial 157 mathematics derived before reading A's note; later requested A cross-review is separately labeled below. STOP CONDITION — concrete certificate, obstruction and usable next operation, with no grand unification, headline proof or novelty claim. HANDOFF — coordinator owns integration and any repository changes; this report and the exact checker are the deliverables.

## Finding

There is an operational certificate-discovery problem here, but ordinary bounded-degree coefficient elimination already solves it once the legal evaluation grammar and the observable relations have been specified. Family 157 makes the missing input especially explicit: the characteristic, the symmetry action on contractions, and the *plus* observable `a(x_ij)+a(x_ji)` must fit together. Cancellation order or symmetry alone does not determine the surviving observable. A second, stronger obstruction is that even every local algebraic property used in triangle exclusion can hold while the missing-edge relation is empty and the supersaturation conclusion fails maximally.

The useful next operation is therefore to compute the legal evaluation-to-observable map, its attainable residuals, and a dual obstruction inside a declared finite grammar. This is a synthesis/diagnostic procedure using existing mathematics, with no novelty or AI-causality claim.

## B-T1. Parameterized triangle relation; injectivity can be removed locally

Let `k` be a field of characteristic two, `X,V` vector spaces, `a in X*`, and `T:X x X -> k` symmetric bilinear. For three labels `1,2,3`, let `U_i:X -> V` and `u_i in V*` be arbitrary linear maps/functionals. Injectivity is not assumed. Suppose each directed incidence has a witness `x_ij in X` and, for each unordered pair `{i,j}`,

`U_i x_ij = U_j x_ji`,

`u_j U_i = a + T(x_ij, -)` as functionals on all of `X`.

Define the edge observable `c_ij = a(x_ij)+a(x_ji)`. Then

`c_12 + c_23 + c_31 = 0`.

In particular, prescribing `c_ij=1` on all three edges is impossible.

**Proof.** For every permutation `(i,j,k)` of `(1,2,3)`, evaluate the functional identity on `x_ik`:

`u_j U_i x_ik = a(x_ik) + T(x_ij,x_ik)`.

Sum these six identities. For fixed `j`, the left terms have equal arguments by sharing on edge `{i,k}` and therefore sum to zero. For fixed `i`, the two bilinear terms are equal by symmetry and therefore sum to zero. The six remaining linear evaluations sum to `c_12+c_23+c_31`. This proves the relation. No step uses injectivity, finite dimensionality, the special identity `T(x,x)=a(x)`, tensor frames, or a probability law. QED.

The same local hypotheses make the `c=1` relation loopless even without injectivity. Indeed, for a putative loop with witnesses `lambda,lambda'`, put `delta=lambda+lambda'`. Sharing gives `U delta=0`; the two functional identities give `T(delta,-)=0`. Evaluate `uU=a+T(lambda,-)` on `delta`. By symmetry, `T(lambda,delta)=0`, so `a(delta)=0`, contradicting `a(lambda)+a(lambda')=1`.

**Scope.** Removing injectivity here does not remove it from the manuscript's frame/rank arguments. This is a weakening of the local triangle/loop lemma only. The source's loop proof uses injectivity, but its triangle proof already does not.

## B-T2. The six-evaluation scalar template determines the arithmetic obstruction

Declare the following six scalar evaluation rows, indexed by the permutations `(i,j,k)`:

`L_(j;ik) - B_(i;jk) - A_(i;k) = 0`,

where `A_(i;k)=a(x_ik)`, sharing identifies `L_(j;ik)=L_(j;ki)`, and symmetry identifies `B_(i;jk)=B_(i;kj)`. Treat the three surviving `L` symbols, three `B` symbols and six directed `A` symbols as formally independent except for these declared identifications. Ask for all weighted sums of the six rows whose nuisance `L,B` coefficients vanish and whose residual depends only on the three plus-observables

`c_ik=A_(i;k)+A_(k;i)`.

Over a field of characteristic two this certificate space is one-dimensional, generated by the all-ones sum, and its residual is a scalar multiple of `c_12+c_23+c_31`. Over a field of characteristic different from two the certificate space is zero.

**Proof.** Let the row weights be `w_ijk`. Vanishing of each sharing symbol requires

`w_ijk+w_kji=0`;

vanishing of each symmetric bilinear symbol requires

`w_ijk+w_ikj=0`.

The transpositions of positions `(1,3)` and `(2,3)` generate `S_3`. Consequently all six weights equal the sign of their permutation times one parameter `w`. For the residual to depend only on the plus-observable on edge `{i,k}`, the coefficients of `A_(i;k)` and `A_(k;i)` must agree. They are opposite by the first relation, so `2w=0`. In characteristic two the signs coincide and every weight is `w`; in other characteristics `w=0`. QED.

This is a completeness theorem *inside the six-row scalar evaluation grammar*, not a lower bound against all possible proofs. It precisely identifies why replacing a plus-observable by an oriented difference changes the permitted certificate. It also identifies more information than a label such as “bilinear cancellation of order two.”

## B-C1. Full counterexamples when essential hypotheses change

**Odd characteristic.** Let `k` have characteristic other than two, `X=V=k`, `a=id`, `T=0`, every `U_i=id`, every `u_i=a`, and take every witness `x_ij=1/2`. Sharing and both functional identities hold, while `a(x_ij)+a(x_ji)=1` on every pair. Any three labels form a triangle; loops exist too. Thus the characteristic restriction is mathematically essential, not merely a restriction of the certificate search.

**Nonsymmetric bilinear form in characteristic two.** Let `X=F_2^2`, `V=F_2^3`, `a=(0,1)` and

`T(x,y)=x^t [[0,0],[1,1]] y`.

Give the injections by their ordered columns:

`U_1=(e_1,e_2)`, `U_2=(e_3,e_1)`, `U_3=(e_2,e_3)`.

Let `u_1=e_3*`, `u_2=e_2*`, `u_3=e_1*`. The witness table is

| incidence | 12 | 13 | 21 | 23 | 31 | 32 |
| --- | --- | --- | --- | --- | --- | --- |
| witness | (1,0) | (0,1) | (0,1) | (1,0) | (1,0) | (0,1) |

Every sharing identity, full functional identity and parity-one condition holds. Each `U_i` is injective and each `u_iU_i=0`. There is a triangle. The matrix of `T` is nonsymmetric. This example does not retain `T(x,x)=a(x)`; over `F_2`, retaining that diagonal identity for every `x` would itself imply symmetry by polarization, so it cannot be an independent nonsymmetry control.

## B-C2. Triangle exclusion supplies no positive missing-edge density

Even the following stronger collection of local properties does not imply the distribution bottleneck:

`char(k)=2`, `T` symmetric, `T(x,x)=a(x)`, every `U_i` injective, and every `u_iU_i=0`.

Take `k=F_2`, `X=V=F_2`, `a=id`, `T(x,y)=xy`, and, on an arbitrary nonempty finite label set `Omega`, take every `U_i=id` and `u_i=0`. Then

`r(lambda)=a+T(lambda,-)=(1+lambda) id`.

The functional identities for a hole force both witnesses to equal one, whose `a` values sum to zero. There are **no holes at all**. All five listed properties hold. Let `mu` be any probability measure on `Omega` and `sigma=mu^2`; every pair is a unit, and `sigma_1=sigma_2=mu`, `sigma=mu^2` satisfy the source's upper density caps whenever `M>=1` and `2^(DN)>=1`. Nevertheless, the four-cross-hole probability is zero. The sampled graph is `K_m`, whose connected/touching matching number is `floor(m/2)`, far above `m/100` for large `m`.

This refutes a concrete proposed transfer from the cancellation interface to supersaturation. It does **not** refute the source theorem, which imposes the much richer moment/tensor/frame construction and its uniform reference law. Those discarded hypotheses are exactly where positive supply of holes is manufactured.

## The actual second bottleneck in family 157

The source explicitly separates two tasks in `02-geometry.tex`: triangle exclusion makes `alpha(G)<=2`; the tensor/frame construction must additionally force many four-hole conflicts between pairs of units.

The theorem in `03-distributions.tex`, lines 9-20, requires that **every** unit law obeying the marginal caps `sigma_i<=M mu` and joint cap `sigma<=2^(DN)mu^2` gives four-cross-hole probability at least `2^(-100gN)`. Endpoints within one unit may be dependent. It is not enough to verify the product reference law or independent individual vertices.

Conditional on that theorem, the remaining transfer uses known but substantive ingredients: entropy minimizers with full feasible support; a capacitated max-flow terminal cut; deterministic fingerprints deleting conflict neighborhoods; binomial/union bounds on the random sample; and a connected-matching-to-clique-minor counting inequality. These cannot be inferred from the six contractions.

Selected additional source inspection shows what the bottleneck actually contains:

- `03-frame-laws.tex` prepares bounded-minentropy leaf laws by pinning and peeling; its Walsh estimate is the classical character-matrix norm bound `2^(-rank/2)`.
- `05-realization.tex` describes the task as arranging gradient identities on the *whole* cut-profile space and reducing it to `O(n)` cross-Gram prescriptions, with a bounded-rank correction and private-channel capacity.
- `07-phases.tex`, lines 82-116, gives a phase alternative: small nontrivial character means, or a bounded-dimensional tensor cover. The latter can leave only inverse-polynomial compatibility mass, requiring a separate overlap argument.
- `13-rare-overlap.tex`, lines 440-470, combines leaf preparation, positive/rare overlap and collision estimates to get a lower bound `2^(-(56(g-1)+.03)N-o(N))`, which exceeds the required `2^(-100gN)` for large `n`.
- `14-parameters.tex` must select construction constants before the unit law and `n`, preserve rank/channel slack, and compare exponential versus inverse-polynomial scales.

These passages were read as dependency evidence. Their entire proofs were not independently audited or formalized here.

## B-P1. A usable existing synthesis procedure, with a declared completeness boundary

Inputs: a field with exact arithmetic; polynomial equations `f_i=0`; for each equation a finite list `M_i` of allowed multipliers (or a degree bound generating such a list); an explicitly defined target observable polynomial `g`.

Construct the coefficient matrix whose columns are the polynomials `m f_i` for `m in M_i`, using their finite union of monomial supports plus the support of `g`. Solve

`sum_(i,m) lambda_(i,m) m f_i = g`

by coefficient matching. If solvable, the coefficients are a directly checkable certificate that the hypotheses force `g=0`. If not, Gaussian elimination returns a linear functional on the finite coefficient space that vanishes on every available `m f_i` but not on `g`, certifying that no certificate exists **within this grammar**. Enumerating the matrices at successive declared degree bounds discovers certificates when the permitted proof class contains one.

Proof: polynomial equality is coefficient equality, so the first conclusion is exactly the matrix equation. If `g` is not in the finite column span, extend a basis of that span by `g` and define a functional to vanish on the former and take value one on `g`. This proves the second conclusion and gives the elimination algorithm. The dual functional need not correspond to an actual solution of the original equations. Dense elimination is polynomial in the constructed matrix dimensions; those dimensions may grow combinatorially with degree and variable count.

This is the classical bounded-degree Nullstellensatz linear algebra method, not a newly missing theory. Applying it to selected scalar contractions rather than all coordinates can be a useful problem-specific compression, but the compression must be proved faithful for its asserted scope. B-T2 gives such a complete local classification for one declared compression.

Primary prior art inspected: J. A. De Loera, J. Lee, P. Malkin, S. Margulies, *Hilbert's Nullstellensatz and an Algorithm for Proving Combinatorial Infeasibility*, arXiv:0801.3788v1, sections 2 and 3.2. Section 2 searches coefficient certificates by solving linear systems. Theorem 3.5 proves completeness of its symmetry orbit compression when the field characteristic does not divide the symmetry-group order. In the modular case it states only the sound direction for that compression. Thus its Reynolds averaging theorem cannot simply be applied to `S_3` over characteristic two; the full matrix and the direct six-row calculation remain valid. Source: https://arxiv.org/html/0801.3788v1 .

## Comparison with 197 and 107

| family | Input needed before elimination can be useful | Attainable residual | Construction burden not produced by cancellation order |
| --- | --- | --- | --- |
| 157 | Sharing contractions; full functional identities; symmetric `T`; characteristic two; plus-observable on opposite incidences | `c_12+c_23+c_31=0`; parity-one gives contradiction | Rich frame law, gradient realization, overlap/collision bounds, uniform supersaturation over capped dependent unit laws |
| 197 | Full finite-field lines; degree bound on products; interpolation space and the actual evaluations of deleted points; scalar incidence degree | Full sums vanish; deleting an evaluation basis leaves `-I`; regular incidence requires `D(-I)=0` | Constructing suitable holes/regular high-girth lines, group embeddings and character packing |
| 107 | Primitive root with invertible period; no-wrap label bounds; actual phase equation; integral exponents; legal tensor-leg locality of weights | On phase zero, total weight is `(g-h)^2`; its zero degree isolates the diagonal | Choosing legal weights and representation, then the tensor/spectral/growth complexity bridges |

For 197, `03-pairing.tex` proves the polynomial degrees and line sums directly, explicitly credits lower-set Newton interpolation and related coding constructions, and explicitly observes the characteristic-two compatibility of even `D`. The residual `-I` needs interpolation on the deleted-hole evaluation geometry. The zero line sums alone do not prescribe that Gram defect.

For 107, the pinned `SquareWeights.lean` explicitly gives the reduction

`g^2 + hu - h^2 - hv = (g-h)^2 + h [u-v+2(g-h)]`.

The phase relation therefore explains the residual only after a legal decomposition into the three tensor-leg weights has been found. Coefficient matching can recover this identity from the phase, a permitted local polynomial ansatz, and a specified residual shape. Choosing those inputs is separate. The square lives in the ordered integer exponent grading; complex Fourier coefficients are not being ordered.

These are different application interfaces to a known synthesis method. There is no proved transfer here from the triangle obstruction to the polynomial Gram construction or to the square filter.

## Exact computation and next operation

Run `python /tmp/pm_synth_b_checks.py`. This dependency-free exact script checked all equations of the nonsymmetric full triangle example and the odd-characteristic example at characteristics 3,5,7. It also formed the scalar linear systems from B-T2, appended the three parity equations, and computed exact ranks:

| case | coefficient rank | augmented rank |
| --- | --- | --- |
| characteristic 2, symmetric/shared, all c=1 | 8 | 9 |
| characteristic 3,5,7, symmetric/shared, all c=1 | 9 | 9 |
| characteristic 2, symmetry identification removed | 9 | 9 |
| characteristic 2, sharing identification removed | 9 | 9 |
| characteristic 2, c=(1,1,0) | 8 | 8 |

All assertions passed. Consistency of an abstract scalar system is not asserted to prove realization by actual vector data; the two explicit examples separately supply realizations where claimed. The results are not a Lean build.

The ranks also follow without computation. There are nine scalar equations: six evaluations and three edge-observable equations. A row dependence has evaluation weights satisfying the nuisance cancellation conditions in B-T2; cancellation of the directed `A` symbols then forces the edge-row coefficients. Thus the space of row dependencies is one-dimensional in characteristic two and zero in odd characteristic, yielding ranks eight and nine. In characteristic two the sole dependency has right side `c_12+c_23+c_31`, so augmentation increases the rank exactly when this sum is nonzero. Without sharing or symmetry, an uncancelled nuisance symbol forces every evaluation-row coefficient to zero and then every edge-row coefficient to zero, giving rank nine.

Concrete next operation: freeze the six-evaluation grammar; use the full coefficient matrix as the established-method baseline; vary characteristic, sharing/symmetry identifications and observable edge relations; require either an explicit certificate or a dual finite-grammar obstruction. Confirm that deleting injectivity preserves the certificate. Separately reject a proposed transfer to supersaturation using B-C2 unless the input supplies an actual rich frame law and gradient-realization/overlap hypotheses. This is a controlled test of hypothesis preservation and certificate construction, not a held-out mathematical discovery.

## Pinned primary source ledger

All openai/math reads used revision `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.

- `preprints/A-counterexample-to-Hadwigers-conjecture-September-23-2026/build/preamble.tex`, blob `2617c24676b53664b6ccf02c0efc35db1d6756fb`: defines `F=F_2`.
- `.../sections/02-geometry.tex`, blob `615530e1f2e5052afd794b3e0719ce1c28553d23`: complete read, especially the definition and triangle lemma, then tensor/frame construction.
- `.../sections/03-distributions.tex`, blob `e1078d63fdcbcde436a021b5345534b66a66ca36`: complete read; supersaturation statement, entropy/cut/container/sample/minor transfer.
- `.../sections/03-frame-laws.tex`, blob `c047b08e480e2b82816a8d85bd0fcef8585c8341`: selected dependency passages; frame image laws, peeling and Walsh estimates.
- `.../sections/05-realization.tex`, blob `ddc5ff129c59f67d78f06cc142b6f6aa74702475`: selected dependency passages, gradient realization and rank budgets.
- `.../sections/07-phases.tex`, blob `4845f58651baeab8af20a52fc3c7013eaa73b36a`: selected dependency passages, especially lines 82-116.
- `.../sections/13-rare-overlap.tex`, blob `26c5da67411fcf66eb37f93635ad1023cea22ce7`: selected dependency passages, especially completion lines 440-470.
- `.../sections/14-parameters.tex`, blob `2ba5bc5c3c67830677871c6a94b7fe65a22cfebc`: selected dependency passages, construction order and rank/probability scales.
- Family 157 Lean `Main.lean`, blob `0b8b8d46203e289c68f117b10916c28cc0573e23`; `lean/docs/157.md`, blob `20bff8f685912f4bbb837e4c5942e3814ba1bb7d`: scope/dependency reads, not compiled.
- Family 197 pinned `03-pairing.tex` (manifest B07), blob `f77a972f6e99d6c7f312c802b7a5b8b59de5a184`: complete read.
- Family 107 pinned `SquareWeights.lean` (B19), blob `2592d0adba3c73d7d8925262e8e2568c79656c1d`, and `FiniteProjection.lean` (B18), blob `585d246122aebba1c7fec25f180c2fab16e0c92c`: complete local source reads; not compiled.

Canonical links follow the pattern `https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/<full path>`. The short `...` ledger paths above have the same family-157 preprint prefix as the first full entry.

## Separately requested cross-review of PM-SYNTH-A

This section was added after the independent initial report was complete, after reading `/tmp/pm_synth_a_note.md` in full. It is not independent proposal evidence for A's original ideas. The following checks found no material mathematical error in the two requested constructions.

**A197-1 and A197-3.** With `m=|O|` and output dimension exactly `m`, `2d<=q-2` gives full-space Gram sum zero. A punctured residual `-I_m` therefore gives `XX^t=I_m` for the square matrix of hole columns; over any field this forces `X` invertible. Its rows are degree-`d` evaluations, so the evaluation map is onto. Conversely, onto evaluation gives cardinal rows and hence the required Gram identity. No positivity is needed in characteristic two.

For the good holes `{(a_i,0):0<=i<=d} union {(0,1)}`, evaluate `L_i(X)-L_i(0)Y` on each axis point: it gives `delta_ij`; at `(0,1)` it gives zero. `Y` is zero at the axis points and one at the last hole. The components have degree at most `d` provided `d>=1`, which A explicitly assumes. The `d+2` columns are therefore cardinal and have product degree at most `2d`. For the bad collinear holes, restriction has dimension `d+1`; Vandermonde evaluation attains that dimension. The barycentric weights annihilate degrees `0,...,d` by comparing the leading coefficient in Lagrange interpolation on `d+2` nodes. The field-size inequality supplies enough distinct nodes. The same `m`, field, ambient space and degree budgets are held fixed. Both constructions only concern local Gram feasibility, not the regular-incidence/girth hypotheses of the full manuscript.

The equality `output dimension=|O|` is essential for this iff argument. With a smaller output dimension `k`, a rectangular `k`-by-`m` matrix may have `XX^t=I_k` without spanning all hole coordinate functions; surjectivity onto `k^O` is no longer necessary.

**A107-1 and A107-2.** If `s=(g,h,u,v)` has phase zero, `s^R=(h,g,v,u)` also does. Its two singleton-coordinate marginals together with those of `s` agree with the marginals of `(g,g,u,u)` and `(h,h,v,v)`. Thus arbitrary unary additive weights satisfy the exact two-branch trade, and nonnegativity makes both off-target weights zero. For `M>=3`, `(1,2,3,1)` and its reversal are genuinely off target. For `M<=2` there is no off-target phase-zero branch. Total-degree-one polynomials on the allowed readouts `g`, `(h,u)`, `(h,v)` are unary after collecting the two `h` coefficients, so the same obstruction proves degree-one impossibility. The displayed quadratic identity is correct and supplies sufficiency at degree two.

This no-go requires the fixed phase, the nonnegative total ordinary-polynomial grading, and desired terms placed at degree zero. The unary signed Laurent exponent `g-h`, an ordinary polynomial shift with extraction of an interior coefficient, or an additional independent Fourier selector lies outside that model and can separate the desired branches locally. The note already preserves these limits. No claim that the quadratic filter is universally necessary is justified or needed.

Minor completeness note outside the requested core: in A-LOC, if `S\\D` is empty, the statement is trivially true with zero weight; its nearest-point convex-hull proof should either handle that case first or explicitly assume nonempty off-target support. This is a proof presentation edge case, not a false theorem.

Cross-review status: complete elementary independent proof pass for the stated local results; no formal verification, no surrounding complexity bridge audit, and no historical novelty assessment. Coordinator should retain A's original statement qualifications.

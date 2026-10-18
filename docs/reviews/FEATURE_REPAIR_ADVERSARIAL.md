# PM-REPAIR-C: independent adversarial and prior-art audit

Audit date: 18 October 2026 UTC. The clock tool returned 2026-10-18 17:14:40 UTC during the final review. This is an independent AI task-scoped review, not human peer review or formal verification.

## Task ledger

- TASK ID: PM-REPAIR-C.
- RESEARCH QUESTION: Given an explicit finite rational feature matrix A0 on Omega, a nonempty target D, optional feature-row blocks B_j and nonnegative rational block costs, what exact existing algorithms choose minimum-cost blocks admitting a legal weight zero on D and positive elsewhere? Does that selection preserve the stated independent-product operation? What proposed shortcuts or novelty claims fail?
- KNOWN ASSUMPTIONS: Omega finite and explicitly tabulated; D nonempty; rational matrices; selected rows have arbitrary real/rational coefficients with no coefficient bounds; cost charges selected blocks, not discovery/table-generation/inference; extra blocks only enlarge the legal row span; the scalar weight is evaluated on every point of Omega; independent products mean full support Omega^n. The grid family is an ordinary rational/real grid, not a field of characteristic three.
- AVAILABLE EVIDENCE: Read-only repository AGENTS.md, research/RESEARCH_PROGRAM.md, STATUS.md, HANDOFF.md, ROADMAP.md, CLAIMS.md, research/mechanisms/CONSTRUCTION_CONTRACTS.md; later root-provided tools/feature_repair.py, frozen panel/report JSON, and integrated FEATURE_REPAIR.md. Primary literature was retrieved independently through the web tool; exact URLs and theorem locators are below.
- EXPECTED OUTPUT: Independent initial proposal; fatal counterexamples if present; corrected theorem and yes/no certificates; source-specific prior-art boundaries; read-only review of root's algorithm/manuscript; independently replayed panel results; complete temporary audit and scripts.
- ALLOWED SCOPE: Repository read-only; web reading; own /tmp/pm_repair_c* writes only through apply_patch; no repository writes, Git changes, external correspondence, payments or subagents. All work complied.
- INDEPENDENCE REQUIREMENT: Initial theorem/cut proposal and both original-ray counterexamples were derived and sent to root before seeing another agent's mathematics or root's implementation. Later cross-review was explicitly informed by root's supplied design. Independent numerical checking uses Fourier--Motzkin/Farkas elimination, not the root's orthogonal-projection/Gram-KKT oracle. Root code was read but never imported by the independent panel checker.
- CONFIGURATION: Coordinator requested GPT-6.1 Sol / Ultra. This worker cannot independently inspect runtime model metadata; no stronger configuration claim is made.
- STOP CONDITIONS: Stop after precise mathematical/source audit and all supplied panels have independently checkable results. No new direction, source-headline audit, field-orbit search, formalization, or held-out application was authorized.
- HANDOFF: This note plus /tmp/pm_repair_c_exact.py and /tmp/pm_repair_c_panel.py. Coordinator owns acceptance, durable project integration and publication. Small manuscript metadata/terminology corrections are listed below; no repository edit was made here.

## Executive determination

The fixed-stack alternative, adaptive-cut optimum theorem, static-ray counterexamples, and rational-grid degree/mandatory-feature theorem are correct within the displayed hypotheses. The reference code's exact arithmetic and all supplied panel certificates/results pass an independent oracle. This is an operational synthesis baseline using established separation, sparse feature selection and Benders principles; it does not establish a missing general mathematical instrument or historical theorem novelty.

One qualification is required: without an available constant row, the general theorem is homogeneous/conical facial separation. Literal identification with ordinary faces of the convex hull, or with Rauh--Kahle--Ay under their standing assumptions, needs the all-ones vector in the legal row span. All concrete frozen panels do have a constant row in that span. An initially raised date discrepancy was resolved: root reports the user's explicit timezone is Asia/Singapore, where the UTC audit time is already 19 October. Labeling local versus UTC dates removes the ambiguity; the local date is not future-dated.

## C-1. Independent initial theorem and exact certificates

Let O=Omega\D, A=A_J, and a_s its columns. Exactly one of the following exists:

1. A rational c with c^t a_d=0 for d in D and c^t a_o>=1 for o in O.
2. A rational z with Az=0, z_o>=0 for o in O, and sum_O z_o=1; target coefficients z_d may have either sign.

Proof: Let T=span{a_d:d in D}, and project rationally onto T-perpendicular. Call the projected off-target columns b_o. A legal c is a functional on that quotient strictly positive on every b_o. If zero is outside their convex hull, strict separation gives such a functional; perturbing in the rational target-annihilator subspace and scaling gives a rational unit-margin solution. If zero is in the hull, rational convex coefficients lambda lift to sum_O lambda_o a_o in T; expressing this vector using target columns gives z. Pairing c with Az rules out coexistence. If O is empty, c=0 works and normalization forbids a trade.

For actual exact computation a feasible rational primal vector is a YES certificate; a normalized rational trade is a NO certificate. Clearing a common denominator of the evaluated scalar weights W_s, rather than just the entries of c, makes the weights integral. Their nonnegative sum is zero exactly when every factor is in D, for every independent product length.

Useful boundaries:

- Target coefficients must remain unrestricted in sign. Ordinary separation of conv(D) from conv(O) does not express the zero-target contract. For columns a_d1=(1,0), a_d2=(1,1), a_o=(1,2), these two convex hulls are disjoint, but no legal c can vanish on both target columns and be positive at o. The trade (1,-2,1) certifies failure.
- The quotient is by the target column span, not merely by their convex hull. With a constant row it is equivalent to the appropriate affine-hull quotient, but convex-hull disjointness remains insufficient.
- For A=[1,2] and D={first column}, D is a vertex of conv{1,2}, but no homogeneous linear functional is zero at 1 and positive at 2. Adding a constant would change the authorized row space and cannot be treated as harmless in the general contract.
- Coincidence of selected columns between an outside point and a target is an obstruction, but distinct columns alone do not imply existence; convex/signed dependencies matter.
- Full independent support is required for the converse all-product theorem for arbitrary integral multigradings. A nonnegative scalar selector remains sufficient on any restricted/coupled product support; coupling can make it unnecessary. This result makes no tensor-rank or asymptotic-complexity conclusion.
- All claims here are support-level statements. Cancellation of numerical coefficients in a particular polynomial/tensor is a different contract.

## C-2. Correct costed-repair theorem and its limits

Define the normalized base trade polyhedron

    P0 = {z : A0 z=0, z_O>=0, sum_O z_O=1}.

A selected set J is feasible exactly when

    P0 intersect (intersection over j in J of ker B_j) = empty.

Equivalently it must meet every detection set K(z)={j:B_jz!=0}, for all z in P0. This is an exact hitting formulation over all base trades, not merely over the original extreme rays or original circuit vectors. There may be infinitely many trades, but at most 2^p different detection sets; this does not imply an efficient enumeration.

At a failing incumbent J, obtain any current rational trade z. Every feasible repair must satisfy

    sum_{j in K(z)} x_j >= 1.

If it did not, the same z would annihilate its entire feature stack and disprove feasibility. Selected incumbent blocks already annihilate z, so the cut excludes the incumbent. With an exact cheapest-mask master, the first primal success attains a lower bound valid for every repair and is optimal. At most 2^p distinct incumbent masks are queried, plus an optional full-dictionary precheck. The full-stack trade, when present, is a universal impossibility certificate for all subsets. A full-stack feasible selector settles dictionary existence in one call; subset search is for cost, not existence.

Global optimality needs exact verification of the binary master's lower bound, as well as all local trade/primal checks. Enumerating masks consistent with the cuts is a valid, potentially exponential verifier. Local certificate verification does not make sparse optimization polynomial-time or supply a guaranteed short optimality proof.

### Weighted-set-cover subcase

Given a universe U and sets S_j, set Omega={d} union U, D={d}, A0=ones, and let B_j be the 0/1 indicator row of S_j, zero at d. A selected family admits a selector iff it covers U. A cover's summed indicator rows give a selector; an uncovered u has the same selected feature column as d and is impossible. Costs are preserved exactly. This proves weighted set cover is a subcase; minimum repair is NP-hard even with one 0/1 row per block and a singleton target.

For explicitly encoded rational input the decision version is in NP: a mask and a polynomial-bit rational feasible solution suffice. A minimal-support nonnegative solution after splitting free variables has linearly independent columns, so Cramer's determinant bounds give polynomial bit length. Thus the decision version is NP-complete. No approximation ratio, parameterized improvement or general practical speedup is established here.

### Coefficient/encoding boundary

No fixed arbitrary big-M is justified by feasibility. For A0=(1,1), D={first}, and B=(0,1/1024), a unit-margin selector needs feature coefficient at least 1024. More generally feature value 2^-L requires coefficient at least 2^L, although its input encoding has O(L) bits. A sound MIP must use valid data-dependent bounds or indicator/disjunctive formulations; adding coefficient bounds changes the theorem. The explicit Omega table can itself be exponentially large in a succinct source description. Costs must not silently stand in for degree, period, physical readout count or coefficient bit complexity.

## C-3. Fatal shortcut: original extreme trades can cancel after repair

The following was independently derived before root code was supplied.

Take Omega=(d,p,q), D={d}, A0=(1,1,1). The original pointed bad-trade cone has extreme rays

    r1=(-1,1,0), r2=(-1,0,1).

The additional row B=(0,1,-1) has Br1=1 and Br2=-1, so it individually breaks every original extreme ray (and every original circuit vector). Nevertheless r1+r2=(-2,1,1) is annihilated by both A0 and B. The normalized trade (-1,1/2,1/2) survives. No cB can be strictly positive at both outside points. Killing all original ray vectors is therefore not enough.

The failure also occurs for whole categorical one-hot blocks, with no negative feature entries. Order the columns (d1,d2,p,q), take D={d1,d2}, and use

    A0 = [[1,0,1,0], [0,1,0,1]],
    B  = [[1,0,0,1], [0,1,1,0]].

The original cone is {(-a,-b,a,b):a,b>=0}, so it is pointed with rays (-1,0,1,0) and (0,-1,0,1). Their B-images are opposite nonzero vectors. Their sum, and hence the normalized trade (-1/2,-1/2,1/2,1/2), survives. This is the diagonal/off-diagonal 2x2 marginal trade. It excludes any interpretation of the failure as an artifact of artificial signed features.

The corrected theorem is the entire-cone intersection/current-matrix circuit condition in C-2. Original circuits suffice to characterize the original faciality problem, but intersections with added kernels can create new current circuits that are combinations of them. Adaptive rechecking is essential unless an additional special sign condition prevents all such cancellations.

## C-4. Source-specific nearest primary theory

The following are actual inspected primary materials, not claims inferred solely from search snippets.

### Facial sets and signed trades

Johannes Rauh, Thomas Kahle and Nihat Ay, *Support Sets in Exponential Families and Oriented Matroid Theory*, arXiv:0906.5462v2, 16 September 2011.

- Actual PDF: https://arxiv.org/pdf/0906.5462
- Standing all-ones-row-span assumption: PDF p4, immediately before Remark 2.
- Definition 6: PDF p5, exactly zero on F and at least one off F.
- Lemma 7: PDF pp5--6, signed-kernel criterion for facial sets.
- Proposition 34: PDF p22, circuit/face criterion.
- Retrieved references: turn176view0; targeted passages turn177view3/4 and turn181view0.

Mapping: with a constant in row span, fixed-stack feasibility is precisely their facial-set problem. Our normalized trade is a one-sided-off-target signed dependence. General matrices without a constant are handled by the homogeneous alternative directly, or by the appropriate cone interpretation, not by silently changing the feature space. Their circuit reduction does not justify static original-circuit hitting after rows are added.

### Inference cuts and finite-master optimality

J.N. Hooker and G. Ottosson, *Logic-based Benders decomposition*, Mathematical Programming, Series A 96 (2003), 33--60; DOI 10.1007/s10107-003-0375-9.

- Actual author manuscript: https://johnhooker.tepper.cmu.edu/benders2.pdf ; title page says November 1995, revised November 2000.
- Author publication index: https://johnhooker.tepper.cmu.edu/papers.html links that manuscript and records final publication.
- Independently verified publisher metadata: https://link.springer.com/article/10.1007/s10107-003-0375-9 ; issue April 2003, published online 21 March 2003.
- Manuscript Section 5, Theorem 1: valid-cut correctness; Theorem 2: finite master-domain termination.
- Retrieved references: turn181view3, turn182view2/4/5, turn209view0.

Mapping: block masks are the finite master decisions; fixed-stack separation is the subproblem; a trade supplies a proof of infeasibility; K(z) records exactly the master changes under which that proof ceases to apply. This is an inference/Benders feasibility cut. The proof pattern and finite-domain termination are established, not a new optimization principle.

### Explicit sparse/costed feature selection

P.S. Bradley, O.L. Mangasarian and W.N. Street, *Feature Selection via Mathematical Programming*, INFORMS Journal on Computing 10(2) (1998), 209--217; DOI 10.1287/ijoc.10.2.209.

- Direct publisher abstract and metadata inspected: https://pubsonline.informs.org/doi/10.1287/ijoc.10.2.209 ; retrieved turn210view0.
- The abstract expressly formulates separating-plane selection using as few features as possible as a mathematical program with linear constraints. No claim is made here to have read its complete paywalled article or certified every algorithm in it.

Sebastian Maldonado, Juan Perez, Richard Weber and Martine Labbe, *Feature selection for Support Vector Machines via Mixed Integer Linear Programming*, Information Sciences 279 (2014), 163--175; DOI 10.1016/j.ins.2014.03.110.

- Actual primary full PDF: https://repositorio.uchile.cl/bitstream/2250/126859/1/Feature-selection-for-Support-Vector-Machines-via-Mixed-Integer-Linear-Programming.pdf
- Section 3 and equation (9), article pp166--167: per-attribute binary indicators, acquisition costs, budget, and conditional coefficient intervals.
- Retrieved references: turn190view0, turn191view0.

Mapping: sparse representation choice with a linear classifier, binary feature switches and costs predates this proposal. Their classification losses/margins and specified coefficient intervals are not identical to exact-zero target faces. Grouped blocks and the precise facial objective should be described as the present specialization, not as a newly invented selection principle. Their interval constraints are a reason to state coefficient-bound assumptions explicitly.

### Purely combinatorial Benders cuts

Gianni Codato and Matteo Fischetti, *Combinatorial Benders' Cuts for Mixed-Integer Linear Programming*, Operations Research 54(4) (2006), 756--766; DOI 10.1287/opre.1060.0286.

- Primary publisher abstract inspected: https://pubsonline.informs.org/doi/10.1287/opre.1060.0286 ; retrieved turn190view1.
- It describes an integer master, LP validation subproblem, and combinatorial inequalities distilled from infeasible subsystems without relying on big-M values. Full text was not obtained here.

Mapping: this strengthens the assessment that a binary master with exact LP failure feedback is an established architecture. The specific trade-detection cut has a direct proof in C-2; no claim of literal identity to every Codato--Fischetti cut is needed.

### Tensor-support selection and actual synthesis, not just feasibility

Matthias Christandl, Omar Fawzi, Hoang Ta and Jeroen Zuiddam, *Larger Corner-Free Sets from Combinatorial Degenerations*, ITCS 2022, LIPIcs 215, 48:1--48:20; DOI 10.4230/LIPIcs.ITCS.2022.48.

- Actual primary proceedings PDF: https://drops.dagstuhl.de/storage/00lipics/lipics-vol215-itcs2022/LIPIcs.ITCS.2022.48/LIPIcs.ITCS.2022.48.pdf
- Section 2.3, Definition 21, p48:12: integer coordinate-readout weights summing to zero on target support and strictly positive on its complement.
- Same Section, equation (1), p48:13: integer programming explicitly constructs these degenerations, using binary target-vertex indicators and integer local weights.
- Retrieved references: turn190view2, turn191view4, turn192view0. HTML arXiv version https://arxiv.org/html/2111.08262v1 has the integer program numbered (3), not (1).

Mapping: with one-hot coordinate readouts, this is exactly the additive positive zero-target selector contract. Their optimization selects retained diagonal vertices under fixed readouts, whereas this task fixes D and pays for optional readout blocks. Thus it is direct primary evidence that existing methods synthesize composition-compatible selection weights, but not a claim that their optimization problem is identical. Their stated large-M assumption must not be imported as an arbitrary numerical bound.

Historical limit: this paper attributes the concept to Strassen and to Burgisser--Clausen--Shokrollahi. Their original full texts were not inspected in this task; the direct prior-art comparison rests on the actually read 2022 definition/program, not an unsupported priority reconstruction. A fresh Gordan scan request also failed through the web tool; its theorem was not newly source-audited here. The repo's earlier Gordan audit remains separate evidence.

## C-5. Independent check of root's new grid family

Root supplied this family only after the independent initial proposal/counterexamples. It is therefore cross-review, not an independently proposed family or a held-out test.

For r>=1, Omega={-1,0,1}^r and D={s:some s_i=0}. Put b(-1)=b(1)=1 and b(0)=-2. The tensor trade

    z(s)=2^-r product_i b(s_i)

has z_O=2^-r and sum_O z_O=1. The moments for powers 0,1,2 are 0,0,2. Every monomial of total degree less than 2r has some coordinate exponent 0 or 1, so it is annihilated even if another coordinate exponent exceeds 2. Hence a polynomial positive on O and zero on D cannot have degree below 2r. The product of coordinate squares attains the bound.

The stronger reduced-dictionary claim is also valid. Reduce by x_i^3-x_i without increasing degree. Finite-grid interpolation gives a unique representative with all exponents in {0,1,2}. Vanishing on each zero-coordinate slice forces every surviving monomial to include every variable. Uniform averaging over the sign cube O then kills every such monomial except product_i x_i^2. Therefore its coefficient is the positive average of W on O, and is strictly positive. The top reduced-monomial feature cannot be replaced by any selection of the other reduced monomials.

This is a tensor second-difference/leading-coefficient interpolation argument, a classical mechanism. There are 3^r dictionary monomials and 3^r points; the complete feature-evaluation matrix has 9^r entries (and the coordinate list has r*3^r entries). It is not an efficient general-purpose high-order discovery theorem, a characteristic-three statement, or an external unread target.

## C-6. Read-only implementation audit

Inspected tools/feature_repair.py with SHA256 e282773688db1ba4a14387c9fe829834e09c19d17da63d06d1d3463a7d09807d.

The root oracle forms rational orthogonal projections off the target-column span. It enumerates candidate affine-independent hull supports, solves their Gram KKT systems over Fraction, checks nonnegative barycentric coefficients, and verifies the global supporting inequality p.b_o>=p.p. A nonzero p gives c=p/(p.p); a zero p gives a convex combination lifted into a signed target trade. Affine independence makes the bordered KKT matrix invertible; a closest hull point always has such a support of size at most ambient dimension plus one. Thus the finite enumeration is complete. Global supporting inequalities prevent acceptance of a merely local-face closest point.

The code correctly clears denominators of evaluated weights, not just coefficients. It directly validates all returned selector/trade certificates. The full-stack impossibility check is monotonic. Cut masks are computed using whole block vectors, and the master only accepts masks satisfying every cut. Sorting all masks by exact rational cost and then mask index makes each incumbent a globally cheapest survivor. Exact oracle-call counters count the full-stack precheck and actual repeated final queries; mask-scan counts are separate. No code correctness issue was found in the declared valid-input contract.

The reference is exponential both in its binary master and potentially in its convex-hull oracle. The adaptive and exhaustive root baselines share the same oracle, so their agreement alone is not independent verification. The separate checker below removes that limitation for these panels. General software hardening, malformed-input handling, floating-point JSON conventions, and production-scale exact LP performance were not audited or claimed.

## C-7. Independent exact computations and actual successful commands

All authored files were created using apply_patch. Both scripts use Python standard-library Fraction arithmetic only, perform no repository writes, and print results without writing JSON files.

Successful command:

    PYTHONDONTWRITEBYTECODE=1 python3 /tmp/pm_repair_c_exact.py

This first script implements tracked rational Fourier--Motzkin directly in the original coefficient space. It produces exact primal coefficients or exact Farkas trades, tests both independently derived ray failures, performs an adaptive repair demonstration, checks all eight masks of a three-block cover example, checks the 1/1024 coefficient-scale boundary, and directly evaluates all grid/monomial moments in dimensions 1 through 4. Grid point/monomial counts are 3,9,27,81 respectively, with the sole surviving top moment 2^r. All assertions passed.

Successful command:

    PYTHONDONTWRITEBYTECODE=1 python3 /tmp/pm_repair_c_panel.py

This second script independently removes target equalities by rational row reduction, constructs a target-annihilator basis, and uses tracked exact Fourier--Motzkin on the resulting inequalities. It recovers signed target coefficients for failure certificates. It does not import or execute tools/feature_repair.py. It independently constructs the two grid panels from the stated dictionary rather than importing root's grid factory.

For every supplied panel it replays each stored current trade, recomputes every detection/cut mask, verifies the incumbent is the cheapest mask satisfying all earlier cuts, validates the final primal or full-stack failure, checks selected names/costs, and queries its independent oracle on every possible mask, not only up to the optimum.

| Panel | All masks independently checked | Feasible masks | Stored certificates replayed | Adaptive cuts replayed | Independent result |
| --- | ---: | ---: | ---: | ---: | --- |
| signed-repair | 4 | 1 | 3 | 2 | mask3, cost3, both blocks |
| categorical-rays | 2 | 0 | 1 | 0 | dictionary impossible |
| weighted-cover | 32 | 11 | 6 | 5 | mask14, blocks b,c,d, cost5 |
| coordinate-zero-union | 64 | 32 | 14 | 13 | mask32, top monomial only, cost5 |
| coordinate-zero-union-without-top | 32 | 0 | 1 | 0 | dictionary impossible |
| Total | 134 | 44 | 25 | 20 | all assertions passed |

The root report's oracle counts 4/1/7/15/1 and exhaustive counts 4/2/12/33/32 were inspected. The independent checker establishes the optimum/failure and replays the certificates/cuts; it does not treat matching root oracle-call counts as a mathematical performance theorem.

Audited input snapshots before the requested local/UTC date clarification:

- panel JSON SHA256: 80e6bc9a1b7e342b304f27539e9a0128846c1c636af775061bb5775d6cfd8ab9.
- report JSON SHA256: ccc54941da2b3b5d2161ed4b5fd22d70aca9fc9594a475c18ea0b1b26495c429.
- integrated draft SHA256: 2dc98b45ceffdc008dc0c3edd7e372b67db85a24d64e9a37658b77f1955342ff.
- independent original checker SHA256: 390454ae3affddd23286de4229c426ebe8381196a3b85211d1dcd4440ee843c0.
- independent panel checker SHA256: f5d3ac784702a4246d8528832db876e8cdbfaca7db91689bfc155f3ea36c3ca0.

These hashes identify actual inspected versions, not an assertion that root's files will remain unchanged after integration. Root should recompute final hashes after metadata/terminology changes and rerun the checker if mathematical input changes.

## C-7b. Additional classical bounded-MILP baseline, separately cross-reviewed

After the initial complete audit, root supplied an additional proposed lemma from another researcher. It was independently checked here before acceptance; it was not part of this worker's initial proposal.

First clear each row's rational denominators in the full dictionary. This preserves every selected row span and its block cost. Suppose the resulting full integer matrix has R>=1 rows and entries of absolute value at most H>=1. For every feasible mask with O nonempty, there are integer coefficients on the available **integralized rows**, zero on all unavailable rows, whose absolute values are at most

    M = R! * H^(R-1),

and whose evaluated weights are zero on D and at least one on O.

Proof: Choose q linearly independent available feature rows spanning the selected row space. The unit-margin coefficient polyhedron in R^q is nonempty. Its lineality is ker(A^t)=0 because these rows are independent; hence it is pointed and has a vertex. At a vertex choose q linearly independent active constraints, including target equalities as needed. Their coefficient matrix is integral with entries bounded by H and their right-hand sides lie in {0,1}. Cramer's rule gives rational vertex coefficients. Multiply by the absolute determinant to obtain integer coefficients. Expansion of each numerator determinant along its {0,1} replacement column bounds it by q*(q-1)!*H^(q-1)=q!*H^(q-1). The positive scaling preserves all zero equalities and makes each outside weight at least the positive integer determinant magnitude. Set unused basis-complement coefficients to zero. Since q<=R and H>=1, the claimed M follows.

If O is empty, use c=0. If R=0 and O is nonempty, no selector exists. The logarithmic bit length of M is O(R log R + R log H), and rowwise common-denominator clearing has polynomial bit complexity in explicit rational input. Thus this is a complete finite bound, not an arbitrary guessed M, and not a polynomial-time optimization result.

One exact bounded MILP is therefore complete: integer row coefficients, binary block switches x_j, equations W_D=0, inequalities W_O>=1, coefficient bounds |c_i|<=M on base rows and -M*x_j<=c_i<=M*x_j on rows in block j, and objective sum cost_j*x_j. The coefficients could alternatively be continuous with the same valid bound without changing the feasible mask family, since an integral bounded witness exists whenever any witness exists. Solving either version can still require exponential time.

Important qualification: M is a bound for the **scaled** integer features. If original row a_i is replaced by L_i*a_i, a bounded integralized coefficient tilde_c_i corresponds to original coefficient L_i*tilde_c_i. Do not claim the same M for the original rational rows. The earlier (0,1/1024) example exhibits this distinction.

Successful additional independent command:

    PYTHONDONTWRITEBYTECODE=1 python3 /tmp/pm_repair_c_bound.py

This checks every 1-by-3 and 2-by-3 matrix with entries in {-1,0,1}, target the first point: 27+729=756 matrices in total. A target-nullspace/Fourier--Motzkin feasibility oracle is compared with separately enumerated active-constraint vertices and integerized coefficient bounds. Exactly 2 and 200 matrices respectively are feasible. All feasibility/bound assertions pass. The two-row matrix [[0,1,-1],[0,0,1]] has unit-margin requirements c1>=1 and c2-c1>=1; its integer vertex (1,2) attains M=2. These finite checks corroborate the Cramer proof; they are not a universal exhaustive test.

Disposition: ACCEPT as a classical Cramer/basic-feasible-solution bound and complete existing-MILP baseline, with the scaled-row qualification. It further narrows, rather than supports, a missing-general-optimizer claim. No new bounded-MIP theorem or historical priority is established by this elementary application.

## C-8. Manuscript disposition, objections and novelty gate

- PM-REPAIR-0001: ACCEPT within finite rational, arbitrary coefficient, exact zero-target contract. Add the constant-row/conical-facial qualification. Rational perturbation should be understood within the target-annihilator subspace. Integralize evaluated weights. Those latter two points are already mathematically respected in code/draft.
- PM-REPAIR-0002: ACCEPT. The exact full-cone trade cut is valid and adaptive cheapest-mask success proves optimum. Weighted set cover embeds exactly; decision NP-completeness follows. No new Benders theorem or polynomial sparse optimizer is established.
- PM-REPAIR-0003: ACCEPT. Both signed and categorical examples genuinely defeat static original extreme-ray/circuit-vector hitting. The categorical example eliminates the signed-feature escape objection.
- PM-REPAIR-0004: ACCEPT. Both degree2r and top reduced-monomial necessity hold for ordinary rational/real grids in every r>=1. The method is tensor finite differences/interpolation; no novelty credit beyond a checked calibration/application is justified by this audit.
- Additional proposed Cramer/bounded-MILP baseline: ACCEPT with coefficients interpreted on integralized feature rows, as proved and checked in C-7b.
- Reference code/panels: ACCEPT the mathematical implementation and all five exact results. Complete supplied panel space was checked with a distinct exact oracle. This is finite corroboration, not a universal code-verification theorem or formal proof.
- Prior art: The inspected sources already provide the underlying facial criterion, sparse-feature optimization, finite inference/Benders architecture, and explicit integer-program synthesis of additive combinatorial degenerations. Minimum costed optional-block repair is a useful precise formulation, but it has not passed a historical-new-method gate.
- Missing universal-tool claim: NOT ESTABLISHED. A genuine further result would need structural compression, automatic useful dictionary/auxiliary-object generation, a restricted-model complexity gain, or a preregistered unread transfer with equal-input existing-method baselines. This task does not supply one.
- Verification label: MANUAL MATHEMATICAL REVIEW plus INDEPENDENT EXACT FINITE CHECKS. Formalization NOT_STARTED. No human review, source headline certification, causal AI explanation, or held-out success is claimed.

Stop condition met. Handoff to coordinator for final wording/metadata correction, persistence of these checks, and the central-program decision. No further action is being undertaken by this worker.

# PM-REPAIR-B — exact dictionary repair, independent certificates, and limits

Date: 18 October 2026. Task-scoped independent mathematical development; coordinator integration is outstanding. Repository was read-only throughout. Read `AGENTS.md`, `research/RESEARCH_PROGRAM.md`, and `research/mechanisms/CONSTRUCTION_CONTRACTS.md`; no other agents' temporary notes were read. Repository HEAD observed: `5a70bf8d8b5105d9eb08a4df2eb0dc1be2be4e7c`, clean worktree at that observation. Actual runtime identity available to this agent does not independently expose the model/effort configuration; the requested configuration in the assignment is not a verification of it.

## Outcome

There is a complete exact bounded-dictionary representation-selection method, not merely coefficient recovery after supplying a residual. It selects minimum-cost optional feature blocks, returns a rational nonnegative scalar defect with zero set exactly D, and returns valid dual trade cuts establishing the lower bound. It uses ordinary facial-set feasibility plus binary feature selection/Benders reasoning. These are established techniques; this is an operational synthesis and exact implementation, not evidence for a missing mathematical theory or historical novelty.

The principal independent additions useful for integration are:

1. A full certificate-size argument, an explicit uniform coefficient bound making the conventional MILP baseline exact, and a warning/counterexample against killing only the initial obstruction circuits.
2. A separately frozen, newly designed sparse-monomial calibration instance, with a different target from the old four-variable phase graph. Minimum repair cost is 4, rising to 9 under the frozen feature-deletion control. An odd-only grammar is impossible. Exact adaptive-cut search used 20 and 142 oracle calls respectively: exactly the same counts as the cost-ordered exhaustive baseline. There is **no demonstrated search advantage** on these tests.
3. A stand-alone certificate checker with no imports from the discovery code and no optimization subroutine. It verifies all 180 dual cuts, both primal constructions, and exhaustive master optimality. A second, special-family lower bound reproduces both optima without those cuts.
4. Independent proof/checks of the coordinator's marked-coordinate grid family, including the sharp nonnegative degree 2r versus signed degree r distinction and a bad signed product of length two.

External held-out transfer remains outstanding. The new sparse-polynomial instance is **designed calibration**, not externally sourced or blinded held-out mathematics. During design, alternating zero-pattern/root-count structure was already contemplated; only its concrete costed dictionary and optimization instance were frozen before solving. It must not be marketed as an unseen natural-problem transfer.

## Inputs and contract

Let Omega be a finite set with n points, let D be a designated subset, and put O=Omega\D. Supply rational-valued base features F_0 and m rational-valued optional blocks F_1,...,F_m. Each F_j is an evaluation matrix whose rows are the points of Omega. Selecting a set B of blocks permits exactly the linear span of columns of

    F_B = [F_0 | F_j, j in B].

Column copies are allowed, so overlapping blocks are harmless. Costs c_j are nonnegative rationals. The required output is B and rational a such that

    F_B(d,:) a = 0                (d in D),
    F_B(s,:) a >= 1               (s in O).

Minimize sum_{j in B} c_j; deterministic cardinality/bitmask tie-breaking is optional. The threshold 1 loses nothing: a finite positive off-target weight can be scaled by the reciprocal of its minimum positive value. When O is empty, a=0 and a minimum-cost legal empty selection work. No assumption that a constant feature is present is needed for the algebra below. The usual *polytope face* terminology uses the additional constant-coordinate hypothesis; without it the same homogeneous separation system still applies.

The input includes the candidate dictionary, not a prescribed square, polynomial factorization, phase, residual, or desired coefficient vector. This closes the bounded feature-selection operation. It does not discover features outside that dictionary. New auxiliary-variable maps can be covered only after their legal evaluation tables and costs are explicitly supplied. A phase that changes the support Omega, or a nonlinear composition of representations, is not automatically an optional column block.

### PM-RB-001: exact primal/dual alternative with short rational witnesses

For any fixed B, exactly one of the following exists:

* Primal a satisfying the displayed equalities/inequalities.
* Dual z in Q^Omega with

      z_s >= 0 (s in O),  sum_{s in O} z_s = 1,  F_B^T z = 0.

The entries z_d for d in D may have either sign. A dual witness can be chosen with at most r+1 nonzero entries, where r=rank(F_B). More precisely it needs at most r-t+1 off-target entries and t target entries, where t is the rank of the target rows of F_B.

Proof. First discard dependent feature columns without changing their function span, leaving n-by-r matrix A with independent columns. Write T for the span of its target row vectors. Choose a rational basis N for the coefficient-space kernel of the target rows. This basis has k=r-t vectors. Let q_s=A(s,:)N in Q^k for s in O. A coefficient vector satisfying target vanishing is N b, and the primal is exactly

    q_s b >= 1 for all s in O.

The q_s span Q^k, since all rows of A span Q^r. If 0 does not belong to their convex hull, strict separation from the origin gives b with every q_s b positive, then scaling gives the inequalities. Conversely, if 0=sum_s y_s q_s with y>=0 and sum y=1, their inequalities would imply 0>=1. Finite rational linear systems have rational solutions here; an elementary rational construction is given below. This proves the alternative by ordinary finite-dimensional convex separation.

For the dual, choose an inclusion-minimal convex representation of 0. Its augmented vectors (q_s,1) are linearly independent: otherwise an affine dependence permits perturbing the positive coefficients until one becomes zero. Thus at most k+1 off-target points are needed. The vector -sum_s y_s A(s,:) annihilates N, so belongs to T. Express it using t independent target rows. Taking these target coefficients as z_d and taking z_s=y_s gives A^T z=0. Column-span preservation gives F_B^T z=0. There are at most (k+1)+t=r+1 nonzero entries. The augmented linear systems have rational coefficients and unique solutions on their chosen supports, hence rational solutions. Mutual exclusion also follows directly: z^T F_B a is both zero and at least 1. QED.

The dual is an equality of signed feature moments, sometimes a balanced trade if a constant column is present. Nonnegativity is imposed only off target, not on the target coefficients. Requiring the latter to all have one sign would incorrectly exclude valid infeasibility certificates in the general contract.

### Exact elementary oracle and its cost

This implementation deliberately uses no floating-point LP and no third-party optimizer.

1. Remove dependent feature columns by rational elimination and compute N and q_s as above.
2. For each k-element off-target subset I, solve q_i b=1 for i in I if this is a nonsingular system. Check all inequalities. A passing candidate is a primal witness.
3. If none passes, enumerate off-target subsets of sizes 1 through k+1. Solve sum y_s q_s=0 and sum y_s=1, demanding a unique solution with every selected y_s>0. Recover the target coefficients from t independent target rows and verify the original matrix identity.

Completeness of step 2 does not require boundedness of the feasible polyhedron. Because q_s span Q^k, this polyhedron has no line. Starting at any feasible b, if its active rows span a proper subspace, choose a nonzero direction annihilating those rows. Some inactive row has nonzero derivative; choose the direction's sign so some derivative is negative. Move to the first inactive inequality reached. Its row is independent of the previous active rows, since its derivative is nonzero. Repeat to obtain k independent active rows. Thus a feasible point with k active independent inequalities exists. Step 3 is complete by the minimal convex representation in PM-RB-001. The cases k=0 and O empty are treated explicitly by the code.

Let h=|O|. The number of candidate linear systems is at most

    binom(h,k) + sum_{i=1}^{min(k+1,h)} binom(h,i) <= 2^(h+1).

Each is solved and checked by exact rational elimination and matrix multiplication. A deliberately loose bound is O(2^h (n+p)^4) rational arithmetic operations per architecture, with p its supplied column count; rank reduction is included. This is not a polynomial-time LP implementation and is not proposed to beat exact LP. Its benefit here is transparent, dependency-free reproducibility on small instances.

### Rational bit-size and uniform coefficient bound

Clear a common denominator L of the full evaluation matrix and write F'=L F, with all integer entries of absolute value at most H>=1. The binary length of L and log H is polynomial in the explicitly encoded rational input length. For an architecture of rank r, use independent feature columns as above and t target equations together with k independent active off-target equations. Their r-by-r matrix is nonsingular, integer, bounded by H, and their right-hand side entries are 0 or 1. Cramer's rule gives numerator and denominator bounds

    Delta_r = r! H^r

for the resulting coefficients in F'. Unused feature coefficients can be set to zero. For the original F, multiply these coefficients by L; their absolute values are at most L Delta_r. Integer clearing of the resulting rational weight is therefore effective, with polynomial certificate bit length.

For the dual support of size at most r+1, the equations F'^T z=0 plus off-target normalization have an independent square subsystem. Independence follows from affine independence of the selected quotient points together with independence of the chosen target rows. Its entries are bounded by H or 1 and its right-hand side by 1. Thus dual numerators/denominators can be bounded by (r+1)! H^(r+1). This also gives polynomial witness bit length. The support-size statement does not claim that all optimality proofs over feature subsets are polynomial size.

### PM-RB-002: adaptive obstruction-cut repair is exact

For any dual z annihilating the base, define its killed-by block set

    K(z) = {j : F_j^T z is not the zero vector}.

Every feasible architecture B obeys B intersect K(z) nonempty. Otherwise z annihilates all its permitted features and contradicts the primal by PM-RB-001.

Algorithm. Start with no cuts. Solve the binary master problem minimizing cost subject to

    sum_{j in K(z_i)} x_j >= 1

for all stored dual witnesses. Test the architecture given by the master optimum using the exact oracle. If feasible, return its primal and the master lower bound. If infeasible, store its dual and add the corresponding cut. If K(z) is empty, the entire supplied dictionary is infeasible.

Proof of correctness and termination. Every cut is valid for every feasible architecture by the preceding argument. The infeasible current architecture violates its new cut because its feature columns annihilate z. It can therefore never be selected again. At most 2^m architecture-oracle calls occur. A feasible returned architecture has cost equal to a relaxation's minimum and belongs to the true feasible set; its cost is consequently the true minimum. An empty cut proves full-dictionary infeasibility. If the master becomes infeasible, its valid cuts also prove no true feasible architecture exists. QED.

For a stand-alone optimality certificate one may supply the final primal, all dual witnesses generating the cuts, and a checked proof of the binary master's lower bound. Enumerating the 2^m masks is a valid exact lower-bound check, as done here. It is exponential; no polynomial-size general optimality certificate is promised. With such a simple enumerating master, the worst-case work is exponential even apart from the oracle. An exact rational LP may replace the elementary oracle without changing this proof or the oracle-call bound.

### PM-RB-003: static initial-circuit hitting is insufficient

It is tempting to enumerate the initially infeasible model's minimal trades and select blocks that kill each one. This is not generally complete because new dual trades can be positive combinations whose optional moments cancel.

Take Omega={d,p,q}, D={d}, and only the constant feature initially. The normalized obstruction polytope is

    z=(-1,y,1-y), 0<=y<=1.

Its extreme certificates/circuit trades are z_1=(-1,1,0) and z_2=(-1,0,1). Supply a single optional feature f(d)=0, f(p)=1, f(q)=-1. It kills both extreme trades. Nevertheless their average z=(-1,1/2,1/2) annihilates f and is a surviving obstruction. Indeed the target equation forces the constant coefficient to zero and the two off-target weights are b and -b. No b makes both positive. This is a complete counterexample to a one-shot strategy that merely hits all the original minimal obstruction trades. Adaptive re-solving avoids it.

### PM-RB-004: conventional bounded MILP baseline is exact

Let p be the full number of feature columns, counting copies. Assume p>=1, and define

    M = L p! H^p.

Use the original evaluation matrix F. Give each optional coefficient in block j the bounds -M x_j <= a_l <= M x_j, give base coefficients bounds -M<=a_l<=M, impose F_D a=0 and F_O a>=1, and minimize sum c_j x_j over x_j in {0,1}.

This is an exact MILP formulation of the bounded-dictionary repair problem. One direction is immediate. For the converse, every feasible architecture has a primal with rank r<=p and coefficient bounds L r! H^r<=M by the preceding determinant argument, so these bounds exclude no feasible architecture. The r=0, p=0 and O-empty cases are trivial exceptions handled separately. The bound has polynomial binary encoding but can be numerically enormous and give a weak LP relaxation. This formulation is a standard group-feature-selection MIP with a proved safe big-M; it is not a new optimization method.

### PM-RB-005: general minimum-cost selection already contains weighted set cover

For a weighted set-cover instance (U,{S_j},c_j), take Omega={d} union U, D={d}, include a constant base feature, and let f_j(d)=0, f_j(u)=1 when u in S_j and 0 otherwise. Target vanishing forces the constant coefficient to zero. If selected sets cover U, assigning every selected feature coefficient 1 gives a valid positive weight. If an element is uncovered, its row is zero in every selected optional feature, and its weight is necessarily zero. Thus feasible architectures are exactly set covers and optimum costs are identical. This is a direct exact reduction, not an appeal to superficially similar terminology. In particular the general optimization is NP-hard; feasibility of a fixed architecture remains ordinary rational LP, and the budgeted decision problem has polynomial-size rational primal certificates by the determinant bound.

The inclusion-minimal feasible architectures need not be matroid bases: a set system with one block covering all of {1,2,3} and three singleton blocks has minimal feasible architectures of sizes one and three. Oriented-matroid feasibility therefore does not imply a greedy matroid minimum-basis algorithm for feature repair.

### PM-RB-006: all-product stability

For any returned W(s)=F_B(s,:)a, W(d)=0 on D and W(s)>0 off D. For every finite independent product support Omega^N,

    sum_{i=1}^N W(s_i)=0  iff  every s_i belongs to D,

because each summand is nonnegative. Clearing all value denominators makes the scalar weight integral without changing this property. This is exactly the needed additive grading contract; no unspecified coefficient cancellation under powers is assumed. It is elementary and consistent with PM-CONSTRUCTION-0004, not a new product theorem.

## Frozen designed calibration and results

The file `/tmp/pm_repair_b_frozen.json` was created before solving the concrete dictionary instance. Its SHA-256 is `476a983f7b806a7ff1cb4dd0a71ad3fc758f10541e85faeb1697480f2cd68192`. The script asserts that pin before running. It freezes:

* Omega={-6,-5,...,5,6}; D={-5,-3,-1,1,3,5}.
* Base monomials 1,t, with arbitrary rational coefficients.
* Ten optional blocks indexed j=0,...,9, given by exponents {2(j+1), 2(((3j+4) mod 11)+1), 2j+3}, deleting duplicates within each block.
* Cost c_j=1+((7j+3) mod 5).
* No supplied square, target polynomial, coefficient vector, sign pattern, or factorization.
* Optimize total cost, then block count, then increasing bitmask.
* Frozen restriction: remove the three numerically smallest positive even exponents occurring in the chosen optimum, from all blocks; solve again.
* Baseline: the same exact oracle and grammar, examining all architecture masks in increasing objective order until the first success.

The explicit dictionary is:

| j | Block exponents | Cost |
|---|---|---:|
|0|2,3,10|4|
|1|4,5,16|1|
|2|6,7,22|3|
|3|6,8,9|5|
|4|10,11,12|2|
|5|12,13,18|4|
|6|2,14,15|1|
|7|8,16,17|3|
|8|14,18,19|5|
|9|20,21|2|

| Test | Optimum | Selected blocks | Adaptive oracle calls | Exhaustive oracle calls |
|---|---:|---|---:|---:|
| Frozen original | 4 | {1,4,6}, mask 82 | 20 | 20 |
| Delete even exponents 2,4,10 | 9 | {1,2,5,6}, mask 102 | 142 | 142 |
| Retain odd optional exponents only | Impossible | — | 20 | Not needed for the full-dictionary dual |

The original run's primal is the even polynomial

    W(t) = 1
      -(241989763072/173318069925)t^2
      +(4338388538368/10919038405275)t^4
      -(94927744/76356911925)t^10
      +(30268/211621575)t^12
      -(947344/173318069925)t^14
      +(67451/992639855025)t^16.

Its evaluations in increasing order t=-6,...,6 are exactly

    [1,0,1,0,1,0,1,0,1,0,1,0,1].

All odd coefficients found by the unrestricted oracle are zero; they were not manually excluded. The JSON also contains the full rational restricted-control primal. The odd-only obstruction has z_0=1 and z_{-1}=z_1=-1/2, all other entries zero. It annihilates the constant and every odd monomial, is nonnegative off target with off-target mass one, and is therefore a certificate against the entire odd-only dictionary.

### PM-RB-007: independent sparse-root lower bound for this designed target

Any feasible polynomial on the frozen Omega needs at least six distinct nonconstant even monomials in its supplied span. This is not an experimental inference.

Proof. Symmetrize W to (W(t)+W(-t))/2=Q(t^2). It is still zero on D and positive at all off-target grid points. Thus Q is positive at u=0,4,16,36 and zero at u=1,9,25. In each of the three disjoint intervals (0,4),(4,16),(16,36), the sum of multiplicities of its real roots is positive and even: the endpoint signs agree and the interval contains the prescribed root. There are therefore at least six positive roots counted with multiplicity.

A nonzero polynomial with a nonzero constant coefficient and k other nonzero monomials has at most k positive roots counted with multiplicity. Here is a short proof rather than assuming a classification theorem: for k=0 there are none. For k>0, differentiation removes the constant and factoring its smallest power of u leaves a polynomial with at most k terms and nonzero constant. Induction bounds its positive roots by k-1. Rolle's theorem including multiplicities bounds the original polynomial's positive roots by at most k. Consequently Q needs k>=6, proving the assertion. QED.

In the original dictionary any cost below 4 buys at most two blocks (there are just two unit-cost blocks), hence at most four distinct even monomials. The returned cost-4 construction is optimal. Among objective-earlier masks at cost 4, the only possible three-block choices use both unit blocks and one cost-2 block; adding block 9 gives just five even exponents, whereas adding block 4 gives six. This also verifies the chosen mask's deterministic tie-break.

For the restricted dictionary, the independent checker enumerates 1024 masks and minimizes the objective subject only to covering six distinct remaining positive even exponents. That necessary-condition optimum is exactly (9,4,102). Combined with its verified primal, this proves the restricted optimum independently of all dual cuts and without using an optimization oracle.

The sparse-root lemma generalizes to alternating zero patterns on a positive-node grid, but no novelty is asserted for this elementary fewnomial/Rolle argument. The concrete engineered cost dictionary is not a natural external target. The adaptive trade cuts delivered no oracle-count saving on these two successful instances; this is a useful negative control for claims of algorithmic benefit.

## Independent audit requested by the coordinator after initial development

After the independent route, instance freeze, and primary script were already developed, the coordinator reported the same projected-convex-hull/adaptive-cut direction and requested a different checker rather than another primary implementation. The stand-alone checker below therefore also audits the coordinator's marked-coordinate family. This audit is independent verification of a supplied family, not independent discovery of that family or a claim that its input had been frozen by this agent.

### PM-RB-008: exact degree threshold on the marked-coordinate grid

Let 1<=r<=p, Omega={-1,0,1}^p, and D={x: some x_i=0 with 1<=i<=r}. In the grammar of rational polynomials of total degree at most d, a nonnegative scalar weight vanishing exactly on D exists iff d>=2r. The assertion remains true if all coordinate exponents are required to lie in {0,1,2}.

Proof of the lower bound. Define l(-1)=l(1)=1 and l(0)=-2. Define an unnormalized signed measure z on Omega by

    z(x) = product_{i=1}^r l(x_i)  when x_{r+1}=...=x_p=0,
           0                     otherwise.

On O, all its nonzero entries are +1; their total is 2^r. For any monomial of total degree less than 2r, at least one marked coordinate has exponent 0 or 1. Its l-moment is respectively 1-2+1=0 or -1+1=0. Tensor factorization gives zero full moment. Thus z/2^r is an obstruction against the full degree-(2r-1) grammar, not just a selected subdictionary. Any positive off-target W would have z.W>0, contradicting annihilation. The polynomial product_{i=1}^r x_i^2 has degree 2r and takes values 0 on D and 1 on O, proving sufficiency and all-product stability. QED.

For the full reduced dictionary e in {0,1,2}^p there is a stronger exact moment statement: z has a nonzero moment only at e=(2,...,2,0,...,0), with the first r entries 2, and that moment is 2^r. Therefore if the optional blocks contain *individual reduced monomials only*, every successful architecture must include that particular monomial somewhere. Its absence is a single full-dictionary dual obstruction, not a difficult discovery case; minimum block repair in that strict monomial grammar simply chooses the cheapest block containing it (assuming the base does not already include it). Broader blocks can of course contain linear combinations rather than individual monomials; then the moment criterion must be applied to their actual evaluation columns.

The nonnegative/all-product condition is load-bearing. The signed polynomial product_{i=1}^r x_i has degree r and vanishes exactly on D, but its values at the all-ones point and the point with only x_1=-1 are +1 and -1. Their two-factor additive grading returns to zero although neither factor is a target. Signed zero-set selection alone therefore does not meet the required composition contract. Its minimum signed degree is r in the reduced grammar: uniqueness of grid interpolation implies every nonzero monomial coefficient of a function vanishing on every marked zero hyperplane must contain each marked coordinate to a positive exponent; degree at least r follows. Coordinatewise reduction x_i^3=x_i never increases degree, so the same lower bound holds for unreduced polynomials on this grid.

Direct exact audits ran for p=r=1,2,3,4 and p=6,r=2. They check all reduced monomial moments, all grid primal values, the positive off-target support, and the bad signed product. The low-degree annihilated monomial counts are respectively 2,8,26,80,78. For p=6,r=2 there are 729 grid points and 78 reduced monomials of total degree below 4. These checks corroborate the arbitrary-p,r tensor proof; they are not an infinite proof by enumeration.

## Prior-art gate and source pins

These primary sources were inspected on 18 October 2026. None of the historical comparisons below rests on a failure to retrieve a search hit.

* Rauh, Kahle and Ay, **Support Sets in Exponential Families and Oriented Matroid Theory**, arXiv:0906.5462v2 (16 September 2011), especially Definition 6 and Lemma 7 (PDF pp.5–6), Theorem 18 (p.13), and Proposition 34 (p.22). Definition 6 is literally the fixed-architecture target-zero/off-target-at-least-one system, under its constant-coordinate setup. Lemma 7 and the signed-circuit criterion already certify failure through signed dependencies. Adding optional feature rows changes the point configuration; costed block selection is not solved by merely naming its oriented matroid. Pin: https://arxiv.org/pdf/0906.5462v2 ; DOI https://doi.org/10.1016/j.ijar.2011.01.013 . Web refs available to coordinator: `turn178view0`, `turn180view2`, `turn180view3`.

* J. F. Benders, **Partitioning procedures for solving mixed-variables programming problems**, Numerische Mathematik 4 (1962), 238–252. Its opening page describes fixing the difficult variables and successively solving independent linear subproblems with a coordinating program. This is established decomposition prior art, not a newly inferred connection. Pin: DOI https://doi.org/10.1007/BF01386316 ; inspected scan https://www.im-uff.mat.br/puc-rio/disciplinas/2006.1/soe/arquivos/benders-numerische-mathematik-1962.pdf . The scan has 8 scanned pages, some scans pairing printed pages; the opening page was visually inspected. Web refs: `turn178view1`, `turn202view4`.

* Hooker and Ottosson, **Logic-based Benders decomposition**, Mathematical Programming 96 (2003), 33–60, DOI https://doi.org/10.1007/s10107-003-0375-9 . The author-hosted 38-page manuscript's Section 5, Figure 1 and Theorem 1 explicitly give a master driven by valid subproblem-derived cuts and lower bounds. Its SAT specialization writes cuts as clauses. The disjunction “at least one block changes this infeasibility proof” is a direct special case of that perspective. Pin: https://johnhooker.tepper.cmu.edu/benders2.pdf , linked from the author's publications page https://johnhooker.tepper.cmu.edu/papers.html . Web refs: `turn202view0`, `turn207view0`, `turn207view1`.

* Maldonado, Pérez, Weber and Labbé, **Feature selection for Support Vector Machines via Mixed Integer Linear Programming**, Information Sciences 279 (2014), 163–175, DOI https://doi.org/10.1016/j.ins.2014.03.110 . Section 3 and formulation (9) already use binary acquisition variables, acquisition costs, and coefficient bounds tied to selected features. Our target-equality/positive-off-target constraints and grouped columns differ from their statistical objective, but the feature-selection formulation is standard. The determinant-derived safe bound addresses completeness of the finite mathematical formulation, not a claimed replacement for this prior art. Pin: https://repositorio.uchile.cl/bitstream/2250/126859/1/Feature-selection-for-Support-Vector-Machines-via-Mixed-Integer-Linear-Programming.pdf . Web refs: `turn196view0`, `turn202view2`.

* Amaldi and Kann, **On the approximability of some NP-hard minimization problems for linear systems**, ECCC TR96-015, dated 16 February 1996. Its minimum-relevant-variable formulation explicitly seeks solutions with few nonzero variables, and studies relations including equalities and inequalities. This is older sparse-linear-system optimization prior art; the direct set-cover reduction above establishes this contract's hardness without depending on a mismatch between their variants. Pin: https://eccc.weizmann.ac.il/report/1996/015/ ; later article DOI https://doi.org/10.1016/S0304-3975(97)00115-1 . Only the primary ECCC abstract/metadata and publisher result were inspected here, not every proof in the later article. Web refs: `turn196view2`, `turn207view2`, `turn174search29`.

No closest-source claim is made that any one paper contains every detail of this exact grouped-positive-zero-set contract. The ingredients and the general feature-selection/decomposition operation are clearly established. Correctness of the synthesis, its implementation, potential utility, and historical novelty are separate fields.

## Reproduction and artifact pins

All files below belong to this task and were written only with `apply_patch`; there were no repository edits, external messages, payments, or further delegation.

    python3 /tmp/pm_repair_b.py
    python3 /tmp/pm_repair_b_check.py

Both require only Python's standard library. `pm_repair_b.py` prints the complete result JSON; the saved run is `/tmp/pm_repair_b_results.json`. The checker reads that file, reconstructs the original matrices independently, verifies every dual cut against the full unsimplified dictionary, verifies both primals, enumerates all masks for master lower bounds, separately enumerates the six-even-feature necessary-condition bound, and audits the marked-coordinate family. It has no Gaussian elimination, simplex, convex-hull routine, or import of the discovery implementation. Its saved output is `/tmp/pm_repair_b_check_results.json`.

SHA-256 pins for the delivered checkpoint:

* `pm_repair_b.py`: `2f89c26d907a35a04f32e5f32571bcc27d4b31bc9e30bb6f92ec0afe2f7879dc`
* `pm_repair_b_frozen.json`: `476a983f7b806a7ff1cb4dd0a71ad3fc758f10541e85faeb1697480f2cd68192`
* `pm_repair_b_results.json`: `d3361bcb648944c3ab9b4ae89913b9c06fe9ec89ccf20ba36dd1801a4d406b37`
* `pm_repair_b_check.py`: `ce046aa394de2b2afd62282437e758fe855bb5e0dcdee0cb8261416385fae0df`
* `pm_repair_b_check_results.json`: `ef226b66e20106a965edbbccc381e4752bb80e9b958513c88e31cba9492c526b`

The result JSON's elapsed-time field is non-semantic and changes on rerun; all architecture objectives, rational coefficients, rational dual witnesses and oracle counts are deterministic for this code. The saved run reported 3.195 seconds for all three discovery runs and both successful exhaustive baselines. This single local elapsed time is not a comparative runtime claim.

Repository source pins read for context:

* `AGENTS.md`: `fe626ca7e18451e46c97f94eb9dce11fe90faa8cb898582835b177bda7f01940`
* `research/RESEARCH_PROGRAM.md`: `f7f88ff91826358c8f4983bc5a1c08e6e467fd184c1a50a718bf6f732ae71521`
* `research/mechanisms/CONSTRUCTION_CONTRACTS.md`: `00f349a51e302181ca4d04415052efe598accd113cf7951d028755f9eec51a86`

## Review, limitations, and exact next operation

Status: mathematical proof supplied and exact independent implementation/checking supplied; coordinator/adversarial acceptance pending. No Lean compilation, formal verification, human peer review, natural held-out success, general speed advantage, causal model-performance result, or historical novelty is claimed. The independently coded checker is a separate implementation within this agent's task, not another independent human or agent reviewer.

The bounded-dictionary representation-selection operation is now routine exact optimization, with transparent certificates and NP-hard worst-case selection. The important remaining scientific test is not another rebranding of this alternative. It is to freeze an external previously uninspected target's *candidate representation grammar, legal composition and costs*, compare equal-input exact LP/MILP or established specialized methods, and test whether any proposed additional mechanism improves resource use or discovers a legal representation outside those baselines. The coordinator's reduced-monomial grid family is a good sharp degree calibration, but PM-RB-008 shows why its feature selection is structurally easy when the product-square monomial is itself a dictionary item. That should be disclosed when evaluating an operational discovery claim.

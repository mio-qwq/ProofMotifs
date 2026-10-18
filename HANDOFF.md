# Recovery handoff

Read AGENTS, STATUS, ROADMAP and CLAIMS; inspect live remote refs and recent commits. The last fetched predecessor is 87f227b150df9a32ca398bb047323ecaad0c64e5. The containing checkpoint's SHA is resolved from the branch, not predicted here. Preserve unexpected changes and use expected-predecessor non-forced writes.

## Current mathematics

Finite weights on a field: M_n(mu)=sum mu(x)x^n, x^0=1, ord(0)=infinity. SC-001 proves the binomial convolution identity and equality of leading order iff its binomial coefficient is nonzero. SC-002 proves the saturated prime-field-subspace formula. These are classical Level 0 infrastructure.

SC-003 (PM-THEOREM-0003): for mu=Delta_a*Delta_b*Delta_c in characteristic three, M_0,...,M_4=M_6=0, M_5=-abc(a^2+b^2+c^2), M_7=-abc(a^2b^2+a^2c^2+b^2c^2). The only finite orders are 5 and 7. If both invariants vanish and abc!=0, the directions are +/- on one line and the weight is zero. Full proof and the F_27 triples (1,alpha,alpha^2) versus (1,alpha,alpha^2+2alpha) are in workstreams/SC-003/RESULTS.md. Both triples are independent and all proper subproducts have the same orders, yet full orders differ.

SC-005 (PM-THEOREM-0004): additive bijections T of F_{3^m} preserve every ternary order exactly when T=lambda*x^{3^j}, except F_9 where all additive bijections do. Proof: parameterize a quadratic zero relation by (1-t^2+t,1-t^2-t,-1-t^2); after T the sum of squares is G(t)=T(1)T(t^2)-T(t)^2. At most six parameters have a zero coordinate. Represent T by a linearized polynomial L of degree <=q/3. For q>=27, q-6>2q/3, so G has too many roots unless it is the zero polynomial. Its distinct cross exponents force only one nonzero coefficient. Handle F_3/F_9 separately. See workstreams/SC-005/RESULTS.md for all hypotheses and proof. Novelty remains unverified.

## Exact next operations

1. Read the entire SC-005 proof and challenge the six-parameter exclusion, polynomial-versus-function step, exceptional F_9 case, and coefficient-field scope. Do not equate computational review with an independent proof.
2. Compare its actual hypothesis with Carlitz-McConnel and additive conic/square-preserver results. Known scalar-Frobenius conclusions do not by themselves certify or refute novelty of this condition. Literature leads are in INITIAL_REVIEW.
3. Construct an explicit witness extractor: for non-semilinear additive T, inspect the conic parameter family to find a triple of order 7 sent to order 5. The proof suggests at least q/3-6 good violations; this quantitative statement and its sharpness have not yet been entered as a verified claim. Check signs, distinct parameters, even/odd extension behavior and compare standard linearized-polynomial tests.
4. Formalize the core only with an actual compiler and pinned dependencies. None was available in this window. Do not mark upstream or generated Lean as verified without a run.
5. SC-004 four-difference coefficient formulas remain unverified in NEXT.md. The preserver direction was prioritized for structural value; see docs/decisions/0002-preserver-priority.md.

## Verification commands and evidence

python -m unittest discover -s tests -v
python tools/run_experiments.py
python tools/ternary_differences.py
python tools/order_preservers.py

The current 20-test suite passed. Expected deterministic JSON and hashes are in research/experiments. Counts: 66,281 baseline pairs; 5,606 saturated tuples; 20,439 ternary triples; 439 normalized additive bijections; 63,921 preserver label comparisons. Accepted maps are checked on all triples; rejected maps stop at a witness. Normalize by T(1)=1 only because scalar preservation is proved. A separate discrete-log multiplication check covers all 729 F_27 products. No independent mathematical author review or Lean run exists.

First hosted CI run 39100933546 for 87f227b succeeded, with job 117596877400 confirming both test and deterministic replay steps. The next commit's hosted run needs a fresh fetch. A scheduled 90-minute recovery task was created; no continuous inter-run computation is implied.

## Provenance and safe transport

Sources pinned: OpenAI 1581d4cbdd69a0faf34b2089614fe2a814316a6a; mio math 029e05b3f45f43690f19dd599834690bcbbf016e. Targeted pilots are not a prevalence study; the MUB case was already read and is not a held-out or human control. Xie already discusses transfer; Drapal-Vojtechovsky already develops polarization and p-degree. SC-001/002 are reproduction, SC-003/005 priority is unverified.

Container Python/Git function, direct GitHub DNS does not. Use the authorized connector, compare remote tree with local git write-tree, create a child commit and update the expected branch non-forcibly. The local index may be ahead of local HEAD when API transport was used; inspect rather than reset blindly. Only ProofMotifs is writable under this charter. Licensing remains undecided.

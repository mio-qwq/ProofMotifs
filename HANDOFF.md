# Recovery handoff

Read AGENTS, STATUS, ROADMAP, CLAIMS, then fresh remote refs, recent commits and working tree. Last remotely verified predecessor: 2e990a7c00899321dc202e3f6c083b3181481c67. Resolve the live containing commit independently. Preserve unexpected changes and never force-push.

## Mathematical state and exact notation

For a finite weight mu on a characteristic-three field K, M_n(mu)=sum_x mu(x)x^n, with x^0=1; ordinary order is the first nonzero moment, infinity only for the zero weight. Vandermonde on its s support nodes detects zero using moments 0 through s-1, including over infinite fields. Delta_a=delta_a-delta_0, C(a,b,c)=ord(Delta_a*Delta_b*Delta_c).

SC-003 gives M_0,...,M_4=M_6=0, M_5=-abc*e1 and M_7=-abc*e2, where e1=a²+b²+c² and e2=a²b²+a²c²+b²c². For abc!=0, order is 5 if e1!=0, 7 if e1=0,e2!=0, infinity otherwise; the last case has directions signed copies of one another. Zero directions also give infinity.

SC-005 classifies additive bijections of finite F_(3^m): scalar Frobenius if m!=2, all GL(2,3) if m=2. Its original polynomial proof and F9 exception have now passed actual independent AI review (not human or Lean).

SC-006/RESULTS.md contains the current strongest proof. For a(t)=1-t²+t, b(t)=1-t²-t, c(t)=-1-t², one has e1=0 and e2=-(t-t³)². The zero-coordinate set E is empty unless K contains F9, in which case E=F9 minus F3. Identity: abc=-(t²+1)(t⁴+1), (t³-t)*abc=-(t⁹-t).

For additive bijective T, A=T(1)!=0 and Q(t)=A*T(t²)-T(t)². Its polar is B(x,y)=2*(A*T(xy)-T(x)*T(y)); Q(1)=0,B(1,x)=0,Q(t+r)=Q(t) for r in F3. Q(t+u)+Q(t-u)=2Q(t)+2Q(u). Transformed conic sum of squares equals Q(t). A nonzero Q-value outside E automatically gives a strict source7->target5 witness; Q vanishes on F3, so no infinity source is hidden.

PM-THEOREM-0005: for basis (1,e1,...), test Q(e_i) and Q(e_i+e_j), i,j>=1. There are N=m(m-1)/2 tests. All zero implies Q identically zero by quadratic expansion, hence T/A is a field automorphism by square polarization. Otherwise obtain t. If t in E, choose basis element u outside F9: Q(u) or Q(t+u) or Q(t-u) is a usable nonzero value. Up to3 directly checked extras (2 if last is inferred). A basis adapted to (1,i,u,...) replaces the bad test i by i-u and proves an N-test bound, but that version is NOT implemented. Costs are oracle-query counts with field/basis setup, rank validation and full verification separate.

PM-THEOREM-0006: the same repair proves the arbitrary-field classification K!=F9, T=lambda*sigma with sigma an arbitrary field automorphism. If a preserver had any nonzero Q, repair gives an admissible conic violation. Thus Q identically zero and polarization gives multiplicativity after normalization. No finiteness, perfectness or Frobenius-surjectivity assumption is used. Infinite-field sigma must NOT be restricted to Frobenius powers. F9 retains all 48 additive bijections.

## Evidence and reproducibility

python -m unittest discover -s tests -v
python tools/constructive_witness.py > /tmp/constructive-results.json
diff -u research/experiments/constructive-results.json /tmp/constructive-results.json

29 tests passed. F27 all 432 normalized bijections: 3 semilinear, 429 strict witnesses verified by complete27 moments on each side, max 3 defect queries / 6 distinct extraction T calls. Selected F81 tests are 18 transvections, not a full GL(4,3) enumeration. An even-repair example uses modulus x⁴+x²+2, columns(1,4,16,27), initial t=9 repaired to12, source(39,51,28), image(38,46,28), verified7->5 by complete81 moments. Output and hashes: research/experiments/constructive-results.json and constructive-SHA256.json. The script constructs O(q²) field tables, so it makes NO O(m²) end-to-end runtime claim.

Independent tasks A/B/C/D completed; task scopes, objections, resolution and review limits are in docs/reviews/THIRD_CYCLE.md. A accepted the manuscript and implementation and ran all 9 new tests. Root fixed A's docstring objection that q moments are sufficient rather than necessary. Mathematical correctness, independent AI review, human review, formalization and novelty remain separate. No Lean/Lake/Elan tool is available.

Historical baseline commands remain available: python tools/run_experiments.py; python tools/ternary_differences.py; python tools/order_preservers.py. Do not repeat large enumerations just to appear active. CI run 39102950233 covers 037ea1c only; verify each later run separately. The workflow now also replays constructive-results.json.

## Generator-row advance: SC-007

Read workstreams/SC-007/RESULTS.md. With a genuine power basis (1,alpha,...,alpha^(m-1)), polar defects H(alpha,x)=A*T(alpha*x)-T(alpha)*T(x) need only vanish on that row. After normalizing S=T/A, S(alpha*x)=S(alpha)S(x) on every x forces multiplicativity by iteration and polynomial expansion. The endpoint alpha^(m-1) enforces the degree-m defining relation and cannot be dropped.

PM-THEOREM-0007 uses Q(alpha), then two parameters for each u=alpha^k, 2<=k<m. Let F={x:x^9=x}. If u in F, query alpha+u and alpha-u. Else if alpha+u in F, query u and alpha-u. Otherwise query u and alpha+u. With Q(alpha)=0, parallelogram recovers the original row conditions from each chosen pair. All queried points lie outside F and are directly admissible. Total <=2m-3 Q evaluations, no repair. This is not a universal quadratic-form test or an optimal T-query bound; m T-basis images already determine T.

PM-THEOREM-0008: deterministic Q-only decision with no T images/matrix/description needs >=floor(m/2) queries. On a shorter all-zero transcript choose phi annihilating span{1,t_i,t_i²}, define S(x)=x+phi(x). N²=0 implies invertibility, it fixes queried inputs and squares, and its fixedspace dimension m-1 excludes nontrivial Frobenius. Adaptive transcript is identical to identity. With the upper bound this gives Theta(m) ONLY for that decision model; no promised-negative witness-only, randomized, exact-constant or richer-input lower bound is asserted.

Negative controls: F27 columns(1,9,15) passes Q(alpha)=0 but fails the final generator-row relation. F81 modulus(2,0,1,0,1), columns(1,4,9,36), i=11, has H(i,x)=0 for every x while Q(alpha)=5. A coordinate quadratic x_2*x_3 shows why generic quadratic maps cannot use the smaller test.

## New reproduction commands and actual evidence

python -m unittest discover -s tests -v
python tools/generator_witness.py > /tmp/generator-results.json
diff -u research/experiments/generator-results.json /tmp/generator-results.json

41 tests passed. Task A independently ran the 12 new tests and accepted saved proof/code. F27 generator scan: 408 rejected after one Q, 21 after two, 3 accepted after three; all 429 witnesses verified by all 27 moments. Selected larger cases: 18 maps on each of two F81 presentations and 32 on F243. Thirty-eight controls exercise full bounds. All 81 possible F81 single-query positions admit a constructed zero-answer adversary; these instances contain eight distinct maps, not 81 distinct maps. Complete-moment verification validates their separate extracted witnesses. Source/result hashes are in generator-SHA256.json, actual log in generator-tests.log. No new independent arithmetic engine or Lean run exists.

## Exact next mathematical operations

1. Read workstreams/SC-008/RESULTS.md, docs/reviews/FIFTH_CYCLE.md and research/literature/NONADDITIVE_AUDIT_20261018.md. The independent-sign obstruction and quotient theorem are complete; do not try to recover additivity from the original labels.
2. PM-CONJECTURE-0002 asks whether every H_K automorphism is `u -> s*u^(3^j)` for m>=3. Full exact computations now establish it in F_27 and F_81. Next improve the enumerator/certificate for F_243 or derive a structural reduction; a first bounded F_243 attempt exceeded 30 seconds and was terminated with no result.
3. Compare the exact 3-uniform square zero-sum hypergraph with restricted Freiman automorphisms, cyclotomic hypergraphs and additive designs. Buratti-Nakic's square embedding is classical background; their blocks have size four in PG(3,3), not the project's size-three relation.
4. SC-007's Theta(m) result is retained only in deterministic exact Q-only access. Do not optimize constants without an external application, and do not imply direct-T or randomized optimality.
5. Genuine formalization or a held-out application remain alternatives if the general hypergraph classification is covered or stalls. SC004 remains deferred. Maintain separate proof, computation, AI-review, human-review, Lean and originality fields.

## SC-008 exact state

For q>3, every arbitrary ternary-order preserver fixes zero, is odd, and induces an automorphism on `S=(K^*)^2`. Define H_K to have distinct zero-sum triples of S as edges. Then `Pres(C)=C_2^((q-1)/2) semidirect Aut(H_K)`. The proof uses SC-003 to show that nonzero labels are infinity for one square class, 7 for a distinct zero-sum triple, and 5 otherwise.

The independent sign map swapping only 1 and -1 in F_27 is a complete negative example to additivity. It was compared on all 27^3 ordered triples. The quotient degree is `(q-6-3eta)/8`, eta=(-1)^m, and the edge count is `(q-1)(q-6-3eta)/48`.

Exact small fields: F_9 has four quotient vertices, no edges, Aut=S_4 and 384 full preservers. F_27 has 13 quotient vertices and 13 edges; exhaustive forced-third backtracking gives 39 automorphisms, identical to square-scaling/Frobenius actions, and 319488 full preservers. F_81 has 40 vertices and 120 edges; the same complete enumerator gives exactly 160 automorphisms, again the semilinear actions, and 175921860444160 full preservers.

Reproduce with `python -m unittest discover -s tests -v` and `python tools/nonadditive_preservers.py`. The expected files are research/experiments/nonadditive-results.json and nonadditive-tests.log; hashes are in nonadditive-SHA256.json. Current local suite: 46 tests.

## Operational recovery

Only ProofMotifs/research/ongoing is writable under this charter; main remains stable. Direct clone succeeded in this window; earlier DNS failure is historical, not a permanent assumption. Check both Git and connector access afresh. Nonforced connector updates with expected predecessor remain a fallback. The existing 90-minute scheduled task was actually re-enabled and its unified coordinator/short-task/adversarial-review instructions updated. The stored first start is 2026-10-18 07:14:59 UTC (15:14:59 Asia/Singapore). No future run or continuous between-run process is asserted. No license decision, DOI, correspondence or final paper release has been made.

## Delivery resolution

The user explicitly authorized immediate public pushing on 2026-10-18. Terminal Git push then failed for missing credentials, not an approval rejection. The authorized GitHub API delivered the exact original mathematical tree 6275963256aaa91b47b37ff082fdec2da0dd4066 as remote a434475c0863a80e79ebadc98ae563c07a20253c. Hosted run 39105407423, job 117610052289, passed all verification steps. Previous local commits 310b87a / e8b2051 remain in the saved bundle; their mathematical files are synchronized and the old blocker is superseded. The generator checkpoint 8836e298 was verified with tree afb1531b6718ee7e8fd03c5fe3737037610f7503 and successful CI run 39105897724, job 117611547104, including all five replay steps and the 41-test suite. See docs/reviews/CI_GENERATOR_CHECKPOINT.json. The containing receipt checkpoint changes only state/evidence records. The enabled 90-minute task was updated to use current remote recovery and no longer wait for already received authorization.

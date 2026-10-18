# Recovery handoff

Read AGENTS, STATUS, ROADMAP, CLAIMS and fresh remote refs before writing.
Last verified remote mathematical checkpoint: `f363f13cc3adfc9dc0b14c6e486e7754c3ba5ac5`.
Resolve the containing live head separately. Preserve unexpected work;
never force-push. Unified branch: `research/ongoing`; main stays stable.

## Latest accepted continuation: SC-015

Recovered actual10c06a57d5b4795c69fec819c832f141a0c8e863, no newer remote
branch increment and no concurrent task. Read SC-015/RESULTS.md and its
COMPUTATION.md before another normal-filter search. PM0019 is now proved:
normal y with chi(y-1)=chi(y)=chi(y+1)!=0 exists iff m>=5, in the range
m>=3. Count bound Theta/4[q-3-6(W-1)sqrt(q)] uses CRT Fourier coefficient
mass and the classical field Kloosterman bound2sqrt(q), allows3|m. Integer
checks plus induction cover m>=9 and6,7; direct normal witnesses cover5,8.
Degree4 is impossible by a pure F3 three-input Bezout/annihilator certificate,
not failed search; degree3 is impossible by the constant cubic frequency13.

One parameter simultaneously excludes nonaffine cubic-representable frequencies.
PM0020 gives quartic Q(y)=-1, and normality excludes 2+2 repetitions. Do not
assume it controls 2+1+1 or four-distinct patterns. PM-COUNTEREXAMPLE0009:
F6561 modulusX8+X3+2, y4863, a4783,b2761, gamma-seed{0,76,2368}, index4.
Normal determinant2, all signs-1; quartic frequency820 survives. Trace witness
on true edge{1,81,164} is2,1,2. Components force kernel at least36 versus
full9. No exact sparse dimension or connected-normal counterexample claimed.

A/C independently derived the count, D supplied polynomial basecases, B
quartic structure/boundary, E independent proof and arithmetic audit. The
120-test suite passed, sc015-tests.log. Five deterministic outputs match;
sc015-SHA256.json records this mathematical snapshot. Verify its actual
new hosted run after delivery, distinct from the previous f363f13 run.

Next: PM-QUESTION0002, connected normal filtered parameters for every m>=5.
Force a=(y+1)/y of orderN if a suitable rational-image sieve is available;
full-group primitive orderq-1 is incompatible with a being square. Check
primary 2-primitive/normal rational-image results and small exceptions before
claiming any general connectedness. PM-QUESTION0001 remains open; even a
connected normal seed needs genuine quartic/higher-frequency control.

## Previous continuation: SC-014

Recovered true head e19781a36e1267f1850751cc4a9ad18e025588f3 after all-branch
and working-tree checks. No external increment or other active main task
was found. Read SC-014/RESULTS.md and COMPUTATION.md before repeating any
search. The predecessor mathematical CI at7e12402 was re-read successfully.

PM0018: P_(3^r+3^s)=-(a-1)^(3^r+3^s); cubic digitweight
gives Pk=-(a-1)^k L((a-1)^-1). The L-kernel dimension is deg gcd(Tm-1,G),
proved via linearized composition and separable roots, without a squarefree
assumption on Tm-1. Exact square filtering, proper-subfield and sixfold
differential-fiber exclusions are in the proof. Do not label every cubic
representation extra: some are constant/Frobenius residues.

PM-COUNTEREXAMPLE0008: m13, modulusX13+2X+1, N797161prime, k85.
y=X2+X3+X9; a=2X5+2X11+X12; b=2+X5+X11+2X12. Both vertices are squares,
1+a+b=1+a85+b85=0, and a!=1 generates the prime-order square group.
The sparse kernel is at least27, full kernel14. Tr(u85) takes1,1,0 on the
true edge with coordinates1,112,223. No exact sparse rank is claimed.

All81 points of the four-dimensional L-kernel were checked;78 outsideF3
give exactlyB85 and13 seed orbits. The group y->+-y^(3j)+c of order78 acts
freely/transitively, preserves the square filter, and proves all78 from one
point. Quotienting the six normalizations gives Frobenius transitivity on
the13 seed orbits. Independent E arithmetic and A/E proofs accepted;
TENTH_CYCLE reviews preserve methods and limits. The111-test suite passed;
sc014-tests.log and three new JSON outputs record actual execution.

General existence remainsOPEN, as does historical originality. The next
operation is a simultaneous cubic sieve using normal-element/character
conditions or a controlled quartic obstruction; details in ROADMAP. Do not
reopen the refuted odd-degree connectedness route, scan the full m13 field,
or compute exact nullity merely to sharpen an unused number. Mathematical
commit f363f13cc3adfc9dc0b14c6e486e7754c3ba5ac5 has matching local/remote
tree ff3d03878cdd8c8fb5a7d2eb4886be6981470711. Fresh hosted
run39128991481/job117680063593 reads confirmed the unit suite and all18
deterministic replay steps passed. Receipt: CI_LINEARIZED_SEED_CHECKPOINT.json.
This containing receipt checkpoint changes evidence/recovery only; the
SC-014 manifest belongs to the mathematical tree, before metadata changes.

## Previous continuation: SC-013

Recovered e35f0dfcb8e5446be3e0840d54c8f89e9967b34e after fresh Git and
GitHub reads of all branches (main and research/ongoing only). No unseen
external increment or conflicting working changes was found at recovery.

PM-THEOREM-0017: for E={1,a,b}, H=<a,b>, F_3(H)=F_(3^d), the seed-orbit
components are tH and kernel dimension is at least [S:H]*(d+1). If H<S
this exceeds m+1, so connectivity is necessary for full row-code generation.

PM-COUNTEREXAMPLE-0007: over F_729=F_3[X]/(X^6+X+2), gamma=X^2,
the connected seed {0,25,311} has kernel 13 rather than 7. Its extra
frequency orbit starts at 34. Tr(u^34) satisfies every one of its 364
scaled equations but has values 0,0,1 on the true edge {0,5,255}.
Independent ordinary polynomial gcd and coordinate trace programs confirm
the certificate without importing the search implementation.

The complete orbit scans cover m=3..6 (1,3,10,30 orbits). Good orbits are
certified for m=3..8, but m=7,8 stop at the first good seed. General
existence remains OPEN. The next operation is a simultaneous spectral-factor
avoidance argument or an all-seed covering obstruction, not more positive
small-field tables. Read SC-013/RESULTS.md, COMPUTATION.md,
NINTH_CYCLE.md and SINGLE_ORBIT_GATE_20261018.md.

The integrated local suite passed 102 tests; log sc013-tests.log. New
reports, independent-check outputs and command log are in research/experiments;
sc013-SHA256.json records this checkpoint's source/evidence hashes. Mathematical commit 7e12402671c6c2f30bf91f6eadb3d2729fbc35df was delivered
with matching local/remote tree 30e78c285996baacee9acf8bb458d9df492b4737.
Fresh reads confirmed hosted run39122726149/job117661432531 success: the
unit suite and all16 deterministic replay steps passed. Receipt:
docs/reviews/CI_SINGLE_ORBIT_CHECKPOINT.json. This containing receipt
checkpoint changes evidence/recovery only. The SC-013 manifest records
the mathematical commit, before this metadata update.
Classical tools, finite evidence, independent AI review, historical novelty,
human review and Lean remain separate.

## Strongest accepted statements

C(a,b,c) is the ordinary-moment order of the convolution of three first
finite-difference weights over a characteristic-three field. SC-003 proves:
a zero direction gives infinity; otherwise, writing u=a²,v=b²,w=c²,
equal squares give infinity, distinct zero-sum squares give 7, and all other
cases give 5. SC-005/006 classify additive preservers and retain F_9 as the
exception; the arbitrary-field additive result allows arbitrary field
automorphisms, not only Frobenius powers.

SC-007 proves <=2m-3 admissible Q evaluations with a supplied power basis
and >=floor(m/2) for deterministic decision from Q alone. Theta(m) is ONLY
that oracle model; no direct-T, randomized or bit-complexity optimality.

SC-008 gives all arbitrary preservers for finite q>3 as the independent-sign
kernel over Aut(H_K), where H_K is the distinct zero-sum triples on
S=(K*)². The sign swap on just {1,-1} in F_27 is nonadditive and preserves
all 19,683 ordered triple labels. This obstruction must not be discarded.

SC-009 now proves PM-THEOREM-0013: every incidence-kernel function S->F_3
is affine for m>=3. Combined with PM-THEOREM-0011 and classical Carlitz,

`Aut(H_K)={u -> s*u^(3^j):s in S,0<=j<m}`.

The arbitrary preserver group has order `2^((q-1)/2)*(q-1)*m/2`.
F_9 remains exceptional (384 arbitrary preservers); F_3 has S_3.
PM-CONJECTURE-0002 is proved, not still open. Read the full self-contained
proof in workstreams/SC-009/RESULTS.md before changing this status.

SC-009 also has a second uniform proof in `FOURIER_PROOF.md`. The square
subgroup diagonalizes the incidence kernel into characters `u->u^k`. Root
bounds and Frobenius-orbit dynamics leave only
`k=0,1,3,...,3^(m-1)`; a cubic Weil sum excludes the even-degree order-two
candidate. Task F independently accepted every step. This covers all `m>=3`
without finite base certificates.

SC-010 proves PM-THEOREM-0014. For an index-`d` multiplicative subgroup, the
condition `q-[6(d-1)^2+8(d-1)^3+3(d-1)^4]sqrt(q)-4d^3>0` forces the
line-incidence kernel to be affine. Its exact automorphism group is then
`Stab_GL(m,3)(H)`. Do not replace this by scalar--Frobenius for `d>2` without
a separate generalized-Paley theorem.

## New accepted continuation

Read SC-011/RESULTS.md and SC-012/RESULTS.md. PM0015 is classical cyclic
incidence coding: rank=N-deg(gcd(Z^N-1,p_e)). A standalone F3 polynomial
certificate proves the F_243 seed {0,4,68} has rank115 and six-dimensional
affine kernel. Only121 cyclic edges suffice for the full1210-edge row code.
Yet the seed's group is C121 and the full group's order is605. Equal kernels
do not recover the hyperedge collection. Preserve all five Frobenius patterns
and the F_81 rank25 bad-orbit versus rank35 good-orbit control.

PM0016 gives H=F_s* union beta F_s*, beta² a nonsquare inF_s, s=3^e,e>=2.
Its hypergraph is two connected punctured e-spaces; kernel2e+2, affine2e+1,
Aut=GL(e,3) wreath S2 equals the ambient linear stabilizer. Extra mode is
u^(s-1). For e1 the union has four isolated vertices and AutS4. This shows
minimal affine kernel is sufficient, not necessary, for linear extension.
These are Level0 structural/coding boundaries, not certified original work.

All89 tests passed; research/experiments/sc012-tests.log records the run.
New reports: cyclic-incidence-certificate.json, cyclic-incidence-verification.json,
two-subspace-results.json. The cyclic --check path imports no project code;
the two-axis program uses no extension-field arithmetic. Its e2 component
checks all40320 permutations, while full4608 and e3 group252315648 follow
from the wreath theorem, not full-group enumeration. sc012-SHA256.json is the
current new-file manifest; old manifests describe historical source versions.

Recovered21999eb was accepted through a74-test replay, both exact report
diffs, allSC010 manifest hashes and fresh run39113374667/job117634030262
reads. Audits and task ledger are in EIGHTH_CYCLE.md and its three full audit
files. Mathematical commit1da34c83c3b528d745c96e23834e570cdddae0de has matching
local/remote tree0a3ef95f9f7c27f3f54e9a90f5b3884a625d26be. Hosted
run39117122857/job117645060777 passed all89 tests and all13 replay
steps; fresh run/job reads were inspected. See
docs/reviews/CI_SPARSE_SUBSPACE_CHECKPOINT.json. The containing receipt
checkpoint changes evidence/recovery only.

## Why the general proof works

The F_3 incidence kernel includes every affine restriction. If its dimension
is m+1, coordinate pullbacks under any hypergraph automorphism extend
uniquely to an affine map. Since S affinely spans K, its linear part is
invertible. Sum S=0 and |S|=1 modulo3 kill the translation. Additivity and
preservation of squares give square difference quotients, meeting Carlitz.

For q>=243, a nontrivial u+v=w+z in S has four distinct roots
0,-u,-w,z-u. A parameter a making a,-u-a,-w-a,u+a-z squares exists by
`N4 >= (q-38-11sqrt(q))/16>0`. Four zero-sum triples give the Freiman
identity. Repeated triples are automatic: characteristic three forces all
entries equal and 3f=0. Do not exclude extra diagonal parameters.

For x!=0, the exact difference count is
`(q-3-(1+chi(-1))*chi(x))/4>0`. Thus define L(x)=f(a)-f(b) for a-b=x;
Freiman relations make it well-defined. Three-square-translate intersections
are at least `(q-15-2sqrt(q))/8>0`; telescoping gives additivity, with zero
arguments and x+y=0 checked separately. Hence f is affine. Exact rank
certificates for q=27 and 81 finish the two degrees below243.

Weil's multiplicative-character version applies to distinct-root degree2/3/4
polynomials here, without a degree-coprime-to-characteristic restriction.
Primary statement: Kim–Yip–Yoo2024 Lemma2.1; final Carlitz step: Yip2024
Theorem1.2 with the square subgroup. E independently checked the complete
proof and primary sources; root accepted. No Lean or human review occurred.

## Exact certificates and commands

The rank reports are (q,vertices,edges,rank,nullity):
(9,4,0,0,4), (27,13,13,9,4), (81,40,120,35,5),
(243,121,1210,115,6). F_9 is the essential failing affine-rank control.

F_243 has exactly605 quotient automorphisms. The rank certificate supplies
matching nonzero minor and six independent kernel vectors. A separate
color certificate fixes1, yielding cell counts2,3,15,25,25; fixing(1,9)
yields3,6,121,121. The upper bound121*5*1 matches605 edge-preserving known
actions. Its checker imports no other project module and reconstructs
arithmetic from alpha^5=alpha+2 and a242-element cyclic-log table.

```bash
python -m unittest discover -s tests -v
python tools/incidence_rank_certificate.py > /tmp/incidence-rank-results.json
diff -u research/experiments/incidence-rank-results.json /tmp/incidence-rank-results.json
python tools/color_refinement_certificate.py --check research/experiments/color-certificate.json
python tools/freiman_completion.py > /tmp/freiman-completion-results.json
diff -u research/experiments/freiman-completion-results.json /tmp/freiman-completion-results.json
python tools/fourier_incidence_spectrum.py > /tmp/fourier-incidence-spectrum.json
diff -u research/experiments/fourier-incidence-spectrum.json /tmp/fourier-incidence-spectrum.json
python tools/cyclotomic_incidence.py > /tmp/cyclotomic-incidence-results.json
diff -u research/experiments/cyclotomic-incidence-results.json /tmp/cyclotomic-incidence-results.json
```

The historical SC-010 suite passed 74 tests; log research/experiments/sc010-tests.log.
The workflow replays all historical reports plus the SC-009 and SC-010 reports.
Mathematical commit 029a65ff5920f6f9bc05e5102ee3cd5d2f545154 was delivered
with matching local/remote tree 4afcd66a268a42f18f4fd4f7f8a09ebaba5a5298.
Hosted run39109178633/job117621402329 passed the full suite and all nine
replay steps; fresh run/job reads were inspected. See
docs/reviews/CI_INCIDENCE_CHECKPOINT.json. The containing receipt checkpoint
changes evidence/recovery metadata only. Hashes: sc009-SHA256.json. Negative tests
reject missing edges, unsafe color splits and altered Frobenius data; exact
F_9 functions and missing completions witness the true exception.

The Fourier/SC-010 mathematical checkpoint is remote
`3ab50849fa7a61ff3cae220dd21ea1feb74fc97d`, tree
`635e39e6a3a18aaab45f69db89dacec3b283b2ea`, parent `31f3d393`. Hosted run
39113374667/job 117634030262 passed the 74-test suite and all eleven replay
steps. The one Node 20 checkout annotation is infrastructure-only. See
`docs/reviews/CI_CYCLOTOMIC_CHECKPOINT.json`; do not confuse a later metadata
receipt run with this mathematical-commit CI.

## Recovered external increment

Accepted f172123bd60e27bccbea31fb335994418d95d5d9 (SC-008),
b82c344012c4af879f6e6e4d7a5320efb77d4f8b (workflow), and
bfe32279b502fd07ec646d4a7f173808d0ad8a2a (receipt).
Fresh run 39108039870/job 117618028562 reads confirmed success; local46-test
replay, exact regenerated JSON and all saved hashes also passed.
See docs/reviews/EXTERNAL_SC008_ACCEPTANCE.md. The producing execution's
identity is not established by the shared Git author. The earlier mistaken
predecessor string was corrected to 2e990a70585e0fd7230a2c8b47d34627722a011b.

## Exact next operation and limits

Continue PM-QUESTION-0001 through simultaneous spectral-factor avoidance.
Use the precise B_k forbidden sets in ROADMAP; distinguish collective ideal
generation from a unit seed quotient. Positive instances m=3..8 and the
connected m=6 failure are controls, not an infinite theorem. Preserve equal
row-code versus equal-automorphism distinctions and the SC-010 stabilizer
endpoint. No unmotivated tables or threshold polishing.

One full publicly extracted Zhihu answer was read via Parallel Search; not
all33 answers or comments. The evidence gate rejects universal cancellation
or AI/human prevalence conclusions. Source and method comparisons:
research/literature/DISCUSSION_GATE_20261018.md.

Architecture remains one coordinator with actual task-scoped subagents,
independent views, adversarial checks and a single shared roadmap. See
SEVENTH_CYCLE.md, SIXTH_CYCLE.md and SC009_GENERAL_AUDIT.md for accepted
handoffs, objections and decisions. Distinguish software certificates,
AI review, human review, Lean and historical novelty.

## Delivery and scheduling

The user authorized immediate ordinary project pushes. Terminal Git lacks
credentials; authorized GitHub API tree/commit/ref writes work. Fresh-read
the expected predecessor, match local `git write-tree` with remote tree,
create a child commit, update the ref non-forced with expected_sha, fetch and
verify live SHA. Never overwrite unexpected remote changes.

A fresh self-continuation task was created in this research conversation,
enabled=true, first scheduled start2026-10-18 19:10:12Asia/Singapore,
recurring every90minutes. Its instruction resumes actual work here and
prohibits reminders/wake-ups in other conversations. Do not reuse inherited
automation IDs from another chat. Real scoped subagents here remain allowed.
Every window reads fresh remote state; no between-window process is claimed.
Ordinary checkpoint pushing remains authorized, without permission changes,
other repositories, expenses, correspondence, DOI or final paper releases.

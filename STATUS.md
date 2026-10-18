# Current research status

Updated: 2026-10-18. Branch: `research/ongoing`; `main` remains the stable baseline.
Last remotely verified mathematical checkpoint: `1da34c83c3b528d745c96e23834e570cdddae0de`.
Resolve the live containing commit independently; no file names its own future SHA.

## Current mathematical result

SC-009 completes the finite-field arbitrary ternary-order preserver classification.
For K=F_(3^m), m>=3, S=(K*)^2, the zero-sum square hypergraph has

`Aut(H_K)={u -> s*u^(3^j):s in S,0<=j<m}`.

The full group preserving every ordinary ternary cancellation order is
`C_2^((q-1)/2) semidirect Aut(H_K)`, of order
`2^((q-1)/2)*(q-1)*m/2`. Each map fixes zero and acts by a common scalar/Frobenius
with an independent sign on each opposite pair. F_9 retains 384 arbitrary
preservers; F_3 has all six permutations. Additivity is not implied.

PM-THEOREM-0011 reconstructs the affine ambient space when the F_3 incidence
kernel has dimension m+1, then applies classical Carlitz. PM-THEOREM-0013 proves
that kernel condition for every m>=3: four-edge character-sum completion and
Freiman extension cover q>=243, and exact rank certificates cover m=3,4.
The invoked Weil and Carlitz statements were checked against primary research
sources. PM-CONJECTURE-0002 is proved within this precise model.

F_243 has rank 115, nullity 6 and exactly 605 quotient automorphisms. A separate
color-refinement certificate proves the same group count; its checker uses
independent alpha-recurrence/cyclic-log multiplication and checks all 1,210
edges and 605 known actions. This is independent software arithmetic, not Lean.

Proofs and exceptions: workstreams/SC-009/RESULTS.md and COLOR_CERTIFICATE.md.
Classical tools, general proof, finite evidence, AI reviews and novelty are
separate. Historical originality, human peer review and formalization remain
unestablished. No universal new cancellation theory is claimed.

SC-009 now also has an independent uniform proof. Multiplicative Fourier
decomposition reduces the kernel to exponents `k` satisfying
`1+a^k+(-1-a)^k=0` on the square relation. Root bounds and Frobenius-orbit
dynamics leave `0,1,3,...,3^(m-1)`; one cubic Weil sum excludes the sole
even-degree order-two candidate. This route works for every `m>=3` without
the finite `m=3,4` rank certificates. It is manual and AI-reviewed, not Lean.

SC-010 proves a controlled extension. For an index-`d>=2` multiplicative
subgroup `H`, let `B4=6(d-1)^2+8(d-1)^3+3(d-1)^4`. If
`q-B4*sqrt(q)-4d^3>0`, its internal zero-sum-line kernel is exactly the affine
restrictions. The hypergraph automorphism group is the linear setwise
stabilizer of `H`; scalar--Frobenius needs an additional generalized-Paley
normality hypothesis and is not inferred from incidence affinity alone.

## New continuation: SC-011 and SC-012

The recovered Fourier/SC-010 increment was independently accepted in this
window. All 74 previous tests passed, both new JSON reports regenerated
byte-for-byte, every SC-010 manifest hash matched, and fresh hosted run/job
reads confirmed success. The full branch inventory found only main and
research/ongoing; the increment was on research/ongoing. See EIGHTH_CYCLE.md.

SC-011 supplies a polynomial-only F_243 certificate. The gcd of Z^121-1
and 1+Z^4+Z^68 is (Z-1)(Z^5+2Z+2), of degree six. Supplied Bezout and
divisibility witnesses prove rank 115 using one 121-edge orbit instead of
all 1,210 edges. The verifier imports no other project modules and checks
field irreducibility, subgroup order and the actual seed. The sparse and
full hypergraphs have identical kernels but automorphism orders 121 and605,
respectively; the preserved Frobenius-pattern obstruction is essential.

SC-012 explains the index-five F_81 failure by an infinite two-subspace
subgroup family, s=3^e,e>=2. Its kernel dimension2e+2 exceeds ambient affine
2e+1 by one, but Aut=GL(e,3) wreath S2 still equals the ambient linear
stabilizer. The additional direction is the order-two character u^(s-1).
The e=1 two-axis hypergraph is empty and has S4, not the wreath group.
Both new workstreams are conservatively classified as classical
infrastructure/boundaries, without a priority or new-method claim.

The combined local suite passed 89 tests, log sc012-tests.log. Exact new
reports are cyclic-incidence-certificate.json, cyclic-incidence-verification.json
and two-subspace-results.json. The two-subspace program uses direct F3
coordinates, enumerates only the eight-point component, and derives large
group orders from the written theorem. Source/report/review hashes are in
sc012-SHA256.json. Mathematical and code reviews are preserved in the
EIGHTH_CYCLE audit documents. Mathematical commit 1da34c83c3b528d745c96e23834e570cdddae0de was delivered
with matching tree 0a3ef95f9f7c27f3f54e9a90f5b3884a625d26be. Fresh reads
confirmed hosted run39117122857/job117645060777 success: the unit suite
and all13 deterministic replay steps passed. Receipt:
docs/reviews/CI_SPARSE_SUBSPACE_CHECKPOINT.json. The containing receipt
checkpoint changes evidence/recovery only. No Lean or human review is claimed.

## Acceptance of recovered work

SC-008 arrived through remote commits f172123 (mathematics), b82c344 (workflow)
and bfe3227 (CI receipt). It was accepted through proof inspection, fresh
46-test replay, byte-identical nonadditive output and all four saved hash
checks. Hosted run 39108039870, job 117618028562 was separately read and
confirmed successful at b82c344. See docs/reviews/EXTERNAL_SC008_ACCEPTANCE.md.
The Git author does not identify the exact producing execution.

The recovered general statement was only a conjecture; it was not treated as
an existing theorem. SC-009 supplies the new proof. The recovered invalid
full predecessor string was corrected: its actual predecessor was
2e990a70585e0fd7230a2c8b47d34627722a011b.

## Actual verification

All 74 tests passed in the integrated local suite; current log:
research/experiments/sc010-tests.log. New deterministic reports record exact
rank minors and kernel vectors, full color traces and an independent arithmetic
receipt, and completion-gadget checks. F_27/F_81 cover all 780/28,880 nontrivial
ordered relations; F_243's 7,080 normalized representatives cover 856,680
relations by square scaling. All 218,124 instantiated gadgets pass; F_9 supplies
real failing completions and a nonaffine kernel function. Finite enumeration
is not the proof for unbounded degree.

The new reports `fourier-incidence-spectrum.json` and
`cyclotomic-incidence-results.json` check the spectral exponents and preserve
small-field subgroup failures. In `F_81`, the index-5 kernel has dimension six
versus affine dimension five; the index-16 subgroup has minimal kernel but a
linear stabilizer `S_5` larger than scalar--Frobenius. These are negative
controls, not counterexamples to the stated large-field theorem.

Actual independent AI tasks A/B/C/D/E and coordinator decisions are recorded
in docs/reviews/SIXTH_CYCLE.md; E's complete proof audit is preserved separately.
A counting subtask that was interrupted is not counted as a completed review.
The six value/Fourier/cyclotomic tasks and the coordinator's endpoint decision
are recorded in docs/reviews/SEVENTH_CYCLE.md.
No Lean/Lake/Elan tool is installed; no formal-verification claim is made.
The mathematical tree was delivered as 029a65ff5920f6f9bc05e5102ee3cd5d2f545154,
with local/remote tree 4afcd66a268a42f18f4fd4f7f8a09ebaba5a5298. Hosted run
39109178633, job 117621402329, passed the unit suite and all nine replay
steps. The fresh run and job endpoints agree. The receipt is
docs/reviews/CI_INCIDENCE_CHECKPOINT.json. The containing receipt checkpoint
changes only recovery metadata and evidence, not mathematics or source code.

The independent Fourier proof and SC-010 extension were delivered as
`3ab50849fa7a61ff3cae220dd21ea1feb74fc97d`, with matching local/remote tree
`635e39e6a3a18aaab45f69db89dacec3b283b2ea` and parent `31f3d393`. Hosted run
39113374667, job 117634030262, passed the 74-test suite and all eleven
deterministic replay steps. Its sole annotation is the hosted runner's Node 20
deprecation warning for checkout; no test or mathematical check failed. The
receipt is `docs/reviews/CI_CYCLOTOMIC_CHECKPOINT.json`. The containing receipt
checkpoint changes recovery metadata and evidence only; distinguish its CI
from this mathematical-commit run.

Prior successful mathematical CI: a434475c/run39105407423 (SC-006),
8836e298/run39105897724 (SC-007), b82c344/run39108039870 (SC-008).
Corresponding JSON receipts remain in docs/reviews.

## Discussion and next research gate

Parallel Search extracted the body of one specified Zhihu answer. Other
answers and comments were not read. Its request to explain structure behind
identities is useful; its sweeping homology/cancellation claim is not a
precise theorem. The bounded source audit does not establish corpus-wide
prevalence, AI/human differences or a missing universal mathematical tool.
See research/literature/DISCUSSION_GATE_20261018.md.

The completed value gate provisionally classifies SC-009 as Level 1. Full
affine Reed--Muller duality, the full nonzero zero-sum design, the square
embedding, Freiman extension and Paley/Carlitz theory are close but do not
directly imply the induced-square incidence kernel. This bounded outcome does
not establish priority. See `INCIDENCE_VALUE_GATE_20261018.md`.

Next precise target is PM-QUESTION-0001: does every m>=3 admit at least
one square-multiplication edge orbit spanning the full incidence row code?
Express the question as a trinomial gcd, compare cyclic-code precedents
first, and distinguish existence from the refuted claim that any orbit works.
Known positive cases m=3,4,5 and the F_81 bad seed must remain controls.
Select a proof route or a counterexample; do not generate more subgroup
tables or optimize SC-010 constants without a mathematical purpose.

## Scheduling and delivery

A new 90-minute self-continuation task was created in this research
conversation on 2026-10-18, with first scheduled start 19:10:12
Asia/Singapore. Creation returned enabled=true and the current conversation
binding. It instructs the researcher to execute work here and prohibits
reminders or research wake-ups in other conversations. An inherited task
identifier from a different conversation must not be reused. Short-lived
subagents inside this conversation remain allowed. Every invocation checks
live state; scheduling does not imply computation between invocations.

Immediate ordinary project pushes are explicitly authorized. Terminal Git
lacks push credentials; authorized GitHub tree/commit/ref operations are used
with an expected predecessor, matching local/remote tree and non-forced ref
updates. No other repository, permissions, expenses, correspondence, DOI or
final academic release is in scope.

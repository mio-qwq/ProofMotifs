# Current research status

Updated: 2026-10-18. Branch: `research/ongoing`; `main` remains the stable baseline.
Last remotely verified predecessor: `bfe32279b502fd07ec646d4a7f173808d0ad8a2a`.
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

All 65 tests passed in the integrated local suite; log:
research/experiments/sc009-tests.log. New deterministic reports record exact
rank minors and kernel vectors, full color traces and an independent arithmetic
receipt, and completion-gadget checks. F_27/F_81 cover all 780/28,880 nontrivial
ordered relations; F_243's 7,080 normalized representatives cover 856,680
relations by square scaling. All 218,124 instantiated gadgets pass; F_9 supplies
real failing completions and a nonaffine kernel function. Finite enumeration
is not the proof for unbounded degree.

Actual independent AI tasks A/B/C/D/E and coordinator decisions are recorded
in docs/reviews/SIXTH_CYCLE.md; E's complete proof audit is preserved separately.
A counting subtask that was interrupted is not counted as a completed review.
No Lean/Lake/Elan tool is installed; no formal-verification claim is made.
The new workflow includes all deterministic reports. Its hosted result must
be checked at the actual new commit after delivery.

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

Next: compare the exact incidence-affinity statement with restricted Freiman
extension, partial affine geometry codes and quadratic-residue preserver
literature. Identify a direct prior theorem or the precise uncovered step.
Conlon–Gowers' difference-extension mechanism and prescribed-character-pattern
completion are established background. Do not optimize SC-007 constants or
repeat small-field enumeration without a new validation need. If the result
is covered, retain it as infrastructure and select a genuinely new application
or a small formalizable core. SC-004 remains deferred.

## Scheduling and delivery

The existing 90-minute task was observed disabled, then successfully re-enabled
and updated on 2026-10-18 with latest recovery and research instructions.
Timezone: Asia/Singapore. The service records a last invocation at
2026-10-18 07:34:32 UTC; this timestamp alone does not identify its outputs.
A single coordinator owns integration and publication; genuine short-lived
subagents remain allowed. Every invocation checks live state and reconciles
external increments before writing. Scheduling does not imply computation
between invocations.

Immediate ordinary project pushes are explicitly authorized. Terminal Git
lacks push credentials; authorized GitHub tree/commit/ref operations are used
with an expected predecessor, matching local/remote tree and non-forced ref
updates. No other repository, permissions, expenses, correspondence, DOI or
final academic release is in scope.

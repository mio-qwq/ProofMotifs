# Project status

Checkpoint: arbitrary-preserver quotient obstruction and small-field classification, 2026-10-18. Coordinator: PM-ROOT-20261018.

Stable branch: `main`. Unified research branch: `research/ongoing`.
Last remotely verified predecessor: `2e990a7c00899321dc202e3f6c083b3181481c67`. Resolve the live ref for the containing checkpoint; no file predicts its own future SHA.

## Current verified work

SC-001/002 remain classical Level 0 infrastructure. SC-003 classifies ternary orders as 5, 7 or infinity and refutes rank/proper-order sufficiency. SC-005 classifies additive finite-field preservers, with the essential F_9 exception. Separate actual AI reviewers now accept the SC-003 core and SC-005 proof; human review and formalization are outstanding.

SC-006 adds two complete written results:

* PM-THEOREM-0005: on F_(3^m), m>=3, a non-scalar-Frobenius additive bijection has an explicit strict 7-to-5 witness detectable in at most m(m-1)/2+3 directly checked quadratic-defect values. The last repair check can be inferred, and a separately proved adapted-basis version needs only m(m-1)/2 tests. Only the conservative standard-basis version is implemented.
* PM-THEOREM-0006: over ANY characteristic-three field K other than F_9, additive ternary-order preservers are exactly scalar times field automorphisms. The proof covers infinite and imperfect fields. For F_9 all 48 additive bijections remain preservers.

Historical novelty remains unverified. Lester's 1977 full-cone preserver theorem is a closer classical precedent than the earlier Carlitz-only comparison. The missing-coordinate/punctured-cone bridge, precise F_9 exception and extractor need source-specific further comparison. No new general theory or public-conjecture solution is asserted.

## Generator-row results

SC-007 adds PM-THEOREM-0007: given a genuine degree-m power basis, 2m-3 directly evaluated defect values suffice, all at admissible order-7 conic parameters. The first nonzero value yields a strict 7-to-5 witness with no extra repair. This uses the special multiplicativity-defect structure; it is false for arbitrary quadratic maps.

PM-THEOREM-0008 proves at least floor(m/2) queries necessary for deterministic decision with access only to the defect Q, no T images or description. An annihilator transvection imitates the identity's zero transcript below that bound. Thus query growth is Theta(m) in precisely this model, with no exact-constant, randomized, direct-T or bit-complexity conclusion. PM-COUNTEREXAMPLE-0004 preserves failures caused by omitting closure or using a proper-subfield multiplier. All have separate AI challenges; historical novelty and formalization remain unresolved.

## Arbitrary-preserver quotient result

SC-008 proves PM-THEOREM-0009. For every F_(3^m) with q>3, arbitrary bijections preserving all ternary cancellation labels form

`C_2^((q-1)/2) semidirect Aut(H_K)`,

where H_K has the nonzero squares as vertices and distinct zero-sum triples as edges. The kernel is one genuinely independent sign choice on every opposite pair. This decisively refutes any attempt to infer additivity from order preservation alone. An explicit F_27 map swapping only 1 and -1 preserves all labels but is nonadditive.

The quotient hypergraph is regular of degree `(q-6-3*(-1)^m)/8` and has `(q-1)(q-6-3*(-1)^m)/48` edges. F_9 has no edges and 384 arbitrary preservers. Exact F_27 and F_81 backtracking gives respectively 39 and 160 quotient automorphisms, exactly square-scalings and Frobenius; the full arbitrary-preserver counts are 319,488 and 175,921,860,444,160. The analogous semilinear quotient classification for every m>=3 is PM-CONJECTURE-0002, not a theorem.

## Actual verification and collaboration

46 unit tests passed in the current local checkpoint; actual log: research/experiments/nonadditive-tests.log. The new exact program compares all 19,683 F_27 triples for the one-pair sign flip and enumerates every quotient automorphism in F_9, F_27 and F_81. The respective quotient parameters `(vertices,edges,automorphisms)` are `(4,0,24)`, `(13,13,39)` and `(40,120,160)`. No general classification or F_243 count is claimed.

The earlier generator scan remains valid: all 432 normalized F_27 maps were covered, together with selected F_81/F_243 cases and exact adversaries. Its separate actual log and receipt remain unchanged.

Three new task-scoped AI researchers independently examined SC-007 prior art, the nonadditive structure and adversarial counterexamples. All returned handoffs; none remains asserted to run. Their scopes, objections and coordinator decisions are in docs/reviews/FIFTH_CYCLE.md. Shared finite-field arithmetic remains a common dependency; no Lean or human peer review is claimed.

Remote commit a434475c delivered the exact previous mathematical tree, and hosted CI 39105407423 passed every verification step. Its receipt is persisted. The generator checkpoint 8836e298 passed hosted run 39105897724, job 117611547104: all 41 tests and five deterministic replay steps succeeded. Its receipt is in docs/reviews/CI_GENERATOR_CHECKPOINT.json; this containing receipt checkpoint changes state/evidence records only. Ordinary terminal Git push lacks credentials; authorized GitHub API tree/commit/ref writes work and are verified. No Lean/Lake/Elan tool is available.

## Scheduling and next decision

The existing 90-minute task was found disabled and successfully re-enabled on 2026-10-18; its stored first future start remains 15:14:59 Asia/Shanghai. No future execution has yet been observed. Every window reads live remote state before writing. Unified coordinator ownership, independent mathematical views, adversarial review and checkpoint requirements are in AGENTS and the task instructions. This does not imply computation between invocations.

The SC-007 value gate is now resolved: retain its exact Q-only bound as a supporting proposition, not a standalone optimal-testing result, and do not optimize constants without an application. PM-CONJECTURE-0002 now has full exact support in degrees 3 and 4. Next priority is either a scalable F_243 certificate/search or a structural reduction to restricted Freiman/cyclotomic-hypergraph theory; a prototype F_243 backtracking run exceeded the 30-second bounded attempt and was terminated without a result. Buratti-Nakic's 2024 work already uses the same projective square embedding, so that embedding is established background. SC-004 remains deferred. No license decision, DOI, external correspondence or final academic release was enacted.

## Delivery and authorization

The project owner explicitly authorized immediate public delivery on 2026-10-18. The mathematical contents of local checkpoint 310b87a were delivered with identical tree as remote a434475c; the local-only e8b2051 blocker note is historical and superseded. No publication-authorization blocker remains. Continue ordinary project checkpoints under the charter, checking live refs before each non-forced update. No prior result is claimed Lean-verified or historically original.

# Project status

Checkpoint: linear generator test and restricted-oracle lower bound, 2026-10-18. Coordinator: PM-ROOT-20261018.

Stable branch: `main`. Unified research branch: `research/ongoing`.
Last remotely verified predecessor: `8836e29869569f3098c20a961f202e9df46d8db3`. Resolve the live ref for the containing checkpoint; no file predicts its own future SHA.

## Current verified work

SC-001/002 remain classical Level 0 infrastructure. SC-003 classifies ternary orders as 5, 7 or infinity and refutes rank/proper-order sufficiency. SC-005 classifies additive finite-field preservers, with the essential F_9 exception. Separate actual AI reviewers now accept the SC-003 core and SC-005 proof; human review and formalization are outstanding.

SC-006 adds two complete written results:

* PM-THEOREM-0005: on F_(3^m), m>=3, a non-scalar-Frobenius additive bijection has an explicit strict 7-to-5 witness detectable in at most m(m-1)/2+3 directly checked quadratic-defect values. The last repair check can be inferred, and a separately proved adapted-basis version needs only m(m-1)/2 tests. Only the conservative standard-basis version is implemented.
* PM-THEOREM-0006: over ANY characteristic-three field K other than F_9, additive ternary-order preservers are exactly scalar times field automorphisms. The proof covers infinite and imperfect fields. For F_9 all 48 additive bijections remain preservers.

Historical novelty remains unverified. Lester's 1977 full-cone preserver theorem is a closer classical precedent than the earlier Carlitz-only comparison. The missing-coordinate/punctured-cone bridge, precise F_9 exception and extractor need source-specific further comparison. No new general theory or public-conjecture solution is asserted.

## Generator-row results

SC-007 adds PM-THEOREM-0007: given a genuine degree-m power basis, 2m-3 directly evaluated defect values suffice, all at admissible order-7 conic parameters. The first nonzero value yields a strict 7-to-5 witness with no extra repair. This uses the special multiplicativity-defect structure; it is false for arbitrary quadratic maps.

PM-THEOREM-0008 proves at least floor(m/2) queries necessary for deterministic decision with access only to the defect Q, no T images or description. An annihilator transvection imitates the identity's zero transcript below that bound. Thus query growth is Theta(m) in precisely this model, with no exact-constant, randomized, direct-T or bit-complexity conclusion. PM-COUNTEREXAMPLE-0004 preserves failures caused by omitting closure or using a proper-subfield multiplier. All have separate AI challenges; historical novelty and formalization remain unresolved.

## Actual verification and collaboration

41 unit tests passed; actual log: research/experiments/generator-tests.log. The generator scan checks all 432 normalized F_27 maps: 408 non-preservers rejected after one Q query, 21 after two, and three semilinear maps accepted after three. All 429 returned witnesses are checked by complete actual moment vectors. Further output covers 68 selected maps across two F_81 presentations and F_243, 38 scaled-Frobenius controls, and 81 one-query adversary instances comprising eight distinct maps. None is an exhaustive GL(4,3) or GL(5,3) enumeration.

Four task-scoped AI researchers independently challenged proof, construction, access model, prior art and code. All have returned handoffs; none remains asserted to run. Task A accepted the saved manuscript/code and independently replayed all 12 new tests. See docs/reviews/FOURTH_CYCLE.md. Shared finite-field arithmetic remains a common dependency; no Lean or human peer review is claimed.

Remote commit a434475c delivered the exact previous mathematical tree, and hosted CI 39105407423 passed every verification step. Its receipt is persisted. The generator checkpoint 8836e298 passed hosted run 39105897724, job 117611547104: all 41 tests and five deterministic replay steps succeeded. Its receipt is in docs/reviews/CI_GENERATOR_CHECKPOINT.json; this containing receipt checkpoint changes state/evidence records only. Ordinary terminal Git push lacks credentials; authorized GitHub API tree/commit/ref writes work and are verified. No Lean/Lake/Elan tool is available.

## Scheduling and next decision

The existing 90-minute task was found disabled and successfully re-enabled on 2026-10-18; its stored first future start remains 15:14:59 Asia/Shanghai. No future execution has yet been observed. Every window reads live remote state before writing. Unified coordinator ownership, independent mathematical views, adversarial review and checkpoint requirements are in AGENTS and the task instructions. This does not imply computation between invocations.

Next priority: assess the exact restricted-oracle result against prior art, then review value before further constant optimization. For a broader preserver question, begin by testing independent sign changes on opposite pairs and do not assume additivity follows from ternary-order preservation. This is a next research target, not an accepted arbitrary-permutation classification. SC-004 remains deferred. No license decision, DOI, external correspondence or final academic release was enacted.

## Delivery and authorization

The project owner explicitly authorized immediate public delivery on 2026-10-18. The mathematical contents of local checkpoint 310b87a were delivered with identical tree as remote a434475c; the local-only e8b2051 blocker note is historical and superseded. No publication-authorization blocker remains. Continue ordinary project checkpoints under the charter, checking live refs before each non-forced update. No prior result is claimed Lean-verified or historically original.

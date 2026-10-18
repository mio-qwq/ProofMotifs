# Project status

Checkpoint: constructive witnesses, arbitrary-field extension and independent AI review, 2026-10-18. Coordinator: PM-ROOT-20261018.

Stable branch: `main`. Unified research branch: `research/ongoing`.
Last remotely verified predecessor: `4f6db95fe5b72c12bdbfc875026f47698735f817`. Resolve the live ref for the containing checkpoint; no file predicts its own future SHA.

## Current verified work

SC-001/002 remain classical Level 0 infrastructure. SC-003 classifies ternary orders as 5, 7 or infinity and refutes rank/proper-order sufficiency. SC-005 classifies additive finite-field preservers, with the essential F_9 exception. Separate actual AI reviewers now accept the SC-003 core and SC-005 proof; human review and formalization are outstanding.

SC-006 adds two complete written results:

* PM-THEOREM-0005: on F_(3^m), m>=3, a non-scalar-Frobenius additive bijection has an explicit strict 7-to-5 witness detectable in at most m(m-1)/2+3 directly checked quadratic-defect values. The last repair check can be inferred, and a separately proved adapted-basis version needs only m(m-1)/2 tests. Only the conservative standard-basis version is implemented.
* PM-THEOREM-0006: over ANY characteristic-three field K other than F_9, additive ternary-order preservers are exactly scalar times field automorphisms. The proof covers infinite and imperfect fields. For F_9 all 48 additive bijections remain preservers.

Historical novelty remains unverified. Lester's 1977 full-cone preserver theorem is a closer classical precedent than the earlier Carlitz-only comparison. The missing-coordinate/punctured-cone bridge, precise F_9 exception and extractor need source-specific further comparison. No new general theory or public-conjecture solution is asserted.

## Actual verification and collaboration

29 unit tests passed; actual log: research/experiments/constructive-tests.log. All 432 normalized F_27 additive bijections were classified by the extractor: 3 semilinear, 429 with complete-moment-verified 7-to-5 witnesses. Maximum observed extraction: 3 defect queries and 6 distinct map-oracle calls. New deterministic output also records 18 selected F_81 transvections, an explicit degenerate-parameter repair, 20 scaled-Frobenius controls and the six normalized F_9 cases. Tests additionally check all 416 scaled-Frobenius controls on the four fields. This does not enumerate GL(4,3).

Four actual task-scoped AI subagents were used: independent proof review, constructive theory, adversarial/prior-art review and computation. All have returned their handoffs; none is asserted to remain running. See docs/reviews/THIRD_CYCLE.md. Task A accepted the saved SC-006 proof and code and independently replayed its nine new tests. These are separate AI checks, not human peer review or Lean verification.

Earlier hosted CI succeeded for mathematical commit 037ea1c, run 39102950233. The new mathematical commit requires its own hosted run; no future CI outcome is assumed here. Exact source/result hashes accompany the constructive experiment. No Lean, Lake or Elan executable is available in this window. A normal local Git clone succeeded.

## Scheduling and next decision

The existing 90-minute task was found disabled and successfully re-enabled on 2026-10-18; its stored first future start remains 15:14:59 Asia/Shanghai. No future execution has yet been observed. Every window reads live remote state before writing. Unified coordinator ownership, independent mathematical views, adversarial review and checkpoint requirements are in AGENTS and the task instructions. This does not imply computation between invocations.

Next priority: assess the exact punctured-cone extension and witness test against additive cone preservers and quadratic identity-testing literature; then examine whether the current query bound has a meaningful lower bound or a genuinely new application. Do not repeat the completed F_27 enumeration without an evidence-driven reason. SC-004 remains deferred. No project-wide license, DOI, external correspondence or final academic release was enacted.

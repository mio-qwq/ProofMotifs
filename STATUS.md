# Project status

Checkpoint: ternary classification and additive-preserver cycle, 2026-10-18. Coordinator: PM-ROOT-20261018.

Stable branch: `main` (governance baseline). Research branch: `research/ongoing`.
Last remotely verified predecessor: `037ea1c17f711f73f823737a19c1c0dfa67e4b68` (the complete mathematical checkpoint). Resolve the live ref for the containing commit; no self-referential future SHA is claimed.

## Results

SC-001 and SC-002: written classical convolution/moment and saturated-subspace proofs, Level 0.
SC-003: complete written characteristic-three triple classification (orders 5, 7 or infinity); explicit same-field, same-rank, same-proper-order counterexample. Novelty unverified.
SC-005: complete written classification of additive bijections preserving all ternary cancellation orders on F_{3^m}. For m!=2 they are exactly lambda*x^{3^j}; F_9 is exceptional and admits all 48 additive bijections. Novelty unverified, independent review and Lean outstanding.
SC-004: four-difference formulas remain unverified working targets, deferred in favor of the more structural preserver question.

## Actual verification

20 current unit tests passed. Baseline checks: 66,281 weight pairs, 5,606 saturated tuples, 40,000 Lucas comparisons. Ternary checks: 20,439 triples and exact coefficients through degree 7. Preserver checks: all 439 normalized additive bijections across F_3/F_9/F_27; 63,921 before/after comparisons and 20,421 parameter-identity checks. A second F_27 multiplication algorithm agrees on 729 products; one F_81 non-preserver is checked.

Hosted CI succeeded for the complete mathematical checkpoint 037ea1c, run 39102950233, job 117602787653. Unit tests and all three deterministic experiment replay steps were actually fetched as successful. See docs/reviews/CI_SECOND_CHECKPOINT.json. This final state-only checkpoint changes no mathematical proof, test or experiment source. CI is not independent mathematical review or Lean verification.

## Boundaries and recovery

No genuine subagent interface or local Lean/Lake/Elan compiler was available. Same-coordinator sequential reviews are labeled accordingly. GitHub connector writes work; container GitHub DNS failed. No project license, DOI, external correspondence or final paper release was enacted. Five targeted source cards are not a representative corpus.

A 90-minute scheduled research invocation is enabled; first future run not yet observed. It does not imply continuous work between calls. See docs/RECOVERY_SCHEDULING.md.

## Highest-priority next tasks

Audit SC-005 against finite-field preserver literature, and obtain a genuinely independent or formal review when available. Then construct a rejecting ternary witness for non-scalar-Frobenius maps using the conic parameter family; compare with existing linearized-polynomial tests before claiming algorithmic novelty. Do not merely expand SC-004 coefficients for activity's sake.

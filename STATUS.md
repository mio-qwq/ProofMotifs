# Project status

Checkpoint: first mathematical cycle, 2026-10-18. Coordinator: PM-ROOT-20261018.

Stable baseline: `main`. Unified research branch: `research/ongoing`.
Last remotely verified predecessor: `063f99f67aba436c11feeb8157c1689bd8e82961` (governance baseline). Resolve the live ref for this checkpoint's actual commit.

## Completed

SC-001: complete written proof of the characteristic-free convolution identity and exact leading-order criterion; exact F_2 annihilation and F_4 finite-jump counterexamples. Classified Level 0.
SC-002: complete written proof of the saturated-difference/subspace dichotomy and exact order p^d-1, with Moore-determinant leading coefficient. Classified Level 0.
Ten unit tests passed. Exhaustive checks cover all 66,281 weight pairs over F_2/F_3/F_4, 5,606 saturated direction tuples over five fields, and 40,000 Lucas comparisons. Logs, deterministic JSON and source hashes are in research/experiments.
Five pinned pilot source cards, three detailed mechanism comparisons, withdrawal-date distinction and a candidate-specific literature review are recorded. No prevalence estimate is made.

## Active work

SC-003: unsaturated triple differences in characteristic three. Search found independent direction triples in the same F_27 with ordinary moment orders 5 and 7. The exact classification, persisted witnesses, expanded tests and focused novelty review are the next cycle; this lead is not yet a registered completed theorem.

## Verification boundaries

No callable subagent interface, no independent researcher review and no local Lean/Lake/Elan compiler. Exact algorithms share a field implementation. GitHub connector works; direct container Git networking does not. A pinned CI workflow is provided but a remote successful run has not yet been observed. No project-wide license has been selected. No formal paper release or DOI exists for this work.

## Next operation

Prove the ternary formula M_5=-abc(a^2+b^2+c^2), M_7=-abc(a^2b^2+a^2c^2+b^2c^2), and classify the double-zero case; verify with an independent subset-expansion algorithm. Save a second research checkpoint after checking the F_27 witnesses.

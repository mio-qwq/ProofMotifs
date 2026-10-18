# Generator-row tests and a restricted-oracle lower bound

Date: 2026-10-18. Starting remote checkpoint: a434475c0863a80e79ebadc98ae563c07a20253c. The coordinator publishes one unified research branch; all tasks below are short-lived contributions to it.

## Task ledger and independent challenges

All tasks read AGENTS and SC-006, assumed a characteristic-three finite field and an additive bijection, and were prohibited from changing other files or publishing. Initial mathematical proposals were checked independently before cross-review. The coordinator proposed the generator row and subsequent oracle lower bound, and resolves the objections below.

| Task | Question and allowed scope | Independence, output and stopping condition |
| --- | --- | --- |
| PM-SC007-A | Challenge generator-row detection, admissible parameter replacement, lower-bound model and all boundaries; read only | Independently derive identities and produce a mathematical verdict; stop at a bounded audit and return precise qualifications |
| PM-SC007-B | Develop a self-contained proof and negative controls; only workstreams/SC-007/RESULTS.md | Independently check the original proposal; contribute the replacement of forbidden test points; preserve exact cost model, lower-bound argument and closure counterexample |
| PM-SC007-C | Challenge hypotheses and compare primary computational-algebra sources; only research/literature/GENERATOR_TEST_AUDIT_20261018.md | Read original documentation and distinguish classical recognition from the exact defect certificate; return a bounded source-specific judgment with no originality inference |
| PM-SC007-D | Implement and test; only tools/generator_witness.py and tests/test_generator_witness.py | Independently derive the adaptive pairs and verify actual returned moments; include closure, subfield and oracle-boundary controls; stop after a reproducible handoff, without commit or push |

## Accepted mathematics and objections

The original SC-006 argument treated Q as a general quadratic map on a quotient vector space. The new argument uses its special multiplicativity-defect structure. If the polar row with one full field generator vanishes on a power basis, the normalized additive map intertwines multiplication by that generator and is multiplicative on every field element.

Task A checked the full row, including its last basis element. Tasks B/C supplied an explicit F_27 linear bijection with Q(alpha)=0 but a failed defining relation. This prevents silently dropping the closure condition. A field generator is required; a generator of a proper subfield is insufficient. No multiplicative primitive-element assumption is needed.

Task B proposed replacing the at-most-one forbidden point in each pair by alpha-u. Task A independently checked all three cases and the parallelogram identity. Thus all 2m-3 tested parameters can be admissible, rather than evaluating a forbidden point and repairing afterward. The selected set depends only on the field and generator; early termination depends on Q.

Task C correctly objected that m direct T-image queries already determine an additive map. Consequently no lower bound for direct T access follows from the Q test count. The coordinator formulated a narrower model: deterministic decision from Q values alone, with no matrix or T-image access. On the identity transcript, a functional vanishing on the span of 1, queried points and their squares yields an indistinguishable unital transvection until at least floor(m/2) queries. Task A independently accepted the adaptive argument and fixed-space obstruction. This proves the linear asymptotic order only in that specified oracle model; it does not determine constants, randomization or bit complexity.

The source audit identifies the generator-image/defining-polynomial principle as classical. These results are a project refinement with NOVELTY_UNVERIFIED, not a new general field-homomorphism algorithm or an established original discovery. All review is by actual separate AI tasks; no human peer review or Lean verification is claimed.

## Final acceptance and exact experiments

Task A accepted the saved SC-007 manuscript and implementation without a required correction, and independently ran the 12 new tests once, all passing. The coordinator then completed the full 41-test suite and saved the actual log. Source/result hashes are in research/experiments/generator-SHA256.json.

The generator algorithm rejects all 429 normalized F_27 non-preservers, using one defect value on 408 and two on 21; the three accepted Frobenius maps use all three tests. Every rejection is checked by complete actual moment vectors. Selected larger-field cases cover 18 maps in each of two F_81 presentations and 32 maps in F_243, exercising all parameter-selection branches; these are 68 selected maps, not exhaustive general-linear-group enumeration. Thirty-eight scaled-Frobenius controls include full-bound executions.

For each of the 81 possible single-query positions over one F_81 presentation, the annihilator construction supplies a map with a zero answer at that position and a separately verified rejecting witness elsewhere. Those 81 transcript-specific constructions contain only eight distinct maps. Both counts are recorded; no distinctness inflation is intended. Their span-dimension histogram is 3 of dimension one, 6 of dimension two and 72 of dimension three. The general lower bound is established by the proof, not by this finite check.

Hosted run 39105897724 for the complete generator mathematical commit 8836e29869569f3098c20a961f202e9df46d8db3 succeeded. The coordinator fetched the job and every verification step as successful; see CI_GENERATOR_CHECKPOINT.json. This receipt checkpoint changes no mathematical source, tests or deterministic experiment output.

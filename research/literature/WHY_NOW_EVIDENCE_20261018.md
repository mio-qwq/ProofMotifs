# Why-now evidence and competing explanations

Read date: 18 October 2026. This is a bounded primary-source audit, not a
systematic review. The explanatory research question remains open.

## A controlled-system comparison is stronger than a proof motif count

[Feng et al., Towards Autonomous Mathematics Research, arXiv:2602.10177v3,
6 March 2026](https://arxiv.org/html/2602.10177v3), Sections 2.1–2.3 and 5.1:
the study varies inference compute on fixed benchmarks and compares an agent
with a generator/verifier/reviser harness to its base-model system. Section 5.1
retests the 13 Erdős tasks selected because the full agent succeeded: the
comparison system solves eight at roughly twice the mean compute. This is a
success-conditioned subset, not an unbiased all-task agent effect. The authors
also report comparable-compute research-prompt comparisons and selected-sample,
version, grading and tool limitations. These support investigating compute,
retrieval and verification/revision as candidate explanations. They neither
code cancellation nor isolate its causal role. Model/version changes and agent
changes must not be conflated. The statement that a new mathematical tool is
necessary is not tested.

## A different system supplies an independent competing mechanism

[Hubert et al., Olympiad-level formal mathematical reasoning with reinforcement
learning](https://www.nature.com/articles/s41586-025-09833-y), published online
12 November 2025; Nature volume 651 (2026), pp. 607–613. Inspected abstract,
main method and inference-time discussion. AlphaProof combines formal Lean
feedback, reinforcement learning and proof search, with problem-specific
test-time learning at large compute. The study makes a concrete system-level
explanation available for comparison. Its competition benchmark and resources
do not match the OpenAI research release; its results cannot be substituted
for a causal explanation of that release or of all modern AI mathematics.

## Immediate discriminating question

Under a fixed model, task population, tools and resource accounting, compare
ordinary problem solving, matched-information guidance and an explicit
cancellation certificate. Independently grade intended-statement correctness,
not only plausibility or a final numeric answer. Separate witness discovery
from checking a supplied witness. Log failures, abstentions and all attempts.

Such an experiment can estimate the added usefulness of the intervention. It
cannot prove an unrestricted need for new mathematics or identify the full
internal cause of the model's competence. A before/after time series without
matched tasks and resources remains descriptive. No new experiment is claimed
to have been executed in this checkpoint; no paid model evaluation was launched.

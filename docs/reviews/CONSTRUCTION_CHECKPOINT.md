# Construction and composition checkpoint

Date: 2026-10-18. Coordinating acceptance of PM-CONSTRUCTION-0001..0004.
Branch: research/ongoing. Last freshly verified predecessor:
44d83247bae4deb1f6369c7d150f00801393c547, tree
3ffabfb73a5ce21562d22c1bf4114b8235cc4c85. Initial complete GitHub/Git remote
reads found only main and research/ongoing; main was
063f99f67aba436c11feeb8157c1689bd8e82961. Fresh workspace was clean.
Read AGENTS/STATUS/HANDOFF/ROADMAP/CLAIMS and RESEARCH_PROGRAM before writing.
Resolve the containing live commit independently; it cannot name itself here.

## Substantive mathematical outcome

CONSTRUCTION_CONTRACTS.md completes the three-source construction comparison.
It supplies exact interaction-scope, interpolation-geometry and scalar
contraction criteria, then identifies the distinction between one-copy
selection and selection preserved by every independent product. The finite
integral product criterion collapses to positive scalar grading by Gordan's
classical alternative. It explains precisely why the Laurent/middle-coefficient
escape is insufficient for that stronger contract. No novel general separation
theorem or requirement to invent a new tool is claimed.

The constructive baseline solves a15-by20 coefficient system, independently
checks identities off the phase, recovers the source's weights, and constructs
the c3 perturbation. It classifies all64 interaction graphs with57 explicit
quadratic primal patterns and7 balanced-trade obstruction graphs. The general
proof holds for every M>=3; M7 finite checks are corroboration. Hole feasibility
is parametrically separated at equal budgets; the F8 certificate checks
rank5/4, barycentric moments, punctured Gram and72 full affine lines.
Triangle proof-class completeness is proved symbolically; exact scalar ranks,
realized damaged-hypothesis examples and an empty-hole law prevent false
transfer to supersaturation.

## Actual independent tasks and adjudication

All three task-scoped researchers were explicitly configured with
model=gpt-6.1-sol and reasoning_effort=ultra. This records child configuration;
it is not evidence for the coordinating/main model's runtime configuration.
No readable main-model setting was available. No human peer review or Lean
compilation was performed.

| Task | Independent initial question/output | Later cross-review and acceptance |
| --- | --- | --- |
| PM-SYNTH-A | 197/107 source-pinned construction requirements, arbitrary-unary trade, parametric good/bad hole geometry | Separately checked B's triangle proof; independently proved tensor-stability lemma after proposal |
| PM-SYNTH-B | 157 contraction grammar, complete local certificate space, countermodels and raw NulLA baseline | Separately checked A's interpolation/trade proofs, scope and cardinal formula |
| PM-SYNTH-C | Original prior art and adversarial failure tests, separate from A/B proposals | Checked all four integrated propositions, interaction repair classification and all implementations; independently recomputed GF8 with a different representation/solver |

Their complete notes and task boundaries are CONSTRUCTION_A.md,
CONSTRUCTION_B.md and CONSTRUCTION_ADVERSARIAL.md. The coordinator integrated
the proposals and proofs, derived the full graph repair criterion and product
contract, implemented the primary exact solver and checked its reports.

Accepted objections and their resolutions:

1. Unary signed and shifted ordinary degrees *can* select a single copy.
   The degree-two/interactions theorem explicitly requires a nonnegative
   zero-target defect. The all-product theorem explains that requirement,
   while restricting its conclusion to full independent product support.
2. Multiple Fourier selectors change the method and have a cost; they are
   retained as alternatives, not ruled out by the local lower bound.
3. Hole evaluation surjectivity is necessary only for the stated square
   output architecture. Rank alone is insufficient in rectangular cases.
4. Odd-characteristic triangle data do not retain extra self-annihilation
   hypotheses. The counterexample is limited to the local triangle interface.
5. A suggested distinct-map no-hole control with T=I2,a=(1,0) does not retain
   T(x,x)=a(x). An exact assertion exposed this; the integrated stronger
   control and checker use a=(1,1), which does retain it. This was a local
   implementation/construction error corrected before acceptance.
6. Finiteness and rational/integer grading are essential for the product
   equivalence. Explicit infinite-integral and finite-irrational countermodels
   are retained. The new operation is not simply an unrestricted kernel.

## Actual verification commands and boundaries

Executed from the repository root:

```sh
python3 tools/construction_contracts.py > research/experiments/construction-contracts.json
python3 tools/triangle_contracts.py > research/experiments/triangle-contracts.json
python3 tools/construction_boundary_check.py > research/experiments/construction-boundary-check.json
python3 tools/construction_independent_field.py > research/experiments/construction-independent-field.json
python3 -m unittest discover -s tests -v > research/experiments/construction-tests.log 2>&1
awk '/^        run: \|/{block=1;next} /^      -/{block=0} block{sub(/^          /, ""); print}' .github/workflows/verify.yml > /tmp/proofmotifs-replay-all.sh
bash -ex /tmp/proofmotifs-replay-all.sh > research/experiments/construction-replays.log 2>&1
git diff --check
```

The120 existing unit tests passed. The replay log records the actual executed
commands and successful byte comparisons, including all22 historical blocks
and the3 new construction blocks at the time of that run. The subsequently
added independent-field block was executed separately and its command/diff
trace appended to the same log. The final workflow has26 replay blocks.
Use the actual final CI receipt as authority for hosted execution. The four exact JSON
reports include positive and negative certificates. The triangle script was
adapted from B's independent code; the damaged-boundary script from C's code.
Local execution and independent AI mathematical acceptance remain separate
from hosted CI. Do not assert hosted success until its exact run/head/job
records have been inspected; record that in a separate receipt.

Primary reads: four pinned OpenAI source blobs listed in the manuscript and
review notes; original Rauh–Kahle–Ay Definition6/Lemma7; NulLA sections2/3.2;
Gordan's1873 original first-page alternative and official publication record.
The independent audit also records interpolation and summation source ranges.
No third-party bulk source or scripts were executed or redistributed.

## Next mathematical operation

The general local synthesis operations already have established methods.
The unresolved candidate is representation/auxiliary-object choice under
locality, composition and cost constraints. Freeze a bounded repair grammar
and compare its total search cost and output against exact facial-set LP,
NulLA and interpolation supplied the same information. Then select and freeze
an unread target before running transfer. The present phase, prescribed square,
hole templates and contraction evaluations were informed by inspected proofs;
they cannot supply a held-out claim. PM-H1..H5 remain open; supporting orbit
questions and archived connected-normal material remain in their prior status.

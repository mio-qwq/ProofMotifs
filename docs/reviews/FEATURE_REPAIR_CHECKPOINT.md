# Feature-repair checkpoint and coordinating acceptance

Date: 19 October 2026, Asia/Singapore. Initial recovered mathematical head
aca4bff2caf13c501c880f397f6cb750ea4295b2; actual containing predecessor
5a70bf8d8b5105d9eb08a4df2eb0dc1be2be4e7c, tree
e6e937cecb78cbaffebad60917cbd75b281f90d4. Fresh complete branch inventory
found only main and research/ongoing, matching local refs; the workspace was
clean and no other scoped execution was running. Main was
063f99f67aba436c11feeb8157c1689bd8e82961. Read the governing recovery files
and program before writing. This checkpoint cannot name its own future SHA.

## Accepted mathematics and exact scope

FEATURE_REPAIR.md contains PM-REPAIR-0001..0005: exact homogeneous selector/
trade separation; minimum-cost adaptive necessary cuts and NP-completeness;
the failure of initial-ray hitting, including full one-hot blocks; sharp
degree2r and mandatory top monomial on the designed rational grid; and an
explicit Cramer bound making a conventional bounded MILP complete. All are
classical mathematical synthesis or designed applications, not a historical
new-method claim. Formalization NOT_STARTED. No human peer review, AI-causal
experiment or held-out external transfer has occurred.

The algorithm selects feature blocks rather than being given the residual
square. It is still given the complete finite dictionary and legal support.
It does not discover arbitrary auxiliary objects from a raw mathematical
statement. The full-stack existence question needs one LP; minimizing cost
contains weighted set cover. The exact reference implementation uses face
enumeration and a mask-enumerating master, so is not a faster LP or general
polynomial sparse solver. Master lower bounds are actually replayed when
claiming optimality; trades plus a primal without that check would not suffice.

## Independent research ledger and adjudication

Three task-scoped initial proposals were requested independently before
cross-sharing. Each orchestration call explicitly selected gpt-6.1-sol and
reasoning_effort=ultra; this records the readable requested child configuration,
not backend attestation or verification of the coordinating main-model setting.
The latter remains unverified; it was not changed through an unavailable field.

| Task | Initial independent contribution | Subsequent review and reproducible source |
| --- | --- | --- |
| PM-REPAIR-A | Exact finite repair/cuts, sparse trades, set-cover reduction and coefficient bound; original sparse-feature prior art | Independently audited primary KKT oracle and grid theorem; separate basic-support/active-set reference;336 comparisons on80 separate deterministic dictionaries |
| PM-REPAIR-B | Independent sparse-polynomial dictionary construction and exact discovery/checker; safe coefficient-bound proof | Independently proved grid degree distinction; froze its own designed panel and retained an explicit no-oracle-count-advantage outcome |
| PM-REPAIR-C | Independent counterexamples and original literature, including direct combinatorial-degeneration integer programming | Separate target-nullspace/Fourier–Motzkin oracle;134 complete masks;25 stored certificates/20 cuts;756 coefficient-bound controls; adversarial proof acceptance |

Full initial reports, nine-field task ledgers, proof hypotheses, stop/handoff
boundaries and separately marked cross-reviews are FEATURE_REPAIR_A.md,
FEATURE_REPAIR_B.md and FEATURE_REPAIR_ADVERSARIAL.md. Historical statements
that integration was outstanding belong to the initial report stage; the
coordinating disposition here accepts the five integrated statements with
the qualifications below. Independent AI reviews are not human review.

1. **Constant-row qualification.** General input gives a homogeneous/conical
   problem. Ordinary convex-polytope facial terminology additionally requires
   a legal constant row. It cannot be silently added; the unit test contrasts
   A=(1,2) with its explicitly augmented affine version.
2. **Sign qualification.** Trade coefficients are nonnegative only off target.
   Target coefficients may be positive or negative; the grid tensor trade
   and a unit control require that freedom.
3. **No static-ray shortcut.** Optional images of individually broken rays
   can cancel. The full current cone or valid adaptive oracle must be used.
4. **Scaling qualification.** Integral selector weights require clearing
   their evaluated denominators. The M=R!H^(R-1) coefficient bound applies
   to integralized rows, not the original rational rows without rescaling.
5. **No automatic speed/novelty inference.** Some primary panel oracle counts
   improve over enumeration, but B's separate panels show equal counts.
   Costs of table construction/dictionary invention are not block costs.
6. **No held-out relabeling.** Both grid and univariate panels are designed
   calibration. Their designers contemplated their structures before freezing
   concrete inputs. Dense grid input has9^r entries. The unread external
   transfer requirement remains outstanding.

## Actual evidence and commands

Frozen primary protocol: feature-repair-panel.json, SHA256
80e6bc9a1b7e342b304f27539e9a0128846c1c636af775061bb5775d6cfd8ab9.
B's separate frozen input retains its original SHA256
476a983f7b806a7ff1cb4dd0a71ad3fc758f10541e85faeb1697480f2cd68192.
Neither is an external preregistration. Code and reports are versioned under
tools/feature_repair*.py and research/experiments/feature-repair-*.

Actual executed commands, from the repository root:

```sh
python3 tools/feature_repair.py > research/experiments/feature-repair-report.json
python3 tools/feature_repair_boundary.py > research/experiments/feature-repair-boundary.json
python3 tools/feature_repair_independent.py > research/experiments/feature-repair-independent.json
python3 tools/feature_repair_coefficient_bound.py > research/experiments/feature-repair-coefficient-bound.json
python3 tools/feature_repair_reference.py > research/experiments/feature-repair-reference.json
python3 tools/feature_repair_crosscheck.py > research/experiments/feature-repair-crosscheck.log
python3 tools/feature_repair_monomial.py > research/experiments/feature-repair-monomial-report.json
python3 tools/feature_repair_monomial_check.py > research/experiments/feature-repair-monomial-check.json
python3 -m unittest tests.test_feature_repair -v
python3 -m unittest discover -s tests -v > research/experiments/feature-repair-tests.log 2>&1
awk '/^        run: \|/{block=1;next} /^      -/{block=0} block{sub(/^          /, ""); print}' .github/workflows/verify.yml > /tmp/proofmotifs-repair-replay-all.sh
bash -ex /tmp/proofmotifs-repair-replay-all.sh > research/experiments/feature-repair-replays.log 2>&1
```

All127 unit tests passed, including seven mathematical boundary/corruption
controls. The actual shell trace records successful byte comparisons for
all30 workflow replay blocks:26 prior blocks plus4 new blocks, the latter
containing eight discovery/independent-check commands. No failed command is
silently labeled successful. A transient execution-server disconnect was
retried without changing permission or access scope.

Primary results: signed repair cost3; categorical dictionary impossible;
cover b,c,d cost5; grid chooses x^2 y^2 cost5; deleting that feature impossible.
C's separate oracle checks all134 masks, not only reported optima, and all25
stored certificates including20 cuts. A's reference cross-checks336 stacks,
including empty/dependent feature spaces and multi-target spans. C's bound
checker covers756 unit-entry matrices; these are finite controls, not the
general bound proof. B's separate panels cost4 and9, odd-only impossible;
its optimizer-free verifier checks180 cuts and full master lower bounds.

Independent code was preserved, with only repository-relative paths/imports
adapted; B's nondeterministic elapsed-time output was omitted from replay
data. The original frozen input hash remains checked by its program. No
third-party script was executed. Replays use standard-library exact rationals.
Hosted CI must be inspected at the eventual mathematical commit; local success
is not its receipt. Record the fresh run/head/job separately after delivery.

## Primary-source comparison and next operation

The original ITCS2022 paper *Larger Corner-Free Sets from Combinatorial
Degenerations*, Definition21 and section2.3 equation(1), already specifies
integer local zero-target/positive-complement weights and constructs them by
integer programming. This is a direct antecedent to the proposed operation.
The original Hooker–Ottosson manuscript section5 Theorems1–2 covers the
valid-cut/finite-master pattern. Bradley–Mangasarian–Street1998's original
publisher abstract explicitly optimizes separating-plane feature count;
its full theorem was not substituted for a same-contract comparison. Exact
links, versions, read ranges and further sources are in the manuscript and
adversarial report. No lack-of-search-hit originality argument is used.

The finite-dictionary optimizer is now an explicit **existing-tool baseline**.
Next freeze a genuinely unread external target and its available information
before solving, then seek structural dictionary/auxiliary-map generation or
compression with a parametric cost bound. Compare equal-information methods,
including combinatorial degeneration and polynomial synthesis. Do not repeat
small panel masks or treat a provided candidate list as invention from the
problem itself. PM-H1..H5 remain open; archived connected-normal and old
orbit-existence questions retain their previous supporting status.

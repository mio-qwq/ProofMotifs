# Fifth-cycle collaboration and review record

Date: 2026-10-18. Baseline: remote `research/ongoing` checkpoint `2e990a7`.

The coordinator used three genuine short-lived research tasks. They did not
create permanent branches or write repository files. Their initial work was
independent; the coordinator integrated, re-derived and tested the result.

| Task | Question and assumptions | Expected output and stop condition | Result |
| --- | --- | --- | --- |
| PM-SC007-PRIOR | Assess exact deterministic `Q`-only bounds; no claim of direct-`T`, randomized or bit complexity | Primary-source comparisons and a value decision; stop after nearest models are separated | Accepted correctness and scope; generator/Jordan core is classical, restricted oracle packaging may be specific but is not a strong standalone result |
| PM-SC008-STRUCTURE | Remove additivity only after testing opposite-pair signs | Derive the observable quotient and rigorous lemmas; stop before asserting a general hypergraph classification | Proved the sign kernel, quotient hypergraph, edge formula, F_9 count and an exact F_27 incidence route |
| PM-SC008-ADVERSARY | Challenge any claim that order preservation forces additivity or semilinearity | Produce a concrete negative map and small-field exact checks | Found the one-pair sign flip, independently obtained F_9/F_27 counts, and warned that F_81 power-map checks are not a full automorphism search |

## Coordinator resolution

The independent-sign objection is decisive. The project rejects the proposed
direct classification of arbitrary preservers as additive semilinear maps.
The accepted theorem is instead the exact semidirect-product reduction through
the zero-sum hypergraph on square classes.

The two mathematical tasks independently agreed on the quotient and the F_9
and F_27 counts. The coordinator checked the structural proof, re-ran exact
enumeration with repository arithmetic, added complete `27^3` label comparison
for the explicit nonadditive map, and separately checked the general degree
formula in F_9, F_27 and F_81.
The coordinator then strengthened the enumerator with forced third-vertex
propagation and classified all 160 F_81 quotient automorphisms, not merely the
multiplicative power maps.

The prior-art task's conclusion is adopted: SC-007 remains a supporting
restricted-oracle result. The coordinator additionally located Buratti-Nakic's
published square embedding of projective points, which narrows any novelty
claim for SC-008.

## Remaining objections

* The general semilinear quotient classification is only a conjecture.
* A bounded F_243 prototype exceeded 30 seconds and was terminated without a result.
* Shared repository finite-field arithmetic is still a common dependency.
* The backtracking program is exact but is not a proof assistant.
* No human review or Lean verification exists.
* Historical originality remains unresolved; the square embedding is known.

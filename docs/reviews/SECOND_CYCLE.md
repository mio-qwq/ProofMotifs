# Second-cycle proof and adversarial review

Same-coordinator sequential review; no independent researcher or Lean verification.

## SC-003

Initial proposal: rank, characteristic and proper-subproduct orders determine the full order. Rejected by the explicit pair of full-rank F_27 triples. Revised objective: classify all characteristic-three triples via e_1 and e_2. The multinomial calculation gives orders 5 and 7; both vanishing cannot hide an untested higher term because the support has at most eight points. A separate Frobenius/translation argument proves the zero case. Degenerate directions and coincident support points remain in the statement and tests.

Literature challenge: the subset-defect formula and p-degree reasoning are already established in combinatorial polarization. Retain the exact statement and witness with novelty unverified; do not claim a new method.

## SC-005

First preserver proposal: every additive order-preserving bijection is scalar-Frobenius. Adversarial enumeration found all six normalized bijections of F_9 preserve ternary order, although only two are Frobenius. Record the exception rather than removing the field.

Revised statement: scalar-Frobenius outside F_9; all additive bijections on F_9. Algebraic proof uses the family (1-t^2+t,1-t^2-t,-1-t^2), whose transformed quadratic sum is T(1)T(t^2)-T(t)^2. At most six excluded parameters must be removed before applying the root bound. For q>=27 the remaining number exceeds 2q/3, forcing a polynomial identity. Distinct base-three exponent patterns force only one linearized coefficient.

Checks: linearized representation is proved by injectivity and finite cardinality; no perfectness assumption is smuggled in. The q=3 and q=9 cases are handled separately. Sufficiency relies on coefficients in F_3; it must not be generalized to unchanged arbitrary K-valued coefficients. Counterexamples are to project proposals, not to published open conjectures.

Exact verification: all 439 normalized bijections in the three tested fields; accepted maps checked against all actual triple-order labels and rejected maps supplied with a first differing triple. A second F_27 multiplication algorithm using discrete exponents agrees on all 729 products. An F_81 rejection test covers an even extension beyond the exceptional field. These remain same-author computational checks.

Remaining gaps: independent mathematical review; Lean proof and semantic correspondence; complete prior-art implication audit; held-out application. Neither passing CI nor the strength of the statement removes these gaps.

# Independent AI review and constructive cycle

Date: 2026-10-18. Source checkpoint: `4f6db95fe5b72c12bdbfc875026f47698735f817`.

## Actual collaboration

The coordinating researcher used four genuine task-scoped subagents in a single shared project. No permanent agent branches were created. Initial assignments were independent; mathematical objections and improvements were exchanged only after those first derivations. The coordinator integrates and publishes the checkpoint.

All tasks assumed an additive bijection in characteristic three, used the pinned SC-003/SC-005 proofs as evidence rather than authority, prohibited unrelated edits and remote writes, and ended at a bounded mathematical handoff. These are AI reviews, not human peer review or proof-assistant certification.

| Task | Question and scope | Independent work and expected output | Stop condition and handoff |
| --- | --- | --- | --- |
| PM-REVIEW-20261018-A | Audit every step and boundary of SC-005; read only | Re-derive moments, zero-weight case, conic identity, root bound, exponent separation, F_9 exception and converse; identify defects | Completed: accepted the pinned proof without a mathematical correction; supplied detailed reasoning to the coordinator |
| PM-WITNESS-20261018-B | Construct a strict order-7 to order-5 witness | Derive conic degeneracy and defect identities independently, then challenge proposed basis tests and the arbitrary-field extension | Completed mathematical derivation; writes only SC-006/RESULTS.md; handoff contains proof, costs and limitations |
| PM-AUDIT-20261018-C | Adversarial boundaries and nearest primary prior art; read only | Challenge small fields, zero coordinates and polynomial/function distinctions; inspect original preserver literature | Bounded literature handoff; exact hypothesis comparison is recorded separately |
| PM-COMPUTE-20261018-D | Implement and challenge the finite extractor | Independently check the defect algebra; own only tools/constructive_witness.py and tests/test_constructive_witness.py; verify outputs using complete actual moments | Handoff includes exact commands, query counts, repair example and limitations; no commit or push by the subagent |

## Accepted audit of SC-005

Task A independently checked the inclusion-exclusion coefficients through degree seven. On writing A=a^2, B=b^2, C=c^2, the simultaneous equations e_1=e_2=0 imply

`(X-A)(X-B)(X-C)=X^3-ABC`.

Injectivity of the cubing map in a field forces A=B=C; the directions are therefore on one prime-field line and their threefold difference is zero. This excludes a missing higher-order branch.

The review also checked the transformed conic identity, the strict inequality q-6>2q/3 for q>=27, distinct base-three exponents, the finite linearized-polynomial representation, the F_9 projective-line argument, and the moment-level Frobenius converse. No logical defect was found. This changes the separate AI-review field, not the originality or formalization fields.

## Challenges that changed the next proof

The handoff's uniform q/3-6 bound omitted an available parity refinement: the degenerate set is empty for odd extension degree and consists of F_9 minus F_3 for even degree. On the conic e_2=-(t-t^3)^2; a nonzero defect cannot occur in F_3. Thus a nondegenerate parameter with nonzero defect always gives a strict 7-to-5 change.

The coordinator proposed testing the quadratic defect on basis vectors and their pairwise sums. Tasks A, B and D independently checked the coefficient argument. Task B observed that the final repair value can be inferred after two additional defect evaluations; an implementation may directly check it as a third evaluation. The distinction between an oracle bound and the running time of a table-based experiment is essential.

The coordinator then proposed removing the finiteness hypothesis. Tasks A and B independently accepted the extension after checking the exceptional embedded F_9, the repair step, arbitrary field automorphisms, and finite-support Vandermonde detection. Infinite-field automorphisms must not be restricted to Frobenius powers. The infinite-field statement is a written theorem, not an infinite computational check.

Task A subsequently audited the saved SC-006 manuscript and the standard-basis implementation, accepted both, and independently ran all nine new tests successfully. One documentation objection was accepted and corrected: all q moments are sufficient to certify a zero weight, but they are not necessary when the support is smaller. The optional adapted-basis improvement is proved but not implemented. The coordinator's later manuscript edits only add source/review links.

## Limits

There is no human referee report or Lean compilation in this cycle. Reviewers share the same model family and project assumptions; their separate derivations do not remove common-mode risk. Historical priority remains unresolved. Source-specific prior-art inspection can downgrade the originality assessment even when the proof is correct.

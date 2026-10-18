# ProofMotifs

**Structural Cancellation, Proof Mechanisms, and Cross-Domain Mathematical Discovery**

ProofMotifs investigates reusable mathematical proof mechanisms and the exact conditions under which cancellation survives composition and changes of representation. It does not assume that superficially similar proofs share a new underlying theory.

[Claims](CLAIMS.md) · [Current status](STATUS.md) · [Roadmap](ROADMAP.md) · [Reproduction](REPRODUCIBILITY.md) · [Prior art](research/literature/INITIAL_REVIEW.md)

## Research checkpoints

The unified `research/ongoing` branch contains current research. `main` is the stable governance baseline. The results have written proofs and exact finite computational checks. The ternary preserver results have separate task-scoped AI reviews; no Lean verification or human peer review is claimed.

| Workstream | Result | Originality status |
| --- | --- | --- |
| SC-001 | Leading moment of additive convolution and characteristic-sensitive failure of order additivity | Classical reproduction |
| SC-002 | Saturated differences, finite additive subspaces and Moore leading coefficient | Classical reproduction |
| SC-003 | Ternary first differences in characteristic three have finite order 5 or 7; rank and proper orders do not determine the outcome | Novelty not established |
| SC-005 | Additive bijections preserving every ternary cancellation order on F_{3^m}: scalar-Frobenius maps except for F_9, where all 48 additive bijections qualify | Novelty not established |
| SC-006 | Construct strict order-loss witnesses using quadratic-basis tests; extend the preserver statement to arbitrary characteristic-three fields, retaining F_9 as the exception | Novelty not established; classical cone-preserver theory is close prior art |

The current verification system uses exact arithmetic and deterministic enumeration, including a separate F_27 multiplication algorithm. The first research checkpoint was replayed successfully on GitHub Actions. CI success is not human peer review or proof-assistant verification; each run's commit and scope are recorded explicitly.

## Research scope

The initial focus is finite-support moment functionals, positive-characteristic differences, failure of under-specified transfer certificates, and exact structure-preserving maps. The source corpus currently contains targeted calibration cases, not a representative sample of AI-generated or human mathematics. No statistical predominance of cancellation or universal new framework is claimed.

## Integrity and provenance

AI systems make substantive contributions to research, exposition and software in this project. Mathematical correctness, finite computation, formalization, independent review and historical priority are assessed separately. Classical tools are credited; failed proposals and exceptions remain in the record. Third-party sources are pinned and linked rather than republished as a bulk corpus.

## Licensing

No project-wide license has been selected. Original software and mathematical documentation have a separate licensing proposal pending approval. Third-party rights remain unchanged. There is no final academic paper release or DOI associated with this startup checkpoint.

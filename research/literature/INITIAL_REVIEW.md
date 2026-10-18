# Initial literature and provenance review

Research date: **2026-10-18**. This is a targeted startup review, not a complete historical-priority certification. Directly inspected original source sections are distinguished from abstracts and publisher metadata. No count of search queries is used as a substitute for evidence.

## Correction of the project's preliminary framing

[Ying Xie, *What the Machine Invented*, arXiv:2610.17090v1](https://arxiv.org/html/2610.17090v1), submitted 12 October 2026, analyzes 38 problem families and discusses eleven repeated proof patterns. The body already discusses reuse and proposed cross-domain transfer. Therefore neither motif mining nor 'adding transfer' is an original research agenda by itself. Its novelty judgments are provisional and it reports no Lean recompilation. This project must differentiate through specific proved statements and genuinely new applications, not a broader label. Inspected: abstract, introduction, method/limitations and transfer discussion; no verification of all extracted instruments.

## Source-collection facts

The pinned [OpenAI README](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/README.md) reports 719 manuscripts, 372 families and approximately 4,000 attempted problems. Its [history](https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/history.md) reports 300/719 top-line formalizations and three withdrawals. These are upstream catalogue statements, not an independent recount, proof audit or measure of accepted discoveries. Earlier conversational assertions of initial counts and dates are not imported as independently established facts.

The history lists the withdrawal update under October 7, 2026; the individual Weil-classes notice says withdrawn October 6. Preserve this notice/log-date distinction. The sign error invalidates a required cancellation premise; the notice does not say the theorem is false. Source cards and the mechanism comparison record the exact affected argument.

## Closest mathematical prior art

| Source | Checked material | Relevance and decision |
| --- | --- | --- |
| [Stacks Project, 07GK](https://stacks.math.columbia.edu/tag/07GK) | Definition 23.2.1 and adjacent explanation | Divided powers multiply with binomial coefficients. SC-001 is classical algebra, not a new formalism. |
| [Lucas coefficient proof](https://larryriddle.agnesscott.org/ifs/siertri/LucasProof.htm) | Author exposition; coefficient identity also reproved in SC-001 | Carry-free criterion is known. No priority claim. |
| [Aichinger-Moosbauer, arXiv:1912.08448](https://arxiv.org/abs/1912.08448) | Bibliographic record and abstract; full-text HTML unavailable in this pass | Functional degree and finite differences on abelian groups are established. Full source comparison remains necessary. |
| [Clark-Schauz, arXiv:2305.01304v1](https://arxiv.org/html/2305.01304v1) | Sections 1.3 and 4.1, including the group-ring action and p-weight discussion | Strong overlap with any proposed difference/augmentation filtration. Ordinary moment order for a fixed weight is not the same invariant as functional degree of a function. |
| [Subspace Polynomials and Cyclic Subspace Codes, arXiv:1404.7739v3](https://arxiv.org/html/1404.7739v3) | Subspace-polynomial definitions and elementary lemmas | SC-002 uses established linearized polynomials and interpolation. |
| [Fresnel-Matignon, On the Moore determinant](https://ems.press/journals/rsmup/articles/13549914) | Publisher metadata and abstract | DOI 10.4171/RSMUP/142; online 2023, volume 153 (2025). No assertion that this review checked every theorem of the paper. |
| [Waldron, Refinements of the Peano kernel theorem](https://www.math.auckland.ac.nz/~waldron/Preprints/Peano/peano.html) | Author abstract page | Vanishing moments and analytic remainder representations already have a theory. Future analytic work must compare precise hypotheses. |
| [Lai, Higher Order Derivatives and Differential Cryptanalysis](https://link.springer.com/chapter/10.1007/978-1-4615-2694-0_23) | Publisher record | Important boundary for SC-003. Full-text theorem comparison is still outstanding. |

## Automated proof reuse and proof mining

[REFACTOR](https://arxiv.org/abs/2402.17032), submitted February 2024, extracts reusable intermediate theorems from **Metamath** proofs. Do not describe it as a Lean experiment. [MathlibLemma](https://proceedings.mlr.press/v306/liu26ez.html) reports 1,506 kernel-checked proofs; its [arXiv paper](https://arxiv.org/html/2602.02561v3) distinguishes these from a larger set of type-checked statements. Those numbers are author-reported, not rebuilt here. [Lean Graph Search](https://arxiv.org/html/2610.22339) already uses proof dependencies for retrieval; this is not a proof that any extracted mathematical mechanism is novel.

[Applied Proof Theory](https://link.springer.com/book/10.1007/978-3-540-77533-1) and [Kohlenbach's bibliography](https://www2.mathematik.tu-darmstadt.de/~kohlenbach/) document proof mining in its established quantitative/logical sense. The present project must not implicitly claim to invent that field. Creative telescoping, Prouhet-Tarry-Escott identities, sign-reversing involutions and character orthogonality remain required background; their full theorem-level survey is not completed in this checkpoint.

## Live adjacent result requiring follow-up

[Croot-Mao-Yip, arXiv:2609.05061](https://arxiv.org/abs/2609.05061), *The Prouhet--Tarry--Escott problem for subsets with small doubling in integral domains*, is a particularly relevant recent lead. The abstract concerns equal power sums and characteristic-sensitive barriers. Its HTML fetch failed; do not infer its detailed theorems from the title or claim a novelty comparison has been completed. Prioritize the original full text before proposing sparse equal-moment constructions as new.

## Candidate-by-candidate novelty decisions

PM-THEOREM-0001: an immediate binomial-algebra result, with the classical Lucas criterion. **Level 0.**

PM-THEOREM-0002: finite-group fiber counting plus subspace-polynomial interpolation and Moore determinants. **Level 0.**

The prospective ternary unsaturated classification in SC-003 has an exact computational lead and a short symbolic route. Its precise prior-art comparison remains open: **Novelty not yet established.** A short derivation is useful for the project but does not itself imply a publishable new theorem.

No result in this review establishes a new universal theory, statistical predominance of cancellation in AI proofs, or a successful held-out cross-domain discovery.

## Second-cycle additions and stronger overlap warning

The original HTML of [Drapal-Vojtechovsky, arXiv:1509.05707v1](https://arxiv.org/html/1509.05707v1) was inspected at section 2.1, Lemma 3.1, Theorem 4.8 and Corollary 4.11. It already defines the precise inclusion-exclusion defect and develops the p-degree mechanism, including the noninvertibility of factorials. SC-003 is not an invention of combinatorial polarization. The exact order classification and rank-only counterexample may be a useful packaged consequence, but priority is unverified.

The abstract of [arXiv:1410.4095](https://arxiv.org/abs/1410.4095) confirms pre-existing higher-order differentiation over general finite fields. Full-text comparison remains outstanding.

The original [Yip, arXiv:2407.21362, section 1](https://arxiv.org/html/2407.21362) was inspected for the Carlitz-McConnel preserver context. Its hypotheses restrict difference quotients to a multiplicative subgroup or a suitable direction set. SC-005 instead requires preservation of ordinary moment order of ternary differences by an additive bijection. The conclusion's scalar-Frobenius form is certainly not new as a general phenomenon. It is not yet established whether the specific cancellation-order condition and F_9 exception are already covered elsewhere. A proof using classical tools does not settle this historical question.

Searches combining additive maps, conic preservation, finite fields, third differences and cancellation order returned substantial noise as well as these relevant sources. No unsuccessful exact-string search is treated as evidence of novelty. The full theorem-to-theorem implication check, especially finite-geometry and preserver literature, is the next priority for PM-THEOREM-0004.

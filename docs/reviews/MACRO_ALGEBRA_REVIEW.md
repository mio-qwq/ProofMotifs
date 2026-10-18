# PM-UNIFY-A review ledger

Date: 2026-10-18. Companion to `/tmp/pm_unify_a_note.md`.

## Scope

Repository `/workspace/scratch/2a838d5cea65/ProofMotifs` was read-only. The only files written by this subtask were `/tmp/pm_unify_a_note.md` and this ledger, through apply_patch. No Git writes were performed. This is a theorem/proof and prior-art audit, not a new field enumeration or a novelty certificate.

## Independent mathematical views

View 1: the assigned researcher developed a filtered-group-algebra/difference-certificate approach and the exact digit-sum conversion between moment and augmentation orders. Main question: what extra data turns annihilation into a composable/transportable operation, and where does augmentation lose information?

View 2: a real task-scoped agent, `/root/unification_algebra_ultra/dual_view`, was assigned an independent derivation before receiving the candidate theorem. It independently proposed the finite-field moment transform as an algebra isomorphism with a truncated Hurwitz/divided-power algebra, and derived augmentation order as the minimum p-digit-sum of a nonzero moment. After comparing results, it confirmed extension to arbitrary finite F_p-subspaces of a characteristic-p field. This extension discussion was not blind; the original finite-field derivation was independent.

The independent view also independently identified the C_2 idempotent-augmentation obstruction in characteristic different from 2. It agreed with the Z^2/scalar-geometry obstruction and supplied the exact interpolation transfer matrix, including its p-weight triangularity for additive maps.

## Adversarial followup on the completed note

The same task-scoped agent was then explicitly instructed to attack the candidate statements, inspect missing hypotheses, and distinguish a meaningful transport theorem from a redundant one. This is a separately labeled adversarial pass by the second mathematical researcher, not a third independent researcher. A third-person adversarial review remains outside this subtask.

Objection A, material: T2 originally assumed the target observable filtration was itself lowered by every target difference. That already implied target annihilation, making transport redundant. Without that assumption the pullback calculation implies vanishing only on the image of T; global target vanishing requires T to be surjective. Resolution: removed target lowering, stated image-only vanishing and the explicit pointed identity, and added the surjectivity condition for a global conclusion.

Objection B, material hypothesis: the annihilator paragraph originally followed an arbitrary-ring/module theorem with an unqualified double-annihilator argument. Resolution: specialized the equality to a finite regular group action over a field with the full function space. For arbitrary finite G-sets, specified the submodule I^(d+1)k[X]. Did not extend double annihilation to general coefficient rings.

Objection C, integrability: the convolution statement specified compact support for mu but was linguistically ambiguous about nu. Finite first nonzero moment orders alone do not imply the absolute moments required at order r+s. Resolution: required both measures compactly supported. The reviewer supplied the counterexample mu=delta_1-delta_0 and nu=sum_(n>=1)8^(-n)delta_(4^n)-(1/7)delta_0: both have order 1 and finite first absolute moment, but the disjoint signed atoms in the convolution have infinite absolute second moment.

Checks with no fatal objection: Vandermonde/moment theorem for V not a subfield; sharp bound at r=0, p=2, m=0 and the top nilpotent degree; abelian action convention; multivariate exact moment-order additivity over R/C once integrability is fixed; author-hosted divided-power citation; additive-map interpolation triangularity.

The reviewer validated the final direct transfer idea: push each involution pair through any map into R^d, rewrite it as a translated additive difference, then convolve r such measures and apply the r-th mixed derivative bound. The assigned researcher wrote its full proof as T4.

## Evidence classification

T1-T4: written proofs provided in the companion note; classical mechanisms and elementary consequences, no novelty claim. Formal verification: not performed. Human peer review: none. Separate external adversarial researcher: outside this subtask.

The independent agent reported exact checks of the binomial moment identity on all delta-basis pairs for q=4 and q=9 and digit-generator coefficients. The assigned researcher did not independently rerun or preserve those code outputs; these reports are supplemental and are not used in place of the proof.

Primary-source checks: author/publisher pages for Passi, Jennings/Quillen metadata, Aichinger-Moosbauer arXiv v1 sections 2/4/12, Clark-Schauz sections 1.3/4, Grinberg-Reiner Exercise 1.6.4, Stacks divided powers, and Drapal-Vojtechovsky polarization were inspected. Original full-text publisher fetches for Passi 1968, Jennings 1941 and Quillen 1968 failed. The companion note explicitly limits those citations accordingly.

## Decision

Accept the note as a useful classical unification-and-obstruction result, subject to any additional coordinating review. Reject the stronger proposal that augmentation order alone is a faithful common order for moments, involution cancellation and real geometric cancellation. Existing tools already cover the demonstrated algebraic mechanism; no mathematical necessity for a new instrument has been established.

The next mathematical operation should transfer a certificate to a held-out target with specified observables and geometry, using the explicit adapter or T4, and probe its first failing hypothesis. Explaining AI performance requires separate causal/controlled evidence; this theorem does not supply it.

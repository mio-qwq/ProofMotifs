# PM-UNIFY-D — adversarial macro audit and prospective protocol

Date: 2026-10-18. Independent task-scoped AI analysis. Repository examined read-only; no repository changes, Git operations, outbound correspondence or expenses. This memo addresses the broad explanatory question, rather than attempting another theorem in the finite-field branch.

## Judgment

The present evidence supports studying explicit cancellation certificates as one reusable proof genre. It does not support cancellation as the distinctive explanation of recent AI progress, nor establish that mathematics requires a new universal tool. The proposed empirical study is worth doing only if it can return a clear negative result. A definition that includes every equality or kernel membership cannot do that.

The existing repository is appropriately cautious: README, corpus PROTOCOL, mechanism COMPARISON and DISCUSSION_GATE explicitly reject population inference from the targeted examples. However, PROTOCOL says H1–H5 remain untested while the current tree contains no definitions of those hypotheses. The replacements below make the inferential ladder explicit. They are proposed hypotheses, not recovered prior definitions.

The finite-field line may produce valuable mathematics on its own merits. Fifteen iterations selected through the researcher's own interests do not constitute fifteen independent confirmations of the macro explanation. A successful theorem using classical character sums, incidence kernels and Freiman extension would still leave the AI/human and historical-causation questions open.

## A precise representation obstruction

**PM-MACRO-COUNTEREXAMPLE-D1 (elementary; exact).** Work over any field F. Let V=F², x=(0,1), and l(x₁,x₂)=x₁. The evaluation l(x)=0 contains one zero coordinate and no displayed subtraction. Apply the invertible change of coordinates

T = [[1,1],[0,1]],  T⁻¹ = [[1,-1],[0,1]].

Now y=Tx=(1,1), while the same functional in the new coordinates is l'=l∘T⁻¹, namely l'(y₁,y₂)=y₁-y₂. The same evaluation is therefore 1-1=0. The underlying pair (x,l) and its image (Tx,l∘T⁻¹) carry exactly the same information. A count of opposed nonzero terms changes under an invertible representation, without introducing redundant variables or an unproved hypothesis. Characteristic two causes no problem: -1=1 and 1+1=0.

More generally, for a nonzero linear functional l on a finite-dimensional vector space and a nonzero v in ker(l), choose b₁ with l(b₁)=1, extend v to a basis of ker(l), and use the resulting basis of V. In those coordinates l(v) is simply the first coordinate 0. Thus any coordinate-sum cancellation of this kind can be hidden. Conversely, the triangular map above exposes one.

This does **not** show that structural cancellation is meaningless. The invariant fact l(v)=0 survives. It shows that an occurrence count is not a coordinate-invariant measure unless its permitted representations and semantic unit are fixed. Replacing the count by unrestricted 'membership in a kernel' avoids this example only by including every linear equality. Every equality A=B in an additive group already becomes A-B=0. That definition therefore cannot discriminate cancellation mechanisms from mathematics in general.

**Required resolution:** decide whether the estimand concerns (a) the written proof's presentation, (b) a restricted family of normalized representations, or (c) semantic structural certificates. For (a), call the result a style measurement. For (b), publish the normalization and acknowledge its limits. For (c), require an independent certificate and a demonstrated consequence as below, and test equivalent rewrites without claiming invariance under every possible equivalence.

An adversarial benchmark must contain the D1 pair, the factored/expanded pair (x-1)(x+1)=x²-1, an involution proof with its paired sum already quotiented out, and a lemma call with its body expanded. A purely semantic label should agree; a presentation label may differ but must say why. Padding with g-g must never increase the semantic occurrence count.

## Operational annotation rule

Use a **semantic lemma application** as the occurrence unit and a **problem family** as the population unit. Count a family at most once for prevalence; preserve subtypes and multiple applications separately. Do not count tokens, minus signs, uses of `simp`, or multiple manuscripts of one family as independent evidence.

Assign `STRUCTURAL_CANCELLATION=yes` only when an annotator can fill all four fields:

1. **Aggregate or operator:** identify the sum, integral, trace, pairing, alternating operator or other fixed operation, with scalar domain and convergence conditions.
2. **Independent certificate:** identify a symmetry, involution, character relation, moment condition, finite-difference identity, simplicial relation, or another predeclared structural condition. It cannot merely restate the particular target equality.
3. **Consequence:** state an exact vanishing, removal of a specified leading part, or a quantitative gain relative to the uncancelled estimate. Record the comparison explicitly.
4. **Proof role:** cite the application in the submitted proof and the downstream conclusion it enables. This is dependency within that proof, not a claim that no other proof exists.

Use `no` for routine algebraic normalization without an independent certificate/gain. Use `uncertain` when source access or the lemma's mathematical meaning is insufficient. An annotator may nominate `OTHER_CANDIDATE`, but a new subtype discovered on the test set cannot be added retrospectively to the primary positive count.

Keep the following fields independent:

- `presentation`: explicit, hidden in lemma/library, or absent;
- `certificate_type`: involution, orbit/character, moment/orthogonality, telescoping, chain-complex identity, filtration/leading-part, or preregistered other;
- `vanishing_order`: exact order with definition, zeroth order, or unknown; do not call every mean-zero argument high order;
- `gain`: exact zero, quantitative scale/order gain, or none;
- `role`: background lemma, supporting step, central dependency, or unknown;
- `validity`: asserted only, checked local lemma, full proof independently checked, formal statement checked, kernel recompiled, withdrawn/invalid, or unknown;
- `discovery_provenance`: model-generated, human-supplied, retrieved known theorem, computationally guessed, or unknown;
- `bottleneck_evidence`: none, author narrative, contemporaneous search trace, or randomized intervention;
- `novelty`: established prior art, new combination, candidate extension, or unresolved after specified search.

Do not infer one field from another. A cancellation can occur in an invalid proof. A verified proof can use a classical mechanism. A central dependency can have been easy to retrieve while a different construction was the hard part.

### Coding examples

| Example | Primary code | Why / needed boundary |
| --- | --- | --- |
| An integrable b has ∫b=0; subtract F(z), then use Lipschitz control and radius s to obtain |∫Fb|≤Ls∫|b| | Yes: moment, zeroth order, scale gain | Independent mean-zero hypothesis; quantitatively stronger than a bound using sup|F|. Dropping mean zero with F=1 breaks the claimed gain. |
| A fixed-point-free sign-reversing involution pairs weighted chains | Yes: involution, exact zero | Must prove admissibility, involutivity and sign reversal. Merely writing a desired pairing is insufficient. |
| Finite-field power sums with degree below q-1 | Yes: field/character structure, exact zero | State coefficient field and degree bound; the excluded monomial X^(q-1) is a negative boundary. |
| Telescoping ∑(a_(i+1)-a_i)=a_n-a_0 used to control accumulated error uniformly | Yes: telescoping | Record endpoint control and actual improvement over summing individual magnitudes. |
| d²=0 proved from alternating face maps and simplicial identities | Yes: chain-complex certificate | Established structural machinery. This does not certify that an unrelated identity has such a complex. |
| A=B rewritten A-B=0 | No | The target is being restated; no independent certificate. |
| `ring` proves two polynomial expressions equal | No by itself | Could hide a genuine structural identity; inspect the semantic lemma before deciding. Tactic name alone is not a mechanism. |
| Bound |∑z_i|≤∑|z_i|, with no stronger estimate | No | No cancellation gain has been used. |
| Injectivity, positivity or a monotonicity proof with no aggregate certificate | No | These proof genres must remain eligible negatives. Do not manufacture a zero identity after seeing the proof. |
| Orthogonal projection removes a subspace component | Borderline until specified | Yes if the annihilated component and gain are explicit; no if 'projection' merely renames the answer. |
| A known helper theorem returns a zero sum, but its body is unavailable | Uncertain mechanism; occurrence claim recorded | A black-box conclusion does not establish its mechanism. |
| Claimed involution misses fixed points; signed count is nonzero | Occurrence asserted, validity failed | Include in failure/withdrawal accounting. Do not promote to a successful mechanism or remove from a fixed historical sample. |
| AI proof expands 300 terms; human proof invokes the same determinant identity | Same semantic label, different presentation | Match proof genre and library visibility. Expansion length is not additional semantic occurrence. |

## Independent draft hypotheses: not the controlling PM-H numbering

The H1–H5 labels below record the reviewer's independent proposal. The controlling identifiers are PM-H1–PM-H5 in research/RESEARCH_PROGRAM.md: capability, prevalence/enrichment, causal utility, existing-tool gaps, and instrument value. In particular draft H1/H2 both inform controlling PM-H2; do not silently substitute these labels.

### Testable versions and rejection conditions

The numerical effect margins below are **illustrative design choices**. Freeze them, the target population and analysis before labels are revealed. Twenty AI families plus ten human controls can calibrate coding and yield intervals; it is not a realistic confirmatory design for all five claims and several strata.

| ID | Bounded hypothesis / estimand | Evidence needed | What would count against it |
| --- | --- | --- | --- |
| H1: common mechanism | More than half of the independently selected released AI families use a valid structural cancellation application central to the submitted proof: p>0.5. Also report any-use p separately. | Family-level random/stratified sample from a pinned catalogue, complete eligibility/exclusion manifest, independent validity adjudication, interval for p. | An upper confidence bound below 0.5 rejects this majority version. A wide interval is inconclusive. Many uncertain labels make the question unresolved, not positive. |
| H2: AI enrichment | Within matched theorem/subject/genre sets, the AI minus human probability of central structural cancellation exceeds a predeclared margin, e.g. 0.15. | Prefer alternative proofs of the same statements; otherwise match field, result type, proof length band, publication/formalization genre and era. Paired outcome with family clustering. Verified human/AI provenance. | Effect near zero or reversed after matching; observed difference disappears when hidden library applications are exposed or equivalent proof summaries are used. High prevalence in both supports a common genre, not AI specificity. |
| H3: causal contribution to solving | In a fixed solver, verified cancellation certificates/schema assistance increase held-out solve rate beyond equal-budget neutral structural assistance; effect is larger on independently coded relevant tasks. | Randomized interventions with the same target premises, comparable general examples, token/tool/compute budgets and no target-solution leakage; proofs graded blind for correctness, statement faithfulness and non-circularity; all attempts/timeouts retained. | No gain against active controls, gain only with answer leakage, or equal gain on negative tasks. Post hoc counts in solved manuscripts do not test H3. |
| H4: cross-domain transfer | A schema frozen on development subjects yields a predeclared success improvement, e.g. ≥0.10, on unseen families from a subject excluded from schema design. | Domain/family holdout, input assumptions and certificate extractor frozen, baseline tools equally available, exact predicted sublemma or theorem independently checked. | It works only after domain-specific hypotheses are supplied from the target solution, transfer drops assumptions, or an equally resourced known-method baseline matches it. |
| H5: added value of a new tool | The proposed abstraction improves held-out correctness or proof/search cost beyond both existing-theorem retrieval and a composition engine under a fixed budget. | At least three arms: nearest-art library/retrieval, existing-method composition engine, proposed tool; common solver, interfaces, examples and verification; an independently checked bridge theorem or explicit algorithm. | Benefit vanishes after baseline receives the same lemmas/representation, or abstraction only renames an already supplied conclusion. This rejects incremental value in the tested setting, not all possible future utility. |

H3 is an operational intervention hypothesis, not a complete answer to **why now**. An old/new model × schema/active-control study, holding tools and compute fixed, can test whether the recent model gain is concentrated on schema-relevant tasks. It still changes many model properties at once. A historical mediation claim requires training/data/tool ablations or credible contemporaneous development evidence. Final proofs alone cannot identify what caused their discovery.

The unrestricted phrase 'no existing mathematics can solve this without a new tool' has no empirical rejection rule. A proved helper theorem can be inlined; a definitional abstraction can be expanded. Thus logical necessity is generally the wrong target. A meaningful necessity statement must specify a restricted calculus, representation or oracle model and prove a lower bound there. H5 tests practical value, not such a universal necessity theorem.

## Selection, denominator and confounding audit

Let C be structural cancellation, S a correct solved attempt, and R inclusion in the public release. A targeted collection typically observes P(C | S=1,R=1), or less if correctness has not been independently checked. It does not observe P(S | C), all model attempts, or the causal effect of enabling C. If release inclusion depends on success, novelty, formalizability or rhetorical prominence, those selection paths can create associations. Conditioning again on 'has Lean' adds another filter.

The release-only population is still a legitimate target, but it must be named exactly. The approximate attempted-problem total cannot serve as an individual-level denominator without the attempt manifest and outcome records. No inference about all AI mathematics follows from a release-only sample.

Required controls:

1. Freeze family catalogue/revision, eligibility, grouping and adjudication date before coding. Separate manuscripts, families, theorem statements and attempt runs.
2. Include withdrawals and failed proofs according to the frozen time rule; retain original inclusion and subsequent status. Report valid-mechanism prevalence and asserted-mechanism prevalence separately.
3. Sample without cancellation keywords, celebrated-problem filters, availability of a chosen mechanism, or formalization success. Stratify only by declared neutral metadata.
4. Match human controls to mathematical content and proof genre. A polished human paper versus verbose generated Lean code mostly measures exposition and library boundary choices.
5. Treat AI involvement as provenance requiring evidence; an unrelated GitHub owner is not proof of human authorship. A pre-LLM source helps provenance but may mismatch mathematical era/library coverage.
6. Separate retrieval of known arguments, experimental computation, construction of a witness, proof checking and proof discovery. Each can be the actual scarce resource.
7. Record human problem selection, prompting, supplied lemmas, repair and editing. A released artifact is the endpoint of that workflow, not automatically an autonomous model run.
8. Do not use validity, novelty, formalization or significance as proxy labels for one another. Check formal statement faithfulness in addition to kernel acceptance.
9. Preserve negative genres such as compactness, extremal choice, induction, positivity, rigidity and classification. Some contain genuine cancellation; their presence must not be automatically recoded after seeing the result.
10. Report label uncertainty and source incompleteness. Do not discard hard-to-code cases after inspecting their mechanisms.

## Paired blinded coding and holdout execution

### Stage A — calibration only

Use the five current source cards plus independently selected positive, negative and borderline examples. Two coders label them independently using the four-field rule. Discuss disagreements, revise the codebook, then freeze it. The existing finite-field and MUB materials belong here; they cannot become unseen transfer evidence. Record coders' prior exposure.

Include an equivalent-rewrite audit: prepare 10–20 pairs varying coordinates, factoring/expansion, lemma inlining and notation. Each member receives a separate randomized identifier and is split across batches so the coder does not see its pair nearby. Semantic-label disagreement reveals representation sensitivity; explanation must identify a genuinely changed mathematical certificate rather than a surface minus sign.

### Stage B — blinded development study

An independent selector freezes the sampling manifest from the full catalogue before mechanism inspection. The selector logs metadata-only strata and exclusions. A preparer removes author names, repository names, AI branding, novelty boasts and obvious formatting signatures while preserving the mathematics and assumptions. Perfect blinding may be impossible; each coder guesses source class and confidence afterward to measure leakage.

Both coders independently label every sampled proof in an identical mathematical template, including negative and uncertain labels and exact evidence spans. Do not have one coder see only AI and the other only human proofs. Do not let the selector be the sole mechanism adjudicator. Human alternative proofs and AI proofs of a matched theorem get separated identifiers and randomized order.

Report the full confusion table, raw agreement, positive agreement and negative agreement; report a chance-corrected measure with its prevalence limitations rather than using one coefficient as a pass/fail oracle. Predeclare a reliability gate, for example ≥0.85 raw agreement and ≥0.75 positive agreement on central cancellation. Failure means revise/recalibrate and obtain a fresh sample; never silently modify a rule until the desired prevalence appears. If only AI coders are available, name that limitation: independent contexts reduce anchoring but do not establish independent human judgment.

Resolve disagreements in a third pass with both rationales visible and a separate mathematical validity reviewer where practical. Preserve initial labels, adjudicated labels and reasons. Primary estimates use the predeclared treatment of uncertainty; also provide worst-case bounds taking all uncertain cases as yes versus no.

### Stage C — locked confirmatory and transfer holdouts

Reserve families, not manuscript variants. When a family uses a crucial imported companion theorem, place that dependency cluster in one partition. For transfer, hold out an entire subject domain or structural object class as well as fresh families. Hash the manifest and freeze the codebook, schema, examples, baseline libraries, prompts, model version, search budget, verifier access and stopping rules before opening target solutions.

No target solution, extracted target lemma, or target-specific counterexample should be available to the proposing solver. A separate evaluator may hold sealed solutions and decide correctness. Log all attempts, seeds, tool calls, costs, timeouts and repairs. A failed target is not replaced. Any target-driven change becomes a new development cycle and needs a fresh holdout.

Use paired randomization within each task for algorithmic comparisons and a fixed number of independent seeds. Report task-level effects and uncertainty, with task/family clusters as independent units; thousands of correlated attempts do not create thousands of independent mathematical problems. Choose one primary endpoint (e.g. fully correct proof within fixed budget) and one primary contrast. Treat subtype/domain analyses as exploratory unless powered separately.

Twenty AI families and ten controls are a pilot, especially for a 0.15 difference. At p=0.5, a sample proportion from twenty independent families has a standard error about 0.112 even before stratification/uncertainty; two small groups provide still less precision for a difference. Determine a larger confirmatory sample from the frozen primary effect and desired interval width/power; do not declare success because a small pilot's point estimate looks large.

## Primary external evidence checked for this audit

All accessed 2026-10-18. These sources document competing explanations or limitations, not a causal explanation of the particular OpenAI release.

- **Ying Xie, arXiv:2610.17090v1**, https://arxiv.org/html/2610.17090v1, especially lines 317–384 and 1525–1529 in the retrieved HTML. The paper selects 38 families for problem prominence, describes eleven patterns and says its work did not identify a new foundational theory. It is a mechanism-discovery source, not a neutral prevalence sample. The present protocol adds testable discrimination rather than claiming motif mining itself is new.
- **Hubert et al., AlphaProof**, https://www.nature.com/articles/s41586-025-09833-y, published online 12 November 2025, journal volume dated 2026. Retrieved sections Training, Inference and Inference-time scaling. The authors describe pretrained mathematical/code knowledge, Mathlib supervision, Lean feedback, reinforcement learning, tree search and problem-specific training. They report improved held-out solve rates as search and test-time learning increase. This is direct evidence that resources and search procedure can change success while the theorem statements remain fixed. It does not show cancellation is irrelevant or identify the release's causal process.
- **Trinh et al., AlphaGeometry**, https://www.nature.com/articles/s41586-023-06747-5, published 17 January 2024, especially empirical evaluation and Extended Data Figs. 3–5. The authors report a decomposition of solved-task gains from algebraic deduction and learned auxiliary construction. They also describe failures involving missing established higher-level rules and a human coordinate proof much shorter than one generated proof. This supports including representation, existing-tool coverage and construction search as active alternatives. It is not evidence about open research conjectures generally.

No reproduced training run, recompiled formal development, human review, complete literature certification or new empirical result is claimed in this audit. The elementary coordinate counterexample above is self-contained.

## Concrete next operation

Freeze a macro-study charter containing the target population, H1–H5 versions, semantic codebook and failure criteria. Then prepare a small balanced calibration/rewrite batch and have two independently instructed coders label it blind. Do not start a 20-family prevalence count before this reliability/representation check. In parallel, inventory attempt-level provenance and exact human counterpart proofs; absence of those records limits the causal question but does not block a clearly scoped release-only descriptive study.

An informative outcome may be: cancellation is common to AI and human proofs; recent AI progress is better predicted by search, library coverage and verification; the useful product is a certificate-aware retrieval/composition system. That would refute the distinctive universal-cancellation narrative while still yielding a valuable research program. A stronger outcome requires the prospective transfer and active-control evidence above.

## Independent review of the coordinator's new charter

Reviewed read-only on 2026-10-18: `research/RESEARCH_PROGRAM.md` in full and the new controlling tops of ROADMAP, AGENTS, STATUS and HANDOFF. **Accept as the governing research charter, with the following substantive corrections before it is treated as an empirical preregistration.** No premature finding or unsupported endorsement of cancellation is present. The move back from default finite-field orbit continuation to capability, mechanisms, existing tools and proposed-tool value responds to the user's macro objective. It preserves negative outcomes and does not discard prior mathematics.

1. **Retain the historical question explicitly.** 'Why specified systems succeed' can become a static catalogue explanation and lose the user's 'why now'. Name comparative model/time/resource evidence as an axis: what changed in search, training, retrieval, verification, libraries and human workflow, and which observed gains survive fixed-task/fixed-budget comparisons. Final proofs alone cannot settle that axis. The current H3 caveat is correct, but there should also be a concrete deliverable for this part of the original question.
2. **Distinguish two H1 denominators.** A release audit can estimate a checked fraction conditional on release; an attempt-level solve rate requires the attempt manifest and compute/stopping policy. Missing attempt records should prohibit the latter inference, without blocking correctness/dependency audits of accessible individual claims.
3. **Make recurring occurrence and AI enrichment separately reportable.** New PM-H2 appropriately asks enrichment, but it should still report the two component prevalences and uncertainty. High occurrence with no matched difference is an informative result, not a failed annotation exercise. My earlier H1–H5 labels are proposals using a different numbering; adopt the charter's new PM-H numbering when integrating, rather than silently swapping meanings.
4. **Do not call the charter itself a completed test specification.** Its five rows are research questions and evidence requirements. The codebook must still freeze population, positive/negative/uncertain criteria, primary endpoint, effect/precision criterion, handling of withdrawals and unknowns, representation checks and stopping rules. The existing 20-family/10-control number lower in ROADMAP should be explicitly a calibration/pilot target, not a confirmatory promise.
5. **Separate synthesis value from mathematical novelty.** The charter already does this well. An efficient hypothesis-checking/retrieval/composition tool can be the main positive result even if all constituent mathematics is established. A failed literature reduction is a research lead, not evidence of a missing theory; unrestricted necessity remains unclaimed.

The new top-level recovery instructions consistently prioritize the macro program over older narrow 'next' paragraphs. Retaining the old chronology is acceptable because the supersession is explicit. Integrate the independent-certificate rule and coordinate counterexample into the upcoming annotation document; they are the most important guard against a category that expands after seeing the evidence.

## Final independent mathematics/scope audit of PM-UNIFY-A

Reviewed `/tmp/pm_unify_a_note.md` in full, read-only, after the reported repairs to regular-action, field, surjectivity and compact-support hypotheses. **Verdict: accept T1–T4 and C1–C3 as written within their stated scope, as an independently checked elementary mathematical bridge in established theory.** This is written-proof review, without execution, formal compilation, historical-priority certification or human review.

### T1: moment coordinates, augmentation powers and functional degree

The generality of a finite F_p-linear subspace V of any characteristic-p field K is valid; V need not be a subfield. Closure under addition supplies the group-algebra product, and q distinct field elements supply the invertible q-by-q Vandermonde transform. The binomial convolution identity proves multiplicativity of the first-q-moments map into the truncated divided-power algebra. Lucas digitwise coefficients yield the truncated-polynomial presentation. Its monomial total degree is s_p(n), giving exactly the displayed I^r description and minimum digit-sum formula.

The sharp ordinary-moment lower bound follows by filling the lowest p-adic digits first. Both endpoint r=m(p-1) and m=0 are handled. The saturated-difference deduction uses a genuine group basis and its actual smaller support, so the Vandermonde equality argument is legitimate. The 5/7 comparison does not equate scalar ordinary order with augmentation order: it demonstrates their discrepancy correctly.

The observable adapter is also valid. An arbitrary map has a unique interpolation on V; additive pullback preserves finite-difference degree. The perfect-duality argument and T1 identify the exact functional-degree basis even when V is not a subfield. Hence the digit-sum triangularity assertion is justified. This is a complete coordinate conversion, not a claim that one scalar order determines the other.

### T2: modules, actions, duality and transport

The main statement uses an abelian group and the specified action, so composition of the displayed differences is coherent. The mixed-difference certificate follows from the generators of the augmentation ideal. The target conclusion is correctly limited to T(X), with surjectivity required for vanishing on all Y. Pullback compatibility is substantive; target lowering is not assumed circularly.

The perfect-pairing/double-annihilation assertion is correctly confined to a finite regular group action over a field. For a general finite G-set, the note correctly substitutes I^(d+1)k[X]; for a general ring it does not claim field double duality. Associated-graded nonvanishing is exactly the criterion for preserving a specified finite order under the induced filtered map or product. The coefficient-ring and action repairs therefore remove the material overgeneralizations.

### C1–C3: necessary obstructions

The modular p-cycle identity is correct and does not imply vanishing for every observable; the free-orbit indicator is an effective negative example. For a characteristic-not-two involution, I²=I follows from (tau-1)²=-2(tau-1), so an I-adic module order can be infinite even though ordinary first moment is nonzero. The involution does not satisfy ordinary polynomial-degree lowering in general, as the swap calculation shows. The Z² real-scalar example has augmentation order one, mass and first moment zero, and second moment 2-sqrt(2), as stated. These examples prevent the common certificate language from being misrepresented as one faithful universal order.

### T3: analytic assumptions and exact convolution order

The Taylor estimate is valid for finite signed/complex measures with the stated bounded support and C^r control on a neighborhood of the relevant segments. The r=1 Lipschitz version is valid separately. For the exact convolution-order assertion, compact support of **both** factors ensures existence of the required moments and Fubini/convolution operations. Finite nonzero leading moment orders exclude the zero-measure case. The homogeneous leading polynomials multiply, and R[ξ] or C[ξ] has no zero divisors, so exact order r+s follows. This step would require revised integrability hypotheses without compact support.

The translated mixed-difference bound requires derivative control on every parallelepiped reached by the actual certificate, including translation by h_j and z. It supplies quantitative data absent from augmentation membership alone. The affine and degree-e polynomial pushforward conclusions have the correct lower-order guarantee, and the x↦x² negative example is exact.

### T4: the concrete cross-mechanism bridge

The construction works for arbitrary h_i because each signed orbit pair pushes forward to a difference of two target atoms. No equivariance or translation action on the original X_i is needed. For a tuple of representatives x_i, set

b_i=h_i(tau_i x_i),  a_i=h_i(x_i)-h_i(tau_i x_i).

The derivative domain for the resulting summand is precisely the set

z + sum_i b_i + sum_i t_i a_i,   0<=t_i<=1.

A C^r neighborhood of the union of these finitely many parallelepipeds with ||D^r f||<=L is sufficient. Repeated one-dimensional fundamental-theorem integration gives the bound L product_i ||a_i||. Summing absolute tuple coefficients factors into product_i C_i. There is no missing factorial: the mixed-difference integral is over a unit cube, whereas the Taylor estimate uses a simplex/factorial remainder. Polynomials of total degree less than r are annihilated by those r differences. All measures here are finite atomic, so no integrability or convolution-exchange issue remains.

An independent nondegenerate check also proves the constant one cannot be uniformly reduced: take every X_i={0,1}, tau_i the swap, w_i(1)=1, w_i(0)=-1, and h_i(1)=1, h_i(0)=0 in R. Then C_i=1 and eta=(delta_1-delta_0)^(convolution r). For f(t)=t^r/r!, the r-th derivative equals one and integral f d eta=1. Thus the displayed product-cost bound is attained, and this example has exact ordinary order r.

### What the accepted bridge establishes, and what remains open

T4 is more than renaming a kernel: it gives an explicit observation adapter, an actual convolution construction, an auditable finite-difference certificate and a quantitative target estimate. Together with T1/T2 it demonstrates that several mechanisms already have concrete bridges in established algebra and analysis. It is therefore fair to call this **a concrete cross-mechanism bridge within existing theory**.

The necessary scope limits are:

- General T4 gives order **at least** r; eta can vanish identically or have higher order. One involution alone does not imply arbitrary higher-order cancellation; the r-factor convolution is extra structure.
- C_i is the cost of the supplied pairing, independent of the choice of orientation of each pair. It is not claimed to be an optimized transport cost or a representation-invariant complexity measure.
- The constructed convolution need not be the natural quantity in an unsolved target problem. A separate application must show why this construction is useful there and how its hypotheses are obtained without target-solution leakage.
- These statements do not constitute a held-out cross-domain discovery, a new mathematical method, evidence of new-tool necessity or an explanation of an AI system's internal/discovery mechanism.

No further mathematical repair is needed before integrating the note with these scope statements. Stating r>=1 explicitly in T4 and spelling out its derivative domain would improve precision, but the existing intended interpretation is already sound.

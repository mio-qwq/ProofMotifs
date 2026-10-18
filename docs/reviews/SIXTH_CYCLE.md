# Sixth-cycle review: external acceptance and general classification

Date: 2026-10-18. Verified starting remote:
`bfe32279b502fd07ec646d4a7f173808d0ad8a2a`.

The coordinator first accepted the recovered SC-008 increment through proof
inspection, 46-test replay, byte-identical experiment regeneration, source
hash checks and fresh hosted-CI reads. See
[external acceptance](EXTERNAL_SC008_ACCEPTANCE.md). The recovered result
was reused; its completed small-field search was not mistaken for an
unproved all-degree classification.

## Actual task ledger

All tasks assumed the explicitly defined characteristic-three square
zero-sum hypergraph, with historical novelty and formalization unestablished.
They used the shared research branch without separate permanent ownership.
Only the coordinator integrated shared state and published commits.

| Task | Research question and initial evidence | Allowed output and stop condition | Handoff |
| --- | --- | --- | --- |
| PM-CYCLE6-A | Can incidence equations reconstruct the ambient affine space? SC-008 quotient and exact small fields were known | SC-009 manuscript, exact incidence-rank tool and tests; stop at a complete reduction/certificate or identify the gap; no shared-state edits or push | Independently proposed the affine-kernel criterion, computed exact ranks through F_243, then derived four-edge completion and Freiman extension |
| PM-CYCLE6-B | Can F_243 be classified without backtracking? Began independently of A's rank route | Color-certificate tool, tests and explanation; stop at a sound complete group bound or explicit obstruction | Equivariant refinement gives upper bound 605; 605 verified known actions attain it; separate recurrence/log arithmetic reconstructs all edges |
| PM-CYCLE6-C | Which discussion claims and nearest literature can actually guide the research? | One bounded literature/evidence report, primary-source checks and adversarial objections; no other edits or push | Read one publicly extracted Zhihu answer; separated its useful structural motivation from broad unsupported claims; accepted affine extension and withdrew the diagonal objection after checking the F_3 codomain |
| PM-CYCLE6-D | Do the completion gadgets survive exact small-field and degeneracy checks? | Completion tool and meaningful negative-control tests; stop at bounded exact checks, no infinite inference | Exhaustive F_27/F_81 and normalized F_243 relations all complete; real F_9 failures preserved |
| PM-CYCLE6-E | Independently challenge all general-proof algebra, constants, roots, exceptional cases and classical hypotheses | Read-only proof audit; stop with a complete accept/reject verdict and reasons | Accepted every step; independently recomputed base ranks with a separate row loop and checked published Weil/Carlitz statements |

E's additional counting subtask was interrupted and supplied no completed
handoff. It is not counted as another independent review. E personally
completed the audit recorded in [SC009_GENERAL_AUDIT.md](SC009_GENERAL_AUDIT.md).

## Coordinator's mathematical resolution

The new invariant is the F_3 incidence kernel, not an assumed full affine
geometry. A minimal kernel implies that each coordinate of a hypergraph
automorphism extends affinely. Its image spans the field, so the linear part
is invertible. Summing over the square subgroup kills the translation.
Classical Carlitz then gives square-scaling composed with Frobenius.

For all q>=243, the four-edge gadget converts the line equations to every
Freiman two-sum equation. Distinct roots justify the multiplicative Weil
bound; deleting four roots costs at most 32 in the unnormalized indicator
sum, giving `(q-38-11*sqrt(q))/16>0`. The exact S-S count and three-translate
intersection give a well-defined additive extension. This proves affine
kernel equality for m>=5. Exact nonzero minors and independent affine
kernel vectors finish m=3,4. PM-CONJECTURE-0002 is therefore proved as
PM-THEOREM-0013, subject to the stated classical inputs rather than any
novelty assumption.

The coordinator checked the complete manuscript, the gadget subtraction,
all six root collisions, threshold positivity, both finite certificate
implementations and the full suite. The scalar/sign description is kept
separate from a canonical group splitting: choosing opposite-pair
representatives gives the abstract split sign kernel, while a global sign
is redundant in the explicit formula for maps.

## Objections preserved

1. Could a repeated vertex make a gadget equation unavailable? No. In
   characteristic three a repeated zero-sum triple has three equal entries,
   and its F_3-valued equation is automatically zero. No extra exclusions
   belong in the completion bound. C's initial conservative objection was
   withdrawn after checking this point.
2. Does characteristic three invalidate the cubic character bound? No.
   This is a multiplicative quadratic-character sum; squarefreeness and
   non-square status are the relevant conditions, and distinct roots
   establish both. No degree-coprime-to-characteristic hypothesis is used.
3. Does a discrete coloring falsely assume all automorphisms were listed?
   No. Every transition is equivariant and independently checked. The
   two-point stabilizer is trivial; orbit-stabilizer supplies an upper bound,
   and the known full edge-preserving set supplies a matching lower bound.
   Unsafe extra color splits are explicitly rejected by a negative test.
4. Does finite rank prove the infinite theorem? No. Finite minors are used
   only for degrees three and four; the character-sum/Freiman proof covers
   every larger degree. F_243 also has two finite certificates for audit.
5. Can the F_9 exception be discarded? No. Its hypergraph has no edges,
   incidence nullity four exceeds affine dimension three, and a delta
   function violates a Freiman relation while satisfying every line equation.

## Reproduction and limits

The combined local suite passed all 65 tests. Saved exact reports are
`incidence-rank-results.json`, `color-certificate.json`,
`color-verification.json` and `freiman-completion-results.json` under
`research/experiments`. The actual suite log is `sc009-tests.log`;
`sc009-SHA256.json` records sources, tests, reports and audit documents.
The workflow replays each new deterministic report and separately invokes
the color checker's independent arithmetic path.

The rank and completion tools share the existing field engine. The color
checker supplies separate multiplication via the alpha recurrence and
cyclic logs, but all computations remain software certificates, not Lean.
The independent reviews are AI reviews; no human peer review occurred.
Classical Weil, Freiman extension, incidence reconstruction and Carlitz are
credited. The bounded literature search found close methods, not a direct
priority certificate: originality remains unverified. The broad forum
claim and a universal cancellation framework are not established by these
finite-field results.

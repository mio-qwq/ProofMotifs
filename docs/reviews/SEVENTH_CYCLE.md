# Seventh-cycle review: value gate, Fourier proof and cyclotomic extension

Date: 18 October 2026. Verified starting remote:
`31f3d3936c654fc4d24c8246144c3308bb0570f7`.

The coordinator first confirmed through terminal fetch and the authorized
GitHub interface that this was still the live `research/ongoing` head and
that its tree was `80f96b3c683c8cd4417b2d3cb83e467c1f21e737`. The checkout used
for this cycle was detached directly from that remote head; the older local
divergent branch was not merged or rewritten.

## Actual task ledger

All tasks were read-only and task-scoped; only the coordinator edited shared
research state and publishes. Historical novelty, human review and Lean were
outside each task's evidence.

| Task | Question, assumptions and evidence | Scope and stop condition | Handoff |
| --- | --- | --- | --- |
| PM-CYCLE7-A | Does finite-geometry, incidence-code or local-Paley literature directly imply SC-009? | Primary-source bounded audit; stop at a theorem-by-theorem hypothesis comparison; no edits/push | Close but not direct: full AG codes, the full nonzero zero-sum design, and the square embedding all omit the induced-square extension step |
| PM-CYCLE7-B | Is the restricted Freiman step already an additive-combinatorics theorem? | Random/dense/restricted Freiman sources; distinguish method from exact deterministic theorem | Difference-map extension is established; no inspected theorem derives all Freiman relations from only square zero-sum triples |
| PM-CYCLE7-C | Adversarially assess value and overbroad claims | Counterexamples plus one next-operation recommendation | Provisional Level 1; density, `m=2`, arbitrary-subgroup and other-characteristic generalizations need explicit guardrails |
| PM-CYCLE7-D | Find an independent structural proof of SC-009 or report the blocking identity | Avoid the four-edge proof; exact derivation required | Multiplicative Fourier decomposition gives a uniform all-`m>=3` proof using root bounds, Frobenius orbit dynamics and one cubic Weil sum |
| PM-CYCLE7-E | Challenge the proposed fixed-index cyclotomic theorem | Verify indicator/root correction, thresholds, gadget and extension; reject on one gap | Accepted the theorem; required explicit `chi^0(0)=1` and conservative root-deletion wording |
| PM-CYCLE7-F | Search for subgroup counterexamples and audit D | Exact small controls; challenge any scalar--Frobenius endpoint; then read the complete Fourier proof | Accepted the Fourier proof; found decisive `F_81` endpoint counterexamples and limited the general conclusion to the linear setwise stabilizer |

No task was reported as human review. All six were genuine task-scoped AI
researchers, not role-played reviewers.

## Coordinator decisions

### SC-009 value

The audit does not locate a direct theorem for the defining-characteristic
kernel of affine three-point lines wholly inside the nonzero squares. It does
locate every surrounding mechanism: full affine Reed--Muller duality,
automorphisms of the full nonzero zero-sum design, the projective square
embedding, Paley/cyclotomic graph automorphisms, character-pattern counts,
Freiman difference extension and Carlitz/McConnel.

Decision: retain correctness and provisionally classify the precise bridge as
Level 1, not Level 0 and not Level 2+. Historical priority remains
`NOVELTY_UNVERIFIED`. The exact comparison is in
`research/literature/INCIDENCE_VALUE_GATE_20261018.md`.

### Independent Fourier proof

The coordinator checked every step in `workstreams/SC-009/FOURIER_PROOF.md`:
normalization, the exact size of `R`, scalar extension and semisimplicity, low
and high polynomial bounds, both interval cases, and the order-two exclusion.
Task F separately accepted the same proof. Exact spectra in `F_27`, `F_81`
and `F_243` are respectively

`{0,1,3,9}`, `{0,1,3,9,27}`, `{0,1,3,9,27,81}`.

The even-degree control finds 24 nonsquare `s` in `F_81` with `s^2+1` square,
and exponent 20 fails explicitly at `(a,b,value)=(4,7,2)`. These are finite
sanity checks, not the uniform proof.

Decision: accept this as a genuinely independent proof of PM-THEOREM-0013.
It removes the logical dependence on the `m=3,4` rank certificates, although
those certificates and the completion/Freiman proof remain valuable separate
checks. Fourier decomposition, Lucas and Weil are classical tools; the second
proof does not upgrade novelty or formal-verification status.

### PM-THEOREM-0014 and endpoint objection

For a multiplicative subgroup of index `d>=2`, the order-`d` character
indicator gives

`N_k >= (q-B_k(d)*sqrt(q)-k*d^(k-1))/d^k`.

The `k=4` bound forces every Freiman relation by the same four-edge gadget;
the `k=2,3` bounds produce the difference extension. Task E accepted all
constants and degeneracies. Thus the stated polynomial threshold proves the
affine kernel.

The coordinator accepts Task F's objection to a stronger endpoint. An
additive map stabilizing one index-`d` subgroup need not preserve every
cyclotomic coset, so Carlitz/McConnel does not apply for `d>2`. In `F_81`, the
index-16 subgroup has five vertices, no edges, and both kernel and affine
restriction dimension five; its linear stabilizer is `S_5` of order 120,
not the 20 scalar--Frobenius maps. The index-5 subgroup has kernel dimension
six and a still larger Hamming-type stabilizer. These examples do not meet
PM-THEOREM-0014's threshold, but they refute the invalid endpoint inference.

Decision: the unconditional conclusion under the polynomial threshold stops
at `Stab_GL(m,3)(H)`. A scalar--Frobenius corollary is stated only under the
separate, much stronger generalized-Paley condition from Ponomarenko's 2025
preprint.

## Reproduction and limits

The integrated suite now has 74 tests. New deterministic outputs are
`cyclotomic-incidence-results.json` and `fourier-incidence-spectrum.json`.
The workflow replays both. The small-field code uses the project's existing
exact arithmetic; it is software evidence, not Lean. `lean` and `lake` were
not installed, so the proposed abstract `completion_to_affine` formalization
was not started or claimed.

The next gate is a targeted comparison of the uniform Fourier/cyclic-code
proof with defining-characteristic cyclic-code and punctured Reed--Muller
literature. If that route is also standard, retain both proofs as robust
infrastructure. Do not optimize the sufficient cyclotomic threshold without
an application, and do not infer generalized-Paley normality from incidence
affinity alone.

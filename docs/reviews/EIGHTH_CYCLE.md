# Eighth-cycle acceptance and continuation

Date: 2026-10-18. Verified starting remote:
`21999eb36433620d4557f01627f8ff53fc5a9fa7`.

## Remote inventory and recovered work

The GitHub branches endpoint and a fresh full fetch found exactly two remote
branches, `main` and `research/ongoing`. The recovered mathematical increment
was on `research/ongoing`: commit
`3ab50849fa7a61ff3cae220dd21ea1feb74fc97d`, followed by receipt commit
`21999eb36433620d4557f01627f8ff53fc5a9fa7`. The clean local checkout was
fast-forwarded rather than replacing the external increment.

It supplies a second, uniform multiplicative-Fourier proof of SC-009 and
SC-010's sufficient fixed-index cyclotomic affinity theorem. The latter's
unconditional automorphism endpoint is the ambient linear setwise stabilizer.
Its further scalar/Frobenius corollary retains the separate large-field and
even-subgroup-order hypotheses of the cited Ponomarenko preprint.

The coordinator replayed all 74 tests, regenerated the two new reports byte
for byte and verified every file in `sc010-SHA256.json`. The acceptance log
is `research/experiments/sc010-acceptance-tests.log`. Earlier manifests remain
historical snapshots at their own commits; they are not assertions that
subsequently extended documents retain old hashes.

Fresh GitHub run and job reads confirmed run
[39113374667](https://github.com/mio-qwq/ProofMotifs/actions/runs/39113374667)
and job 117634030262 completed successfully at mathematical head `3ab5084`,
with the unit suite and eleven deterministic replay steps. This agrees with
the persisted receipt. The shared Git author does not identify which exact
execution produced the increment.

## Genuine scoped task ledger

All tasks retained the same repository and common roadmap. Only the
coordinator accepted results, edited shared state and published commits.
No permanent agent branches were created.

| Task | Question and evidence | Scope and stop condition | Accepted handoff |
| --- | --- | --- | --- |
| PM-CYCLE8-E | Does the recovered Fourier proof really work in every degree, including parity endpoints and the cubic count? | Read-only independent adversarial derivation; stop at a full verdict or a concrete gap | Accepted base change, semisimple decomposition, root bounds, both orbit intervals and the order-two exclusion; full audit preserved separately |
| PM-CYCLE8-A | Are SC-010's composite-character bound, extension and endpoint valid? Can the finite failures be explained structurally? | First read-only source/algebra audit; then only the three SC-012 manuscript/tool/test files; stop at an exact theorem with explicit exceptions | Accepted SC-010 and independently checked the polynomial witnesses; derived and implemented the two-subspace family |
| PM-CYCLE8-B | Can the new Fourier viewpoint yield a smaller exact rank certificate? | Only the three SC-011 manuscript/tool/test files; stop at a replayable certificate with negative controls and accurate group claims | Classical cyclic gcd criterion; polynomial-only F_243 certificate and F_81 proper-orbit control; same-kernel/different-group boundary |
| PM-CYCLE8-E2 | Independently challenge the proposed infinite two-subspace family | Read-only proof review; stop at all-degree acceptance or one failure | Accepted subgroup realization, punctured-space kernel, connected components, wreath group, explicit extra Fourier mode and the e=1 exception |

The coordinator re-derived the polynomial rank argument and group boundary,
read the exact new source and tests, and checked the complete family proof.
The reviews are AI reviews, not human peer review or Lean verification.

## Continuation 1: compact cyclic certificate

SC-011 applies the classical cyclic-code ideal description. For selected edge
orbits, `d=gcd(Z^N-1,p_e)` gives row rank `N-deg(d)`. The F_243 certificate
supplies divisibility quotients and a full Bezout identity proving

`gcd(Z^121-1,1+Z^4+Z^68)=(Z-1)(Z^5+2Z+2)`.

The checker proves its field identification, irreducibility, generator order
121 and true zero-sum seed using only F_3 polynomial arithmetic. It neither
constructs field tables nor trusts a matrix rank. The selected 121-edge orbit
already forces the full six-dimensional affine kernel of all 1,210 edges.

An important objection was retained: that sparse edge orbit is not Frobenius
invariant. Equal row codes do not imply equal combinatorial automorphism
groups. Affine extension/Carlitz bounds the sparse group, and the five exact
Frobenius orbit patterns show that it is C_121, while the full group has
605 elements. PM-COUNTEREXAMPLE-0006 records this project boundary. The
checker verifies finite polynomial and orbit identities; the full group
conclusion additionally uses the explicitly cited mathematical theorem.

The F_81 negative seed has cyclic rank 25 rather than 35, so an arbitrary
edge orbit cannot silently replace all constraints. False Bezout,
divisibility, irreducibility and Frobenius claims are rejected by tests.

## Continuation 2: an infinite structural obstruction

SC-012 replaces the isolated F_81 index-five failure by a family. For
s=3^e, e>=2, the subgroup `F_s* union beta*F_s*` in F_(s^2), with beta^2
a nonsquare in F_s, is two independent punctured e-dimensional subspaces.
The kernel has dimension 2e+2, one above ambient affine dimension 2e+1.
The extra direction is the order-two multiplicative character u^(s-1).

The internal line hypergraph has two connected components. Its automorphism
group is `GL(e,3) wreath S_2`, exactly the ambient linear stabilizer despite
the extra kernel direction. Thus minimal affine kernel is sufficient, not
necessary, for linear extension. For e=1 the four vertices are isolated and
the full group is S_4; only the two-component group argument is exceptional.

The program uses direct F_3 vector coordinates, without GF(729) tables. It
checks the explicit nonaffine function, exact ranks in e=2,3 and all 40,320
permutations of the eight-point component. The large full-group orders follow
from the written wreath-product theorem and are not claimed enumerations.

## Sources, value and verification limits

The coordinator inspected Ponomarenko's primary preprint, Theorem 1.1 and
Remark 5.2, and Pavone's published Theorem 3.4. Pavone applies to each
punctured component with p=3, k=3, e>=2; it does not directly treat an
arbitrary induced multiplicative subgroup. The proofs here remain explicit.
Classical cyclic ideals, punctured-space designs, Hamming decomposition and
disjoint-union automorphisms are credited as Level 0 infrastructure/boundaries.
No historical-first claim or new universal theory follows.

The combined suite passed 89 tests; the actual log is
`research/experiments/sc012-tests.log`. Deterministic new reports are
`cyclic-incidence-certificate.json`, `cyclic-incidence-verification.json` and
`two-subspace-results.json`; their hashes, sources and reviews are recorded in
`sc012-SHA256.json`. New CI steps regenerate and verify all three reports.
Hosted success is to be checked at the actual containing mathematical commit.

The exact next target is PM-QUESTION-0001: whether a single suitable
multiplicative edge orbit can span the full square incidence code in every
degree. Compare cyclic-code precedents before a proof or counterexample
search. The two new boundaries remain controls: equal kernels do not determine
the edge automorphism group, and a minimal affine kernel is not necessary for
linear extension. Avoid threshold polishing or unrelated tables.

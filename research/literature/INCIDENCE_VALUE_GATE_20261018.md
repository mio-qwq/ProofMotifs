# SC-009 incidence-affinity value gate

Date: 18 October 2026. This is a bounded primary-source comparison, not a
priority certificate. Absence of a located theorem does not establish
historical originality.

## Decision

SC-009 is provisionally Level 1: a narrow technical synthesis whose tools are
classical but whose exact deterministic bridge was not found in the inspected
literature. The potentially uncovered statement is only this:

> On the nonzero squares in `F_(3^m)`, the equations on affine three-point
> lines wholly contained in the square set force every Freiman two-sum
> equation, so the defining-characteristic incidence kernel consists exactly
> of affine restrictions.

The Weil estimates, difference-map extension, full affine-geometry code,
square projective embedding, Paley/Carlitz classification and semilinear final
step are established infrastructure. No Level 2 claim, historical-first claim,
human review or formal verification follows from this audit.

## Exact source comparisons

1. **Full affine incidence code.** Key--McDonough--Mavron, *Reed--Muller
   codes and permutation decoding* (2009),
   [postprint](https://users.aber.ac.uk/tpd/papers/reed-muller-pd-sets-postprint.pdf),
   identifies the ternary code of all lines of `AG(m,3)` with the appropriate
   generalized Reed--Muller code; standard duality leaves affine functions.
   SC-009 deletes both all points outside the square set and all line checks
   not wholly contained in it. This is not ordinary puncturing or shortening.
   The `F_9` nullity `4>3` is an exact counterexample to any formal inference
   from the full geometry.

2. **Full nonzero zero-sum design.** Pavone, *Subset sums and block designs in
   a finite vector space*, Designs, Codes and Cryptography 91 (2023),
   [DOI](https://doi.org/10.1007/s10623-023-01213-9), Theorem 3.4 classifies
   the automorphisms of zero-sum `k`-subsets on all nonzero vectors. It does
   not prove that an automorphism of the induced half-set design on squares
   extends to the ambient space. That extension is the role of SC-009's
   incidence kernel.

3. **Square embedding.** Buratti--Nakić, *Additivity of symmetric and
   subspace 2-designs*, Designs, Codes and Cryptography 92 (2024),
   [DOI](https://doi.org/10.1007/s10623-024-01452-4), Theorem 5.1 and Example
   5.3 identify the projective square embedding and zero-sum four-point line
   blocks over `F_3`. They do not state the converse kernel theorem for the
   three-uniform relation.

4. **Linear representations and codes.** Sin--Sorci--Xiang, *Linear
   representations of finite geometries and associated LDPC codes*,
   [arXiv:1908.06824](https://arxiv.org/abs/1908.06824), studies the full
   affine point set with selected directions. Its rank theorem assumes the
   coefficient field does not annihilate `q`; Remark 1.2 explicitly says the
   defining-characteristic rank can be strictly smaller. The point set,
   selected lines and coefficient regime therefore all differ from SC-009.

5. **Freiman extension.** Fiz Pontiveros, *Freiman rank of random subsets of
   Z_N*, [arXiv:1004.3709](https://arxiv.org/html/1004.3709v1), Proposition
   2.1 and Observation 2.1 already use the induced difference map and
   translated triples to prove additivity. Conlon--Gowers, *Freiman
   homomorphisms on sparse random sets*,
   [arXiv:1603.01734](https://arxiv.org/abs/1603.01734), works for random
   domains and starts from every Freiman relation. Neither covers the
   deterministic square set or derives Freiman relations from only its
   zero-sum triples. The extension architecture is nevertheless prior art.

6. **Paley and cyclotomic graphs.** Lim--Praeger, *On generalised Paley
   graphs and their automorphism groups*,
   [arXiv:math/0605252](https://arxiv.org/abs/math/0605252), treats the binary
   difference relation on the whole field. Its `GP(81,20)` example has an
   automorphism group larger than the one-dimensional affine semilinear group.
   Ponomarenko, *The automorphism groups and identification of some Generalized
   Paley Graphs* (2025 preprint),
   [arXiv:2511.18304](https://arxiv.org/abs/2511.18304), obtains the
   semilinear containment only when `q` is sufficiently large relative to the
   subgroup index. These are adjacent binary-relation results, not direct
   proofs of the ternary kernel.

7. **Additive patterns in subgroups.** Alon--Bourgain, *Additive Patterns in
   Multiplicative Subgroups*,
   [author PDF](https://www.cs.tau.ac.il/~nogaa/PDFS/multip1.pdf), proves
   existence and nonexistence results for additive configurations in
   multiplicative subgroups. It does not classify functions satisfying all
   internal line equations.

## Boundary checks

The conditions cannot be replaced by density alone. If independent linear
forms `ell,mu` on `F_3^m` define
`A={x:ell(x) in {0,1}}`, then `A` has density `2/3`. Every affine line wholly
inside `A` lies in one layer of `ell`, so `f(x)=ell(x)mu(x)` sums to zero on
each such line, but is not a global affine restriction.

Nor does an arbitrary multiplicative subgroup automatically behave like the
squares at small `q`. The new SC-010 exact controls find no internal lines for
the index `4` and `8` subgroups of `F_81`, or the index `11` and `22`
subgroups of `F_243`; the index `5` subgroup of `F_81` has kernel dimension
`6` versus affine-restriction dimension `5`. These are genuine failures of an
unconditional generalization, not evidence against the explicit large-field
theorem proved in SC-010.

## Gate outcome

Retain SC-009 as verified mathematical infrastructure with
`NOVELTY_UNVERIFIED`, provisionally Level 1. Its exact direct precedent was
not located, but priority is not established. The next result should test the
bridge outside the quadratic special case with explicit hypotheses, or
formalize the abstract completion-to-affinity lemma when a real Lean toolchain
is available. No Lean/Lake executable was available in this research window.

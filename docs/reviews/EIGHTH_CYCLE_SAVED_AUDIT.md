# PM-CYCLE8 saved-proof integration audit

Reviewer: /root/weil_completion_review. Date: 2026-10-18.
Read actual saved SC-012/RESULTS.md and SC-011/RESULTS.md, not only the
candidate summaries. Read-only: no shared edits or pushes. Coordinator owns
code/tests review and acceptance integration.

## Verdict

APPROVE both saved mathematical proofs as written. No mathematical
correction or status objection found.

## SC-012

The saved proof matches the previously accepted candidate, including:
* genuine quadratic-extension multiplicative realization and subgroup index;
* no mixed edges and precisely two connected punctured-space components
  when e>=2;
* four-edge Freiman completion with at most four forbidden points and
  additive extension with at most three forbidden points;
* exact affine kernel and component GL(e,3) automorphism classification;
* global wreath-product classification, faithful unique ambient linear
  extensions, and equality with Stab_GL(2e,3)(H);
* one-dimensional excess kernel, component-constant obstruction and
  explicit order-two character tau=u^(s-1);
* correctly restricted e=1 exception: the intended two-point pieces are
  NOT connected components, while the single-piece conclusions still hold;
* conservative Level0/classical packaging and no Lean/human/priority claim.

The e=2 counts follow exactly: each eight-point component has eight edges,
rank5 and kernel3; the two-component hypergraph has16 edges, rank10 and
kernel6, while ambient affine restrictions have dimension5.
The e=3 counts are also consistent: each26-point component has104 edges,
so the full graph has52 vertices,208 edges, rank44 and kernel8. Independently
recomputed |GL(3,3)|=26*24*18=11232 and its wreath order
2*11232^2=252315648.

The comparison with classical Hamming-type/generalized Paley decompositions
is appropriately described as comparison, with binary and ternary objects
distinguished. The self-contained proof does not silently depend on a
Pavone classification theorem. No historical novelty is thereby established.

## SC-011

The cyclic ideal proof is correct. Since d divides h, the row ideal (d)
in F3[Z]/(h) has basis d,Zd,...,Z^(N-deg(d)-1)d. The quotient by h and
Bezout identity justify the generator equality; the manuscript correctly
distinguishes row ideal from its orthogonal incidence kernel.

The orbit-size claim is correct: a nonidentity scalar stabilizing a
three-element edge has no fixed vertex, hence acts as a3-cycle; its cube
would fix a nonzero field element, forcing scalar order3, impossible since
3 does not divide N.

The finite field tests are sufficient. For degree5, Z^243=Z modulo M
forces squarefree irreducible factors of degrees dividing5, and exclusion
of degree1 factors forces irreducibility. Order dividing121 but not11
is exactly121. For degree4, Z^81=Z and exclusion of degrees1,2 by gcd with
Z^9-Z similarly forces irreducibility; order dividing40 but neither20 nor8
is exactly40.

The supplied coordinate change is valid: if alpha^5+2alpha+1=0, then
gamma=-alpha satisfies gamma^5+2gamma+2=0. The seed identity gives
gamma^68=2+2gamma^4 and the base-three encodings1,81,164. D=(Z-1)M expands
to1+2Z^2+2Z^5+Z^6 as stated.

Given the finite polynomial certificate, the seed kernel has dimension6.
Affine restrictions provide six independent full-hypergraph kernel vectors
because121>81. Inclusion and equal dimensions therefore prove exact equality
of the seed and full incidence kernels/row codes, without using the general
Fourier theorem.

PM-COUNTEREXAMPLE-0006 follows correctly. An automorphism of the sparse
hypergraph preserves its kernel. Coordinatewise affine extension recovers
an invertible ambient map; sum of squares and121=1mod3 kill translation.
Carlitz applies because the remaining additive permutation preserves
quadratic characters, hence every nonzero slope is a square. This restricts
all sparse automorphisms to square scalings and five Frobenius powers.

I independently recomputed the five canonical normalized patterns, obtaining
exactly the manuscript table:
0:(0,4,68); 1:(0,12,83); 2:(0,7,36);
3:(0,13,34); 4:(0,19,58).
Subtracting each of the three vertices and taking the least sorted triple
is a complete invariant for translation orbits of triples. Thus only the
identity Frobenius power stabilizes this seed orbit. All121 translations
do stabilize it, proving Aut(J)=C121, whereas the full graph has605.
This is a legitimate internal-proposal counterexample: identical incidence
row code does not determine hypergraph edges or their automorphism group.

The explicit statement that the standalone polynomial checker does NOT prove
Carlitz or enumerate arbitrary hypergraph permutations is necessary and
correct. No claim of a third-party independent implementation/proof appears.
The finite certificate can be algebraically independent from the earlier
field/matrix implementation while still using classical algebra and the
written Carlitz dependency; this distinction is preserved.

## Scope of this approval

This approval is for the saved mathematical proofs and their stated
limitations. The coordinator separately reviews code, certificate tampering
tests and final working-tree integration. No Lean or human review, complete
prior-art resolution, or historical originality claim is conferred here.

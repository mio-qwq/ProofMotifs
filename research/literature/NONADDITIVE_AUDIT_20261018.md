# Nonadditive quotient and SC-007 value audit

Date: 2026-10-18. This is a bounded primary-source audit, not a priority
certificate.

## SC-007 value decision

The exact `Q`-only deterministic query result is mathematically useful as a
supporting proposition, but it should not be positioned as standalone field-
automorphism testing.

For normalized `S`, the identity

`Q_S(x)=S(x^2)-S(x)^2`

is the Jordan square-preservation condition. Square preservation plus
additivity polarizes to multiplicativity in characteristic not two. This is
classical Jordan-homomorphism territory; see I. N. Herstein, *Jordan
Homomorphisms*, Transactions of the AMS 81 (1956), 331-341,
[DOI](https://doi.org/10.2307/1992920).

The generator-row upper-bound mechanism is also classical: the image of a
field generator and compatibility with its defining relation determine a
homomorphism. SC-007 packages this as `2m-3` admissible defect queries and an
explicit cancellation witness. Its lower bound is a correct elementary
dimension adversary in a deliberately restricted oracle model.

Classical property-testing work uses a different model: randomized direct
access to a function and a distance promise. The foundational comparison is
Blum, Luby and Rubinfeld, *Self-Testing/Correcting with Applications to
Numerical Problems*, JCSS 47 (1993), 549-595,
[DOI](https://doi.org/10.1016/0022-0000(93)90044-W). It does not imply the
project's exact `Q`-only bound, but it prevents conflating that narrow result
with general homomorphism testing.

Decision: retain PM-THEOREM-0008 as an internal/supporting theorem. Do not
spend another cycle optimizing constants unless an external application makes
the exact oracle natural. Historical originality of the exact test set remains
unverified.

## The square quotient embedding is established background

For `K=F_(3^m)`, the quotient `K^*/F_3^*` is the point set of
`PG(m-1,3)`. The map

`[x] -> x^2`

used in SC-008 is exactly the `x^(q-1)` embedding from Theorem 5.1 of Marco
Buratti and Anamari Nakic, *Additivity of symmetric and subspace 2-designs*,
Designs, Codes and Cryptography 92 (2024), 3561-3572,
[publisher PDF](https://link.springer.com/content/pdf/10.1007/s10623-024-01452-4.pdf),
[DOI](https://doi.org/10.1007/s10623-024-01452-4). Their Example 5.3 explicitly
maps `PG(3,3)` to the 40 nonzero squares of `F_81` and obtains zero-sum blocks.

That paper's projective-line blocks have four points. SC-008 instead records
distinct zero-sum triples among the same square-embedded point set. Therefore
the embedding is not new, while the exact 3-uniform substructure is not
identified with their line design.

Marco Pavone, *Subset sums and block designs in a finite vector space*,
Designs, Codes and Cryptography 91 (2023), 2585-2603,
[DOI](https://doi.org/10.1007/s10623-023-01213-9), studies all zero-sum
`k`-subsets in a finite vector space and their design automorphisms. Its point
set is not restricted to the nonzero-square image used here, so it is adjacent
background rather than a direct classification of `H_K`.

Generalized Paley graph literature is also adjacent because it studies
cyclotomic subsets and automorphism groups, but its binary difference relation
is not the ternary equation `u+v+w=0`. See Lim and Praeger, *On generalised
Paley graphs and their automorphism groups*, Michigan Mathematical Journal 58
(2009), [arXiv version](https://arxiv.org/abs/math/0605252).

## Bounded search outcome

No primary source located in this audit states the exact arbitrary-preserver
quotient theorem or classifies the 3-uniform hypergraph on nonzero squares with
edges `u+v+w=0`. That absence is not evidence of originality. The quotient
reduction is elementary once SC-003 is available, and independent rediscovery
is plausible. Keep PM-THEOREM-0009 and the F_27 count as
`NOVELTY_UNVERIFIED`; do not call either a new general theory.

# SC-008: arbitrary preservers reduce to a square zero-sum hypergraph

Date: 18 October 2026. Source baseline: remote checkpoint `2e990a7` on
`research/ongoing`.

Follow-up: [SC-009](../SC-009/RESULTS.md) subsequently proves the general
conjecture stated in Section 6. The open-status language below records the
scope of the original SC-008 checkpoint, not the latest project state.

This workstream removes additivity from the map but not from the underlying
field. It first proves the obstruction that had to be checked before any broad
classification: independent sign choices on opposite pairs are completely
invisible to ternary cancellation order.

**PM-THEOREM-0009 (exact quotient reduction).** Let `K=F_(3^m)` have
`q>3` elements, and let `C(a,b,c)` be the ordinary-moment order of the product
of the three first-difference weights. Put

`S=(K^*)^2`

and let `H_K` be the 3-uniform hypergraph with vertex set `S` and edges

`{u,v,w}` with `u,v,w` distinct and `u+v+w=0`.

Then the group of all permutations `T:K -> K` satisfying

`C(T(a),T(b),T(c))=C(a,b,c)` for every triple

is

`C_2^((q-1)/2) semidirect Aut(H_K)`.

The elementary abelian kernel consists of one independent orientation choice
on each opposite pair `{x,-x}`. In particular, order preservation alone does
not imply additivity.

**PM-COUNTEREXAMPLE-0005.** In `F_27`, swap `1` and `-1` and fix every
other element. This permutation preserves every ternary cancellation label but
is not additive.

**PM-THEOREM-0010 (small fields).** For `F_9`, `H_K` has four vertices and
no edges, so the full arbitrary preserver group has order

`2^4 * 4! = 384`.

For `F_27`, `H_K` has 13 vertices, 13 edges and automorphism group

`C_13 semidirect C_3`,

of order 39. These are exactly the square-scaling and Frobenius actions on the
quotient. Hence the full arbitrary preserver group has order

`2^13 * 39 = 319488`.

For `F_81`, `H_K` has 40 vertices, 120 edges and exactly 160 automorphisms,
again precisely the square-scaling and Frobenius actions. Its full arbitrary
preserver group has order `2^40*160=175921860444160`.

The general quotient reduction and edge-count formula below are manually
proved. The F_9 conclusion is immediate from the formula. The F_27
automorphism count is a finite exact classification supported by the displayed
incidence structure and exhaustive backtracking. A general semilinear
classification of `Aut(H_K)` is NOT proved.

Formalization: NOT_STARTED. Three genuine task-scoped AI researchers supplied
independent structural, adversarial and prior-art views; the coordinator
re-derived and tested the integrated result. This is independent AI review,
not human or Lean review. Historical novelty remains unverified.

## 1. Order depends only on square classes

SC-003 proves that, for nonzero `a,b,c`, writing

`u=a^2`, `v=b^2`, `w=c^2`,

the order is 5 when `u+v+w` is nonzero, 7 when `u+v+w=0` but the second
elementary symmetric function is nonzero, and infinity when both elementary
symmetric functions vanish.

If both vanish, `u,v,w` are roots of

`X^3-uvw`.

In characteristic three the cube map is injective on a field, so the three
roots coincide. Conversely equal square classes give vanishing first and
second elementary symmetric functions. Therefore:

* a triple with a zero direction has order infinity;
* a nonzero triple has order infinity exactly when `u=v=w`;
* a nonzero triple has order 7 exactly when `u,v,w` are distinct and sum to
  zero;
* every remaining triple has order 5.

This is the complete information visible to an arbitrary order preserver.

## 2. Every preserver fixes zero and is odd when q>3

The element zero is characterized by

`C(0,x,y)=infinity` for every `x,y`.

If a preserver sent zero to a nonzero element `z`, choose an image `y` outside
`{0,z,-z}` and pull it back. The triple `(0,a,a)` has infinite order, whereas
`(z,y,y)` does not. Thus `T(0)=0`.

For nonzero `x`, the triple `(x,x,-x)` has infinite order. Its image must
consist of three elements in one opposite pair, so

`T(-x)^2=T(x)^2`.

Injectivity rules out equality and gives `T(-x)=-T(x)`. Hence `T` permutes the
opposite pairs and induces a permutation on

`K^*/{+1,-1}`.

The map `[x] -> x^2` identifies this quotient bijectively with `S`. Section 1
then says exactly that the induced permutation must preserve the edges of
`H_K`. Conversely every hypergraph automorphism lifts after choosing an
orientation independently for every target pair. Fixing one representative
per pair gives a splitting, proving PM-THEOREM-0009.

For `q=3`, every ternary weight is zero and every label is infinity. The full
group is `S_3`; even zero is not distinguished. This is why the theorem assumes
`q>3`.

## 3. Explicit nonadditive preserver

In the repository presentation

`F_27=F_3[alpha]/(alpha^3+2alpha+1)`,

define `T(1)=-1`, `T(-1)=1`, and `T(x)=x` otherwise. Pointwise,

`T(x)^2=x^2`,

so Section 1 proves that every label is preserved. But

`T(1+alpha)=1+alpha`,

while

`T(1)+T(alpha)=-1+alpha`.

Thus `T` is not additive. The exact program compares all `27^3=19683`
ordered triples and separately records this additivity failure.

## 4. Exact edge and degree counts

Let `chi` be the quadratic character and put

`eta=chi(-1)=(-1)^m`.

Fix a vertex `u` and write another square as `v=r*u`. A distinct zero-sum
third vertex exists exactly when

`chi(r)=1` and `chi(1+r)=eta`.

Over `r` different from 0 and -1, expand the two character indicators and use

`sum chi(r)=-eta`,

`sum chi(1+r)=-1`,

`sum chi(r(r+1))=-1`

with the omitted endpoints understood. The number of admissible `r` before
removing the repeated solution `r=1` is

`(q-2-3eta)/4`.

After removing `r=1` and dividing by two because the other two vertices of an
edge can be exchanged, every vertex has degree

`d=(q-6-3eta)/8`.

Consequently

`|E(H_K)|=(q-1)(q-6-3eta)/48`.

For `q=9`, this is zero. For `q=27`, it gives degree 3 and 13 edges. For
`q=81`, it gives degree 9 and 120 edges. The full automorphism groups for both
nontrivial computed fields are classified in the next section.

## 5. Exact F_27 and F_81 quotient classifications

The machine-readable field elements and all 13 edges are in
`research/experiments/nonadditive-results.json`. In cyclic exponent
coordinates for the square group, the edge set is the 13 translates of a
single three-subset. Square multiplication supplies a regular `C_13`, and
Frobenius supplies a stabilizing `C_3`, so at least 39 automorphisms exist.

The exact backtracking enumerator uses the fact that a vertex pair lies in at
most one edge. Mapping an adjacent pair forces the third image. It branches on
every remaining candidate compatible with degree and pair incidence, and
accepts only when the transported full edge set equals the original edge set.
It returns exactly those 39 actions for F_27.

The same complete algorithm on F_81, with 40 vertices and 120 edges, returns
exactly 160 automorphisms. This equals the 40 square scalings times the four
Frobenius actions. The full arbitrary ternary-order preserver group in F_81
therefore has order

`2^40 * 160 = 175921860444160`.

The pruning predicates are necessary invariants only; forced third images are
logical consequences of the edge relation, and the final full equality remains
the acceptance test. Thus these are complete finite enumerations, not samples.

This finite result supports the following next question but does not answer it.

## 6. Open general classification

**PM-CONJECTURE-0002.** For `m>=3`, every automorphism of `H_K` has the
form

`u -> s*u^(3^j)`, with `s` a nonzero square and `0<=j<m`.

The conjecture holds for `F_27` and `F_81` by exact complete classifications.
It is false at `F_9`, where the hypergraph is empty. A first bounded F_243
prototype did not finish within 30 seconds and was terminated; it supplies no
mathematical conclusion.

The correct comparison is with restricted Freiman automorphisms of the square
subset, cyclotomic hypergraphs, and additive/projective designs. It is not
ordinary projective collinearity, so the fundamental theorem of projective
geometry cannot be applied without a new reduction.

## 7. Reproduction

```bash
python -m unittest discover -s tests -v
python tools/nonadditive_preservers.py > /tmp/nonadditive-results.json
diff -u research/experiments/nonadditive-results.json /tmp/nonadditive-results.json
```

The program uses the repository's exact finite-field tables. It is not a Lean
proof or an independent arithmetic implementation.

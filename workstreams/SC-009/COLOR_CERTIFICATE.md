# An independent color-refinement certificate for F_243

Date: 18 October 2026. Task: PM-CYCLE6-B. This supplies a second exact
finite certificate for the SC-009 classification, independently of the
rank-115 approach. It uses color refinement and orbit-stabilizer, with no
backtracking, rank computation or assumed general classification.

The finite computation proves that the square zero-sum hypergraph over
F_243 has exactly 605 automorphisms, all square-scalings composed with
Frobenius powers. Historical originality remains unverified: color
refinement and orbit-stabilizer are established methods. This is an exact
finite certificate with independent AI review, not a human or Lean proof.

## Hypergraph and arithmetic

Use the presentation

`K=F_3[alpha]/(alpha^5+2alpha+1)`,

with field element `sum c_i*alpha^i` encoded as `sum c_i*3^i`. Vertices
are the 121 nonzero squares. The 1,210 edges are the distinct unordered
zero-sum triples of vertices, and each vertex has degree 30.

The certificate builder uses the existing project finite-field engine.
The verifier uses a separate arithmetic implementation. From
`alpha^5=alpha+2`, multiplication by alpha sends the coordinate vector

`(c_0,c_1,c_2,c_3,c_4)`

to

`(2c_4,c_0+c_4,c_1,c_2,c_3)` over F_3.

Starting at 1, this recurrence visits all 242 nonzero coordinate vectors
before returning to 1. Every nonzero element is consequently a power of
alpha and has an inverse in the quotient. General multiplication in the
verifier uses the resulting cyclic logarithm table, rather than the
builder's polynomial-reduction multiplication tables. Addition is direct
coordinate addition over F_3. The verifier reconstructs the full vertex
and edge sets and checks equality with the certificate.

## Safe, equivariant refinement

Initially distinguish each named fixed vertex by its own color and give
all other vertices color zero. At a vertex x use the signature

`(old_color(x), multiset {{old_color(y),old_color(z)} : {x,y,z} is an edge})`.

The inner pair is unordered and the outer collection is a multiset, so
edge and vertex presentation order do not affect the signature. Retain
the old color and assign new colors by sorted distinct signatures.

Every automorphism fixing the named vertices preserves every successive
coloring. This follows by induction: it preserves the initial colors,
and maps incident edges bijectively, preserving the unordered endpoint
color pairs and their multiplicities. The old-color component prevents
merging cells. Equal consecutive cell counts therefore certify a stable
partition. This argument works for any finite 3-uniform hypergraph; it
does not assume that every adjacent pair has a unique third vertex.

The builder records every full color vector. The separate verifier
checks each transition using a `Counter` of endpoint-color pairs. It
checks that two vertices receive equal new colors exactly when their
old-color and incident-pair signatures coincide. An arbitrary extra
split, which could falsely make a stabilizer look trivial, is rejected.

## Two explicit stabilizer certificates

Individualizing vertex 1 gives these successive cell counts, including
the initial partition and final stability check:

`2, 3, 15, 25, 25`.

The stable cells are one singleton and 24 cells of size five. The cell
containing `9=alpha^2` is precisely

`{9,15,69,148,239}`.

This is the five-element Frobenius orbit of alpha squared. Every
automorphism fixing 1 must send 9 into this cell, so its orbit has size
at most five.

Individualizing the ordered pair `(1,9)` gives cell counts

`3, 6, 121, 121`.

The stable partition is discrete. Every automorphism fixing both named
vertices preserves its singleton cells and is therefore the identity.
These color counts are results of exact replay, not assumptions about
how a generic color-refinement algorithm behaves.

Let G be the full automorphism group. Orbit-stabilizer now gives

`|G| = |G.1| * |G_1.9| * |G_(1,9)| <= 121*5*1 = 605`.

For the matching lower bound, the verifier explicitly builds all
permutations

`u -> s*u^(3^j)`, for s a nonzero square and `0<=j<5`.

It verifies 605 distinct permutations and checks that each transports
the complete 1,210-edge set to itself. Thus `|G|>=605`; equality follows,
and every automorphism is one of those known actions. Multiplication by
the square encoded as 6 has order 121 and supplies a regular cyclic
action; Frobenius supplies the order-five stabilizer. No unidentified
automorphism is inferred from group size alone: the complete known
605-element set is contained in G and exhausts its sharp upper bound.

## Certificate, checker and negative controls

The deterministic report contains the complete labelled field edge set,
both full refinement traces, named pivots, the root cell, generator
permutations and the recomputed verification receipt. It also includes a
SHA-256 of the canonical certificate JSON. The digest is an integrity
aid; the verifier checks the mathematics from the full data.

```bash
python tools/color_refinement_certificate.py > /tmp/color-certificate.json
python tools/color_refinement_certificate.py --check /tmp/color-certificate.json
python -m unittest discover -s tests -p test_color_refinement_certificate.py -v
```

The `--check` path imports no other project module, constructs its own
cyclic-log arithmetic, and does not call the certificate builder or its
refinement implementation. Tests remove a true edge, insert an unsafe
color split and corrupt the claimed Frobenius action; each false
certificate is rejected. A relabelled F_27 instance checks equivariance.
The empty F_9 quotient remains non-discrete after two fixed vertices,
preventing a false extension of this certificate to that exceptional
field.

The rank certificate and this color certificate use different upper-bound
mechanisms. This verifier also uses different finite-field multiplication
from the builder, while retaining the same specified modulus and
coordinate convention. These are algorithmic and actual task-scoped AI
cross-checks; no kernel formalization or human peer review is claimed.
This certificate alone concerns F_243. The general classification is proved
separately in [RESULTS.md](RESULTS.md) by the incidence/Freiman argument.

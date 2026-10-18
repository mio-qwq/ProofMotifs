# SC-012: an infinite two-subspace obstruction family

Date: 18 October 2026. This workstream explains structurally the F_81,
index-five negative control in SC-010. It does not optimize the sufficient
completion bound or enumerate additional cyclotomic automorphism groups.

**PM-THEOREM-0016.** Let s=3^e, e>=2, and K=F_(s^2). Choose a nonsquare
a in F_s and beta in K with beta^2=a. The multiplicative subgroup

`H=F_s* union beta*F_s*`

has index `(s+1)/2`. Its internal zero-sum triple hypergraph consists of two
disjoint copies of the line hypergraph on the punctured F_3-space F_s*.
Its incidence kernel has dimension `2e+2`, strictly larger than the
ambient affine restriction dimension `2e+1`. Nevertheless every hypergraph
automorphism extends uniquely to an ambient F_3-linear map, and

`Aut(line_3(H)) = GL(e,3) wreath S_2 = Stab_GL(2e,3)(H)`.

The group order is `2*product_(j=0)^(e-1)(3^e-3^j)^2`. For e=1 the
hypergraph is empty on four vertices and its automorphism group is S_4;
the wreath-product conclusion is not asserted in that case.

Status: full written proof below, with exact direct-sum coordinate checks.
Independent AI review, human review, formal verification and originality
are separate fields. No human or Lean review is claimed. This is classical
Hamming-type decomposition and disjoint-union geometry, presented as a
project boundary example. **Level 0/background packaging;
NOVELTY_UNVERIFIED, with no new-method or priority claim.**

## 1. A genuine multiplicative subgroup

The polynomial X^2-a is irreducible over F_s. Thus beta is outside F_s,
and K is the direct sum `F_s plus beta*F_s` over F_s. Multiplication of
the two displayed nonzero cosets closes because beta^2 lies in F_s*.
Inversion closes as well; therefore their union H is a subgroup of K*.
Its order is `2(s-1)` and its index in K* is `(s+1)/2`.

As an F_3-space, K is the direct sum of two e-dimensional subspaces V_0
and V_1, and H is exactly `V_0* union V_1*`. A triple with elements in
both subspaces cannot sum to zero: its component occurring only once
would be nonzero. Consequently every hyperedge lies wholly inside one
punctured subspace. This proves the asserted disjoint-union structure.

The subgroup index grows with s. This family does not contradict SC-010's
large-q theorem with fixed index; its hypothesis is not satisfied here.

## 2. The punctured-space incidence kernel

Let V be an e-dimensional F_3-space, e>=2, and A=V minus {0}. Suppose
f:A -> F_3 sums to zero on each distinct zero-sum triple in A. A repeated
zero-sum triple in characteristic three has all entries equal, and its
equation is automatically `3*f(x)=0`. Thus those equations may also be used.

**Freiman relations.** Given u+v=w+z in A, choose t outside

`{0,-u,-w,z-u}`.

There are at most four forbidden points, and |V|=3^e>=9. Hence all four
auxiliary elements

`t`, `b=-u-t`, `c=-w-t`, `d=u+t-z`

are nonzero. The four zero-sum equations on

`(u,t,b)`, `(w,t,c)`, `(b,z,d)`, `(c,v,d)`

give `f(u)+f(v)=f(w)+f(z)`. No character estimate or assumption of distinct
forbidden points is needed.

**Extension.** For any x in V choose a,b in A with a-b=x; this is possible
by choosing b outside `{0,-x}`. Define `L(x)=f(a)-f(b)`. Freiman relations
make this well-defined. For arbitrary x,y choose b outside

`{0,-x,-x-y}`.

All of b,b+x,b+x+y then belong to A, and telescoping gives
`L(x+y)=L(x)+L(y)`. Thus L is F_3-linear. Fixing any b in A gives

`f(x)=L(x)+c` on A.

Conversely every affine restriction satisfies all zero-sum triple
equations. Restrictions are independent: A-A=V, so an affine functional
vanishing on A has zero linear part and then zero constant. The
incidence kernel therefore has dimension e+1.

## 3. Component automorphisms

The preceding kernel statement implies that every automorphism pi of the
punctured-space hypergraph extends uniquely to an affine map F of V.
Indeed the pullback of each coordinate functional through pi is an affine
restriction; their extensions form F. The set A affinely spans V, so its
linear part is invertible and the extension is unique.

The sum of all elements of A is zero, whereas |A|=3^e-1 is nonzero modulo
three. Summing F over A therefore kills its translation. Thus

`Aut(line_3(V minus {0}))=GL(e,3)`.

This conclusion is also true for e=1, since both groups act as S_2 on the
two nonzero elements; that trivial case is separate from the completion
proof above.

For e>=2 the component is connected. Any distinct x,y in A not opposite
to one another complete an edge with -x-y. Thus its two-section graph is
the complete graph on `3^e-1` vertices with the opposite-pair matching
removed. It is connected because there are at least eight vertices.

## 4. Global kernel and exact automorphism group

Since the two connected components are disjoint, their incidence kernels
are independent. Every kernel function has the form

`f(x)=ell_0(x)+c_0` on V_0*,

`f(y)=ell_1(y)+c_1` on V_1*.

The dimension is `2(e+1)`. Ambient affine restrictions have the same
linear parts but a single common constant: `c_0=c_1`. Their dimension is
`2e+1`, because H-H spans K and H affinely spans K. One can also prove
independence directly by restricting to the two subspaces as in Section 2.

An explicit nonaffine kernel function is

`f=0 on V_0*`, `f=1 on V_1*`.

Its line sums vanish because every edge is wholly in one component. It
cannot extend affinely: its constant restrictions to the two punctured
subspaces would force zero linear parts and the same constant, whereas
the two constants here differ.

There is also an exact Fourier description. The nontrivial conjugate of
beta over F_s is -beta, so `beta^s=-beta`. Therefore the multiplicative
character

`tau(u)=u^(s-1)` on H

is +1 on F_s* and -1 on beta*F_s*. It has order two, takes values in F_3,
and lies in the line kernel. The preceding nonaffine indicator is
`(1-tau)/2`. Since the kernel exceeds ambient affine restrictions by
exactly one dimension, tau spans that quotient. In cyclic exponent
coordinates on H it is the mode with exponent `|H|/2=s-1`.

Thus this family retains exactly the order-two type of extra mode that
the square-subgroup argument in SC-009 excludes. This identifies a
specific structural reason for failure of the minimal-kernel condition;
it is not an assertion that arbitrary cyclotomic failures have only one
extra mode.

Every hypergraph automorphism permutes the two connected components. Its
restrictions are independent GL(e,3) maps by Section 3, followed possibly
by the component swap. Conversely these operations preserve every edge.
This proves the wreath-product classification and its order.

Under the direct-sum identification they are precisely invertible block
diagonal or block antidiagonal linear maps of K. Hence every automorphism
extends to an ambient linear map. Uniqueness follows because H spans K.
Conversely every ambient linear stabilizer of H preserves the hypergraph.
Thus the stated equality with the linear setwise stabilizer follows.

This is the boundary demonstrated by the family: **minimal affine
incidence kernel is sufficient, but not necessary, for every hypergraph
automorphism to extend linearly.** Extra component constants in the
kernel do not produce extra permutations beyond the linear stabilizer.

## 5. The e=1 exception and concrete counts

For e=1, each punctured one-dimensional subspace has only two vertices
and no edges. Their union is an empty four-vertex hypergraph, whose
automorphism group is S_4 of order 24. The two intended two-point pieces
are not connected components; all four vertices are isolated. This is
why the wreath-product argument fails, and it recovers the F_9 exception.

For e=2, s=9 and K=F_81, H has index five. The exact parameters are

`16 vertices, 16 edges, incidence rank 10, kernel dimension 6`,

versus ambient affine dimension five. Since |GL(2,3)|=48,

`|Aut(line_3(H))|=2*48^2=4608`.

The scalar--Frobenius subgroup has order `|H|*(2e)=64`. The larger group
is explained by independent linear transformations of the two subspaces,
not a numerical anomaly.

For e=3, the direct-sum model has 52 vertices, 208 edges, incidence rank
44 and kernel dimension eight versus ambient affine dimension seven.
The component linear group has order 11,232; the full group order from
the theorem is 252,315,648. The program does not enumerate that full group.

## 6. Exact computation and interpretation

The source `tools/two_subspace_obstruction.py` uses integer encodings of
vectors in F_3^e and coordinatewise addition. It constructs the two
punctured subspaces, their edges and an exact F_3 incidence rank. It
checks the displayed component-constant function and verifies that
adjoining it raises the ambient affine restriction rank by one. No
extension-field multiplication or GF(729) table is constructed.

For the eight-point component only, it examines all 40,320 permutations,
finds exactly 48 automorphisms, and checks equality with the actions of
all invertible two-by-two matrices over F_3. The full sixteen-point
group order is obtained from the proved wreath product, not a full
sixteen-point permutation search.

```bash
python -m unittest tests.test_two_subspace_obstruction -v
python tools/two_subspace_obstruction.py
```

The ambient multiplicative realization uses the elementary irreducible
quadratic construction in Section 1; the program verifies its isomorphic
additive model rather than constructing that extension field.

Hamming-type generalized Paley decompositions and automorphism groups of
disjoint copies are classical. Relevant comparison includes
[Lim--Praeger, generalized Paley graphs](https://arxiv.org/abs/math/0605252)
and [Pavone, subset sums and block designs](https://doi.org/10.1007/s10623-023-01213-9).
The binary Hamming graph and the internal ternary hypergraph are different
objects. The elementary proofs here establish the stated boundary without
claiming that the decomposition, punctured geometry or wreath-product
mechanism is historically new. Formal verification and a source-specific
novelty assessment remain separate.

# SC-010: fixed-index cyclotomic line kernels

Date: 18 October 2026. Baseline: accepted SC-009 at remote predecessor
`31f3d3936c654fc4d24c8246144c3308bb0570f7`.

**PM-THEOREM-0014.** Let `K=F_(3^m)`, let `H` be the multiplicative subgroup
of index `d>=2`, and put

`B_4(d)=6(d-1)^2+8(d-1)^3+3(d-1)^4`.

If

`q-B_4(d)*sqrt(q)-4*d^3>0`,

then every `f:H->F_3` whose values sum to zero on every distinct zero-sum
triple in `H` is the restriction of a unique affine `F_3`-functional on `K`.
Equivalently, the incidence kernel has dimension `m+1`.

Consequently the automorphism group of the zero-sum triple hypergraph on `H`
is exactly the setwise stabilizer of `H` in `GL(m,3)`. This conclusion is not
silently replaced by scalar--Frobenius: generalized Paley stabilizers can be
larger in small fields.

Status: manual proof, independently challenged; exact finite negative
controls. The multiplicative-character bound and difference-extension
architecture are prior art. Historical originality and formal verification
are unestablished. `NOVELTY_UNVERIFIED`, provisionally Level 1.

## 1. A uniform coset-pattern count

Choose a multiplicative character `chi` of exact order `d`, with kernel `H`,
and extend nontrivial characters by `chi(0)=0`. In the indicator sum define
the exponent-zero term to be `1` even at zero. Thus

`J(t)=sum_(e=0)^(d-1) chi(t)^e`

is `d` on `H`, zero on `K*\H`, and one at zero.

Let `l_1,...,l_k` be affine linear forms with distinct roots, where `2<=k<=4`.
Expanding `product_i J(l_i(a))`, a term with support size one sums to zero.
For support size `r>=2`, its polynomial has `r` distinct roots and exponents
strictly between zero and `d`; it is not a `d`th power. The standard
multiplicative Weil bound is therefore `(r-1)*sqrt(q)`. At each excluded root
the unnormalized product is at most `d^(k-1)`. Hence the number `N_k` of
parameters for which every form lies in `H` satisfies

`N_k >= (q-B_k(d)*sqrt(q)-k*d^(k-1))/d^k`,

where

`B_k(d)=sum_(r=2)^k binom(k,r)(d-1)^r(r-1)`.

In particular,

* `B_2=(d-1)^2`,
* `B_3=3(d-1)^2+2(d-1)^3`,
* `B_4=6(d-1)^2+8(d-1)^3+3(d-1)^4`.

The stated `k=4` positivity strictly implies the `k=3` and `k=2` positivity:
`B_4-B_3=3d^2(d-1)^2>0` and
`B_3-B_2=2d(d-1)^2>0`, while the root terms also strictly decrease.
Leading coefficients merely multiply character sums by roots of unity, so
no assumption `-1 in H` is needed.

This count is a direct character-indicator application, not a new Weil
theorem. A close published pattern-count form is Kim--Yip--Yoo, Lemmas 2.1--2.2,
already cited in SC-009. Ponomarenko's 2025 preprint, Theorem 4.1, gives a
closely related `q/d^k +/- k*sqrt(q)` estimate for equal prescribed cosets.

## 2. Four edges force every Freiman relation

Let `u+v=w+z` in `H`. If `u=w` or `u=z`, the desired identity is tautological.
Otherwise seek `a` for which

`a, -u-a, -w-a, u+a-z`

all belong to `H`. Their roots are `0,-u,-w,z-u`. Every collision forces an
original zero element or one of the two tautological cases, so the roots are
distinct. The `k=4` count supplies such an `a`.

Put `b=-u-a`, `c=-w-a`, `e=u+a-z`. The four triples

`(u,a,b), (w,a,c), (b,z,e), (c,v,e)`

sum to zero. A repeated zero-sum triple in characteristic three is diagonal,
and its equation is automatically `3f(h)=0`; hence the distinct-edge
hypothesis legitimately covers all four equations. Subtracting them gives

`f(u)+f(v)=f(w)+f(z)`.

Thus `f` is a Freiman 2-homomorphism on `H`.

## 3. Difference extension and exact kernel

The positive `k=2` count gives `H-H=K`. Define

`L(x)=f(a)-f(b)` whenever `a-b=x` with `a,b in H`.

The Freiman identity makes this independent of the representation. For
nonzero `x,y,x+y`, the positive `k=3` count supplies a common translate
`b,b+x,b+x+y in H`; telescoping proves
`L(x+y)=L(x)+L(y)`. Zero arguments are immediate and `x+y=0` follows from
`L(-x)=-L(x)`. Therefore `L` is `F_3`-linear and
`f(h)=L(h)+c` on `H`.

Conversely every affine restriction satisfies the line equations. Since
`H-H=K`, an affine functional vanishing on `H` vanishes identically; the
restriction space has dimension `m+1`. This proves PM-THEOREM-0014.

## 4. Hypergraph automorphisms

Let `pi:H->H` preserve the zero-sum triples. Pulling back each coordinate
functional through `pi` and applying the kernel theorem extends `pi` uniquely
to an affine map `F(x)=A(x)+b` on `K`. Because `H-H=K`, the set `H` affinely
spans `K`, so `A` is invertible. The sum of a nontrivial multiplicative
subgroup is zero. Also `|H|=(q-1)/d` is nonzero in `F_3`, because `d` divides
`q-1` and is therefore prime to three. Summing `F(h)` over `H` forces `b=0`.

Hence

`Aut(line_3(H))={A in GL(m,3):A(H)=H}`.

The reverse inclusion is immediate from additivity. For `d=2`, preserving
the square set also preserves its complement and Carlitz recovers SC-009's
scalar--Frobenius group. For general `d`, setwise preservation of one
multiplicative coset does not by itself preserve every cyclotomic class.

If additionally `|H|` is even and

`sqrt(q)>max(5*d^3/(d-1),10*(2*d^2+d)*2^(d^2+2*d))`,

then Ponomarenko's Remark 5.2 supplies his much stronger large-`q` hypothesis
for the index-`d` generalized Paley graph. His Theorem 1.1 puts every graph
automorphism in `A Gamma L(1,q)`. Applying it to the linear stabilizer above
then yields the corollary

`Aut(line_3(H))={x -> h*x^(3^j):h in H,0<=j<m}`.

This asymptotic corollary explicitly depends on that 2025 preprint and is not
claimed as an independent classification theorem here. Its exponential
condition is much stronger than PM-THEOREM-0014's polynomial completion
threshold. McConnel/Carlitz alone cannot replace it: those theorems require
every difference quotient to lie in one subgroup, not merely `A(H)=H`.

## 5. Exact negative controls and limits

`tools/cyclotomic_incidence.py` exactly constructs the subgroup, all internal
three-point lines, the `F_3` incidence rank and the dimension of restricted
affine functions. The saved report includes:

| Field/index | `|H|` | edges | kernel dim | affine dim | equality |
| --- | ---: | ---: | ---: | ---: | --- |
| `F_81`, 4 | 20 | 0 | 20 | 5 | no |
| `F_81`, 5 | 16 | 16 | 6 | 5 | no |
| `F_81`, 8 | 10 | 0 | 10 | 5 | no |
| `F_81`, 10 | 8 | 8 | 3 | 3 | yes, on a subfield-sized span |
| `F_81`, 16 | 5 | 0 | 5 | 5 | yes, but the hypergraph is empty |
| `F_243`, 11 | 22 | 0 | 22 | 6 | no |
| `F_243`, 22 | 11 | 0 | 11 | 6 | no |

These fields do not satisfy the theorem's sufficient bound. The failures show
why the large-field condition cannot be deleted and why density or subgroup
structure alone is insufficient. The finite controls do not prove the
all-field theorem, and the sufficient bound is not asserted sharp.

The index-16 row is also a guardrail on the automorphism conclusion. Its five
vertices form an affine basis, so every vertex permutation extends uniquely to
an affine map; their sum is zero, so the extension is linear. Consequently the
linear setwise stabilizer is `S_5` of order 120, whereas the visible
scalar--Frobenius subgroup has order `5*4=20`. Minimal incidence kernel alone
does not justify a Carlitz conclusion for index greater than two.

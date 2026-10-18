# SC-013: connectivity is necessary, but insufficient, for one edge orbit

Date: 18 October 2026. Baseline: verified research checkpoint
`e35f0dfcb8e5446be3e0840d54c8f89e9967b34e`.

PM-QUESTION-0001 asks whether, for every m>=3, some single multiplicative
edge orbit spans the full square-set incidence row code. This workstream
does **not** solve that existence question. It proves a necessary condition
and refutes a plausible intermediate sufficiency criterion, with a complete
polynomial certificate and an explicit nonaffine kernel function.

**PM-THEOREM-0017.** Let K=F_(3^m), m>=3, S=(K*)², N=(3^m-1)/2,
and E={1,a,b} a distinct zero-sum triple in S. Put H=<a,b>,
delta=[S:H], and F_3(H)=F_(3^d). For the hypergraph J_E with edges tE,
t in S, the connected components are precisely the cosets tH and

`dim_F3 ker(M_E) >= delta*(d+1)`.

If H is proper in S, this lower bound exceeds m+1. Consequently a seed
whose orbit spans the complete row code must satisfy H=S. With a=gamma^i
and b=gamma^j this is the necessary condition `gcd(i,j,N)=1`.

**PM-COUNTEREXAMPLE-0007.** In F_729, the seed with exponent set
`{0,25,311}` is connected, but its incidence kernel has dimension 13,
whereas the full hypergraph kernel has dimension 7. Thus connectivity is
not sufficient. The function `f(u)=Tr_(F729/F3)(u^34)` satisfies every seed
orbit equation and violates an actual full-hypergraph edge equation.

Status: written proof, exact finite certificates and independent AI proof
and arithmetic reviews. Classical component, cyclic-code and trace tools
are credited; historical novelty is unverified. No human review or Lean
verification is claimed, and no published conjecture is said to be refuted.

## 1. Components and their affine subspaces

Every edge tE lies in tH. The two-section graph contains adjacency from x
to xa and xb for every x in S. Paths therefore allow multiplication and
division by a and b. All edge ratios lie in H, so the components are
exactly its delta cosets.

Let V be the F_3-linear span of H. It contains 1, and products of its
spanning elements remain in H. Thus V is a finite subalgebra of a field,
and is itself a field: multiplication by a nonzero element is injective
on the finite set V, hence surjective and supplies an inverse. It follows
that V=F_3(H)=F_(3^d), with d dividing m.

The group H is nontrivial, since E has three distinct vertices. Choose
h_0 in H different from 1. Multiplication by h_0 permutes H, giving
`(h_0-1)*sum_(h in H) h=0`, so sum H=0. Its cardinality h divides 3^m-1,
and is therefore nonzero in F_3. Hence zero is an affine combination of
the points of H, namely their average. Together with its linear span,
this shows that H affinely spans F_(3^d).

All affine restrictions `c+ell(x)` on H, with ell:F_(3^d)->F_3 linear,
satisfy every zero-sum triple equation. They are d+1 independent functions:
if one vanishes on H, summing gives h*c=0, then c=0 and the linear-span
property forces ell=0. Scaling identifies the same construction on every
coset tH. Independently supported functions on the delta components give
the stated kernel lower bound.

## 2. Strictness for a disconnected orbit

If d=m and H is proper, delta>=2, so delta*(d+1)>m+1. Otherwise write
m=r*d with r>=2. Since h<=3^d-1,

`delta >= (3^m-1)/(2*(3^d-1))`

`       = (1+3^d+...+3^((r-1)*d))/2 >= r`.

For the last inequality the sum is at least `1+3*(r-1)>=2r`. Therefore

`delta*(d+1) >= r*(d+1)=m+r>m+1`.

The established full square hypergraph has kernel dimension m+1 for m>=3.
Thus disconnectedness prevents a single orbit from having its complete
row code. This is a necessary condition only.

The old F_81 seed `{0,5,30}` is explained structurally. Here N=40,
H=<gamma^5>=F_9*, delta=5 and d=2. The lower bound is 15, exactly the
earlier polynomial gcd degree, without needing a new incidence enumeration.

## 3. An exact connected counterexample in F_729

Use

`K=F_3[X]/(X^6+X+2)`, `alpha=X`, `gamma=alpha²`, `N=364`.

The compact coordinate recurrence visits all 728 nonzero vectors as powers
of alpha, which proves the quotient is a field and alpha has order 728.
A separate polynomial Rabin test and proper-order tests also verify this.
Consequently gamma has order 364 and generates the nonzero squares.

The actual seed is

`E={1,gamma^25,gamma^311}`.

Its vertices have coordinate encodings `{1,118,235}` and sum to zero.
Since `gcd(25,311,364)=1`, its orbit is connected by Section 1.

Let h(Z)=Z^364-1 and p(Z)=1+Z^25+Z^311. The exact monic gcd is

`D_bad(Z)=Z^13+2Z^10+2Z^6+2Z^4+Z^3+2Z+2`.

The deterministic certificate contains A,B,Q_h,Q_p over F_3 satisfying

`A*h+B*p=D_bad`, `D_bad*Q_h=h`, `D_bad*Q_p=p`.

These identities prove the gcd and hence, by the classical cyclic rank
criterion of SC-011, kernel dimension 13 and row rank 351. All 364 cyclic
edges are distinct: a nontrivial multiplier stabilizing a three-element
edge would have order three, which does not divide 364.

The affine factor has degree seven:

`D_aff(Z)=(Z-1)*(Z^6+Z^3+2Z+1)`

`        =Z^7+2Z^6+Z^4+2Z^3+2Z²+2Z+2`.

In fact

`D_bad=D_aff*(Z^6+Z^5+Z^4+2Z^3+2Z²+1)`.

The extra factor corresponds to the Frobenius frequency orbit
`{34,102,306,190,206,254}`. The complete bad gcd roots in the square
subgroup are this orbit, the constant frequency 0, and
`{1,3,9,27,81,243}`. Direct root checks independently agree with the
polynomial gcd degree.

## 4. A nonlinear function exhibiting the missing constraints

Set `f(u)=Tr_(K/F_3)(u^34)` on S. The extra root means

`1+(gamma^25)^34+(gamma^311)^34=0`.

For every t in S, linearity of the field trace gives

`sum_(u in tE) f(u)=Tr(t^34*(1+(gamma^25)^34+(gamma^311)^34))=0`.

But another actual edge is

`F={1,gamma^5,gamma^255}={1,567,407}`.

Its f-values are `{0,0,1}`, with sum 1. Hence f is not affine: any affine
functional has zero sum on every zero-sum triple in characteristic three.
This witness shows a missing equation, not merely a larger reported rank.

There is also a symmetry check. Since -1 is a square and 34 is even,
f(-u)=f(u). An affine representation c+ell(u) would force ell(u)=0 on S
by comparing opposite points, hence f constant; the nonzero edge sum
again rules this out. Independent coordinate arithmetic checked all 364
seed translates and the omitted edge without the search implementation.

## 5. Bounded search scope

The exact scan covers every multiplicative edge orbit for m=3,4,5,6,
respectively 1,3,10,30 orbits. The complete m=6 distribution is:

| Connectivity index delta | Kernel dimension | Orbit count |
| ---: | ---: | ---: |
| 1 | 7 | 18 |
| 1 | 13 | 3 |
| 2 | 14 | 3 |
| 4 | 40 | 2 |
| 14 | 56 | 3 |
| 28 | 112 | 1 |

Thus m=6 is the first connected failure among the checked degrees 3–6.
It is not a failure of existence: `{0,5,255}` is a good m=6 seed with
gcd degree seven. The report also contains good m=7 and m=8 seeds with
gcd degrees eight and nine. Those larger degrees use a search stopping
at the first good orbit, not a complete orbit classification.

The field code uses O(q) power/log lists rather than O(q²) field tables.
Bitplane ternary gcd search is checked by coefficient-list Bezout identities
and by direct root counts in the field. Separate independent coefficient
arithmetic also verifies the m=6 gcd and trace witness. See COMPUTATION.md
for exact commands and software trust boundaries.

## 6. What remains open

The prior-art gate separates this from principal-ideal generation and, for
odd m, the even-like ternary Hamming-code connection. Collective generation
by all weight-three words does not imply generation by one weight-three
word. Likewise, rejecting each unwanted frequency with some edge does not
select one edge that rejects all frequencies simultaneously.

PM-QUESTION-0001 remains open. The next useful operation is a simultaneous
spectral-factor avoidance theorem for valid seed trinomials, or a complete
field-level factor-covering certificate proving that no seed works. Positive
instances through m=8 and the connectedness counterexample establish neither
universal existence nor universal failure. Classical facts, exact finite
examples, AI review, formal verification and originality remain separate.

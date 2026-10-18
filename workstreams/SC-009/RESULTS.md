# SC-009: incidence kernels recover the affine ambient space

Date: 18 October 2026. Baseline: SC-008, first reviewed at remote
`f172123bd60e27bccbea31fb335994418d95d5d9`.

**PM-THEOREM-0011.** A conditional incidence-rank criterion proves the
semilinear classification of the square zero-sum hypergraph. Its proof is
given below and explicitly uses the classical Carlitz theorem at its last
step.

**PM-THEOREM-0012.** For F_243 the criterion holds: the 121-vertex,
1,210-edge incidence matrix has rank 115 over F_3, so the quotient
automorphism group has exactly 605 elements. This provides a finite exact
classification without enumerating automorphisms. A separate color-refinement
certificate gives a second combinatorial route. Its checker reconstructs
finite-field multiplication using an independent alpha recurrence and cyclic
logarithms; see [COLOR_CERTIFICATE.md](COLOR_CERTIFICATE.md).

**PM-THEOREM-0013.** For every m>=3 the incidence kernel is exactly the
space of affine restrictions. Consequently PM-CONJECTURE-0002 holds for
every m>=3. Sections 5–6 prove this using classical character sums and
Freiman extension, with exact rank certificates for m=3,4.

Status: full written proofs and exact finite certificates; separate AI
structural and adversarial reviews accepted the general argument.
Independent AI review, human review, formal verification and originality are
separate matters. This task's implementation shares the existing validated
field arithmetic. No human, Lean or historical-originality certification is
claimed. **NOVELTY_UNVERIFIED.** Classical tools and the final Carlitz
classification are explicitly credited. The general argument does not infer
an infinite theorem from finite enumeration.

## 1. The incidence kernel

Let K=F_(3^m), m>=3, and S=(K*)^2. Let H have vertex set S and edges the
distinct triples {u,v,w} with u+v+w=0. In characteristic three these are
exactly the affine F_3-lines wholly contained in S. This observation does
not identify H with an entire affine or projective geometry.

Let M be the edge-by-vertex incidence matrix over F_3. Its kernel is

`C={f:S -> F_3 : f(u)+f(v)+f(w)=0 for every edge}`.

All restrictions of affine functions on the F_3-vector space K belong to C:

`f(u)=c+ell(u)`, with c in F_3 and ell:F_3-linear K -> F_3.

The restriction space has dimension m+1. Indeed |S|=(3^m-1)/2>3^(m-1),
whereas a proper affine hyperplane of K has exactly 3^(m-1) points. Thus S
affinely spans K, and no nonzero affine function vanishes identically on S.

## 2. PM-THEOREM-0011: conditional classification

**Theorem.** If `dim_F3 ker(M)=m+1`, every automorphism pi of H has the form

`pi(u)=s*u^(3^j)`, with s a nonzero square and `0<=j<m`.

Consequently Aut(H) has `(3^m-1)*m/2` elements.

**Proof: affine extension.** The kernel then equals the complete space of
affine restrictions from Section 1. Composition with pi preserves this
kernel. Choose any vector-space coordinates x_1,...,x_m on K. Every
coordinate function `u -> x_i(pi(u))` therefore equals an affine function
on S. Combining their affine extensions gives a map

`F(x)=L(x)+b`

on K with F restricted to S equal to pi. Here L is F_3-linear. If L were
singular, F(S)=S would lie in a proper affine subspace, contradicting the
affine spanning established above. Thus L is invertible. The extension is
unique because S affinely spans K.

**Proof: the translation vanishes.** The multiplicative subgroup S has
more than one element and its sum is zero. For example multiply that sum
by any s in S different from 1. Since F permutes S,

`0=sum_(u in S) F(u)=L(sum_(u in S)u)+|S|*b=b`,

because `|S|=(3^m-1)/2` is 1 modulo three. Hence b=0 and L(S)=S.

**Proof: classical final step.** Since L is additive and bijective, L
preserves both nonzero squares and nonsquares. Thus for x!=y,

`(L(x)-L(y))/(x-y)=L(x-y)/(x-y)`

is a square: its numerator and denominator have the same quadratic
character. The classical Carlitz theorem forces

`L(x)=s*x^(3^j)`.

This is precisely the square-subgroup case described in Section 1 of
[Yip, A strengthening of McConnel's theorem, arXiv:2407.21362v3](https://arxiv.org/html/2407.21362v3).
It also follows from that paper's Theorem 1.2 by taking D to be the
square subgroup; the cardinality condition holds because D is a subgroup
of size (q-1)/2. The zero translation follows from L(0)=0, and s=L(1)
belongs to S. This final classification is established prior art, not a
new theorem of this project.

Conversely square scalings and Frobenius preserve S and every edge. These
actions are distinct on S. If two such actions agreed there, their
additive extensions would agree on its affine span K; equality at 1 and
the distinctness of Frobenius automorphisms then identify both parameters.
This proves the theorem and its count.

## 3. PM-THEOREM-0012: the exact F_243 consequence

Use the validated quotient field with modulus

`X^5+2X+1` over F_3.

The exact incidence certificate has the following dimensions:

| Field | Vertices | Edges | Rank over F_3 | Kernel dimension | Affine dimension |
| --- | ---: | ---: | ---: | ---: | ---: |
| F_9 | 4 | 0 | 0 | 4 | 3 |
| F_27 | 13 | 13 | 9 | 4 | 4 |
| F_81 | 40 | 120 | 35 | 5 | 5 |
| F_243 | 121 | 1,210 | 115 | 6 | 6 |

For F_243, a specified 115-by-115 incidence minor has nonzero determinant
over F_3. This proves rank at least 115. Six explicit independent kernel
vectors are the constant vector and the five polynomial-coordinate
vectors on S. They annihilate every edge row, proving rank at most
121-6=115. Their independence is also checked by a nonzero six-by-six
minor. These bounds coincide, without any floating-point rank estimate.
The certificate lists pivot edge/vertex indices, both determinants, and
the six complete kernel vectors so that the minors can be reconstructed.

Theorem 0011 therefore yields

`Aut(H_F243)={u -> s*u^(3^j) : s in S, 0<=j<5}`,

of order `121*5=605`. SC-008 then gives the complete ordinary ternary-order
preserver group as

`C_2^121 semidirect Aut(H_F243)`,

of order `2^121*605`. The F_9 row is a necessary negative control: its
kernel is strictly larger than its affine restriction space, and the
conditional theorem correctly supplies no classification there.

A separate task also obtained a finite color-refinement route: fixing a
root yields 25 cells, and individualizing the second vertex in one
five-element cell gives a discrete refinement. The coordinator owns its
precise labels, replay and acceptance. The incidence proof above does
not depend on that independent combinatorial certificate.

## 4. Exact implementation and limitations

`tools/incidence_rank_certificate.py` constructs edges by completing pairs
to their unique third vertex. It performs exact row elimination modulo
three, retains original pivot row/column indices, and verifies the
resulting lower-bound minor by a separate column-elimination determinant.
It separately verifies the affine kernel and an invertible minor of that
basis. There is no automorphism enumeration or numerical approximation.

The report is generated by:

```bash
python -m unittest tests.test_incidence_rank_certificate -v
python tools/incidence_rank_certificate.py
```

The field class uses shared precomputed arithmetic tables and intentionally
supports only small fields. This is not an independent implementation of
F_243 arithmetic or a scalable all-degree algorithm. Exact linear algebra
and its finite-field assumptions remain subject to review. No Lean run
has occurred. The general criterion is an elementary incidence-code
reconstruction argument; its mathematical usefulness does not establish
historical originality.

## 5. PM-THEOREM-0013: general incidence affinity

For every m>=3, the only functions f:S -> F_3 summing to zero on every
edge are restrictions `f(u)=ell(u)+c`, with ell F_3-linear. Thus

`rank_F3(M)=|S|-(m+1)`.

For m=3,4, the exact matching minor/kernel certificates in Section 3 prove
this directly. For m>=5, q>=243, the following uniform proof applies.
Its classical character-sum input is stated precisely in Lemma 2.1 of
[Kim–Yip–Yoo, Explicit constructions of Diophantine tuples over finite
fields, The Ramanujan Journal 65 (2024)](https://link.springer.com/article/10.1007/s11139-024-00888-5).
For a nonzero scalar times a product of r distinct linear factors, the
quadratic-character sum has absolute value at most `(r-1)*sqrt(q)`.
Here q is odd, the character has order two, and the polynomial has distinct
simple roots, so is not a square even over the algebraic closure. There is
no condition that the characteristic not divide r. The two-factor sum has
the sharper exact value minus the character of its leading coefficient.

## 6. Uniform proof by four-edge completion

Assume q>=243 and f lies in the incidence kernel. Relations on diagonal
triples are automatic because `3*f(u)=0`. Therefore the edge relation
can be used whenever three elements of S sum to zero, including repeated
entries (a repeated pair in characteristic three forces all three equal).

Consider a nontrivial Freiman relation `u+v=w+z`, with u,v,w,z in S. If
u=w or u=z, the corresponding identity for f is automatic. Otherwise
the four roots `0,-u,-w,z-u` are distinct: the remaining possible
collision would force one of u,w,z,v to be zero.

Seek a parameter a for which all four linear forms

`a`, `b=-u-a`, `c=-w-a`, `d=u+a-z`

are nonzero squares. Their leading coefficients are nonzero and their
roots are the four distinct points above. Standard quadratic-character
indicators, exact two-factor sums, and the Weil bound give at least

`(q-38-11*sqrt(q))/16`

such parameters. Here the empty subset contributes q; one-factor sums
are zero; the six two-factor sums have absolute value one; the four
three-factor sums have absolute value at most `2*sqrt(q)` each; and the
four-factor sum has absolute value at most `3*sqrt(q)`. Removing the four
roots subtracts at most `4*8=32` from the unnormalized indicator sum.
Thus the stated lower bound is positive for every q>=243: at q=243 its
numerator is `205-99*sqrt(3)>0`, and it increases thereafter. Every subset
product of these distinct affine factors satisfies the stated Weil
hypotheses. No diagonal-triple exclusions are necessary: their equations
already hold identically in F_3.

The four zero-sum triples

`(u,a,b)`, `(w,a,c)`, `(b,z,d)`, `(c,v,d)`

then imply `f(u)+f(v)=f(w)+f(z)` by subtraction. Thus f satisfies every
Freiman two-sum relation on S.

For each x in K, choose a,b in S with a-b=x and define

`L(x)=f(a)-f(b)`.

For x!=0, with eta=chi(-1), the exact two-factor indicator count is

`#{b : b,b+x in S}=(q-3-(1+eta)*chi(x))/4>0`.

Its numerator is at least q-5; x=0 has |S| representations. Thus S-S=K,
and the Freiman relation makes the definition independent of representation:
a-b=c-d implies a+d=c+b.
For x,y with x,y,x+y all nonzero, choose b such that

`b`, `b+x`, `b+x+y`

are squares. The three roots are distinct, and the same indicator
calculation gives at least `(q-15-2*sqrt(q))/8>0` choices. The empty term
contributes q, the three quadratic sums cost at most three, the cubic
sum costs at most `2*sqrt(q)`, and deleting roots costs at most twelve.
Telescoping the three differences proves `L(x+y)=L(x)+L(y)`. Zero
arguments are immediate, and the case x+y=0 follows from L(-x)=-L(x).
Thus L is F_3-linear. Fixing any b in S then gives

`f(u)=L(u)+c` on S.

This establishes the rank criterion for every m>=5; the exact rank
certificates for m=3,4 finish PM-THEOREM-0013. Theorem 0011 and the
converse square-scaling/Frobenius actions prove

`Aut(H_K)={u -> s*u^(3^j) : s in S, 0<=j<m}`

for every m>=3, of order `m*(3^m-1)/2`. Combining with SC-008 gives the
complete arbitrary ternary-order preserver group

`C_2^((3^m-1)/2) semidirect (S semidirect Gal(K/F_3))`.

Explicitly every such map fixes zero and has
`T(x)=epsilon_[x]*lambda*x^(3^j)` on K*, where lambda!=0,
epsilon_[x] is an independent sign on each opposite pair, and j is one
fixed exponent for the entire map. This description has a redundant global
sign; the group order is `2^((q-1)/2)*(q-1)*m/2`.
The split quotient description requires a choice of representatives for
opposite pairs and does not assert a canonical semilinear lift.

The exceptional finite cases remain: F_9 has 384 arbitrary preservers,
and F_3 has all six permutations. The affine-kernel conclusion fails for
F_9, as the negative rank certificate demonstrates.

The tools are classical character sums, Freiman extension and Carlitz.
This is not a new Weil bound or a new general extension method. See the
sixth-cycle review for objections, their resolution and the bounded
prior-art comparison. No historical-first claim is made.

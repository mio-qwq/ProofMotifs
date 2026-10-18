# SC-007: a generator-based linear defect test

Date: 18 October 2026. Source baseline: SC-006 at verified remote commit
`a434475c` on `research/ongoing`.

**PM-THEOREM-0007.** Given a genuine field generator and its power basis,
at most `2m-3` quadratic-defect values suffice to recognize scalar-Frobenius
maps on F_(3^m). Every tested parameter can be chosen to give an
order-7 source conic, so the first nonzero defect directly supplies an
order-7 to order-5 witness, without extra repair evaluations.

**PM-THEOREM-0008.** In the deterministic defect-only oracle model
specified in Section 8, recognition requires at least
`ceil((m-1)/2)` queries in the worst case. The linear order of growth of
the upper bound is therefore optimal in that model, without a sharp
constant or a T-query optimality claim.

**PM-COUNTEREXAMPLE-0004.** Explicit examples below show why the generator
row must include its last basis position, why the multiplier must
generate the field, and why the linear test is not valid for arbitrary
quadratic maps.

Mathematical status: complete written proofs and exact checks of the two
finite-field counterexamples. Task PM-SC007-B supplied an independent AI
derivation; final cross-review is recorded separately by the coordinator.
Formalization: NOT_STARTED. No human or Lean verification is claimed.
**NOVELTY_UNVERIFIED.** Checking a field homomorphism through the image of
a generator is classical. This file specializes that mechanism to the
project's defect and admissible conic parameters; it does not establish a
new method for validating field homomorphisms.

## 1. Assumptions and definitions

Let `K=F_(3^m)`, where `m>=3`. Fix an element alpha of degree exactly m
over F_3. Thus

`(1,alpha,...,alpha^(m-1))`

is an F_3-basis of K. It is enough that alpha generate K as a field; alpha
need not generate the multiplicative group. A quotient presentation
`K=F_3[X]/(f)` with f irreducible of degree m supplies such an alpha as
the residue class of X. A reducible modulus does not supply the assumed
field and is outside the theorem.

Let `T:K -> K` be an additive bijection. Put

`A=T(1)`, `S(x)=T(x)/A`,

`Q(x)=A*T(x^2)-T(x)^2`,

`H(x,y)=A*T(x*y)-T(x)*T(y)`.

Here `A != 0`, S is additive, bijective and unital, H is F_3-bilinear,
and the SC-006 polarization identities give

`Q(x)=H(x,x)`,

`Q(x+y)-Q(x)-Q(y)=2*H(x,y)`,

`Q(x+y)+Q(x-y)=2*Q(x)+2*Q(y)`.

Also `H(1,x)=0` and `Q(1)=0`. Additivity and bijectivity are hypotheses,
not properties certified by the test below for an arbitrary oracle.

## 2. Why one generator row determines multiplicativity

**Lemma.** If

`H(alpha,alpha^k)=0` for `1<=k<=m-1`,

then S is a field automorphism.

**Proof.** The missing basis position k=0 is automatic because
`H(alpha,1)=0`. F_3-bilinearity in the second argument therefore gives
`H(alpha,x)=0` for every x in K. If `beta=S(alpha)`, division by `A^2`
turns this into

`S(alpha*x)=beta*S(x)` for every x in K.

Iterating gives `S(alpha^r*x)=beta^r*S(x)` for every nonnegative integer
r and every x. In particular `S(alpha^r)=beta^r`. Write an arbitrary
element y as `p(alpha)` for a polynomial p with coefficients in F_3.
Additivity and F_3-linearity now imply

`S(y*x)=p(beta)*S(x)=S(y)*S(x)`.

Thus S is multiplicative. Its assumed bijectivity makes it a field
automorphism. The field automorphisms of F_(3^m) are the Frobenius powers,
so `T(x)=A*x^(3^j)` for some `0<=j<m`. The converse also holds, since
every such map has H and Q identically zero. This proves the lemma.

The last row condition, k=m-1, includes multiplication by alpha of the
last power-basis element. It enforces compatibility with reduction of
`alpha^m` by the minimal polynomial. It cannot be silently omitted.

## 3. The basic 2m-3 defect values

Consider the values of Q on

`alpha`,

`alpha^k` and `alpha+alpha^k` for `2<=k<=m-1`.

There are `1+2*(m-2)=2m-3` listed points. If all values vanish, then

`H(alpha,alpha)=Q(alpha)=0`,

and polarization gives `H(alpha,alpha^k)=0` for every remaining
`2<=k<=m-1`. The generator-row lemma forces T to be scalar-Frobenius.
Consequently a non-scalar-Frobenius additive bijection has a nonzero
defect at one of these points.

This argument uses the special algebraic origin of Q. It does not say
that arbitrary quadratic forms on an m-dimensional F_3-space are
determined by this many values; Section 6 gives an explicit guardrail.

## 4. Making every query an admissible witness parameter

Let

`F={x in K : x^9=x}`.

This is the subfield F_3 when m is odd, and F_9 when m is even. Since
alpha has degree m>=3, `alpha not in F`.

For a parameter t, recall the SC-006 conic

`a(t)=1-t^2+t`, `b(t)=1-t^2-t`, `c(t)=-1-t^2`.

Its invariant values are

`e1(t)=0`, `e2(t)=-t^2*(1-t^2)^2`.

Its zero-coordinate set is `F_9 \ F_3` when that subfield is present;
otherwise the set is empty. Therefore every t outside F has nonzero
coordinates, nonzero e2, and source order exactly 7. If `Q(t) != 0`, the
images have sum of squares Q(t), so their ternary order is exactly 5.
These full-order statements use SC-003 and SC-006, including their
finite-support termination argument.

Here is a test that keeps the bound `2m-3` while using only parameters
outside F.

1. Test Q(alpha). If it is nonzero, return the conic at alpha.
2. For each `k=2,...,m-1`, put `u=alpha^k`, `v=alpha+u`, and
   `w=alpha-u`. Choose two query points by the following rule:

   | Field-membership case | Query points |
   | --- | --- |
   | `u in F` | v and w |
   | `u not in F`, `v in F` | u and w |
   | `u not in F`, `v not in F` | u and v |

   Return the conic at the first queried point with a nonzero Q-value.
3. If every queried value is zero, accept T as scalar-Frobenius.

**Admissibility.** Since alpha is outside the subfield F, u and v cannot
both lie in F. In the first case v and w are outside F, because either
membership would force alpha into F. In the second case u is outside F
by assumption. If w also lay in F, then `v+w=2*alpha` would put alpha in
F, which is impossible. The third case is immediate. Thus every
actually queried point is outside F.

**Completeness.** Suppose the test never finds a nonzero value. Then
`Q(alpha)=0`. For each k the parallelogram identity becomes

`Q(v)+Q(w)=2*Q(u)`.

In the first case the selected zeros at v and w force Q(u)=0. In the
second case the selected zeros at u and w force Q(v)=0. In the third
case those are already the two selected zeros. Thus, in all cases,
the original basic values Q(u) and Q(alpha+u) vanish. Section 3 forces
T to be scalar-Frobenius.

Conversely a scalar-Frobenius map has Q identically zero and is accepted.
Every rejection returns an actually evaluated nonzero Q-value at an
admissible point. No inferred-only output or extra repair query is
needed. This proves PM-THEOREM-0007.

For odd m, the original basic points already lie outside F_3: each is a
nonconstant polynomial in alpha of degree less than m and cannot equal
an F_3 element. Hence no replacements are necessary in that case.

### Cost and access model

The bound `2m-3` counts evaluations of the K-valued defect Q. Field
membership uses ninth powering, a constant number of field operations.
Generating the powers and selected points takes O(m) field operations.
Given unit-cost access to T, each uncached Q-value uses two T calls and
a constant number of field operations; a conservative bound including
`A=T(1)` is `1+2*(2m-3)=4m-5` T calls. Previously known values may be
reused.

This is not an optimal T-query bound. Because T is assumed additive,
its m values on any F_3-basis already determine the entire map. An
implementation may read those m images once and compute every required
Q-value from them. The cost of that linear algebra, finite-field
arithmetic, or applying a dense matrix for T must be accounted for
separately. No O(m) bit-complexity claim follows.

The generator and power basis are also inputs or separately charged
preprocessing. An arbitrary supplied basis cannot be substituted for
the powers in the generator-row proof. Finding a degree-m element,
validating an irreducible modulus, and changing coordinates are not
included in the `2m-3` defect-evaluation count.

The assumption m>=3 is essential for the witness part. In F_9 every
additive bijection preserves ternary order even though some have
nonzero Q. There is no parameter outside F_9 to return there.

## 5. PM-COUNTEREXAMPLE-0004: missing hypotheses fail

### 5.1 Omitting the last generator-row entry

Take

`K=F_3[alpha]/(alpha^3+2*alpha+1)`,

so `alpha^3=alpha+2`. The cubic has no root in F_3 and is irreducible.
Put `beta=alpha^2` and define an F_3-linear map by

`S(1)=1`,

`S(alpha)=alpha^2`,

`S(alpha^2)=beta^2=alpha^2+2*alpha`.

These images are a basis, so S is a unital additive bijection. Nevertheless

`H(alpha,alpha)=S(alpha^2)-S(alpha)^2=0`,

while

`H(alpha,alpha^2)=S(alpha^3)-S(alpha)*S(alpha^2)`

`=(alpha^2+2)-(alpha^2+alpha+1)=1-alpha != 0`.

For m=3 the truncated conditions `1<=k<=m-2` are therefore all satisfied,
but S is not multiplicative. This refutes the proposal to omit the last
row position as a general rule. The full theorem includes that position.

### 5.2 A non-generating multiplier can miss every defect in its row

Let `F_9=F_3[i]`, where `i^2=-1`. Its nonzero squares are
`{1,-1,i,-i}`, so `1+i` is not a square. Consequently

`K=F_9[gamma]/(gamma^2-(1+i))`

is the field F_81. Define an F_9-linear map by

`S(a+b*gamma)=a+b+b*gamma` for `a,b in F_9`.

This is a unital additive bijection with `S(gamma)=gamma+1`, and it fixes
F_9 pointwise. Thus

`H(i,x)=S(i*x)-S(i)*S(x)=0` for every x in K.

Yet

`Q(gamma)=S(gamma^2)-S(gamma)^2`

`=(1+i)-(gamma+1)^2=gamma+2 != 0`.

Thus testing a full multiplier row for the nongenerating element i
does not establish multiplicativity. This example satisfies stronger
row vanishing than any finite subset of that row could test.

### Exact arithmetic checks performed

The two examples were checked using the project's validated `Field`
implementation. The first used modulus coefficients `(1,2,0,1)` and
basis-image encodings `(1,9,15)`. All 729 additive input pairs were
checked; the two displayed row defects encoded as 0 and 7, with
`7=1+2*alpha`.

For the second, eliminating `i=gamma^2-1` gives the irreducible modulus
`gamma^4+gamma^2+2`, with coefficient tuple `(2,0,1,0,1)`. The map's
power-basis images encode as `(1,4,9,36)`, and i encodes as 11. All 6,561
additive input pairs and all 81 values H(i,x) were checked; the former
satisfied additivity and the latter were zero. The defect Q(gamma)
encoded as 5, namely `gamma+2`. The images had 27 and 81 distinct values,
respectively. These checks use an existing common arithmetic engine;
they are not an independent field-arithmetic implementation and do not
replace the algebraic proofs above.

## 6. A generic quadratic-map guardrail

For m>=4 write the power-basis coordinates of x as

`x=x_0+x_1*alpha+...+x_(m-1)*alpha^(m-1)`.

The K-valued homogeneous quadratic map

`R(x)=x_2*x_3`

is nonzero: `R(alpha^2+alpha^3)=1`. It vanishes on all basic test points,
since each has at most one nonzero coordinate among indices 2 through
m-1. It also vanishes on all replacement test points, which are again
single basis elements or a signed sum of alpha with one other basis
element. Moreover 1 lies in the radical of its polar form, as for Q.

Thus the `2m-3` test set is not a universal identity test for arbitrary
quadratic maps with that radical. R is not asserted to arise from an
additive-bijection defect. Indeed PM-THEOREM-0007 shows that a nonzero
such R cannot arise as Q while passing all these tests. The
generator-intertwining argument is the additional structure that makes
the smaller test valid.

## 7. Research interpretation and unresolved work

The project now has a linear number of directly checked admissible
defect parameters when a power-basis generator is supplied. For m=3
this matches the previous three-point bound; from m=4 onward it improves
the number of defect values over the unrestricted quadratic-basis test.
No minimality is claimed.

The underlying field-generator validation is classical. Historical
originality of this exact conic witness packaging and its membership
replacements remains unresolved. Closest-prior-art analysis, the
independent AI review, and deterministic computational replay must be
integrated by the coordinator before changing the claim's acceptance
or originality status. This file makes no claim of a solved published
open problem, formal verification, or publication readiness.

## 8. PM-THEOREM-0008: a deterministic defect-only lower bound

### Exact access model

Fix `K=F_(3^m)`, `m>=3`. An algorithm knows the field and may perform
arbitrary computations in it, including choosing a basis or generator.
An unknown unital additive bijection `S:K -> K` is promised, and the
algorithm may query only

`Q_S(t)=S(t^2)-S(t)^2`.

It has no access to S-values, a matrix or polynomial description of S,
or any other information about S beyond the promise and these answers.
It is deterministic, may choose queries adaptively, and must decide
correctly for every promised S whether S is a field automorphism.
Equivalently, it must distinguish an identically zero defect from all
nonzero defects arising from these maps.

**Theorem.** Every such algorithm needs at least `ceil((m-1)/2)`
defect queries in the worst case. Indeed this many queries are necessary
on the all-zero transcript from the identity map.

**Proof.** Suppose an algorithm halts on that transcript after s queries
`t_1,...,t_s`, where `1+2s<m`. Form the F_3-subspace

`U=span_(F_3){1,t_1,t_1^2,...,t_s,t_s^2}`.

Its dimension is at most `1+2s<m`, so there is a nonzero F_3-linear
functional `phi:K -> F_3` vanishing on U. Embed its values into the prime
subfield of K, and define

`S(x)=x+phi(x)*1`.

This S is additive and unital because phi(1)=0. If
`N(x)=phi(x)*1`, then `N^2=0`; consequently `I-N` is the inverse of
`S=I+N`. Thus S is an additive bijection, and it is not the identity
because phi is nonzero.

Every queried t_i and t_i^2 is fixed by S, so

`Q_S(t_i)=t_i^2-t_i^2=0`.

An induction through the deterministic execution shows that S produces
exactly the same queries and responses as the identity through the
halting point. The algorithm must accept on the identity transcript.

However S is not a field automorphism. Its fixed subspace is exactly
`ker(phi)`, of F_3-dimension m-1. A nonidentity field automorphism of K is
a Frobenius power `x -> x^(3^j)`, `1<=j<m`; its fixed field has
F_3-dimension `gcd(m,j)`, a proper divisor of m and therefore at most
m/2. Since `m-1>m/2` for m>=3, no such automorphism equals S. The identity
was already excluded. Equivalently, S cannot be scalar-Frobenius:
normalization at 1 would force the scalar to be 1.

Thus accepting the all-zero transcript after s queries would also
accept this non-automorphism, a contradiction. It follows that
`1+2s>=m`, hence `s>=ceil((m-1)/2)`.

### What this does and does not establish

Together with PM-THEOREM-0007, the lower bound gives query growth
Theta(m) for this deterministic defect-only decision problem, with
separate field-generator preprocessing. The upper test also returns an
admissible witness on rejection. This does not identify the optimal
constant, and it says nothing here about randomized algorithms.

The lower bound applies to procedures that must both recognize the
automorphism case and reject all other promised maps. It is not asserted
unchanged for an extractor given an additional promise that the unknown
map is not an automorphism and allowed to output an unevaluated point.

The access restriction is essential. If S-values are available, m basis
images determine S. If its matrix or polynomial description is supplied,
one may inspect that description without any oracle queries. No
information-theoretic lower bound on those richer models, total
arithmetic complexity, or bit complexity is claimed here.

The perturbation `I+1 tensor phi` and the annihilator argument are
standard linear-algebra tools. Historical originality of this exact
lower-bound formulation remains unverified.

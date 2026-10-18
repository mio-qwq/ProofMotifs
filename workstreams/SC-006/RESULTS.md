# SC-006: constructive ternary witnesses and arbitrary-field preservers

Date: 18 October 2026. Source baseline: SC-003 and SC-005 at commit
`4f6db95fe5b72c12bdbfc875026f47698735f817`.

**PM-THEOREM-0005:** a deterministic finite-field witness construction using
at most `m(m-1)/2 + 3` directly checked quadratic-defect values, with the final
extra check avoidable by an exact identity. **PM-THEOREM-0006:** the
order-preserver classification over every characteristic-three field, with
the precise exceptional field F_9.

Mathematical status: written proofs below. Formalization: NOT_STARTED; no
Lean verification or human review is claimed. The derivation and challenge
in task PM-WITNESS-20261018-B were performed by a task-scoped AI researcher.
The coordinator has separately received independent AI review; its final
review record belongs in the project review log. **NOVELTY_UNVERIFIED.**
Quadratic polarization, finite-field automorphisms, conic parameterization
and polynomial identity testing are established tools. A new derivation or
a faster implementation does not establish historical originality.

## 1. Definitions and the finite-support issue

Let K be a field of characteristic three. A finite weight is a function
`mu: K -> K` supported on finitely many points. Write `delta_a` for a unit
weight at a, use additive convolution, and put

`Delta_a = delta_a - delta_0`.

For every nonnegative integer n, its ordinary moment is

`M_n(mu) = sum_x mu(x) x^n`,

where `x^0=1`, including at zero. Its order is the least n with a nonzero
moment, and is infinity for the zero weight. These conventions coincide:
if a weight has s distinct support points and moments 0 through s-1 all
vanish, the Vandermonde matrix has determinant equal, up to sign, to the
product of all differences of distinct support points, which is nonzero in
K. The weight is therefore zero. This argument holds over finite and
infinite fields; it makes no assumption about the availability of more
than s distinct field elements.

Define

`C(a,b,c) = ord(Delta_a * Delta_b * Delta_c)`.

Only coefficients in F_3 occur in these particular weights. This
restriction matters when applying field automorphisms to moments.

We use the following SC-003 identities, which also give a short proof of
the classification needed here. Put

`e1 = a^2+b^2+c^2`,

`e2 = a^2*b^2+a^2*c^2+b^2*c^2`.

Inclusion-exclusion and the multinomial formula give

`M_0=...=M_4=M_6=0`,

`M_5=-abc*e1`, and `M_7=-abc*e2`.

If `abc=0`, the weight is zero. If `abc != 0`, these identities give order
5 when `e1 != 0`, and order 7 when `e1=0, e2 != 0`. In the remaining case
the polynomial with roots `a^2,b^2,c^2` is `X^3-a^2*b^2*c^2`. Injectivity
of cubing in a field forces the three squares to coincide, so all three
directions are signed copies of a. Their product of differences is a
translate, with a sign, of `Delta_a^3=0`. Thus there is no unexamined
higher finite order. In particular, for nonzero coordinates,

`C(a,b,c) != 5` if and only if `e1=0`.

## 2. The conic family, including every exceptional parameter

For t in K set

`a(t)=1-t^2+t`,

`b(t)=1-t^2-t`,

`c(t)=-1-t^2`.

Direct expansion gives

`e1(t)=0`,

`e2(t)=-t^2*(1-t^2)^2`.

For the second identity, write A=a(t)^2, B=b(t)^2 and C=c(t)^2. Since
`A+B+C=0`, one has `AB+AC+BC=-(A-B)^2`; also
`A-B=t*(1-t^2)`.

It follows that `e2(t)=0` exactly for `t in F_3`. These parameters give
collinear directions and zero ternary weights. They must not be counted as
order-7 sources.

The zero-coordinate exceptional set is

`E = {t in K : a(t)*b(t)*c(t)=0}`.

Its polynomial is

`a(t)*b(t)*c(t)=-(t^2+1)*(t^4+1)`.

The identity

`(X^3-X)*(X^2+1)*(X^4+1)=X^9-X`

shows that, in an algebraic closure, E consists precisely of
`F_9 \ F_3`. Consequently E is empty if K does not contain F_9, and
otherwise equals the six elements of that subfield outside F_3. In a
finite field F_(3^m), E is empty for odd m and has size six for even m.

Every parameter outside `E union F_3` therefore gives source order exactly
7. No assertion about linear independence of the three directions is
required.

## 3. The quadratic defect

Let `T:K -> K` be an additive bijection and put `A=T(1)`, which is nonzero.
Define the K-valued function

`Q(t)=A*T(t^2)-T(t)^2`.

Additivity includes F_3-linearity. The following are exact identities:

`Q(r*t)=r^2*Q(t)` for `r in F_3`,

`B(x,y):=Q(x+y)-Q(x)-Q(y)=2*(A*T(x*y)-T(x)*T(y))`,

`B(1,x)=0`, and `Q(1)=0`,

`Q(t+r)=Q(t)` for `r in F_3`,

`Q(t+u)+Q(t-u)=2*Q(t)+2*Q(u)`.

Here B is F_3-bilinear, so Q is a homogeneous quadratic map over F_3.
In particular Q vanishes on F_3. These identities hold over infinite K as
well as finite K.

Writing `D=T(t^2)` and `H=T(t)`, the transformed conic directions are
`A-D+H`, `A-D-H`, `-A-D`; their sum of squares is

`(A-D+H)^2+(A-D-H)^2+(-A-D)^2=A*D-H^2=Q(t)`.

Thus any t outside E with `Q(t) != 0` automatically lies outside F_3 and
gives the explicit certificate

`C(a(t),b(t),c(t))=7`,

`C(T(a(t)),T(b(t)),T(c(t)))=5`.

Nonzero source coordinates have nonzero images by injectivity. The
conclusion is a full-order statement, not just nonvanishing of one
selected moment.

## 4. Removing an exceptional parameter

Suppose K is not F_9 and `Q(t) != 0`. If t lies outside E, it is already
usable. Otherwise K contains F_9 and `t in F_9 \ F_3`. Choose
`u in K \ F_9`.

If `Q(u) != 0`, use u. If `Q(u)=0`, the parallelogram identity gives

`Q(t+u)+Q(t-u)=2*Q(t) != 0`.

Both `t+u` and `t-u` lie outside F_9, so at least one is usable. This
requires at most three extra directly checked Q-values: u, then t+u,
then t-u. If the first two are zero, the last value is already proved to
be `2*Q(t) != 0`, so evaluating it is optional and two extra evaluations
suffice to determine a witness.

The hypothesis `K != F_9` is essential: that field has no element u of
the required kind. The repair neither assumes surjectivity of Frobenius
nor takes square roots in K.

## 5. PM-THEOREM-0005: a finite quadratic-basis witness algorithm

**Theorem.** Let `K=F_(3^m)`, `m>=3`, and let T be an additive bijection
which is not of the form `lambda*x^(3^j)`. Given an F_3-basis
`(1,e_1,...,e_(m-1))`, one can construct a source-order-7,
target-order-5 ternary certificate using at most

`N+3` directly checked Q-values, where `N=m*(m-1)/2`.

With the last repair value inferred instead of evaluated, at most `N+2`
Q-evaluations suffice. The construction does not enumerate field triples
or all field parameters.

**Why a nonzero defect exists.** If Q vanishes identically as a function,
put `S(x)=T(x)/A`. Then S is additive, unital and square preserving.
Expanding `S((x+y)^2)=S(x+y)^2`, using additivity and cancelling the square
terms gives

`2*S(x*y)=2*S(x)*S(y)`.

Since 2 is invertible, S is multiplicative. Bijectivity makes S a field
automorphism. The automorphisms of F_(3^m) are the Frobenius powers,
contradicting the hypothesis on T. For completeness, the last standard
finite-field fact follows by choosing an element of degree m over F_3:
its conjugates are its m distinct Frobenius iterates, and an automorphism
must send that generator to one of them. Its value there determines the
automorphism on K.

**Detection.** Evaluate Q successively on the N points

`e_i` for `1<=i<=m-1`,

`e_i+e_j` for `1<=i<j<=m-1`.

If all these values vanished, the diagonal values Q(e_i) and all
off-diagonal polar values B(e_i,e_j) would vanish. Values involving 1
already vanish by Section 3. For every `x=sum r_i*e_i`, with `e_0=1`,
the quadratic expansion

`Q(x)=sum_i r_i^2*Q(e_i)+sum_(i<j) r_i*r_j*B(e_i,e_j)`

would imply Q(x)=0. Thus some tested parameter t has nonzero defect.

If m is odd, E is empty, so this t is immediately usable. If m is even,
test whether `t^9=t`. If false, t is usable. If true, nonzero Q excludes
F_3, so apply Section 4. One of the input basis elements is outside F_9
because `m>=4`; membership can be checked by ninth powering. Finally
return the three displayed conic directions.

**Cost model.** The bound counts evaluations of Q, not prime-field
operations or an entire finite-field representation setup. With oracle
access to T, precompute `A=T(1)`; each uncached Q-value uses two T calls
and a constant number of field operations. A conservative bound is
`1+2*(N+3)` T calls. Known values can be reused. The remaining arithmetic
is O(m^2) field operations, including an O(m) search among basis elements
for u; the cost of a field operation and of applying T depends on the
representation. If an input basis does not contain 1, first change it to
one that does. Constructing the field, validating its representation,
and obtaining or changing a basis are separate preprocessing costs.

**Optional adapted-basis improvement.** For even m, choose the basis to
start `(1,i,u,...)`, where `i in F_9 \ F_3` and `u not in F_9`. Every
point in the preceding N-point test set is outside F_9 except i itself.
Replace that single test point by `i-u`. The points u and i+u are already
in the test set. If all replacement-set values vanished, then

`Q(i-u)+Q(i+u)=2*Q(i)+2*Q(u)`

would also force Q(i)=0, and the original detection proof would force
Q=0. Thus N directly checked, admissible parameters suffice. For odd m
the original N test points are already admissible. This improvement
requires the adapted basis as input or separate preprocessing; it does
not assert that finding that basis is free. For example, a polynomial
basis representation permits computation of the fixed space of
`x -> x^9` by F_3 linear algebra, followed by basis extension.

### A conservative finite witness-count corollary

The earlier root-bound proof also yields an independently useful count.
Represent the additive map by its unique linearized polynomial

`L(X)=sum_(j=0)^(m-1) l_j*X^(3^j)`.

Existence follows because evaluation of these polynomials is injective
(degree at most `3^(m-1)<3^m`) and the coefficient space and the space of
F_3-linear maps both have `3^(m^2)` elements. The polynomial

`G(X)=A*L(X^2)-L(X)^2`

has degree at most `2*q/3`, where `q=3^m`. It is nonzero because Q is not
identically zero as a function. Hence at least q/3 parameters have
nonzero Q. Such parameters never lie in F_3. Removing E leaves at least

* `q/3` order-changing parameters when m is odd;
* `q/3-6` order-changing parameters when m is even.

Both bounds are positive in the asserted range: odd m has `q>=27`;
even m has `q>=81`. These are conservative lower bounds on parameters,
not claims that all their ternary weights are distinct, nor a sampling
guarantee for a particular probability distribution.

## 6. PM-THEOREM-0006: arbitrary characteristic-three fields

**Theorem.** Let K be any field of characteristic three, and let
`T:K -> K` be an additive bijection.

* If `K != F_9`, then T preserves C on every triple if and only if
  `T(x)=lambda*sigma(x)` for `lambda in K*` and a field automorphism
  `sigma in Aut(K)`.
* If `K=F_9`, every additive bijection preserves C; these maps form
  `GL(2,3)` and there are 48 of them.

This includes finite, infinite, perfect and imperfect fields. In an
infinite field, sigma need not be a Frobenius power. The theorem concerns
bijections; merely injective maps would require a different formulation
using embeddings.

**Necessity outside F_9.** Suppose T preserves every order. For every
parameter outside E, the source conic has nonzero coordinates and e1=0.
Its order is therefore not 5. The images have nonzero coordinates too;
order preservation forces their sum of squares, namely Q(t), to vanish.
If Q had any nonzero value, Section 4 would produce a nonzero value
outside E, a contradiction. Thus Q is identically zero as a function.
The square-preserving normalization argument from Section 5, which did
not use finiteness, shows that `T/A` is a field automorphism.

**Sufficiency.** Suppose `T=lambda*sigma`. For every subset of the three
directions, additivity maps its sum to the sum of its images. The signs
in the eight-subset expression for the moments lie in F_3 and are fixed
by sigma. Multiplicativity therefore gives, for every n,

`M_n(Delta_(T(a))*Delta_(T(b))*Delta_(T(c)))`

`=lambda^n*sigma(M_n(Delta_a*Delta_b*Delta_c))`.

The two moments vanish at exactly the same indices. The finite-support
argument in Section 1 handles infinity correctly, so all orders agree.

**The exceptional field.** In F_9 the four one-dimensional F_3-subspaces
have nonzero representatives `1,i,1+i,1-i`, with `i^2=-1`. Their squares
are the four distinct values `1,-1,-i,i`, which sum to zero. Three of
these values sum to zero exactly when all three coincide: with exactly
two equal the sum is the third minus the repeated value; with all
distinct it is the negative of the fourth, nonzero, square value.
Consequently a nonzero triple has e1=0 exactly when all directions lie
on one F_3-line. Such a weight is zero. Every other nonzero triple has
order 5. These cases, and a zero coordinate, are preserved by every
additive bijection, proving the exception and its count
`(9-1)*(9-3)=48`.

## 7. Boundaries, review and prior-art questions

The construction proves an exact 7-to-5 certificate under all of its
stated hypotheses. It supplies no witness for a scalar-automorphism map,
and cannot supply one for an additive bijection of F_9, since none exists
there. It does not classify arbitrary permutations, coefficient weights
outside F_3, approximate preservation, other characteristics, or
non-field rings. No numerical approximation enters the arguments.

For finite K, PM-THEOREM-0006 specializes to the classification of
SC-005. Its proof removes that result's finite-field root-count step and
explains exactly why F_9 is exceptional. This is a mathematical
strengthening within the project; whether it is a historically new
theorem or a consequence of an existing quadratic-cone preserver theorem
requires focused literature comparison. The coefficient representation,
the conic family, the moment identities and square-preserving-map
argument should not be presented as newly invented methods.

See the [independent AI review record](../../docs/reviews/THIRD_CYCLE.md),
[exact replay](../../research/experiments/constructive-results.json), and
[source-specific prior-art audit](../../research/literature/PRESERVER_AUDIT_20261018.md).
Lester's 1977 theorem classifies full-cone preservers over arbitrary fields;
the project must separately assess the missing-coordinate extension, the
F_9 exception and the extractor. No historical-priority,
publication-readiness or formal-verification claim follows from this file.

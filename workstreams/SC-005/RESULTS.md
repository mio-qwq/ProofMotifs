# SC-005: additive maps preserving ternary cancellation order

**PM-THEOREM-0004.** Complete written proof; exhaustive normalized-map checks in F_3, F_9 and F_27. Formalization: NOT_STARTED. Separate task-scoped AI reviews A/C accepted the proof on 2026-10-18; no human peer review is claimed. See [review](../../docs/reviews/THIRD_CYCLE.md). **NOVELTY_UNVERIFIED; no Level 2 or publication claim.**

## Question and definitions

For K=F_{3^m}, m>=1, put

C(a,b,c)=ord((delta_a-delta_0)*(delta_b-delta_0)*(delta_c-delta_0)),

with the full ordinary-moment order of SC-001, including infinity for the zero weight. Which additive bijections T:K->K satisfy

C(T(a),T(b),T(c))=C(a,b,c) for every a,b,c in K?

This asks for a transformation preserving a specified cancellation mechanism, not merely preserving vector-space rank. Coefficients of these weights belong to F_3. It does not assert the same classification for all arbitrary K-valued weights with coefficients held fixed.

## Exact classification

If m!=2, precisely the maps

**T(x)=lambda x^{3^j}, lambda in K*, 0<=j<m**

have the stated property. Their number is (3^m-1)m.

For the exceptional field F_9 (m=2), **every additive bijection** has the property. There are |GL(2,3)|=(9-1)(9-3)=48 such maps; only 16 are scalar-Frobenius maps.

## Proof for q=3^m>=27

### Step 1: what a cancellation-order preserver must preserve

For a,b,c all nonzero, SC-003 proves that C(a,b,c)!=5 exactly when

a^2+b^2+c^2=0.

Since T is injective and additive, it maps nonzero elements to nonzero elements. Thus preservation of C implies preservation of this quadratic zero relation on triples with nonzero coordinates. No converse on triples with a zero coordinate is silently assumed.

### Step 2: a parameterized family and an explicit exceptional set

For t in K, define

a(t)=1-t^2+t, b(t)=1-t^2-t, c(t)=-1-t^2.

Direct expansion in characteristic three gives a(t)^2+b(t)^2+c(t)^2=0. The product of the three displayed quadratics is a nonzero polynomial of degree six, so at most six t have a zero coordinate. For every other t, Step 1 applies.

Write A=T(1), B=T(t), D=T(t^2). Additivity includes F_3-linearity. The transformed sum of squares is

(A-D+B)^2+(A-D-B)^2+(-A-D)^2 = A D - B^2.

It follows that T(1)T(t^2)-T(t)^2=0 for at least q-6 values of t. This is the critical bridge from order preservation to a multiplicative constraint. The six omitted parameters explain why small fields cannot simply be swept into the general proof.

### Step 3: upgrade values to a polynomial identity

Every additive map on F_{3^m} has a unique representation

L(X)=sum_{i=0}^{m-1} l_i X^{3^i}.

Here is a finite proof of the needed representation. These polynomials define additive maps. A nonzero such polynomial has degree at most 3^{m-1}<q and cannot vanish on all q elements, so evaluation is injective. The coefficient space has q^m=3^{m^2} elements, exactly the number of linear maps on an m-dimensional F_3-vector space, hence evaluation is also surjective.

The polynomial

G(X)=T(1)L(X^2)-L(X)^2

has degree at most 2*3^{m-1}=2q/3. For q>=27, q-6>2q/3. The root bound and Step 2 therefore force G=0 as a formal polynomial, not merely a polynomial function modulo X^q-X.

For i<j, the coefficient of X^{3^i+3^j} in G is -2 l_i l_j. These exponents are distinct from one another and from all 2*3^k: their base-three expansions have two digits 1 instead of one digit 2. Since -2 is nonzero and K is a field, l_i l_j=0 for all i<j. At most one l_i is nonzero. T is a bijection, so at least one is nonzero. This proves T(x)=lambda x^{3^j} with lambda!=0.

An alternative last step is to divide T by T(1), obtain an additive unital square-preserving map, and recover multiplication by polarization of (x+y)^2. This is an algebraic cross-check by the same author, not independent review.

### Step 4: sufficiency

A scalar-Frobenius map is additive and bijective. For every n>=0 the subset-sum expression for the moments gives

M_n(Delta_{T(a)}*Delta_{T(b)}*Delta_{T(c)})
 =lambda^n M_n(Delta_a*Delta_b*Delta_c)^{3^j},

because the signs lie in F_3. The two moments vanish at exactly the same indices. Thus their complete ordinary orders agree. This also covers zero weights and all coincident directions. The maps are distinct: evaluation at 1 distinguishes lambda; two different Frobenius powers cannot agree on q elements, by the polynomial root bound.

## The small fields

For F_3 every additive bijection is multiplication by 1 or -1, so the stated non-exceptional classification holds. All ternary differences in F_3 happen to be zero; no extra non-bijective maps are included in the theorem.

Write F_9=F_3[i] with i^2=-1. Its four one-dimensional F_3-subspaces have nonzero representatives 1,i,1+i,1-i, whose squares are respectively 1,-1,-i,i. Opposite representatives have the same square; the four square values are distinct, nonzero, and sum to zero.

For a triple of nonzero directions, three of these square values sum to zero only when they all coincide: if exactly two coincide, the sum is the third minus the repeated value, nonzero; if all three are distinct, the sum is the negative of the fourth square value, also nonzero. Consequently a^2+b^2+c^2=0 precisely when all three directions lie in one F_3-line. SC-003 therefore gives only order 5 off those lines, and infinity on them or when a direction is zero. Every additive bijection preserves these cases, proving the exceptional GL(2,3) conclusion.

## PM-COUNTEREXAMPLE-0003: the exception is genuine

In F_9=F_3[i], take the additive map T(1)=1 and T(i)=1+i. These images are F_3-independent, so T is bijective and preserves C by the theorem. It is not scalar-Frobenius: T(1)=1 forces lambda=1, but i and i^3=-i are the only possible images of i under Frobenius powers, neither equal to 1+i.

Thus a proposed no-exception scalar-Frobenius classification is false. The actual code enumerates all six normalized additive bijections of F_9, not just this witness.

## Exact computational evidence

`python tools/order_preservers.py` builds order labels from actual eight-subset weights and their complete moment vectors. It then enumerates all additive bijections normalized by T(1)=1. This normalization is justified by the scalar case of Step 4; it does not throw away unknown kinds of preservers.

| Field | Normalized bijections checked | Normalized preservers | Full count after scalar normalization |
| --- | ---: | ---: | ---: |
| F_3 | 1 | 1 | 2 |
| F_9 | 6 | 6 | 48 |
| F_27 | 432 | 3 | 78 |

Failed maps are rejected on their first order-changing triple; accepted maps are checked on all triples. The test uses 63,921 actual before/after label comparisons. A separate exact parameter-identity check covers 20,421 instances, including non-bijective maps. The unit tests also contain a non-semilinear rejection in F_81; that is one explicit check, not a GL(4,3) enumeration.

These finite checks do not prove the theorem for all m; the root-bound argument does. The main experiments share arithmetic tables with earlier scripts. A second F_27 multiplication implementation, using a cyclic logarithm table generated from alpha^3=alpha+2 rather than polynomial division, also agrees on all 729 products in a unit test. That original algorithmic cross-check was by the same coordinator. Separate AI mathematical reviews were subsequently completed as recorded above; no Lean kernel has checked the statement.

## Prior art and limitations

The source mechanism is classical combinatorial polarization; see [Drapal-Vojtechovsky, section 2.1 and Theorem 4.8](https://arxiv.org/html/1509.05707v1). The shape lambda*x^{p^j} is also classical in finite-field preserver results. [Yip, A strengthening of McConnel's theorem, section 1](https://arxiv.org/html/2407.21362) reviews Carlitz-McConnel theorems imposing a restriction on all difference quotients. Those hypotheses differ from the order-preservation hypothesis here. We have not established whether another known preserver theorem directly yields this exact ternary-order statement or its F_9 exception.

The conic parameterization, linearized-polynomial representation and polynomial root bound are established tools. The proof above is self-contained, but a self-contained derivation is not proof of historical originality. Record this as a proved project result with NOVELTY_UNVERIFIED, not a new general framework, a new finite-field automorphism theorem, or a solution of an identified public conjecture.

The result here concerns finite characteristic-three fields and additive bijections. [SC-006](../SC-006/RESULTS.md) supplies the subsequent arbitrary-field extension and a quadratic-basis rejecting-witness construction. The new [prior-art audit](../../research/literature/PRESERVER_AUDIT_20261018.md) identifies Lester's 1977 full-cone theorem as closer precedent; extending the initial punctured-cone information is a distinct hypothesis step. Arbitrary permutations, other characteristics, weighted coefficients outside F_3 and approximate preservation require separate analysis. No cross-domain held-out problem has yet been solved by this result.

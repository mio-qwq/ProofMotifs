# PM-Q-B: independent rational q-word seed criterion

Task-scoped theory handoff. Repository read-only; only this temporary note was
written. Read `AGENTS.md`, `research/RESEARCH_PROGRAM.md`, and all of
`research/mechanisms/SUCCINCT_CANCELLATION.md`. No other task notes were read,
and no children were used, as requested. Requested configuration was
GPT-6.1-Sol/Ultra; this agent cannot independently inspect its runtime model
configuration. The source116 example is already exposed calibration, not a
held-out transfer. No novelty, human-review, or formal-verification claim.

## 1. Verdict and exact object

The proposed equivalence is correct in every characteristic. Its target is
**linear independence of all word series over K(z)**, not merely faithfulness
of the operators as a K-algebra representation. The latter is strictly weaker.

Let K be any field, let q belong to K^* have infinite multiplicative order,
and let sigma fix K and send z to qz. Put F=K(z), E=K((z)), and Delta=sigma-1.
Let b_1,...,b_m belong to zK[[z]] intersect F. Define

    Delta^{-1}(sum_{n>=1} a_n z^n)
      = sum_{n>=1} a_n/(q^n-1) z^n,
    J_i(f) = Delta^{-1}(b_i f),  f in K[[z]],
    h_empty=1,  h_{iw}=J_i(h_w).

The domain of J_i here is all K[[z]], because h_empty=1. Multiplication by b_i
lands in zK[[z]], where the inverse is defined. All h_w with nonempty w have
zero constant term and satisfy

    sigma(h_{iw})=h_{iw}+b_i h_w.                         (1)

**PM-Q-B1.** The following are equivalent:

1. The family (h_w), including h_empty, is F-linearly independent.
2. The classes [b_i] in the K-vector space F/Delta(F) are K-linearly independent.

This states rational-linear word freeness for every finite relation; it is
not a finite-jet theorem, an order-of-vanishing bound, or an optimality claim
over representations outside the supplied dictionary.

## 2. Complete proof

First E^sigma=K: if sum_{n>=N} a_n z^n is invariant, then
(q^n-1)a_n=0 for every integer n. Infinite order makes every coefficient with
n != 0 vanish. In particular F^sigma=K. This is valid in positive
characteristic and is the constant-field fact needed by the minimal-relation
argument.

### Necessity

Suppose sum_i c_i b_i=Delta(g), with c_i in K not all zero and g in F.
The rational function g is regular at zero. Indeed, if its Laurent expansion
started with a_n z^n for some n<0, then Delta(g) would have the same negative
leading exponent, since (q^n-1)a_n != 0. This contradicts the regularity of
sum_i c_i b_i.

The zero-constant series sum_i c_i h_i and g-g(0) have the same Delta image.
Their difference lies in E^sigma=K and has zero constant term, so

    sum_i c_i h_i = g-g(0).

Thus sum_i c_i h_i - (g-g(0))h_empty=0 is a nontrivial F-linear relation.

### Sufficiency

Let V be the free F-vector space on all words, and let ev:V->E send w to h_w.
Define the sigma-semilinear transformation S by

    S(a_w w)=sigma(a_w)(w+b_i v) for w=iv,
    S(a_empty empty)=sigma(a_empty) empty.

Equation (1) says ev(SP)=sigma(ev(P)), so ker(ev) is S-stable.

Assume ker(ev) contains a nonzero element. Choose P=sum a_w w in the kernel
of least maximal word length n. Among all such P choose one with the fewest
nonzero length-n coefficients, and normalize one of those coefficients to 1.
We have n>=1 because ev(empty)=1.

The element SP-P is in ker(ev). At word length n its coefficients are
sigma(a_w)-a_w; the normalized coefficient becomes zero. If SP-P were nonzero,
it would either have maximal length less than n, or have length n with fewer
nonzero top coefficients. Both contradict the choices. Hence SP-P=0 as an
element of the **free vector space**, not merely after evaluation.

Its top-degree coefficients now give a_w in F^sigma=K whenever |w|=n.
For every word v of length n-1, its coefficient in SP-P gives

    Delta(a_v) + sum_i a_{iv} b_i = 0.                    (2)

Taking classes in F/Delta(F), the assumed independence of [b_i] implies
a_{iv}=0 for every i and v. Every length-n word is uniquely iv, so all top
coefficients vanish, a contradiction. This proves sufficiency.

There is no hidden use of characteristic zero, ordinary differentiation,
algebraic closure, distinct original poles, or positivity of coefficients.

## 3. Split-pole quotient and explicit telescopers

Use the unambiguous normalized definition

    phi_{alpha,k}(z) = (1-z/alpha)^(-k) - 1,
    alpha in K^*, k>=1.                                  (3)

The final -1 is outside the power. Thus phi(0)=0 and
sigma(phi_{alpha,k})=phi_{alpha/q,k}. This avoids a separate constant residue.

Every rational b regular and zero at zero, all of whose nonzero poles split
over K, has a unique decomposition

    b = sum_{r>=1} p_r z^r
        + sum_{alpha,k} c_{alpha,k} phi_{alpha,k},         (4)

with finite support and with distinct pole/order pairs. This is ordinary
partial fractions with their constant terms subtracted. The polynomial part
in (4) has zero constant term. Repeated poles, including orders divisible by
the characteristic, cause no problem; decomposition does not require
division by k or k!.

Supply representatives alpha_O of the distinct q^Z-orbits of occurring poles
and integer positions j so that alpha=q^j alpha_O. For each orbit/order define

    R_{O,k}(b)=sum_j c_{O,k,j}.                           (5)

**PM-Q-B2.** On the space of the split-pole functions (4),

    b belongs to Delta(K(z)) iff all R_{O,k}(b)=0.         (6)

The forward implication concerns a telescoper in the whole K(z), not just
one promised in the displayed split-pole space.

Proof of sufficiency and construction: each positive monomial is exact,

    p_r z^r = Delta(p_r z^r/(q^r-1)).

For a fixed orbit/order, extend c_j by zeros and choose [a,b] containing its
support. If sum c_j=0, set

    d_j=sum_{ell=a}^{j-1} c_ell  for a+1<=j<=b,
    g_{O,k}=sum_{j=a+1}^b d_j phi_{q^j alpha_O,k}.         (7)

Then d_{j+1}-d_j=c_j, with zero boundary coefficients, so
Delta(g_{O,k})=sum_j c_j phi_{q^j alpha_O,k}. Summing (7) and the polynomial
telescopers gives an explicit rational g with Delta(g)=b; this construction
has g(0)=0.

Proof of necessity: let b=Delta(g), g in K(z). The leading-Laurent argument
above excludes a pole of g at zero. Work temporarily over an algebraic
closure to describe all other poles of g. On any nonzero q-orbit, there are
finitely many poles of g. At the two ends of a nonempty orbit support, the
shift produces uncancellable endpoint poles in Delta(g). Consequently an
orbit not occurring in b cannot occur in g. In particular no pole outside K
can occur in g: its entire q-orbit stays outside K because q is in K, whereas
all poles of b lie in K. Thus g itself has a split-pole decomposition, plus a
polynomial and a constant. On each orbit/order its coefficients d_j give
c_j=d_{j+1}-d_j, whose finite sum is zero. This proves (6).

Equivalently, a direct all-characteristic quotient proof uses uniqueness of
partial fractions and the finite-support boundary map d->(d_{j+1}-d_j).
The only quotient coordinate on a single orbit/order is the total sum.
Normalized phi's are essential here: in the basis (z-alpha)^(-k), residue
sums carry q-dependent weights.

## 4. What is needed to identify distinct orbits

For an arbitrary effective field K, exact field operations and an
infinite-order promise on q do **not by themselves supply** a uniform
algorithm for deciding alpha/beta in q^Z. A complete input contract must
include either an effective orbit-membership algorithm, or a supplied
partition with independently checkable distinct-orbit certificates in the
chosen field class. A claimed general polynomial-time algorithm cannot
quietly hide multiplicative subgroup membership in a field-operation model.

**PM-Q-B3.** For K=F(t), q=t, with t transcendental and F an effective field,
there is a complete canonical partition. For alpha in F(t)^*, put

    j(alpha)=v_t(alpha),
    N(alpha)=t^(-j(alpha)) alpha.

Then alpha/beta is in t^Z iff N(alpha)=N(beta). One implication follows by
applying v_t to alpha=t^j beta; the other follows by rearrangement. Thus
canonical representatives have t-valuation zero, integer positions are the
valuations, and distinct representatives are certified by ordinary rational
inequality. Normalizing requires exact polynomial coefficient arithmetic,
not an external discrete-log oracle.

For the proposed Q implementation with q=2, use exactly the analogous
normalization alpha/2^{v_2(alpha)}. Rational poles are in one 2^Z-orbit iff
their normalized odd-numerator/odd-denominator signed rationals agree.
Sign is retained. Pole orders are separate coordinates, not new orbits.

An assignment alpha=q^j alpha_O is verified by an exact identity. Distinctness
of representative poles alone is insufficient: alpha and q alpha are
different poles in the same orbit.

## 5. Exact weighted dictionary discovery

Let a finite dictionary contain m split-pole b_i and supplied costs w_i.
Let d be the number of occurring orbit/order pairs after the exact partition,
and let R be the d-by-m matrix whose i-th column is (5).

**PM-Q-B4.** A subset I has rational-linearly free word series iff the columns
R_i, i in I, are K-linearly independent. Therefore a rank-r subset exists iff
rank_K R>=r, and the minimum-total-cost such subset is the rank-r vector
matroid greedy solution: process the columns by increasing cost, accept a
column exactly when it increases the rank, and stop after r acceptances.

Proof of optimality: work in the rank-r truncation of the column matroid.
Suppose an optimum size-r independent set O contains all previously selected
greedy columns A, and let e be the next selected column. If e is not already
in O, the fundamental dependence of e on O (when e lies in its span), or a
free replacement (when it does not), supplies f in O\A with O-f+e independent.
Such f cannot have appeared strictly before e in the cost order: because
A union {f} is independent, it would have been accepted if encountered before
e (and independence with a smaller earlier greedy set follows). Thus
w_e<=w_f. Replacing f by e preserves optimality and extends the invariant.
Induction proves the claim. Equivalently this is ordinary weighted linear
matroid greedy, not a new optimization principle.

Nonnegative costs are sufficient and are useful if the stated optimization
allows **at least** r selected seeds: deleting surplus elements from an
independent set cannot increase cost, so an optimum of size r exists. For
exactly r, the greedy theorem permits arbitrary comparable costs. The
boundary r=0 returns the empty set.

Primal certificate: selected indices, the relevant orbit partition and
decomposition identities, and an r-by-r nonzero minor of R_I. For a replayable
optimality certificate, include sorted costs and the exact dependence of
every skipped prefix column on the previously accepted columns. No claim of
optimality over rational linear combinations not in the dictionary, seed
families with other pole grammars, or other operator types follows.

Infeasibility certificate: an independent column basis of rank rho<r plus
coordinates expressing every R_i in its span. For each column relation
sum_i lambda_i R_i=0, (7) constructs a rational g with

    sum_i lambda_i b_i=Delta(g),

which gives the explicit length-one obstruction

    sum_i lambda_i h_i=g-g(0).

The rational identity verifies a negative certificate without trusting the
orbit-classification procedure. Positive soundness still needs its complete
distinct-orbit contract.

## 6. Resource bounds and expanded-output caveat

Assume the split-pole decomposition and certified orbit positions are supplied.
Let T be their total number of nonzero listed terms and polynomial monomials.
Residue accumulation takes O(T) field additions into the d-by-m sparse matrix.
Sorting costs takes O(m log m) cost comparisons. Incremental elimination
through rank r uses O(m d r) field operations (or O(m d min(d,m)) for complete
rank), with O(dr) elimination storage in addition to input/output. These are
field-operation bounds, not uniform bit bounds over unspecified fields.
Decomposition extraction, exact orbit normalization, rational-function
coefficient sizes, factorization, and reading the input have their own costs.
Verifying a supplied split factorization and partial-fraction identity does
not establish a polynomial-time factorization algorithm over arbitrary K.

For a dependence, define its expanded chain budget

    W=sum_{active (O,k)} (max support j - min support j),

and let P be the number of its polynomial monomials. Formula (7) uses
O(W+P) coefficient operations and at most W normalized pole terms. Constructing
each q^j alpha and writing expanded rational numerators/denominators also
counts. Degree is controlled by the pole orders and chain lengths, not by
the number of initially listed pole terms alone.

This distinction is necessary. The sparse function

    phi_{alpha,k}-phi_{q^N alpha,k}

has the zero residue certificate with only two listed pole terms, but its
zero-constant rational telescoper is

    sum_{j=1}^N phi_{q^j alpha,k}.

It has N distinct poles of order k. Any rational telescoper differs only by
a constant, so no explicit reduced rational telescoper can avoid the degree
Nk pole denominator. If N or the poles are succinctly encoded, telescoper
output can be exponential in the bit-length of N. Residue/rank selection
can still be fast; producing all expanded telescopers need not be. One may
instead specify a compressed shift-sum certificate, but that changes the
certificate representation and its verification accounting.

## 7. Constant extensions and failure controls

**PM-Q-B5.** Rational-linear word freeness persists under any genuine constant
field extension L/K, with z still an indeterminate and sigma fixing L.
One direct argument avoids splitting assumptions: a hypothetical relation
over L(z), after clearing denominators, is an L-linear dependence of a finite
collection z^j h_w. Those series have coefficients in K. Their K-linear
independence follows from the original K(z)-linear word independence; hence
their coefficient matrix has a finite nonzero full-column-rank minor over K.
That minor remains nonzero over L, contradiction.

The full constant field is K, not an arbitrarily chosen smaller field. For
example, take K=F(t), q=t, and a non-exact b. The seeds b and t b might be
independent over F, but their classes are dependent over K and h_2=t h_1.
Rank must be taken over the field actually fixed by sigma and allowed in
relation coefficients.

If the intended base parameters are F(t) and coefficient extensions F'/F,
use F'(t) with t fresh. This is a field extension. Specializing t to a finite
order element is not such an extension and can destroy the setup. In a finite
field every nonzero q has finite order, so one must adjoin a transcendental
or otherwise work in an infinite field for the infinite-order promise.

Further exact controls:

* Infinite order is necessary to define Delta^{-1} on all zero-constant
  series: if q has order N, Delta(z^N)=0, and z^N is not in its image.
* Pole overlap is not automatically failure. Two poles in the same orbit
  with different orders give independent residue coordinates. Two seeds
  with the same orbit/order can fail despite using distinct poles: the
  difference phi_alpha,k-phi_qalpha,k is exact.
* Positive polynomial terms are all exact and contribute no residue rank.
  Using their degrees as independent seed features would be unsound.
* The strong criterion is not necessary for mere operator faithfulness.
  For the one-letter dictionary b=z, all seed classes vanish, but
  J_z^n(1)=z^n/product_{s=1}^n(q^s-1). These series are K-linearly independent,
  so K[x]->End_K(K[[z]]), x->J_z, is faithful. They are not K(z)-linearly
  independent. Any headline must preserve this distinction.
* Rational-linear independence does imply faithful action of the free
  K-algebra: a nonzero constant-coefficient polynomial in the J_i cannot
  annihilate 1. It does not define an F-algebra representation with rational
  coefficients central, since multiplication by a rational function need
  not commute with J_i.

## 8. Closest primary baseline and evidence limits

Independently opened Chen--Singer, *Residues and telescopers for bivariate
rational functions*, Advances in Applied Mathematics 49 (2012), 111--133,
author-hosted PDF:

https://singer.math.ncsu.edu/papers/YAAMA1465.pdf

Section 2.3, Definition 2.7, Lemma 2.9 and Proposition 2.10 (printed pp116--118)
give weighted q-discrete residues and the complete rational q-summability
criterion, with an additional constant residue at infinity. Section 2 assumes
characteristic zero. The normalized basis (3), restricted to zero-at-zero
rationals with split poles, converts the weights into ordinary orbit sums;
our elementary finite-support proof works in all characteristics. This is
a precise baseline comparison, not evidence of historical originality for
the extension or for combining it with classical matroid greedy.

Exact computational controls: a standalone standard-library Fraction and
polynomial-arithmetic check verified the chain telescoper identity above for
q=2, alpha=1, k in {1,2,3}, N in {1,2,5}, and independently reduced each
telescoper denominator to confirm degree Nk (nine identities and nine degree
checks). SymPy was unavailable, so no CAS result is claimed. These finite
controls support sign/output accounting only; they are not evidence for the
infinite word-independence theorem.

The local source ledger records that source116 uses a minimal-relation word
independence proof. This note obtained the abstract equivalence independently
from (1); the external source116 words.tex fetch failed during this task, so
no fresh line-by-line source116 audit is claimed. The source-derived example
is not a held-out test. A minimum-cost finite-dictionary instrument here is
a synthesis of rational q-summation, the minimal-relation argument, and
weighted linear matroid selection. No stronger missing-tool, transfer, or
AI-performance conclusion follows.

## 9. Handoff

Accept PM-Q-B1--B5 as scoped proved propositions pending the coordinator's
separate adversarial review. Essential integration corrections are: keep the
full constant field explicit; define J on all K[[z]]; spell out phi's outside
-1; certify orbit inequivalence; distinguish strong rational-linear word
freeness from ordinary operator faithfulness; and count chain expansion in
telescoper output bounds. No repository files were changed.

## 10. Follow-up audit: polynomial seeds and weaker operator faithfulness

Follow-up task from the coordinator: determine actual K-free-algebra operator
faithfulness when every supplied b_i is a polynomial with zero constant term.
This section independently proves the coordinator's dimension obstruction,
with a sharper coordinate bound and a compact exact example. It does not
change the stronger rational-linear criterion PM-Q-B1.

Maintain K, q, sigma and J as above. Suppose b_1,...,b_n belong to zK[z],
deg(b_i)<=d, with d>=1. Write b_i=sum_{r=1}^d b_{i,r}z^r. Let J_w denote
the composition in usual word notation, so the rightmost letter acts first.
We consider the homomorphism

    K<x_1,...,x_n> -> End_K(K[[z]]), x_i -> J_i.           (8)

**PM-Q-B6 (polynomial grammar obstruction).** If n>=2, (8) is not injective.
For every L>=1, put M=(d-1)L+1. The span of length-L word operators has
dimension at most

    C_L=M(M+1)/2 <= M^2.                                (9)

Consequently any L with n^L>C_L supplies a nonzero homogeneous degree-L
polynomial in the kernel of (8). Such an L always exists. The coordinator's
square bound is sound; (9) is a refinement.

### Proof on monomials and exact denominator clearing

Set T=q^m for an input monomial z^m, m>=0. Expanding a length-L word by
choosing one monomial from each b_i gives paths with positive steps
r_1,...,r_L in {1,...,d}. The cumulative shifts s_a=r_1+...+r_a are strictly
increasing integers with L<=s_L<=dL. Each path acts by a constant multiple of

    z^{m+s_L}/product_{a=1}^L(q^{s_a}T-1).              (10)

The constants are seed-coefficient products and do not depend on m. Each of
the L denominator factors occurs once and is among the factors of

    D_s(T)=product_{a=1}^s(q^aT-1), D_0=1,

where s=s_L. The factors are distinct because q has infinite order. Let
F_{w,s}(T) be the rational coefficient of z^{m+s} in the word action. Then

    P_{w,s}(T)=D_s(T)F_{w,s}(T) is in K[T],
    deg(P_{w,s})<=s-L, L<=s<=dL.                        (11)

Thus the word operator is encoded by at most
sum_{s=L}^{dL}(s-L+1)=M(M+1)/2 scalars, namely the coefficients in (11).
A K-linear dependence between these arrays implies an operator identity on
each z^m: all factors in D_s(q^m) are q^{a+m}-1 != 0, since a>=1 and m>=0.
The dimension argument now proves the claim. Alternatively the same
denominator D_{dL} for every output shift gives degree <=dL-L and M shifts,
hence the coordinator's simpler M^2 bound.

### Why this holds on all formal series

For a polynomial seed, J_i acts by the finite-band formula

    J_i(sum_{m>=0}a_m z^m)
      =sum_{m>=0}sum_{r=1}^d
          a_m b_{i,r}/(q^{m+r}-1) z^{m+r}.              (12)

Each output coefficient is a finite sum. A length-L word has shifts only in
[L,dL]. Thus an identity on all monomials gives zero for every coefficient
of every input formal series. Equivalently every J_i is z-adically continuous
and raises order by at least one. No arbitrary linear map is applied to an
infinite sum without continuity.

All reasoning holds in every characteristic. Denominators are cleared by
multiplication, not factorial division. Zero coefficients only delete paths.
Nonzero b_i are not needed for the n>=2 obstruction; a zero seed already
gives a length-one relation.

**PM-Q-B7 (one-letter sharp boundary).** If n=1 and b is nonzero, (8) is
injective. Put r=ord_z(b)>=1. For every nonzero f in K[[z]] of order a>=0,
ord_z(J_b f)=a+r, since its leading coefficient is the nonzero leading
coefficient of bf divided by q^{a+r}-1. Consequently
ord_z(J_b^k1)=kr for k>=0. Distinct orders make these powers K-linearly
independent, so any nonzero polynomial in J_b acts nontrivially on 1.
For n=1, b=0 is the only failure; with no letters the scalar representation
is trivially faithful.

B6--B7 give a complete classification inside this polynomial-seed grammar.
They make no claim for arbitrary rational seeds: the split-pole construction
above can be free for arbitrarily many letters under the stronger criterion.

### A small all-characteristic identity

**PM-Q-B8.** Let A=J_z and B=J_{z^2}. Then

    q A^2 B - (q+1) A B A + B A^2 = 0.                  (13)

This is a nonzero formal free polynomial in every field: its words are
distinct and its last coefficient is 1. On z^m, all three words have output
shift 4. Their denominator index sets are {2,3,4}, {1,3,4}, and {1,2,4},
respectively. Clearing D_4 leaves

    q(qT-1) - (q+1)(q^2T-1) + (q^3T-1) = 0.

This proves (13) on all series by (12). A standalone Fraction check verified
its action on z^m for q in {2,3,5}, m=0,...,19 (60 exact controls); a formal
two-variable coefficient check verified the cleared numerator. The proof,
not those finite controls, establishes all m and all characteristics.

### Constructing a relation without enumerating n^L words

The obstruction is effective over an effective field K with the infinite-order
q promise. Find L with n^L>C_L. For d>=2 a loose uniform choice is

    L=8 ceil(log_2(d+1)).                                (14)

Indeed write s=ceil(log_2(d+1)), so d<2^s and M<=dL. For s>=2,
2^{8s}>64s^2 2^{2s}>(dL)^2>=C_L. For d=1, C_1=1 already gives a
length-one relation when n>=2. One can instead increase L until the exact
integer inequality holds.

Choose only C_L+1 distinct words of length L, not all n^L words. Their
arrays must be dependent. Each array can be computed without expanding its
d^L monomial paths. For a word iw with |iw|=ell, use

    P_{iw,s}(T) = sum_{r=1}^d b_{i,r}
         [D_{s-1}(T)/D_{s-r}(T)] P_{w,s-r}(T),           (15)

with P_empty,0=1 and zero outside the allowed shift range. The quotient is
the polynomial product over indices s-r+1,...,s-1; inadmissible terms are
omitted. Its degree is r-1, and (15) maintains the bound s-ell. Exact linear
algebra on the C_L-by-(C_L+1) matrix returns nonzero kernel coefficients,
hence an identity supported on at most C_L+1 words.

With dense polynomial multiplication, a conservative implementation costs
O(d^4 L^3) field operations per chosen word, after polynomial ratio tables
are precomputed. Dense elimination costs O(C_L^3), giving the safe bound

    O(n d + C_L d^4 L^3 + C_L^3)

field operations, plus polynomial-table setup and O((C_L+1)L) word-label
output. Shared prefixes can improve this but are unnecessary. Parameters
are expanded d and L, not the logarithm of a sparse huge degree. Field-element
bit sizes and arithmetic growth must be added in a rational bit model.

A certificate consists of nonzero coefficients, listed words, and zero
polynomial sums sum_w c_w P_{w,s}=0 for every shift s. The checker can
recompute (15), verifying an identity on every formal series, not sampled
actions. This is a finite exact obstruction constructor with polynomial
field-operation complexity in expanded d,n using (14). It does not find
minimal relation degree, minimal support, or assert optimal bit complexity.

### Growth and Ore baseline: exact comparison, not novelty

Let A_poly be the unital K-algebra generated by these operators, and let V_L
span words of length at most L. The common denominator D_{dL} works for all
of them. Output shifts lie in [0,dL] and cleared numerator degree is at
most dL, whence

    dim_K V_L <= (dL+1)^2.                              (16)

Thus A_poly has polynomial growth and Gelfand--Kirillov dimension at most 2.
It contains no free K-subalgebra on two or more generators, even with new
generators chosen as finite expressions in the original J_i. This is the
standard growth obstruction underlying B6, not a new abstract principle.

For a q-Ore normal form, let Z=M_z and S=sigma, so SZ=qZS. On K[[z]], the
diagonal operator q^r S-1 is invertible for every r>=1. Directly,

    J_{z^r}=Z^r(q^r S-1)^{-1},
    J_b=sum_{r=1}^d b_r Z^r(q^r S-1)^{-1}.               (17)

A bare appeal to an Ore algebra would not suffice: some Ore extensions or
localizations contain free subalgebras. Bound (16) supplies the required
growth hypothesis for this particular family.

Independently opened primary comparison: S. Paul Smith,
*Free subalgebras of the skew polynomial rings k[x,y][t;sigma] and
k[x^{+/-1},y^{+/-1}][t;sigma]*, arXiv:1308.1694v1 (7 August 2013),
https://arxiv.org/pdf/1308.1694. Sections 1.1--1.3 set out skew-polynomial
word-space multiplication. Sections 1.5.3--1.5.4 (printed p3) explicitly
state the finite-GK-dimension obstruction and n^L growth of a free algebra.
That is an established framework baseline, not an audited prior occurrence
of formulas (9), (13), (15), or this exact q-integral grammar. No historical
priority conclusion is made.

Follow-up handoff: B6--B8 are proved scoped results pending separate
coordinator review. The proposed square bound is correct; the triangular
refinement, cubic identity, whole-series proof, and polynomial-size
obstruction constructor are optional integration gains. No repository writes.

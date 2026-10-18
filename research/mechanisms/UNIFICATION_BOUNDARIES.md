# PM-UNIFY-A: what augmentation ideals do and do not unify

Date: 2026-10-18. Task-scoped research note. Repository inspection was read-only. This note makes no novelty claim and is not a formal verification.

## Question and answer

Can finite-support moment cancellation, modular finite differences and orbit sums, sign-reversing involutions, and real signed-measure cancellation be treated by one operational theory of composition and transfer?

**Partly, using existing tools.** Factorizations by differences give certificates that compose and transport through compatible actions. Associated graded rings identify exactly when the predicted leading term survives. For a finite additive subgroup of a characteristic-p field, a complete moment/divided-power calculation gives an exact conversion between ordinary moments and augmentation order. This conversion explains why the orders 5 and 7 in SC-003 both have augmentation order 3.

**There is a sharp obstruction to identifying all these orders.** An involution in characteristic different from 2 has an idempotent augmentation ideal, so its filtration records no increasing cancellation order. Even in characteristic zero, an additive-group augmentation filtration can miss cancellation caused by scalar-linear geometry. Quantitative analytic estimates additionally require a metric, regularity and integrability; the algebra alone supplies none of these.

Consequently the existing algebra is useful as a common certificate language for compatible difference actions. Renaming arbitrary kernels or demanding a single faithful order for every mechanism adds no demonstrated mathematical power. Nothing in the argument explains why AI performs well on a class of problems; that is a separate empirical question requiring an appropriately sampled corpus and controlled comparisons.

## A. A complete conversion theorem in positive characteristic

**PM-UNIFY-A-T1 (moment coordinates and augmentation order).** Let K be any field of characteristic p, let V be a finite F_p-linear subspace of K of dimension m, and put q=p^m. Let A=K[V] be the additive group algebra, with basis delta_v, product delta_v delta_w=delta_(v+w), unit delta_0, augmentation epsilon(sum c_v delta_v)=sum c_v, and augmentation ideal I=ker epsilon. For mu in A define

M_n(mu)=sum_(v in V) mu(v) v^n,

using v^0=1, including at zero. Let s_p(n) be the sum of the base-p digits of n. Set both orders of the zero element to infinity. For nonzero mu define

ord_M(mu)=min{n>=0: M_n(mu) != 0},

nu_I(mu)=max{r>=0: mu in I^r}.

Then

1. The K-vector space H_q with basis e_0,...,e_(q-1) and product

   e_i e_j = binom(i+j,i)e_(i+j) if i+j<q, and 0 otherwise,

   is a K-algebra, and

   Phi(mu)=sum_(0<=n<q) M_n(mu)e_n

   is an algebra isomorphism A -> H_q. Its augmentation is the coefficient at e_0.

2. There is an algebra isomorphism

   K[z_0,...,z_(m-1)]/(z_0^p,...,z_(m-1)^p) -> H_q,

   z_j -> e_(p^j).

   If n=sum n_j p^j, 0<=n_j<p, then

   product_j z_j^(n_j) -> (product_j n_j!) e_n.

3. Consequently, exactly, not just as a one-sided bound,

   I^r = {mu: M_n(mu)=0 for every 0<=n<q with s_p(n)<r},

   nu_I(mu)=min{s_p(n): 0<=n<q and M_n(mu)!=0}.

   Ordinary moment order is instead min{n:0<=n<q and M_n(mu)!=0}.

4. If 0<=r<=m(p-1) and r=a(p-1)+b with 0<=b<p-1, then mu in I^r implies

   ord_M(mu) >= (b+1)p^a-1.

   The bound is sharp for every V: an element whose first q moments are zero except at n=(b+1)p^a-1 realizes equality and has exact augmentation order r. For r=m(p-1) use a=m,b=0, giving q-1. For m=0 the algebra is K and only r=0 occurs for nonzero elements.

### Proof

For every n the binomial theorem and finite support give

M_n(mu nu)=sum_(i=0)^n binom(n,i) M_i(mu) M_(n-i)(nu).

For n<q this is precisely the stated multiplication of moment coordinate vectors. The q-by-q matrix (v^n)_(0<=n<q, v in V) is a Vandermonde matrix on q distinct elements of a field, with nonzero determinant. Thus Phi is a vector-space isomorphism and multiplicative. It sends delta_0 to e_0. This proves the first assertion and associativity of the displayed product; alternatively, the product is the quotient of the usual divided-power algebra by degrees at least q.

In characteristic p, coefficient comparison in

(1+T)^n = product_j (1+T^(p^j))^(n_j)

shows that binom(n,i) modulo p is product_j binom(n_j,i_j). In particular a product e_i e_j vanishes when base-p addition introduces a carry, and has the digitwise binomial coefficient when there is no carry. Successively multiplying e_(p^j) by itself a<p times gives a! e_(a p^j); the p-th power is zero. Multiplication across distinct digit positions has coefficient 1. Therefore the proposed map from the truncated polynomial algebra is well-defined and maps its q standard monomials to nonzero scalar multiples of the q distinct e_n. It is an isomorphism.

The augmentation ideal in the truncated polynomial algebra is J=(z_0,...,z_(m-1)). Its r-th power has basis the standard monomials of total degree at least r. Under the isomorphism the corresponding total degree is sum_j n_j=s_p(n). This proves the exact ideal description and order formula. It also proves I^(m(p-1)+1)=0.

To minimize n subject to s_p(n)>=r, fill the lowest base-p digit to p-1, then the next, continuing until digit sum r is reached. Moving one unit of digit sum from a higher digit to an unfilled lower digit strictly reduces n, so a minimum must have this form. The resulting integer is

(p-1)(1+p+...+p^(a-1))+b p^a=(b+1)p^a-1.

The exact ideal description forces all moments below this index to vanish. The inverse Vandermonde transform of e_n gives the sharpness example. This also checks the top-degree and empty cases. QED.

### What this resolves in SC-001/002/003

SC-001 uses the ordinary-degree filtration. If mu and nu have ordinary orders r,s, its leading coefficient is

M_(r+s)(mu nu)=binom(r+s,r) M_r(mu) M_s(nu).

Thus exact ordinary-order additivity holds precisely when the binomial coefficient survives; in characteristic p this is the no-carry condition. This is multiplication of divided-power leading symbols, not an unexplained exception.

For independent directions a_1,...,a_d, extend them to an F_p-basis of V. The elements delta_(a_i)-delta_0 are independent truncated-polynomial generators. Hence the saturated product product_i (delta_(a_i)-delta_0)^(p-1) has exact augmentation order d(p-1). T1 forces ordinary order at least p^d-1. Its support lies in their span, whose cardinality is p^d, so the Vandermonde bound forces equality. This recovers the cancellation order in SC-002 without calculating a Moore determinant. T1 does not replace SC-002's formula for the nonzero leading coefficient or its interpolation/remainder formula.

For three independent ternary directions, the product of their first differences has exact augmentation order 3. The sharp ordinary lower bound is 5. The two SC-003 triples have ordinary orders 5 and 7, but s_3(5)=s_3(7)=3. Therefore augmentation order cannot distinguish them. Their observation-specific leading coefficients still matter:

M_5=-abc(a^2+b^2+c^2),

M_7=-abc(a^2b^2+a^2c^2+b^2c^2).

The ordinary order-7 example is a nonzero augmentation leading symbol whose pairing with the particular degree-5 monomial vanishes. It is better described as extra cancellation for a chosen observation than as a failure of the augmentation calculus. Such extra cancellation may have meaningful field-geometric structure; the word accidental should not erase that structure.

## B. A compositional and transportable certificate

**PM-UNIFY-A-T2 (difference certificates).** Let k be a commutative ring, G an abelian group, A=k[G], and I its augmentation ideal. Let P_d be a filtration of a k-module of functions on a G-set X, with P_(-1)=0, such that

(g-1)P_d is contained in P_(d-1) for every g in G and d>=0.

Translations act by (g f)(x)=f(gx). If a in I^r, then a kills P_(r-1). More concretely, membership a in I^r has a finite certificate

a=sum_j c_j [h_j] product_(i=1)^r ([g_(j,i)]-1),

with c_j in k and h_j,g_(j,i) in G. Thus a acts as a sum of translated mixed r-th differences. Multiplying two certificates of lengths r and s gives a certificate of length r+s.

If T:X -> Y is G-equivariant, and Q_d is a family of target observables with T^*Q_d contained in P_d, then (a f)(T(x))=0 for every x in X and f in Q_(r-1). This is vanishing on the image T(X); global vanishing on Y additionally follows if T is surjective. The target differences are not assumed to lower Q_d, since that would give target annihilation directly and make the pullback argument redundant. More generally an additive homomorphism phi:G -> H induces phi_*:k[G] -> k[H] with phi_*(I_G^r) contained in I_H^r. If a has exact finite augmentation order r, its image has exact order r if and only if the degree-r associated graded image of its leading class is nonzero.

### Proof

The ideal I is generated by [g]-1: subtract epsilon(a)[0] and group terms. By the definition of ideal multiplication, I^r is spanned by finite products of r such generators with arbitrary coefficients in A; expanding each coefficient in the group basis gives the displayed certificate. Each difference lowers the observable filtration by one, so r successive differences kill P_(r-1). Expanding and concatenating certificates proves the composition statement. Equivariance gives the pointed identity (a f)(T(x))=(a(T^*f))(x), whose right side vanishes. The ring map phi_* sends [g]-1 to [phi(g)]-1, so it preserves all ideal powers. Its degree-r graded image vanishes exactly when phi_*(a) lies in I_H^(r+1). QED.

For a finite group G over a field k, use the full function space k^G and its perfect pairing <mu,f>=sum_g mu(g)f(g) with the regular group algebra k[G]. The functions of finite-difference degree at most d are precisely those annihilating I^(d+1). Indeed translating a mixed difference at the identity gives every value of the iterated difference, and I^(d+1) is stable under translation. Double annihilation then says I^(d+1) is exactly the set of weights annihilating every such function. For a general finite G-set X the corresponding object is the submodule I^(d+1)k[X], rather than the bare ideal; over a general coefficient ring the field double-annihilator argument is not available. This is the standard Passi/functional-degree viewpoint. The explicit certificate and the specified observable/action compatibility are the operational content; merely stating an unspecified annihilator condition is not enough for transfer.

### Exact order of a composition

For a,b of exact augmentation orders r,s, the product lies in I^(r+s), and it has exact order r+s if and only if the product of their leading symbols in gr_I(A) is nonzero. This last criterion by itself is elementary filtered algebra. Its value depends on actually identifying gr_I(A). For elementary abelian p-groups T1 identifies it as a truncated polynomial ring, where products may vanish. For an injective additive map between finite F_p-vector spaces, choose a basis of the source and extend its image to a basis of the target. The associated truncated-polynomial inclusion is injective, so exact augmentation order is preserved. Ordinary moment order need not be preserved, as SC-003 already demonstrates.

### An explicit observable adapter, rather than only an existence statement

Under the hypotheses of T1 let W be another finite F_p-subspace of K, and let T:V -> W be any map. For each target moment index n, uniquely interpolate its pullback on V:

(T(x))^n=sum_(0<=j<q) c_(n,j) x^j for every x in V.

The q coefficients are obtained by solving the same invertible Vandermonde system. For every mu one then has the exact transfer formula

M_n(T_*mu)=sum_(0<=j<q) c_(n,j) M_j(mu).

This is a finite, reviewable certificate for ordinary moment transfer. If T is additive, the coefficients satisfy the stronger restriction

c_(n,j)=0 whenever s_p(j)>s_p(n).

To justify this, first note that x -> x^n has finite-difference degree at most s_p(n): write x^n as a product of s_p(n) additive Frobenius factors and use the difference product rule. Additive pullback preserves this upper bound. By the perfect-pairing description after T2 and the ideal formula in T1, the functions of finite-difference degree at most d on V have basis {x^j: 0<=j<q, s_p(j)<=d}. Therefore the interpolating polynomial has no coefficient outside that basis. The same argument shows exact finite-difference degree s_p(j) for each basis monomial x^j, without assuming V is a subfield.

Thus additive maps are triangular for digit-sum degree. Preserving a particular ordinary moment order demands the finer coefficient rows, not only this triangularity. This gives a concrete operation for investigating a proposed transfer: compute the first rows allowed to be nonzero and test their pairing with the source moments. A generic nonlinear map has no such digit-sum restriction.

## C. Two symmetry examples and a decisive filtration obstruction

**PM-UNIFY-A-C1 (a modular cyclic orbit).** In characteristic p, if g^p=1, then

1+g+...+g^(p-1)=(g-1)^(p-1).

This follows by expanding (T-1)^(p-1): each coefficient is 1 modulo p. Thus a p-cycle orbit sum is an iterated difference and kills any observable with (g-1)^(p-1)f=0. If f is invariant, the sum is p f=0. Applied to translations of a line and polynomial functions of degree less than p-1, this gives the usual line-sum cancellation. Applied to a general permutation representation it need not vanish: on a free p-orbit, summing the orbit of an indicator of one point gives the nonzero constant-one function on that orbit. Merely having orbit size p is insufficient; the coefficient characteristic and the observable must be specified.

**PM-UNIFY-A-C2 (a sign-reversing involution).** Let tau^2=1 act on finite X, and let a signed weight w satisfy w(tau x)=-w(x). Over a field of characteristic different from 2, a fixed point must have weight zero. Choosing one element of each two-element orbit expresses the weight vector as

w=(1-tau)v.

Every tau-invariant observable therefore pairs to zero with w. This is a first-difference factorization in a permutation module and transports through tau-equivariant maps.

However in k[C_2], with 2 invertible,

(tau-1)^2=-2(tau-1), so I^2=I.

Thus every nonzero vector in I k[X] belongs to I^r k[X] for every r>=1. This cannot be interpreted as arbitrary ordinary-moment cancellation. Take X={0,1}, let tau exchange the two points, and w=delta_1-delta_0. Its ordinary first moment is 1, but its order for the I-adic module filtration would be infinity. In characteristic 2 the sign distinction disappears and I^2=0 instead. This is a sharp obstruction to treating modular cyclic orbit cancellation and characteristic-zero sign reversal by a single faithful augmentation order.

The common object is a symmetry-difference certificate together with the observable filtration it lowers. An arbitrary involution does not lower ordinary polynomial degree: for the swap x -> 1-x, its difference applied to x is 1-2x, still degree 1. The compatibility hypothesis in T2 is substantive.

## D. Real signed measures: the additional data and another obstruction

**PM-UNIFY-A-C3 (scalar geometry is not recovered by group augmentation).** Let G=Z^2, k=R, A=R[x^(+/-1),y^(+/-1)], and I=(x-1,y-1). Observe G in R by phi(m,n)=m+sqrt(2)n. Put

a=(y-1)-sqrt(2)(x-1).

Its leading class in I/I^2 is v-sqrt(2)u, nonzero because u,v are a basis. Hence a has exact augmentation order 1. The observed signed measure is

mu=delta_(sqrt(2))-sqrt(2)delta_1+(sqrt(2)-1)delta_0.

It has M_0=M_1=0 and M_2=2-sqrt(2)!=0, so its ordinary moment order is 2. There are no collisions of support nodes. The discrepancy arises because the scalar-linear relation between directions is invisible to the free abelian group model. Thus even characteristic zero does not make an arbitrary group augmentation filtration coincide with ordinary scalar moments. If the observation is part of the problem, its extra algebraic structure must be retained.

**PM-UNIFY-A-T3 (what yields an analytic gain).** Let mu be a finite signed or complex measure on R^d supported in a ball of radius R about 0. Assume every moment integral x^alpha dmu is zero for |alpha|<r, with r>=1. Let f be C^r on a convex neighborhood of all segments z+[0,1]x for x in the support, and suppose ||D^r f|| there is bounded by L, using the operator norm on r-linear forms. Then

|integral f(z+x) dmu(x)| <= L/r! integral ||x||^r d|mu|(x) <= L R^r ||mu||_TV/r!.

For r=1 the same inequality holds for Lipschitz f with constant L, requiring no differentiability. If both mu and nu are compactly supported finite signed or complex measures, with finite ordinary multivariate moment orders r and s, then their convolution has exact ordinary order r+s. Compact support of both measures ensures all moments and convolutions used here exist.

### Proof

Taylor's formula along each segment gives

f(z+x)=sum_(j<r) D^j f(z)[x,...,x]/j! + R_r(z,x),

with |R_r(z,x)|<=L||x||^r/r!. Each displayed polynomial term integrates to zero by the moment hypotheses, and integration against total variation gives the estimate. For r=1 subtract f(z) and use the Lipschitz inequality directly.

For the convolution statement define the leading homogeneous moment polynomial

P_mu(xi)=1/r! integral <xi,x>^r dmu(x),

and similarly P_nu. These polynomials are nonzero: over R or C their coefficients are the corresponding degree-r moments times nonzero multinomial constants. Expanding <xi,x+y>^n shows that all convolution moments of total degree less than r+s vanish and its homogeneous degree-(r+s) polynomial is P_mu P_nu. The polynomial ring over R or C has no zero divisors, so the product is nonzero. QED.

The nonzero leading moment orders are explicit hypotheses. Without compact support or another determinacy assumption a nonzero measure need not have a first nonzero moment; no assertion here identifies a measure solely from all its moments in that generality.

A difference certificate gives a different, directly usable analytic bound. If a finitely supported real measure is

mu=sum_j c_j delta_(h_j) * product_(i=1)^r (delta_(a_(j,i))-delta_0),

then repeated integration of the fundamental theorem of calculus gives

|integral f(z+x) dmu(x)| <= ||D^r f||_infinity sum_j |c_j| product_i ||a_(j,i)||,

provided f is C^r with that derivative bound on the corresponding translated parallelepipeds. This transfers a combinatorial factorization into a quantitative mixed-derivative estimate. The coefficients, step lengths and regularity are part of the certificate; augmentation membership alone has no numerical scale.

An affine map of real vector spaces preserves annihilation of all ordinary polynomials below r. A nonlinear map can destroy it: delta_0-2delta_1+delta_2 has order 2, but pushing it through x -> x^2 gives delta_0-2delta_1+delta_4, whose first moment is 2. More generally a polynomial map of degree at most e>=1 sends ordinary order at least r to ordinary order at least ceil(r/e), because the pullback of a target polynomial of degree d has degree at most ed. This is an explicit transfer conclusion with an explicit compatibility loss.

### A concrete cross-mechanism transfer

**PM-UNIFY-A-T4 (involution pairing to analytic cancellation).** For an integer r>=1 and i=1,...,r let X_i be a finite set, tau_i an involution, and w_i:X_i -> R satisfy w_i(tau_i x)=-w_i(x). Let h_i:X_i -> R^d be any map; no translation action or equivariance of h_i is assumed. Let mu_i=sum_(x in X_i) w_i(x) delta_(h_i(x)). Choose one representative of each nonfixed two-element tau_i-orbit, forming R_i, and define the cost of the specified pairing

C_i=sum_(x in R_i) |w_i(x)| ||h_i(x)-h_i(tau_i x)||.

Then eta=mu_1*...*mu_r annihilates every polynomial of total degree less than r. For any C^r function f with r-th derivative norm at most L on the translated parallelepipeds used by these pairs,

|integral f(z+y) deta(y)| <= L product_(i=1)^r C_i.

### Proof

Fixed-point weights are zero. Every pair supplies the exact identity

w_i(x)(delta_(h_i(x))-delta_(h_i(tau_i x)))

=w_i(x) delta_(h_i(tau_i x)) * (delta_(h_i(x)-h_i(tau_i x))-delta_0).

Thus mu_i is explicitly a sum of translated first differences on the real target. Multiplying these identities makes eta a sum of translated r-th mixed differences, which kill polynomials of total degree less than r. Repeated integration of the fundamental theorem of calculus bounds each mixed difference by L times the product of its r step lengths. Summing the absolute coefficients factors the bound into product_i C_i. QED.

This is an actual transfer operation: a combinatorial pairing certificate becomes a geometric first-difference certificate under any observation map, then convolution composes it into an analytic higher-order estimate. It does not pretend that the original C_2 augmentation order was a finite moment order. It adds geometry at the adapter and does not assume the target polynomial vanishing. The result is elementary existing difference calculus, not evidence that a new universal tool must be invented.

## E. Nearest established theory; what was actually checked

The following sources were inspected through primary publisher or author-hosted pages on 2026-10-18. They establish that the main algebraic mechanisms predate this project. No exact theorem here is claimed as new.

1. I. B. S. Passi, *Polynomial maps on groups*, Journal of Algebra 9 (1968), 121-151, [DOI](https://doi.org/10.1016/0021-8693(68)90017-3). Original publisher fetch failed; the metadata and the augmentation-ideal formulation were checked against Passi's publisher-hosted [Polynomial Maps chapter](https://link.springer.com/chapter/10.1007/978-3-662-21571-5_58). Passi's [1979 monograph](https://link.springer.com/book/10.1007/BFb0067186), whose publisher contents were read, explicitly covers polynomial maps, dimension subgroups, and the associated graded group ring. Full inaccessible proofs were not represented as read.

2. S. A. Jennings, *The structure of the group ring of a p-group over a modular field*, Transactions AMS 50 (1941), 175-185, [DOI](https://doi.org/10.1090/S0002-9947-1941-0004626-6). D. G. Quillen, *On the associated graded ring of a group ring*, Journal of Algebra 10 (1968), 411-418, [publisher](https://www.sciencedirect.com/science/article/pii/0021869368900690). Publisher access to the original full texts failed. These are the classical general dimension-subgroup/graded-group-ring context, not a claimed proof source for every detail of this note. T1 proves the elementary abelian case directly and does not require a general Jennings or Quillen theorem.

3. E. Aichinger and J. Moosbauer, *Chevalley-Warning type results on abelian groups*, [arXiv:1912.08448](https://arxiv.org/abs/1912.08448), [v1 HTML](https://arxiv.org/html/1912.08448v1), [journal DOI](https://doi.org/10.1016/j.jalgebra.2020.10.033). The original v1 sections 2, 4 and 12 were inspected. Definition 2.1 uses the augmentation-ideal action; Theorem 4.2 already proves the nontrivial composition bound fdeg(g composed with f)<=fdeg(g)fdeg(f); Lemma 12.1 and Theorem 12.3 identify finite-field monomial and reduced-polynomial functional degrees with p-weight. P. L. Clark and U. Schauz, *Functional degrees and arithmetic applications II: The Group-Theoretic Prime Ax-Katz Theorem*, [v1 HTML](https://arxiv.org/html/2305.01304v1), 2023, sections 1.3 and 4 were inspected. Its Theorem 4.6 attributes the reduced-polynomial equality to Aichinger-Moosbauer, journal Theorem 10.3; numbering differs from their 2019 arXiv v1. This directly covers the relevant finite-field p-weight mechanism and shows that a useful general composition calculus already exists.

4. D. Grinberg and V. Reiner, *Hopf Algebras in Combinatorics*, [author-hosted notes](https://www.cip.ifi.lmu.de/~grinberg/algebra/HopfComb.pdf), Exercise 1.6.4, PDF page 30 (printed page 30), was inspected. It gives the divided-power dual basis multiplication f^(i)f^(j)=binom(i+j,i)f^(i+j), the factorial identification over a Q-algebra, and the positive-characteristic p-th-power obstruction. The [Stacks Project, Divided powers](https://stacks.math.columbia.edu/tag/07GK) was also inspected for the standard axioms. These are existing mathematics, not new structures proposed here.

5. A. Drapal and P. Vojtechovsky, *Symmetric multilinear forms and polarization of polynomials*, [v1 HTML](https://arxiv.org/html/1509.05707v1), was checked as the nearest subset-sum/polarization comparison; its functional/combinatorial p-degree mechanism is already noted in SC-003. No historical claim for the exact packaged ternary 5/7 classification follows from either a search hit or its absence.

The mixed finite-difference estimate and Taylor estimate are standard elementary analytic arguments, proved here to expose the required hypotheses. No optimization of constants or exhaustive field enumeration is needed for the conclusion.

## F. Review ledger and next nontrivial operation

Independent mathematical view requested from a real task-scoped agent before it received this note. It independently derived the finite-field moment-to-truncated-divided-power isomorphism and digit-sum formula, then agreed that the same proof extends to any finite F_p-subspace of any characteristic-p field. The same agent subsequently performed a separately labeled adversarial pass on this note. That pass found three issues, all corrected: equivariance gave target vanishing only on the image without surjectivity; double annihilation required a field and either the regular action or the correct permutation submodule; the convolution statement needed compact support for both measures. It checked the sharp-bound endpoints, arbitrary-subspace hypothesis, action convention, interpolation triangularity and multivariate leading-polynomial argument without finding a fatal error. A separate adversarial researcher was not part of this subtask; the coordinating project may arrange one. Details are in `docs/reviews/MACRO_ALGEBRA_REVIEW.md`. There is no formal verification or human peer review.

Useful next operation: take one genuinely held-out proof with a symmetry or analytic cancellation step, extract (i) the actual action or factorization, (ii) the observable filtration, (iii) the leading symbol or derivative seminorm, and (iv) an explicit map to a different target. Prove a target statement whose hypotheses do not already assume the desired vanishing, and test whether a necessary hypothesis can be removed. A successful use of T2 plus the mixed-derivative bound would establish practical proof transfer. If the map is not filtration-compatible, produce its first failing observable and record a no-go result. Merely adding more finite-field examples or restating zero as kernel membership would not settle that question.

For the user's larger AI question, the nontrivial missing operation is separate: define a held-out corpus and compare AI success across matched problems where a known cancellation certificate is present, absent, hidden, or deliberately broken. These theorems justify testable features; they do not establish that cancellation causes AI success or that a new mathematical instrument is necessary.

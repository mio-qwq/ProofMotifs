# SC-003: complete order classification for three ternary differences

**PM-THEOREM-0003.** Mathematical status: PROVED_MANUALLY. Exact finite and symbolic coefficient checks passed. Formalization: NOT_STARTED. Independent review: outstanding. **Novelty not yet established**; conservative Level 1 candidate at most, not a claimed substantive new discovery.

## Statement

Let K be any field of characteristic three, let a,b,c in K, and let

mu = (delta_a-delta_0)*(delta_b-delta_0)*(delta_c-delta_0).

Define ordinary moment order as in SC-001, with zero weight of order infinity. Put

e_1 = a^2+b^2+c^2,
e_2 = a^2b^2+a^2c^2+b^2c^2.

Then exactly one of the following occurs:

| Condition | Conclusion |
| --- | --- |
| abc=0 | mu=0 |
| abc!=0 and e_1!=0 | ord(mu)=5 |
| abc!=0, e_1=0 and e_2!=0 | ord(mu)=7 |
| abc!=0 and e_1=e_2=0 | mu=0 |

In particular the only finite orders are 5 and 7. The statement does not require K to be finite or perfect, and does not assume independent directions.

## Polynomial identities and proof

For every n>=0, expand the eight subset terms defining the three differences. Any monomial missing at least one of a,b,c cancels by inclusion-exclusion. Therefore

M_n(mu) = sum_{i,j,k>=1, i+j+k=n} multinomial(n;i,j,k) a^i b^j c^k.

The sum is empty for n<3. For n=3 and 4, the surviving multinomial coefficients are divisible by three. For n=5, the only nonzero coefficients modulo three are the permutations of (3,1,1), each equal to 20=-1. For n=6 all coefficients are divisible by three. For n=7 only permutations of (3,3,1) remain, with coefficient 140=-1. Hence the exact identities in K[a,b,c] are

M_0=M_1=M_2=M_3=M_4=M_6=0,
M_5=-abc e_1,
M_7=-abc e_2.

One can check the coefficient statements either by the displayed multinomial formula or by base-three digit expansion. They are polynomial identities, not an assumption about generic directions. The script `symbolic_moments` explicitly checks every positive-exponent composition for degrees 0 through 7 using integer factorials before reduction modulo three.

If abc=0, one of the factors is already the zero weight. If abc!=0 and either e_1 or e_2 is the first nonzero invariant, the identities prove the stated order. It remains to show that the double-zero case means a zero weight, rather than an unexamined higher-order residual.

Put A=a^2, B=b^2, C=c^2. When e_1=e_2=0,

(T-A)(T-B)(T-C)=T^3-ABC.

Since A,B,C are roots of the right side and Frobenius is injective in a field, A=B=C. Thus b and c belong to {a,-a}. In the additive convolution algebra, delta_a^3=delta_{3a}=delta_0 and

(delta_a-delta_0)^3=0,
Delta_{-a}=-delta_{-a}*Delta_a.

The product of the three differences is consequently a unit scalar/translation times Delta_a^3, so it is zero. This uses injectivity, not surjectivity, of Frobenius; no unproved cube-root existence or perfectness condition enters.

A second termination check is available: the weight has at most eight distinct support nodes. If the eight moments 0 through 7 all vanish, the Vandermonde bound in SC-001 already forces zero. This cross-check also handles collisions of subset sums.

## PM-CONJECTURE-0001 and PM-COUNTEREXAMPLE-0002

The natural rank-only proposal is **REFUTED**:

> For products of a fixed number of nonzero first differences in a fixed characteristic, their F_p-linear dependence pattern, together with the orders of all proper subproducts, determines the ordinary moment order.

A counterexample already occurs in the single field

K=F_3[alpha]/(alpha^3+2alpha+1).

The cubic has no root in F_3 and is irreducible; hence 1,alpha,alpha^2 form a basis. Compare the direction triples

u=(1,alpha,alpha^2),
v=(1,alpha,alpha^2+2alpha).

Both are linearly independent over F_3. Thus their full dependence patterns are identical. Every singleton has order one, and every pair has order two by SC-001 because binom(2,1)=2 is nonzero. Nevertheless, the full products have orders five and seven respectively.

For u, e_1=1+2alpha+2alpha^2 is nonzero and M_5=2alpha. For v, (alpha^2+2alpha)^2=-1-alpha^2, so e_1=0; direct field reduction gives M_7=2+alpha, nonzero. The classification above proves the claimed orders, not merely lower bounds.

The complete support coefficients and moments are in `research/experiments/ternary-results.json`. The encoding c_0+3c_1+9c_2 means c_0+c_1 alpha+c_2 alpha^2. The triples are encoded as (1,3,9) and (1,3,15), not as integers modulo 27.

This is a counterexample to the stated natural proposal of this project, not to an identified published conjecture. No minimality over all parameters or historical priority is claimed.

## Verification scope

All 20,439 ordered triples over F_3, F_9 and F_27 were checked, including zero directions, repeated directions and linearly dependent triples. Direct convolution was compared with a separate eight-subset inclusion-exclusion implementation. The implementation also checked the invariant formulas and all complete moment vectors.

In F_27 the 19,683 triples divide into 16,848 of order 5, 624 of order 7 and 2,211 zero weights. Normalizing a=1 and requiring F_3-rank three leaves 432 triples: 408 of order 5 and 24 of order 7. These are exact finite counts, not an asymptotic law. Four additional unit tests bring the suite to 14; field axioms were additionally checked on F_27. The algorithms still share finite-field tables and are not independent reviewers.

## Prior art and research value

The mechanism is a finite-difference/polarization calculation in positive characteristic. [Clark-Schauz, sections 1.3 and 4](https://arxiv.org/html/2305.01304v1) already develops the relation with group algebras, functional degree and p-weights, building on [Aichinger-Moosbauer](https://arxiv.org/abs/1912.08448). [Lai's higher-order derivative work](https://link.springer.com/chapter/10.1007/978-1-4615-2694-0_23) is another required comparison, whose full text has not yet been inspected here. Broad exact-term searches returned noisy results and cannot establish absence of prior art.

The precise order-5/order-7 classification and witness are established in this project, but whether the packaged statement already appears in the literature remains unverified. Its immediate value is to rule out an under-specified scalar-order or matroid-only transfer certificate: the higher-degree field relations must also be retained. No claim of a new universal method or a resolved public open problem follows.

### Focused prior-art follow-up

[Drapal-Vojtechovsky, *Symmetric multilinear forms and polarization of polynomials*, section 2.1](https://arxiv.org/html/1509.05707v1) defines exactly the subset-sum defect used above. Lemma 3.1 treats repeated arguments in positive characteristic; Theorem 4.8 and Corollary 4.11 identify combinatorial degree with p-degree in their respective settings. The arXiv version is dated 18 September 2015; that upload date should not be used as the earliest publication date. These sources rule out claiming the defect construction or p-weight mechanism as new.

[Higher Order Differentiation over Finite Fields with Applications to Generalising the Cube Attack, arXiv:1410.4095](https://arxiv.org/abs/1410.4095) is another direct 2014 prior-art lead. Its abstract was read, not its full proof. The exact packaged order classification remains historically unverified. The next structural use is the additive-map preserver classification in SC-005, not a claim that these classical mechanisms were first discovered here.

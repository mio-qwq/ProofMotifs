# SC-002: saturated mixed differences and subspace moments

Claim: **PM-THEOREM-0002**. Complete written argument and exact small-field checks. **Level 0: classical group-algebra, interpolation and subspace-polynomial consequences.** No novelty, Lean or independent-review certification.

## Statement

Let K be a field of characteristic p, d>=0, and a_1,...,a_d in K. With Delta_a=delta_a-delta_0 and multiplication given by additive convolution, set

mu = product_{j=1}^d Delta_{a_j}^{*(p-1)}.

If the directions are linearly dependent over F_p, mu is the zero weight. If they are independent, let W be their F_p-span and N=p^d. Then

mu = sum_{w in W} delta_w,
ord(mu)=N-1,
M_{N-1}(mu)=c_0=(-1)^d det(a_j^{p^i})_{0<=i<d,1<=j<=d}^{p-1} != 0.

Here c_0 is the coefficient of X in P_W(X)=product_{w in W}(X-w). The empty case d=0 means mu=delta_0, N=1, c_0=1 and the empty determinant is 1.

More generally, for every f in K[X],

sum_{w in W}f(w)=c_0 [X^{N-1}](f mod P_W),

where the remainder has degree <N.

## Proof

In F_p[T], (T-1)^{p-1}=sum_{c=0}^{p-1}T^c, since binom(p-1,c)=(-1)^c modulo p. Substitute the translation delta_a to obtain Delta_a^{*(p-1)}=sum_c delta_{ca}. The product is therefore the pushforward of uniform counting on F_p^d under c -> sum c_j a_j. A dependent map has every nonempty fiber of size p^{d-rank}, zero as a scalar in K. An injective map has fiber sizes one on W. This proves the weight identity and the zero case, including zero directions.

We next show that P_W is linearized and P_W'=c_0 is a nonzero constant. Start with P_{0}(X)=X. If W=U direct-sum F_p a and P_U is linearized, then

P_W(X)=product_{c in F_p}(P_U(X)-c P_U(a))
       =P_U(X)^p-P_U(a)^{p-1}P_U(X).

Here P_U(a)!=0 because a is not in U. Thus the induction preserves linearized form and a nonzero coefficient of X. For a polynomial f of degree <N, Lagrange interpolation yields

f(X)=sum_{w in W} f(w) P_W(X)/((X-w)P_W'(w)).

Every P_W'(w)=c_0, and the monic quotient in each summand has degree N-1. Comparing coefficients gives sum f(w)=c_0[X^{N-1}]f. Taking monomials proves the exact order. Reducing a general f modulo P_W preserves its values on W and proves the remainder formula.

For the determinant expression put D=det(a_j^{p^i})_{i=0}^{d-1}. Independence implies D!=0: otherwise a nonzero linearized polynomial of degree at most p^{d-1} would vanish at every element of W, contradicting the root bound. The converse follows from F_p-linearity of the columns. Append the column (X,X^p,...,X^{p^d}) to the d columns of powers of the a_j, and divide this (d+1)-row determinant by D. It is monic of degree p^d, has all W as roots, and hence equals P_W. Expansion at the X entry gives coefficient (-1)^d D^p/D, as required. The empty case is checked separately.

## Prior art and precise contribution

These arguments use classical subspace polynomials and Moore determinants, not a new cancellation framework. See [Subspace Polynomials and Cyclic Subspace Codes, section II](https://arxiv.org/html/1404.7739v3), [Fresnel-Matignon, On the Moore determinant](https://ems.press/journals/rsmup/articles/13549914), and the finite-difference/group-algebra calculus in [Clark-Schauz](https://arxiv.org/html/2305.01304v1). The project contribution at this stage is an explicit hypothesis map and a reproducible cross-check between three representations.

## Verification and limits

`tools/run_experiments.py` exhausts ordered direction tuples of lengths 0 through m+1 over F_{p^m}, for q=2,3,4,8,9: 5,606 tuples total. Direct convolution is compared with fiber counting, ordinary moments, a root-product coefficient and a permutation-computed Moore determinant. Degenerate/dependent/empty cases are included. These are finite checks, not the proof for arbitrary fields.

Saturation is essential. In characteristic three, a product of three first differences is not a product of three saturated (second) differences. The first experiments in SC-003 show that even linearly independent directions can have different ordinary moment orders. Do not transfer this theorem to arbitrary exponent vectors without proof.

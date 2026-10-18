# A uniform multiplicative-Fourier proof of the incidence kernel

Date: 18 October 2026. This is an alternative proof of PM-THEOREM-0013.
It does not replace the independently certified completion/Freiman proof or
the finite rank certificates; it supplies a second mathematical route.

Let `K=F_q`, `q=3^m`, `m>=3`, `S=(K*)^2`, and `N=|S|=(q-1)/2`. Let `C` be
the `F_3`-space of functions `f:S->F_3` whose values sum to zero on each
distinct zero-sum triple in `S`. We prove that `C` is exactly the restrictions
of affine `F_3`-functions on `K`.

## 1. Multiplicative character decomposition

Let `A` be an algebraic closure of `F_3`. Scalar extension commutes with the
kernel of the incidence matrix, so `C_A=C tensor A` is the same incidence
kernel over `A`. Multiplication by `S` permutes all zero-sum triples, hence
`C_A` is stable under the regular `S`-action on `A^S`.

Since `3` does not divide `N` and `A` contains all `N`th roots of unity, the
regular `A[S]`-module is split semisimple and multiplicity-free. Its character
lines are

`V_k=A f_k`, where `f_k(u)=u^k` and `0<=k<N`.

Therefore `C_A` is the direct sum of the admissible `V_k`.

Normalize a zero-sum triple by its first vertex and put

`R={a in S:-1-a in S}`.

The only repeated normalized triple is `(1,1,1)`, whose equation is automatic
in characteristic three. Thus `V_k` is admissible exactly when

`P_k(a)=1+a^k+(-1-a)^k=0` for every `a in R`.                 (1)

If `eta=chi(-1)` for the quadratic character, a direct indicator expansion
gives

`|R|=(q-2-3eta)/4`.

Indeed, after removing `0,-1`, the three nonconstant character sums in the
expansion are each `-eta`; the product sum reduces to the standard quadratic
sum `sum chi(a(a+1))=-1`. Hence, writing `H=|R|`,

* `H=(q+1)/4` when `m` is odd;
* `H=(q-5)/4` when `m` is even.

## 2. Low and high exponent exclusions

If `0<k<H`, then `P_k` has at least `H` roots but degree at most `k`, so it is
the zero polynomial. Its constant and leading terms force `k` odd, and then

`(1+X)^k=1+X^k`.

Lucas' theorem gives exactly `k=3^j`. Conversely every such exponent is
admissible by Frobenius, and `k=0` is admissible because `3=0`.

For a high exponent put `r=N-k`. If (1) holds and `a in R`, set `b=-1-a`.
Since `a^N=b^N=1`, multiplication by `a^r b^r` gives

`Q_r(a)=(ab)^r+a^r+b^r=0`.

As a polynomial in `a`,

`Q_r(X)=X^r(-1-X)^r+X^r+(-1-X)^r`

is nonzero of exact degree `2r`: its leading coefficient is `(-1)^r` and the
other two summands have degree at most `r`. Thus (1) is impossible whenever
`2(N-k)<H`.

## 3. Frobenius orbits leave only one possible exception

Admissibility is closed under

`T(k)=3k mod N`,

by cubing (1) and using `a^N=(-1-a)^N=1`. The map `T` is a permutation because
`gcd(3,N)=1`.

If `m` is odd, write `N=4t+1`, so `H=2t+1`. Any undesired admissible orbit
would have to remain in

`I=[2t+1,3t]`.

An orbit that ever met a lower Frobenius exponent would be the already
accepted Frobenius orbit, because `T` is a permutation.

For `k in I` with `k>=2N/3`, `T(k)=3k-2N` lies outside `I`. Otherwise
`T(k)=3k-N`, and its positive distance from `N/2` is three times the previous
distance. A finite orbit cannot remain in the bounded interval. Thus there is
no undesired orbit.

If `m` is even, write `N=4t`, so `H=2t-1`. The boundary exponent `k=H` is
odd, hence `deg P_k<=k-1=H-1`; if it were admissible, the same root argument
would force `k=3^j`. But `k=(q-5)/4>1` is `1 mod 3`, so this is impossible.
Every remaining undesired orbit would lie in

`I=[2t,3t]`.

The same distance-tripling argument shows that the only orbit wholly inside
this interval is the fixed exponent `k=N/2`.

## 4. Excluding the order-two character

Assume `m` even. Then `q>=81` and `q=1 mod 8`. We first find a nonsquare `s`
such that `s^2+1` is a nonzero square. Put

`T_0=sum_(s in K) chi(s^3+s)`.

The cubic `s^3+s` is squarefree because its derivative is one, so the
quadratic Weil bound gives `|T_0|<=2sqrt(q)`. The number `A_0` of nonsquare
`s in K*` with `chi(s^2+1)=1` is

`A_0=(q-3-T_0)/4`.

To see this, expand `(1-chi(s))(1+chi(s^2+1))/4` over `s!=0` and use
`sum chi(s)=0`, `sum_(s!=0)chi(s^2+1)=-2`, and the product sum `T_0`.
The roots of `s^2+1`, when present, are squares because `q=1 mod 8`, so they
make no spurious half-indicator contribution. Since
`q-3-2sqrt(q)>0` for `q>=81`, such an `s` exists.

Let `a=s^2` and `b=-1-a`. Both lie in `S` and are nonzero: `b` is a square
because both `-1` (as `q=1 mod 8`) and `s^2+1` are squares. For `k=N/2`,

`a^k=s^N=chi(s)=-1`,

while `b^k` is one of `1,-1`. Hence
`1+a^k+b^k=b^k!=0`, contradicting (1). The last possible exponent is not
admissible.

## 5. Conclusion and limits

The admissible spectrum is exactly

`{0,1,3,...,3^(m-1)}`.

These `m+1` exponents are distinct modulo `N`. Hence
`dim_A C_A=dim_F3 C=m+1`. Affine restrictions already lie in `C`, and they
are independent because `|S|>3^(m-1)`, larger than a proper affine
hyperplane. They therefore equal `C`.

This proof uses a multiplicative cyclic-code/Fourier decomposition, Lucas'
theorem, elementary root bounds, and one classical cubic Weil estimate. It is
uniform for every `m>=3` and does not use the exact `m=3,4` rank certificates.
It does not prove a result in other characteristics or for arbitrary
multiplicative subgroups. A naive `M^T M` spectral calculation would be
invalid in characteristic three because the incidence rows are isotropic;
the semisimple regular action of `S` is the relevant decomposition. No Lean
or historical-originality claim is made.

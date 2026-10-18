# PM-CYCLE8-E: independent audit of SC-009 Fourier proof

Reviewer: /root/weil_completion_review, actual scoped AI research agent.
Date: 2026-10-18. Checkout head read: 21999eb.
Scope: read only workstreams/SC-009/FOURIER_PROOF.md; no acceptance decision
from SEVENTH_CYCLE was assumed. No shared files edited or pushed.

## Verdict

ACCEPT the complete uniform proof for every m>=3. No correction required.
The finite rank certificates and completion proof are not used by this route.
This is independent AI mathematical review, not Lean or human verification,
and historical novelty remains unverified.

## 1. Base change and Fourier decomposition

K may be identified with its subfield of an algebraic closure A of F3.
For an incidence matrix with entries in F3, extending scalars to A preserves
rank and identifies its kernel with C tensor A. The subgroup S acts regularly
on itself by multiplication and permutes the zero-sum edge set, so that the
kernel is stable. Since N=(3^m-1)/2 is prime to3 and A contains all Nth roots,
the cyclic regular action is diagonalizable with N distinct character lines
A*(u->u^k), 0<=k<N. These monomial functions are independent (a polynomial
of degree<N cannot vanish on all N points). A stable subspace of an operator
with distinct eigenvalues is the sum of some eigenlines, e.g. by its spectral
projection polynomials. Thus the admissibility test loses no kernel vectors.

Scaling an edge by its first nonzero vertex normalizes it to (1,a,-1-a),
where a and -1-a lie in S. In characteristic3 a repeated entry in such a
zero-sum triple forces all three entries equal. The normalized repeated
triple is (1,1,1), and every monomial automatically satisfies its equation.
Therefore testing P_k on the complete set R is precisely equivalent to
edge admissibility, even though R includes1.

For R the character product is (1+chi(a))(1+chi(-1-a))/4 away from0,-1.
The two single-character sums on this punctured field are each -eta;
their product sum is eta*sum chi(a(a+1))=-eta. Thus
H=|R|=(q-2-3eta)/4, giving the manuscript's odd/even formulas exactly.

## 2. Low and high exponents

If0<k<H and P_k vanishes on R, degree<=k<H implies polynomial zero.
Its constant coefficient is1+(-1)^k, so k is odd. The identity then becomes
(1+X)^k=1+X^k. Lucas' theorem, or the base-three factorization of this
polynomial, forces exactly one nonzero base-three digit, equal to1:
k=3^j. Conversely those exponents are admissible by Frobenius.
k=0 gives the constant character and is admissible since3=0.

For r=N-k>=1, multiplying the relation by a^r(-1-a)^r is legal because
both factors belong to S and hence have Nth power1. The resulting Q_r
has exact degree2r with nonzero leading coefficient(-1)^r. Its remaining
summands have degree<=r<2r, so no cancellation of that leading term occurs.
If2r<H, root counting excludes it. This argument does not confuse ordinary
polynomial identity with polynomial functions modulo X^q-X: the degree is
strictly less than the number H of distinct roots in the range applied.

## 3. Frobenius interval argument and boundary

Cubing the relation sends exponentk to3k modulo N, and this is a permutation
because3 is coprime to N. All desired positive exponents lie in one orbit:
1,3,...,3^(m-1), followed by3^m=1 modulo N. An undesired orbit therefore
cannot meet even one of those allowed exponents.

For oddm, N=4t+1 andH=2t+1. The high exclusion2(N-k)<H is exactly
k>=3t+1; the low exclusion leaves any undesired orbit inI=[2t+1,3t].
For evenm>=4, N=4t andH=2t-1. Boundaryk=H is odd, so degP_H<=H-1.
Its H roots would force the same Frobenius identity, but H>1 andH=1mod3,
which is incompatible with H=3^j. The same high cutoff therefore leaves
I=[2t,3t].

For either I, ifk>=2N/3, thenT(k)=3k-2N is at mostt-2 (odd) or t(even),
hence strictly below I. There is no equality k=2N/3 because3 does not divide N.
Otherwise N<3k<2N, soT(k)=3k-N and
T(k)-N/2=3*(k-N/2).
In the odd interval the distance is always positive; it cannot triple
indefinitely in a finite bounded interval. In the even interval onlyk=N/2
has zero distance, and it is fixed. Every other orbit must leave I.
An actual further scoped reviewer /fourier_interval_audit independently
re-derived and accepted these endpoint calculations.

## 4. Quadratic-order character exclusion

For evenm, q=3^m is1mod8. In particular chi(-1)=1, the roots +/-i of
s^2+1 exist, and both are squares: their order4 divides (q-1)/2.
For s!=0, the expression
(1-chi(s))*(1+chi(s^2+1))/4
is exactly the indicator of chi(s)=-1 andchi(s^2+1)=1. The only possible
spurious half-indicators occur at s^2+1=0, but therechi(s)=1, so they
vanish. The standard quadratic sum gives sum_K chi(s^2+1)=-1, and removing
s=0 changes it to-2. The sum of chi(s) on K* is0 and the mixed sum is
T0=sum_K chi(s^3+s). Expansion therefore gives
A0=((q-1)-2-0-T0)/4=(q-3-T0)/4,
with no missing endpoint correction or eta.

The polynomial s^3+s is squarefree since its derivative is1 inchar3.
The multiplicative quadratic Weil bound gives|T0|<=2sqrtq. Forq>=81,
q-3-2sqrtq>0, so an appropriate nonsquares exists. Its squarea=s^2 lies
in S. The nonzero square s^2+1 and square -1 implyb=-1-a lies in S.
For k=N/2, a^k=s^N=chi(s)=-1, whileb^k is nonzero (in fact +/-1).
Thus P_k(a)=1-1+b^k=b^k!=0, contradiction. The argument never requires
an unproved relation between the quartic characters ofa andb.

The q>=81 bound is compatible with the exceptionalq9: atq9 the bound
can be zero and no exclusion follows. This explains rather than hides
the necessary m=2 failure. The proof assumes m>=3 throughout.

## 5. Dimension conclusion

All exponents1,3,...,3^(m-1) are <N for m>=2, hence distinct as integers
and moduloN; adding0 givesm+1 distinct admissible lines. Their Fourier
dimension equals the original F3 kernel dimension by base change.
Affine restrictions belong to the kernel, and no nonzero affine functional
can vanish on S since |S|>3^(m-1), the size of an affine hyperplane.
Thus the kernel equals exactly the affine restrictions.

## Sources and next action

The only analytic input is the same standard multiplicative quadratic Weil
bound already independently inspected in Kim--Yip--Yoo2024 Lemma2.1:
https://link.springer.com/article/10.1007/s11139-024-00888-5 .
Squarefreeness, character order2, and all degree/leading coefficient
conditions have been checked; there is no coprimality condition between
polynomial degree and characteristic for this multiplicative bound.
The Lucas special case can also be proved directly by base-three binomial
factorization if a self-contained text is preferred.

Concrete next step: coordinator can mark this route independently
AI-reviewed for mathematical correctness and preserve the proof as an
alternative to the completion/Freiman route. A follow-on generalization
should explicitly track where characteristic3, square-subgroup index2,
and the involutory exponent N/2 are essential; none is removed by this proof.
Do not infer historical novelty, Lean verification, or cross-domain
unification from this acceptance.

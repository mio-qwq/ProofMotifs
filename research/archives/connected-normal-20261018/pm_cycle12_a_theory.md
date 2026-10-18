# PM-CYCLE12-A: normal parameters with multiplicatively connected square seeds

Task: PM-CYCLE12-A. Question: PM-QUESTION-0002. Research baseline supplied by
coordinator: c6a1dec3e1032f9c45cafdb9efc2cfe01f37719d; mathematical bf3bbf5.
Scope: repo read-only, /tmp notes and scripts only. No shared repo edit, push,
external correspondence, or claim of human/formal review.

## Outcome

The maximal-prime-index subgroup subtraction works. With the unweighted
hybrid refinement below it proves the requested connected-normal existence
for every m >= 11 and also m = 9. Degree 7 follows automatically from the
prime order of S and SC-015 normality existence. SC-015 already supplies
connected witnesses at 5 and 8. Thus the full m >= 5 claim needs new explicit
connected-normal witnesses only at m = 6,10. I do not claim these remaining
two witness checks here and do not infer any infinite statement from them.

More precisely the following sufficient criterion has a complete classical
character-sum proof. It does not require a or b individually to generate S.

Put q = 3^m, N = (q-1)/2, S = (F_q^*)^2, and let C_m count normal y with
a = (y+1)/y, b = (y-1)/y in S and <a,b> = S. Put

    omega = number of DISTINCT irreducible factors of T^m-1 over F_3,
    W = 2^omega,
    Theta = product_(P | T^m-1) (1-3^(-deg P)),
    r = number of DISTINCT prime divisors of N,
    sigma = sum_(prime ell | N) ell^(-2).

For every m > 1,

    C_m >= Theta/4 * [ q(1-sigma) - 3
          - {6(W-1)+(3W-1)(4r-sigma)} sqrt(q) ].             (A)

In particular, positivity of the displayed bracket proves existence. All
dependence on multiplicative prime divisors is linear in r, not W(N).

## Normality input, including 3 | m

Use the CRT/additive Fourier proof in SC-015 Section 1.1, not a semisimple
Frobenius assertion. If Omega is the normality indicator, then

    Omega(y) = sum_psi c_psi psi(y),
    c_1 = Theta,
    sum_(psi != 1) |c_psi| = Theta(W-1),
    sum_y Omega(y) = Theta q.

Repeated factors P^e remain in F_3[T]/(T^m-1); only omega, W and Theta use
distinct factors. Since m > 1, Omega vanishes on E = {0,1,-1}.

Let A_m count normal parameters with a,b in S, equivalently equal nonzero
quadratic signs at y-1,y,y+1. SC-015's exact quadratic/Kloosterman proof gives

    A_m >= Theta/4 [q - 3 - 6(W-1)sqrt(q)].                 (B)

The -3 is from the three untwisted quadratic sums, each exactly -1. Endpoints
need not be subtracted again because Omega(E) = 0.

## Maximal subgroup obstruction

For a prime ell | N let H_ell = S^ell, the unique subgroup of index ell in
S and index d = 2ell in F_q^*. Let D_ell count normal y with a,b in H_ell.
Since S is cyclic, <a,b> != S if and only if a,b lie in some H_ell. Thus

    C_m >= A_m - sum_(ell | N prime) D_ell.                (C)

No primitive-element assertion is involved; especially no order q-1
condition is imposed on the necessarily-square a or b.

## Uniform D_ell bound with endpoint audit

Fix a character eta of EXACT order d = 2ell, and put U=F_q\E. On U,

    1_(a,b in H_ell)
      = d^(-2) sum_(0<=j,k<d) eta^j((y+1)/y) eta^k((y-1)/y).

For j=k=0 the sum against Omega is exactly Theta q, not Theta(q-3), since
Omega(E)=0. This isolates principal additive endpoints without an artificial
3 Theta(W-1)/d^2 loss.

For any other (j,k), choose t in {0,...,d-1} with t = -j-k mod d, and put

    f(Y) = (Y+1)^j (Y-1)^k Y^t.

On U the summand is eta(f(y)). At least two of j,k,t are nonzero; if just
one were nonzero their sum could not vanish modulo d. Therefore f has
s = 2 or 3 distinct roots, and is not a d-th power even over the algebraic
closure: at least one root valuation is nonzero modulo d.

For the PRINCIPAL additive character, the complete pure multiplicative Weil
bound is (s-1)sqrt(q). If s=3, no endpoint is missing from its zero extension.
If s=2, removing the remaining endpoint adds at most 1. Thus

    |sum_(y in U) eta(f(y))| <= 2sqrt(q).

For every NONPRINCIPAL additive psi, write psi(y)=psi_0(cy), c != 0, for a
fixed nonprincipal additive psi_0 on F_q. The mixed bound with additive
argument g(Y)=cY gives s sqrt(q). If s=2, removing the remaining endpoint
adds at most 1. Hence, uniformly,

    |sum_(y in U) eta(f(y)) psi(y)| <= 3sqrt(q).

Here 1 <= sqrt(q), so the endpoint estimates are valid. Applying the
normal Fourier mass gives, for every nonprincipal (j,k),

    |sum_(y in U) Omega(y) eta(f(y))|
      <= Theta [2+3(W-1)]sqrt(q) = Theta(3W-1)sqrt(q).

Consequently

    D_ell <= Theta q/(4ell^2)
       + Theta(1-1/(4ell^2))(3W-1)sqrt(q).                 (D)

Inserting (B),(D) in (C) is exactly (A).

## Primary character-sum dependency

Directly fetched and inspected 18 October 2026:

Lei Fu and Daqing Wan, *A Class of Incomplete Character Sums*,
arXiv:1303.3650v3, revised 6 January 2025:
https://arxiv.org/pdf/1303.3650v3
https://arxiv.org/abs/1303.3650v3

Theorem 4.5 (PDF pp. 15-16 counting title page as p.1) gives the pure
multiplicative root-count bound. Set their extension parameter d=1 and their
base field equal to our entire F_q; their rational function is the f above.
Their condition that f is not an ord(eta)-th power is checked by valuations.

Theorem 4.6 (PDF p.16) gives the mixed bound. Again set their d=1, D1=s,
D2=1, D3=D4=0, and g=cY. Its constant is s. Its corrected hypothesis is
that g is not r^p-r over the algebraic closure (p=3), NOT merely not r^q-r.
Our g has exactly one pole of order 1 at infinity. Every pole of nonconstant
r^3-r has order divisible by 3; a constant r cannot give cY. Thus the
corrected hypothesis holds, including when 3 divides m. The v3 abstract
explicitly records the correction to the older theorem. No general
primitive-normal theorem or witness-set intersection is imported.

The fetched web PDF uses the current v3 even through the unversioned URL.
Theorem numbering differs from several secondary citations to "Theorem 5.6".

## Elementary infinite range: all m >= 24

Since 3 does not divide N, every prime divisor other than 2 is at least 5.
For r>=1,

    N >= 2*5^(r-1) > 3^r/2,

and N < 3^m/2, so r <= m-1. Also

    sigma <= 1/4 + sum_(k>=2) 1/(2k+1)^2
          < 1/4 + sum_(k>=2) 1/[4k(k+1)] = 3/8.

There are exactly two possible nonzero-root linear irreducibles over F_3
and three monic irreducible quadratics. If their actual counts in T^m-1
are r1,r2, then m >= 3omega-2r1-r2 >= 3omega-7. This is valid with repeated
factors too, since the full degree m is at least the distinct-factor degree.
Thus W <= U_m = 2^floor((m+7)/3).

The bracket in (A) is strictly greater than

    B_m - E_m sqrt(q),
    B_m = 5q/8 - 3,
    E_m = (12m-6) U_m.                                  (E)

Indeed the error in (A) is < (6+12r)W <= (12m-6)U_m.
Exact rational-integer checks prove B_m > E_m sqrt(q) at m=24,25,26.
No floating point is needed: check B_m>0 and B_m^2 > E_m^2 q.

For the induction m->m+3, U_(m+3)=2U_m,

    B_(m+3)=27 B_m+78 > 27 B_m,
    E_(m+3) < 4 E_m   for m>=4,
    sqrt(q_(m+3)) = sqrt(27)sqrt(q_m) < 6sqrt(q_m).

Thus E_(m+3)sqrt(q_(m+3)) < 24 E_m sqrt(q_m)
< 24 B_m < B_(m+3). This completes the infinite proof, not a finite scan.

## Exact smaller arithmetic

For m<24 compute distinct Frobenius factor counts from n=m/3^v_3(m):

    omega = sum_(d | n) phi(d)/ord_d(3), ord_1(3)=1.

Exact factorization of N and exact Fraction squaring in
/tmp/pm_cycle12_a_count.py verifies (A) for

    m = 9,11,12,13,14,15,17,18,19,20,21,22,23.

The criterion fails (meaning only that it is inconclusive) at

    m = 5,6,7,8,10,16.

For transparency, the close successful case m=12 has omega=3, W=8,
r=5 and N=2^3*5*7*13*73. The ratio of its main term to error*sqrt(q)
is about 1.00715, but acceptance uses exact squared rational arithmetic.

## Hybrid unweighted refinement: degree 16

For every prime ell | N, let B_ell count ALL y in U with a,b in H_ell,
without normality. The same multiplicative expansion and the pure bound
above give

    D_ell <= B_ell <= (q-3)/(4ell^2)
                       + 2(1-1/(4ell^2))sqrt(q).         (F)

Thus each D_ell can independently be bounded either by (D) or (F). No
intersection-of-witness-sets argument is involved: we subtract an upper
bound for the entire bad set from a lower bound for normal filtered points.

At m=16 use (D) for ell=2 and (F) for ell=5,17,41,193. Here

    N = 2^5*5*17*41*193, sqrt(q)=6561,
    T^16-1 has two linear, three quadratic and two quartic factors,
    Theta = (2/3)^2 (8/9)^3 (80/81)^2 = 13107200/43046721,
    W=128.

Exact bounds are

    A_lower = 41557727641600/14348907,
    D2_upper = 3360358400/2187,
    sum_(ell=5,17,41,193) D_ell
         <= 72628904110764/137884025.

The remaining margin is

    1648029321615946945052/1978485051510675 > 0.

This gives degree 16 analytically without a field witness search. The saved
checker independently recomputes all factors and Theta and tests this
positive rational margin. Together with the previous range, this proves
existence for every m >= 11, also m=9.

At m=7, S has prime order N=1093 (verified by exact trial division). Every
filtered normal y from SC-015 gives a nonidentity a, since a-1=1/y != 0.
Consequently a alone generates S, so the seed is connected. This uses a
square-group order condition, not full-group primitivity. Existing SC-015
connected degree-5 and degree-8 certificates then leave only degrees 6,10.

## Review and limits

No same-person random search is advertised as an independent arithmetic
check. The theorem is a new application/packaging of classical normality and
character-sum tools; no historical priority claim. No Lean proof. The full
single-orbit row-code problem PM-QUESTION-0001 remains open: connectivity
does not remove genuine quartic or higher spectral obstructions.

Independent review received from task /root/connected_audit_ultra: reviewer
accepted bound (A), the s=2 omitted-endpoint accounting, principal-pair
separation, r/sigma/W estimates and +3 induction, and independently reran the
checker with the same six inconclusive degrees. The reviewer reported an
independent derivation of the same formula before reading this note. This is
AI mathematical review, not human or formal verification. The later hybrid
m16 addition was sent for review separately; do not conflate its status with
the already accepted main formula. Coordinator requested a freeze rather
than further constant optimization; the main route may retain all six fixed
finite witnesses, with the hybrid as optional supplementary evidence.

Actual next lemma: independently verify (A), especially the s=2 endpoint
case and current Fu-Wan r^p-r hypothesis, and the hybrid degree16 rational
margin; then give exact normal and joint multiplicative-generation
certificates for m=6,10 (reuse existing connected-normal m5 and m8 witnesses,
and the prime-order m7 shortcut, rather than rescan those fields).

Reproduction:

    python /tmp/pm_cycle12_a_count.py

Only stdlib Python is needed. Initial attempts to import sympy failed in
both system Python and primary runtime; the saved checker deliberately has
no such dependency. No repository files were written by this task.

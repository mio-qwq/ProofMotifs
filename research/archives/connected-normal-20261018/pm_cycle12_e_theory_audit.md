# PM-CYCLE12-E: independent adversarial connected-normal count audit

Date: 18 October 2026. Task identifier: PM-CYCLE12-E.

## Task ledger and independence

Question: can a normal y in F_(3^m), m>=5, satisfying equal nonzero quadratic
characters at y-1,y,y+1 be chosen so that a=(y+1)/y and b=(y-1)/y jointly
generate the square group S?

Assumptions/evidence: SC-015 normality Fourier calculation and filtered count;
cyclicity of F_q^*; primary Fu--Wan v3 character bounds. Read AGENTS, current
STATUS/HANDOFF, SC-015/RESULTS, and preceding adversarial audit. Repository is
read-only for this task. All writes below are /tmp scratch notes/checkers.
No commits, pushes, external correspondence, or repository modifications.

Independence: the count below, including the exact principal pair and the
constant 3W-1, was derived before reading A's theory note. The finite checker
was written from scratch using only Python's standard library and no project
imports. A separate actual helper, PM-CYCLE12-E2, derived an elementary
threshold m>=40 from the count I supplied; it did not audit the count.
After those independent derivations, I cross-reviewed A's improved m>=24
range and reran A's arithmetic. Human review and formal verification are not
claimed.

Stop conditions: do not infer a missing small-degree witness, do not conflate
connectivity with full row-code generation, and do not infer historical novelty.
Expected output/handoff: a full mathematical verdict with constants, endpoint
audit, infinite range, explicitly unresolved finite degrees, and reproducible
arithmetic. Later final manuscript/certificate review is a separate acceptance.

## Verdict at this stage

ACCEPT the maximal-prime-index subgroup subtraction and the following bound:

    C_m >= Theta/4 * [(1-sigma)q-3
             - {6(W-1)+(4r-sigma)(3W-1)}sqrt(q)].             (E1)

Here q=3^m, m>1, N=(q-1)/2, r is the number of distinct primes dividing N,
sigma is their reciprocal-square sum, W=2^omega with omega the distinct
irreducible factor count of T^m-1 over F_3, and Theta is the normal density.
C_m counts the normal filtered parameters whose two ratios jointly generate S.

The bound and exact finite arithmetic prove existence for every m>=17 and
also m=9,11,12,13,14,15. The raw criterion is inconclusive exactly at
5,6,7,8,10,16 among m>=5. SC-015 already has connected witnesses at 5 and8;
m7 has prime N=1093, so every valid square seed is connected. Thus a complete
all-m>=5 theorem still needs the actual m6,m10,m16 connected-normal
certificates to be supplied and checked. They have not been inspected in this
initial audit. The full row-code question remains open independently.

## 1. The obstruction is a two-variable subgroup event

Write E={0,1,-1}. For y outside E, a=1+1/y and b=1-1/y are distinct,
different from1, and satisfy 1+a+b=0. The square filter is exactly a,b in S.

The cyclic group S has order N. A proper subgroup <a,b> is contained in
one of its unique maximal subgroups H_l of prime index l|N. Conversely,
a,b in H_l prevents generation. H_l has index D=2l in F_q^*, so it is the
kernel of a character eta of exact order D. This includes l=2, for which
D=4, not2. The exceptional characteristic3 prime never divides N.

If B_l counts normal parameters with both ratios in H_l, the union bound is

    C_m >= A_m - sum_(l|N prime) B_l.                       (E2)

There is no requirement that either ratio individually have order N.
The count B_l is already inside the square-filtered set since H_l is in S.

## 2. Normality Fourier facts, including repeated module factors

Let Omega be the normality indicator. The Frobenius module is
F_3[T]/(T^m-1), with every repeated P^e retained. Locally, units are the
complement of the ideal(P), an additive subspace of codimension deg P.
Its Fourier coefficient at the trivial additive character is 1-3^(-deg P),
and the other nonzero coefficients have absolute value3^(-deg P), one
for each nontrivial character annihilating the ideal. Tensoring gives

    c_1=Theta,
    sum_(psi!=1)|c_psi|=Theta(W-1),
    sum_y Omega(y)=Theta q.

The module statement does not assume semisimple Frobenius. No point of F_3
is normal when m>1, so Omega(E)=0. This also eliminates all endpoint terms
after, but not necessarily before, the additive Fourier coefficients are
summed.

## 3. Principal pair and endpoint-free nonprincipal estimate

On U=F_q\E, the pair indicator is

    D^-2 sum_(j,k mod D) eta^j(a) eta^k(b).

The j=k=0 contribution after normal weighting is exactly Theta q/D^2.
It is not Theta(q-3)/D^2: the nonprincipal additive Fourier terms of this
principal multiplicative pair restore3Theta when expanded on U. Dropping
that restoration without placing it in an error is invalid.

For a nonzero pair(j,k), choose t in{0,...,D-1} with t=-j-k mod D, and put

    f(Y)=(Y+1)^j (Y-1)^k Y^t,

omitting factors with exponent0. It has R=2 or3 distinct roots. R=1 is
impossible since j+k+t=0 modD. At least one root valuation is nonzero
modD, so f is not a Dth power even over the algebraic closure.

Although the original rational expression was only defined on U, one can
replace the Omega-weighted summand by the polynomial expression on all K:

    sum_U Omega(y)eta^j(a)eta^k(b)=sum_K Omega(y)eta(f(y)),

where eta(0)=0. This is exact because Omega(E)=0, whether or not a given
endpoint is a root of f. Expand Omega only AFTER this replacement.

The pure sum is bounded by (R-1)sqrt(q). Every nonprincipal additive character
has the form psi_0(cy), c!=0, for a fixed nonprincipal psi_0; the mixed sum
with g(Y)=cY is bounded by R sqrt(q). Therefore

    |sum_U Omega(y)eta^j(a)eta^k(b)|
       <= Theta[(R-1)+R(W-1)]sqrt(q)
        = Theta(RW-1)sqrt(q)
       <= Theta(3W-1)sqrt(q).                             (E3)

This argument avoids endpoint deletions in individual additive sums. A's
alternative argument deletes the sole missing endpoint for R=2 at cost<=1;
its pure<=2sqrt(q), mixed<=3sqrt(q) conclusions are also valid.

Summing D^2-1 nonprincipal pairs proves

    B_l <= Theta[q/(4l^2)
              +(1-1/(4l^2))(3W-1)sqrt(q)].                (E4)

There is no dependence on l in the uniform error constant. Large exponents
do not enter the conductor constant; the number of distinct root factors does.

Optional refinement, not needed for(E1): exactly3(D-1) nonprincipal pairs
have R=2 and(D-1)(D-2) have R=3. Averaging(E3) gives the smaller error
coefficient 3W(1-1/D)-1+1/D^2 in(E4).

## 4. Primary dependency actually inspected

Lei Fu and Daqing Wan, A Class of Incomplete Character Sums,
arXiv:1303.3650v3, revised6 January2025:
https://arxiv.org/html/1303.3650v3
https://arxiv.org/abs/1303.3650

Read the full statements and relevant proof paragraphs of Theorems4.5/4.6
in the versioned primary HTML, including the version correction notice.
Set their extension degree d=1, base field equal to our entire F_q, D1=R,
D2=1, D3=D4=0. Theorem4.5 gives the pure bound via the non-power valuation
check; Theorem4.6 gives mixed constantR.

The corrected nondegeneracy is exclusion of h^p-h, p=3, not merely h^q-h.
Our g=cY has pole order1 at infinity and no finite pole. Any pole of a
nonconstant rational h^3-h over the algebraic closure has order divisible
by3, because the h^3 term dominates there. A constant h does not give cY.
Thus the corrected hypothesis holds, even if3 divides m. Using a canonical
additive psi_0 and c as the argument also checks all nonprincipal additive
Fourier characters, not just one special additive character.

The HF papers skill was read because an arXiv identifier was supplied; its
markdown endpoint returned401. Following its primary fallback, the actual
theorem was read on arXiv. Initial PDF version fetch failed, but primary HTML
and the current unversioned PDF succeeded through web retrieval. No claim is
based merely on a search snippet.

## 5. Combination with the existing filtered count

SC-015 proves

    A_m >= Theta/4[q-3-6(W-1)sqrt(q)].

Substitute(E4) in(E2). The q coefficients are1-sigma, and the square-root
error coefficient after multiplication by4 is

    6(W-1)+4(3W-1)sum_l(1-1/(4l^2))
      =6(W-1)+(4r-sigma)(3W-1).

This proves(E1), with no quantifier interchange and no inference that separate
normal/primitive witness sets intersect.

## 6. Infinite range and finite arithmetic

My independent coarse proof, using W<=2^floor((m+2)/2), r<8m/5 and
sigma<1/2, covers allm>=40. Its separate threshold derivation is in
/tmp/pm_cycle12_e2_threshold.md. My from-scratch arithmetic checker is
/tmp/pm_cycle12_e_arithmetic.py. It uses exact complete trial factorization
of N only through m20, and r<=floor(log2N) beyond that, and independently
recovers the six gaps5,6,7,8,10,16 throughm39. It uses no field arithmetic.

After independent derivation, I cross-reviewed A's stronger elementary
allm>=24 proof in /tmp/pm_cycle12_a_theory.md. Each step is accepted:

* Since3 does not divide N, N>=2*5^(r-1)>3^r/2; hence r<=m-1.
* sigma<1/4+sum_(k>=2)1/[4k(k+1)]=3/8.
* There are at most2 allowed linears and3 irreducible quadratics; therefore
  m>=3omega-7, and W<=U_m=2^floor((m+7)/3), also with repeated factors.
* The(E1) bracket exceeds B_m-E_m sqrt(q), where
  B_m=5q/8-3 and E_m=(12m-6)U_m.
* The three squared anchor margins B_m^2-E_m^2 q are respectively
  486900926659276609679145/64 at m24,
  13032648939782958116718609/64 at m25, and
  97636684430764844241472377/64 at m26, all positive.
* In the +3 step, B_(m+3)=27B_m+78>27B_m,
  E_(m+3)<4E_m for m>=4, and sqrt(27)<6. The error grows by<24 while
  the main grows by>27. This is a real infinite induction.

I reran python /tmp/pm_cycle12_a_count.py, which agrees on all finite gaps
and all three exact anchors. Combined with my independently derived m21..39
coarse checks, the finite range has a second arithmetic route.

## Final current acceptance boundary

The uniform counting theorem and all-large-degree range are correct. I found
no obstruction in the candidate route. The only repaired pitfall was to make
the principal multiplicative pair Thetaq exact, or explicitly absorb the
endpoint restoration if one writes Theta(q-3) instead.

Acceptance of the full all-m>=5 statement awaits inspection of actual
small-degree certificates and final manuscript. No field scan, alleged
primitive-element theorem, or unexamined certificate has been substituted for
those missing checks. Connectivity is only joint generation of S, not full
row-code generation, and no claim of novelty/human review/Lean is accepted.

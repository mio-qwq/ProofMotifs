# PM-CYCLE11-A: normal elements passing the three-character filter

Independent theory note, 18 October 2026. Read-only ProofMotifs task;
written before seeing another agent's proof. No repository files changed.

## Statement

Put K=F_(3^m), q=3^m, m>1, M=T^m-1. Let omega be the number of
DISTINCT monic irreducible factors of M over F_3, W=2^omega, and
Theta=product_(P|M)(1-3^(-deg P)). Let A_m count normal elements y of
K/F_3 satisfying chi(y-1)=chi(y)=chi(y+1) in {1,-1}.

Then

  A_m >= Theta/4 * (q-3-6*(W-1)*sqrt(q)).                 (1)

Consequently A_m>0 whenever (q-3)^2>36*(W-1)^2*q.
The formula and conclusion allow 3|m. In particular A_m>0 for EVERY
m>=9, and also for m=6,7. The same criterion is inconclusive for
m=3,4,5,8. There is a separate obstruction showing A_3=0.

This is a classical normal-element/character-sum argument specialized to
the project's exact three-character predicate. It does not establish
normality plus multiplicative connectivity, nor any all-frequency result.

## A self-contained additive Fourier calculation for normality

Write F(y)=y^3. The minimal polynomial of F on the m-dimensional F_3
space K is exactly M. Indeed F^m=1. A polynomial of degree <m in F,
if nonzero, is a nonzero ordinary linearized polynomial of degree at
most 3^(m-1), so cannot vanish at every one of the q points of K.
The classical cyclic-vector criterion for an operator whose minimal
polynomial has degree equal to the dimension therefore gives a module
isomorphism K ~= R/(M), R=F_3[T]. A vector is normal precisely when it
generates this module, equivalently when the corresponding residue is a
unit modulo M.

Factor M=product P^e. By the Chinese remainder theorem, K is the direct
sum of V_P=R/(P^e). Write d=deg P. An element of V_P generates that
component iff it lies outside P V_P, an additive subspace of codimension d.
For a finite additive group V and subgroup H of index 3^d,

  1_H(v)=3^(-d) * sum_(psi in H^perp) psi(v).

Thus the generator indicator 1-1_(P V_P) has additive Fourier constant
coefficient 1-3^(-d), and exactly 3^d-1 other nonzero Fourier
coefficients, each -3^(-d). Its Fourier l1 norm equals
2*(1-3^(-d)). Tensoring these component expansions yields the normal
indicator

  Omega(y)=sum_psi c_psi psi(y),
  c_1=Theta,
  sum_psi |c_psi|=Theta*W,
  sum_(psi!=1)|c_psi|=Theta*(W-1).                       (2)

Also sum_y Omega(y)=Theta*q. No squarefree or semisimple assumption is
used: P^e remains present throughout. This is equivalent to the standard
polynomial-Mobius normality character indicator, but proves exactly the
coefficient norm needed here without importing its notation.

## Quadratic products, including the additive twist

For distinct a,b in K put Q(y)=(y-a)(y-b). The untwisted exact sum is

  sum_y chi(Q(y))=-1.                                  (3)

To see this, set c=(a+b)/2, d=(a-b)/2 !=0, x=y-c, so Q=x^2-d^2.
The affine curve z^2=x^2-d^2 is parametrized by

  v=x-z in K*, x=(v+d^2/v)/2, z=(d^2/v-v)/2.

It therefore has q-1 points, whereas its count is
q+sum_x chi(x^2-d^2), proving (3).

For every nontrivial additive character psi, the same parametrization and
sum_x psi(x)=0 give

  sum_y chi(Q(y))*psi(y)
    = psi(c) * sum_(v!=0) psi((v+d^2/v)/2).

The right-hand side is a nondegenerate one-variable Kloosterman sum,
whose absolute value is at most 2*sqrt(q), by the classical Weil bound.
Here both coefficients 1/2 and d^2/2 are nonzero. This is a theorem over
the FIELD of q elements, not a modulus-3^m integer-ring estimate.

Combining (2), (3), and the twisted bound gives, for each such Q,

  sum_y Omega(y)*chi(Q(y))
     >= -Theta - 2*Theta*(W-1)*sqrt(q).                 (4)

The sum is real. One may first bound the absolute value of the
nontrivial-character contribution to justify the displayed lower bound.

## The three-character indicator

For y outside {0,1,-1}, all three characters are signs, and their equality
indicator is exactly

  I(y)=1/4*(1+chi(y*(y-1))+chi(y*(y+1))
                 +chi((y-1)*(y+1))).                  (5)

For m>1 none of 0,1,-1 is normal: their Frobenius conjugates span at
most the one-dimensional constant space. Thus Omega vanishes on all
three exceptional points and (5) may be summed with Omega over ALL K
without any boundary correction. Applying (4) to the three distinct-root
quadratics in (5) proves (1).

## A uniform degree range without field enumeration

There are at most two linear irreducible factors of M (T-1,T+1), so
omega <= floor((m+2)/2). Set U_m=2^floor((m+2)/2).
At m=13, sqrt(q)>6*U_13+1=769, since q=1594323>769^2.
At m=14, sqrt(q)>6*U_14+1=1537, since q=4782969>1537^2.
If sqrt(3^m)>6 U_m+1 then

  sqrt(3^(m+2))=3 sqrt(3^m)>18 U_m+3>12 U_m+1
                                        =6 U_(m+2)+1.

So this holds for every m>=13. It implies
q-3>6*(W-1)*sqrt(q): writing x=sqrt(q), x>6U+1 gives
x^2-6(U-1)x-3 > 7x-3>0.

For m=9,10,11,12 the exact distinct factor counts omega are respectively
1,4,3,3; their W are 2,16,8,8. The integer inequality in the Statement
is directly positive in these four cases. For m=6,7 the counts are 2,2
and W=4,4, and the same inequality is positive. These counts follow
without building the extension field: write m=3^v*n, 3∤n; then
rad(T^m-1)=rad(T^n-1), and

  omega=sum_(d|n) phi(d)/ord_d(3), with ord_1(3)=1.

For example n=10 has divisor contributions 1,1,1,1; n=11 gives 1+2
because ord_11(3)=5; n=4 gives 1+1+1. The complete criterion control
for 3<=m<=14 is recorded below solely to document these arithmetic
claims, not as a new field search:

  m:     3 4 5 6 7 8 9 10 11 12 13 14
  omega: 1 3 2 2 2 5 1  4  3  3  5  4
  pass:  N N N Y Y N Y  Y  Y  Y  Y  Y

## What this proves about the cubic sieve

For a normal y satisfying the filter, let a=1+1/y, b=-1-a.
SC-014 gives for k=3^r+3^s+3^t

  P_k(a)=-(a-1)^k * (y^(3^r)+y^(3^s)+y^(3^t)).

Reduce r,s,t modulo m. The normal conjugates form an independent basis.
The parenthesized sum can vanish only if all three reduced indices
coincide, because a multiplicity 1 or 2 is nonzero in F_3. When all
coincide, k is congruent modulo N to a Frobenius power, an affine
frequency that MUST remain. Thus EVERY nonaffine frequency admitting a
three-Frobenius-power representation is simultaneously excluded by this
ONE seed. Quadratic digitweight frequencies are already excluded by
SC-014. This is genuine simultaneous cubic avoidance, not the invalid
exchange of forall-frequency/exists-seed quantifiers.

At m=3, the constant frequency N=13=1+3+9 is cubic and P_13=3=0
on every valid seed. The identity would give y+y^3+y^9=0, a nonzero
relation among three normal conjugates. Hence no normal y can pass the
filter when m=3: A_3=0. The original good orbit in that field still
exists; normality is merely a sufficient cubic-avoidance device.

Normality ensures F_3(y)=K and hence F_3(a)=K, but the multiplicative
subgroup <a,b> can still be a proper subgroup that spans K additively.
Therefore connectivity requires a SEPARATE argument/certificate. Even a
connected seed avoiding all cubic blockers can fail at higher weights.
Do not claim PM-QUESTION-0001 solved.

## Sources and provenance

Primary sources actually opened/read:

1. H. Hazarika, D. K. Basnet, S. D. Cohen, The existence of primitive
   normal elements of quadratic forms over finite fields,
   arXiv:2001.06977v1 (20 Jan 2020), pages 1-3:
   https://arxiv.org/pdf/2001.06977
   Its normality indicator appears on p.3; the additive-twisted product
   bound is Lemma2.3 on p.4 in the PDF page indexing. Its target is
   primitive normal alpha with a quadratic image primitive, rather than
   this exact equality of three quadratic characters. It establishes
   that the underlying toolkit is classical. No priority claim follows
   from this bounded comparison.
2. Keith Conrad, On Weil's proof of the bound for Kloosterman sums,
   Journal of Number Theory97 (2002), source author's PDF:
   https://kconrad.math.uconn.edu/articles/kloosterman.pdf
   The PDF text extraction is corrupted; page1 was visually inspected.
   Its displayed equation(1) gives |Kl(psi,a)|<=2sqrt(q) for finite
   F_q and nonzero a, exactly the field version needed above.

All novel-looking arguments above are specialized applications of these
classical character/module facts, not a new general normality method.
This note is a manual proof proposal, not human refereeing, Lean, or a
complete historical search.

## Explicit failure mechanisms and next operation

1. Counting all valid y and normal y separately does not prove overlap;
   the mixed character estimate is needed.
2. Assuming semisimple Frobenius breaks when 3|m. The CRT proof retains
   powers P^e, so avoids this failure.
3. Formula(5) fails at 0,±1; weighting by normality removes them exactly.
4. Normal does not imply multiplicative generation/connectivity.
5. Cubic avoidance leaves quartic and higher digitweight frequencies.
6. At m3 constant-frequency collision makes the proposed normal filter
   IMPOSSIBLE, without contradicting good-orbit existence.

Next precise mathematical operation: combine normality with an explicit
multiplicative generation condition for a=1+1/y (or <a,b>) using a
separate primitive-element sieve, checking whether the stronger character
condition is already covered by a primitive-normal rational-image theorem.
Alternatively use the guaranteed normal-filter seed family as input to
the quartic quadratic-obstruction analysis. Do not infer that a generic
character-sum bound already controls every frequency.

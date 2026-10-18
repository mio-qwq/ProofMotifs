# SC-015: normal parameters exist from degree five; quartic obstructions remain

Date: 18 October 2026. Starting research head:
`10c06a57d5b4795c69fec819c832f141a0c8e863`.

The purpose is a simultaneous low-weight spectral sieve for
PM-QUESTION-0001, not another table of positive single-orbit examples.
The general single-orbit existence question remains open.

**PM-THEOREM-0019.** For m>=3, there exists a normal element y of
K=F_(3^m) over F_3 satisfying

`chi(y-1)=chi(y)=chi(y+1) in {1,-1}`

if and only if m>=5. Here normal means that y,y³,...,y^(3^(m-1))
are an F_3-basis of K, and chi is the quadratic character, with chi(0)=0.
Such a y gives a valid square seed

`{1,a,b}`, `a=(y+1)/y`, `b=(y-1)/y`.

This one seed simultaneously excludes every nonaffine frequency that
admits a representation as a sum of three Frobenius powers. It also
excludes all quadratic digitweight frequencies by SC-014. The theorem
does not assert that the seed is connected or generates the full row code.

**PM-THEOREM-0020.** For a valid seed, put h=a-1 and y=1/h. If
k=A_1+A_2+A_3+A_4 with each A_i a power of three, then

`P_k(a)=-h^k*(1+Q(y))`,

`Q(y)=sum_(i<j) y^(A_i+A_j)`.

Thus the quartic badness condition is a K-valued quadratic equation
Q(y)=-1, not a linearized homogeneous kernel. If y is normal and m>=3,
the repetition pattern 2+2 cannot be bad. Triple repetition reduces to
the already excluded quadratic family. The genuine patterns 2+1+1
and 1+1+1+1 remain to be controlled.

All exponents are integer powers in the identities, reduced modulo
N=(3^m-1)/2 only when evaluating on the square group. A representation
can collide with an affine or constant residue; it is not automatically
an extra frequency.

Status: manual proof using classical module, character-sum and polarization
methods, exact small-degree polynomial/witness certificates and independent
AI reviews. Historical novelty is unverified. No human review or Lean
verification is claimed.

**PM-COUNTEREXAMPLE-0009.** In F_6561, a normal parameter passing the
square filter can still give a disconnected insufficient seed. The exact
example in Section 6 has four components and an explicit surviving
four-distinct quartic frequency. It does not refute the stronger possible
criterion involving both normality and connectivity.

## 1. A normal-element character bound

Let q=3^m, H(T)=T^m-1, and let omega count its distinct monic irreducible
factors over F_3. Define

`W=2^omega`, `Theta=product_(P|H)(1-3^(-deg P))`.

If A_m counts the normal elements with the required three characters,
then

`A_m >= Theta/4 * (q-3-6*(W-1)*sqrt(q)).`                 (1)

The statement retains repeated factors of H when 3 divides m.

### 1.1 Normality and additive Fourier mass

Write F(y)=y³ as an F_3-linear operator on K. Its minimal polynomial is
H: F^m=1, and a nonzero polynomial of degree <m in F is a nonzero
linearized polynomial of ordinary degree at most 3^(m-1), too small to
vanish on all q field elements. The standard cyclic-vector criterion
therefore identifies the module K with F_3[T]/(H). Normal elements
correspond exactly to its units.

Factor H=product P^e. The Chinese remainder theorem decomposes this
module into V_P=F_3[T]/(P^e). The nongenerators in V_P form its additive
subspace P*V_P, of codimension d=deg P. By additive character
orthogonality, the local generator indicator has principal Fourier
coefficient 1-3^(-d); its other nonzero coefficients are -3^(-d), one
for each of the 3^d-1 nonprincipal characters annihilating P*V_P.
Its Fourier absolute coefficient sum is 2*(1-3^(-d)). Tensoring gives
the normality indicator Omega with

`Omega(y)=sum_psi c_psi*psi(y)`,

`c_1=Theta`, `sum_(psi!=1)|c_psi|=Theta*(W-1)`,

`sum_y Omega(y)=Theta*q`.

Nothing replaces P^e by P in the module. Only the factor count W and
density Theta use distinct factors. No semisimplicity of Frobenius is
assumed.

### 1.2 The quadratic sums

For distinct u,v in K, let R(y)=(y-u)(y-v). Then

`sum_y chi(R(y))=-1`.

Indeed, after completing the square R=x²-d² with d!=0, the conic
z²=x²-d² has q-1 points, parametrized by t=x-z in K* and
x=(t+d²/t)/2. Comparing this with q+sum chi(R) proves the identity.

For a nonprincipal additive character psi the same parametrization gives

`sum_y chi(R(y))*psi(y)`

` = psi((u+v)/2) * sum_(t!=0) psi((t+d²/t)/2)`.

Both Kloosterman coefficients are nonzero. The classical finite-field
Weil bound for this sum is 2*sqrt(q). This is a theorem over the field
F_q, not over the integer residue ring modulo 3^m. A primary exposition
is Keith Conrad, *On Weil's proof of the bound for Kloosterman sums*,
Journal of Number Theory 97 (2002), equation (1) and Theorem 3:
https://kconrad.math.uconn.edu/articles/kloosterman.pdf.

Using the Fourier mass above, each of the three relevant quadratics obeys

`sum_y Omega(y)*chi(R(y))`

` >= -Theta-2*Theta*(W-1)*sqrt(q)`.

### 1.3 The character filter and endpoints

For y outside {0,1,-1}, equality of the three nonzero signs has indicator

`I(y)=(1+chi(y*(y-1))+chi(y*(y+1))+chi((y-1)*(y+1)))/4`.

When m>1, no element of F_3 is normal. Thus Omega is zero at all
three exceptional points, even though the raw formula for I need not
vanish there in even degree. Summing Omega*I over all of K is exact.
The three quadratic estimates prove (1).

This is a classical normality/character-sum argument specialized to the
exact filter, not a new general character-sum method. The literature
gate compares normal indicators, mixed sums and consecutive primitive
elements without assuming that their separate witness sets intersect.

## 2. A range covering every large degree

A sufficient condition for positivity of (1), checked without floating
point arithmetic, is

`(q-3)^2 > 36*(W-1)^2*q`.

There are at most two linear factors of H, while every other factor has
degree at least two. Hence omega<=floor((m+2)/2). Set
U_m=2^floor((m+2)/2). The integer comparisons

`3^13=1594323 > 769²`, `3^14=4782969 > 1537²`

give sqrt(3^m)>6*U_m+1 at m=13,14. The implication from m to m+2
follows because the left side triples and U_m doubles. This proves
the sufficient condition for every m>=13.

For m=6,7,9,10,11,12 the respective distinct factor counts omega are
2,2,1,4,3,3; substituting in the same integer inequality proves
positivity. These counts are small cyclic-polynomial arithmetic, not
field enumeration. Write m=3^v*n with 3 not dividing n; then

`omega=sum_(d|n) phi(d)/ord_d(3)`, with `ord_1(3)=1`.

This also handles the repeated-factor degrees 6,9,12. For example
T^9-1=(T-1)^9, and n=10 contributes one factor for each divisor
1,2,5,10. Thus the analytic argument covers every m>=9 and also
m=6,7. Only 3,4,5,8 require separate treatment.

## 3. The exceptional and remaining base degrees

### 3.1 Degree three is impossible

For a valid square seed in F_27, N=13=1+3+9 is a constant frequency,
so P_13=0. The SC-014 cubic identity forces
y+y³+y^9=0. These conjugates cannot be independent, so no normal y
satisfies the filter. A good orbit can still exist in this field:
normality is a sufficient device for a cubic sieve, not a necessary
condition for the original row-code problem.

### 3.2 Degree four has a polynomial obstruction

In F_81 the character is the fortieth power away from zero. In F_3[Y]
the exact gcd is

`G=gcd(Y^81-Y,(Y-1)^40-Y^40,(Y+1)^40-Y^40)`

` =Y^18+Y^10+2Y^6+2Y^4+2=G6*G12`,

where

`G6=Y^6+Y^4+Y²+1`,

`G12=Y^12+2Y^10+2Y^4+Y²+2`.

The three zero-character endpoints are not common roots. Exact polynomial
division verifies

`G6 | Y^9-Y`,

`G12 | Y^27-Y^9+Y³-Y`.

The first factor's roots lie in F_9, so are not normal in F_81. The
second factor's roots satisfy the nonzero relation
(F-1)(F²+1)y=0, of Frobenius degree three, so are not normal either.
All filtered parameters are roots of G, proving impossibility. The
standalone coefficient-polynomial verifier recomputes these identities;
a separate coordinate implementation checks all 81 elements and obtains
18 filtered points, none normal. This is an exact negative certificate,
not failure to locate a witness.

### 3.3 Explicit degree-five and degree-eight witnesses

For m=5 use K=F_3[X]/(X^5+2X+1) and y=1+X. Its Frobenius
conjugates have coordinate encodings

`4,28,165,180,228`.

Their rank is five; all three characters are -1. For m=8 use
K=F_3[X]/(X^8+X³+2) and y=1+X+X²+X³. Its conjugates are

`40,922,2525,612,4143,4914,5444,1811`,

of rank eight, again with all three characters -1. The certificate
verifies field irreducibility, these ranks, character powers and the
transformed square seeds with independent ordinary polynomial arithmetic.
These witnesses complete the proof of existence for every m>=5.
Their particular seeds are additionally connected, but that finite fact
is not transferred to the general existence theorem.

## 4. What normality excludes simultaneously

For k=3^r+3^s+3^t, the SC-014 identity is

`P_k(a)=-(a-1)^k*(F^r y+F^s y+F^t y)`.

Reduce indices modulo m. Normal conjugates are independent; a sum of
three of them can vanish only when all three indices coincide, since
multiplicities one and two are nonzero modulo three. In that case k
is a Frobenius frequency. Consequently one normal filtered parameter
rejects every nonaffine cubic-representable frequency at once. This
is a simultaneous statement, not an exchange of existential quantifiers.
All quadratic-representable frequencies were already excluded in SC-014.

Normality implies that y, and hence a, generates K as a field. It does
not imply that a,b generate its square multiplicative group. A proper
multiplicative subgroup can span the full field. Connectivity and all
higher-frequency exclusions therefore remain separate tasks.

## 5. The exact quartic equation

Let A_i=3^(r_i), k=sum A_i. In a=1+h, b=1-h, the odd elementary
symmetric terms cancel. Characteristic three gives

`P_k(a)=-(sum_(i<j) h^(A_i+A_j)+h^k)`

`       =-h^k*(1+sum_(i<j) y^(A_i+A_j))`.

Complementing a pair permutes the six unordered pairs, which justifies
the final expression. Each term is a homogeneous F_3-quadratic monomial
in y. Its K-valued equation need not define a linear subspace.

For the repeated pattern r,r,s,t, direct simplification gives

`Q(y)=(F^r y-F^s y)*(F^r y-F^t y)`.

For r,r,s,s this becomes the square (F^r y-F^s y)². If it equals -1,
put z=F^r y-F^s y; then z^9=z. Thus

`F^(r+2)y-F^(s+2)y-F^r y+F^s y=0`.

If y is normal, independence forces the positive index multiset
{r+2,s} to equal the negative multiset {s+2,r}, modulo m. Coefficient
differences have absolute value at most two, so cannot disappear modulo
three without genuine equality. This requires either r=s, giving z=0,
or m dividing 2, impossible for m>=3. Hence a normal parameter excludes
every 2+2 quartic pattern. If three indices agree, the integer exponent
collapses to a sum of two powers of three, already excluded.

The 2+1+1 and four-distinct patterns are not thereby eliminated. Neither
normality nor the analytic existence count proves a good full-code orbit.

## 6. A normal filtered parameter with a surviving quartic frequency

Use K=F_3[X]/(X^8+X³+2), gamma=X², N=3280. In ascending base-three
coordinate encoding take

`y=4863=X+2X^5+2X^7`,

`a=4783=1+X+2X^4+X^5+2X^7`,

`b=2761=1+2X+X^4+2X^5+X^7`.

The coordinate determinant of the eight Frobenius conjugates of y is
2, so y is normal. All three characters at y-1,y,y+1 are -1.
The checker verifies ay=y+1, by=y-1, 1+a+b=0 and a^N=b^N=1.
The vertices are distinct, and

`a=gamma^76`, `b=gamma^2368`, `gcd(76,2368,3280)=4`.

Thus the seed has four components. Normality implies F_3(y)=K;
since y=1/(a-1), also F_3(a)=K. The subgroup generated by a,b
therefore spans the full field. The component theorem of SC-013 gives
sparse kernel dimension at least 4*(8+1)=36, while the full square
hypergraph has dimension nine. Equality with 36 is not needed or claimed
as independently certified here.

The four-distinct quartic exponent is

`k=1+9+81+729=820`.

Direct arithmetic gives Q(y)=2=-1 and a^820=b^820=1. Its frequency
orbit {820,2460} is disjoint from the affine spectrum. The function
f(u)=Tr_(K/F3)(u^820) obeys every scaled seed equation because

`sum_(u in tE) f(u)=Tr(t^820*(1+a^820+b^820))=0`.

A genuine square edge is gamma^[0,2,1672]={1,81,164}. Its f-values
are 2,1,2, summing to two. This explicitly exhibits a missing constraint.
The symbolic trace identity covers all 3280 seed translates; their
equations were not individually enumerated. A standalone coordinate
implementation verifies the field, normal determinant, square filter,
seed powers, quartic equation and separating edge. A separate arithmetic
audit checks the same witness.

This is a boundary for normality alone. Its index-four disconnectedness
is essential: it is not a connected counterexample to normality plus
connectivity, nor a counterexample to existence of some good orbit.

## 7. Research decision

The normal route is now a proved simultaneous cubic sieve with exact
degree-three/four obstructions. Its analytic tools are classical, and
the full all-degree packaging has not been certified historically new.
The remaining task is to enforce multiplicative connectivity and to
control the genuine quartic and higher obstructions. Compare primary
primitive-normal rational-image results before adding a second sieve;
do not assume that normality and a separate primitive-element theorem
choose the same parameter. PM-QUESTION-0001 remains open.

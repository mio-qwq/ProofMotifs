# SC-014: a linearized spectral sieve and an odd-degree connected failure

Date: 18 October 2026. Starting research head:
`e19781a36e1267f1850751cc4a9ad18e025588f3`.

PM-QUESTION-0001 remains open. The results below remove explicit frequency
families from its simultaneous-avoidance problem, then use the remaining
cubic family to construct a connected bad orbit in odd degree 13. Thus the
positive odd-degree observations in degrees 3,5,7 do not justify an
odd-degree sufficiency theorem. No complete degree-13 orbit scan is used.

**PM-THEOREM-0018 (classical spectral sieve).** Let K=F_(3^m), m>=3,
S=(K*)², N=(3^m-1)/2. For a valid normalized seed E={1,a,b}, with
b=-1-a and three distinct elements in S, put P_k(a)=1+a^k+b^k.
All exponents are ultimately read modulo N on S.

1. If k=3^r+3^s, every valid seed has P_k(a)!=0.
2. If k=3^r+3^s+3^t, put G(T)=T^r+T^s+T^t in F_3[T],
   D=gcd(T^m-1,G), and c=deg D. The bad parameters are exactly
   a=1+1/y, where y belongs to the c-dimensional kernel of
   L(y)=y^(3^r)+y^(3^s)+y^(3^t), y not in {0,1,-1}, and
   chi(y-1)=chi(y)=chi(y+1). In particular there are at most 3^c-3
   bad normalized parameters. If D divides T^d-1 for a proper divisor
   d of m, every bad seed is disconnected.
3. Every bad-parameter set B_k has cardinality divisible by six.
   A positive even lift e of k with at most six roots of
   (x+1)^e+x^e=-1 forces B_k empty. A positive odd lift with at most
   eight roots of (x+1)^e-x^e=1 also forces B_k empty.

Repeated powers in item 2 are allowed and their coefficients are reduced
modulo three. These are criteria about particular frequency families;
they do not control all residues. A cubic representation can be an affine
or constant frequency, so it must not automatically be called extra.

**PM-COUNTEREXAMPLE-0008.** Over

`K=F_3[X]/(X^13+2X+1)`, `q=1594323`, `N=797161`,

there is a connected valid seed E whose kernel has dimension at least
27, whereas the full square hypergraph has dimension 14. An explicit
nonaffine sparse-kernel function is Tr_(K/F3)(u^85). This refutes the
project's provisional odd-degree sufficiency route, not the existence of
some good orbit in every degree. The exact sparse kernel dimension is
not asserted to equal 27.

Status: manual proofs, exact polynomial/field identities and independent
AI proof and arithmetic reviews. Quadratic polarization, linearized
polynomials, differential uniformity and cyclic-code methods are classical.
Historical originality, human review and Lean verification are unestablished.

## 1. Quadratic and cubic identities

Put h=a-1. In characteristic three, a=1+h and b=1-h. Write A=3^r,
B=3^s. Frobenius and expansion give

`P_(A+B)(a)=1+(1+h^A)(1+h^B)+(1-h^A)(1-h^B)`

`             =-h^(A+B)!=0`.

This proves item 1 without a differential-uniformity assumption.

With C=3^t and k=A+B+C, the two cubic products give

`P_k(a)=-(h^(A+B)+h^(A+C)+h^(B+C))`

`      =-h^k*(y^A+y^B+y^C)`, where `y=1/h`.

The substitution is injective and has inverse a=(y+1)/y. Also
b=(y-1)/y. Both are nonzero squares exactly when the three nonzero
characters chi(y-1), chi(y), chi(y+1) agree. The excluded y-values
0,1,-1 correspond respectively to no finite parameter, a=-1, a=0.

For the repeated-power case k=2*3^u+3^v, inverse Frobenius reduces
the identity to

`P_(2+3^j)(a)=(a-1)*(a^(3^j)-a)`.

If u and v differ modulo m, badness forces a,b into the proper subfield
F_(3^gcd(v-u,m)), so a connected seed excludes that frequency. If they
coincide modulo m the frequency is Frobenius and must be retained.

## 2. Kernel dimension without a squarefree assumption

For a polynomial A(T)=sum A_i*T^i over F_3, write
`L_A(Y)=sum A_i*Y^(3^i)`. These satisfy
L_(A+B)=L_A+L_B and L_(AB)=L_A composed with L_B. Let H=T^m-1,
so L_H(Y)=Y^q-Y. Its operator on K is zero.

Let D=gcd(H,G), chosen monic. A polynomial Bezout identity D=U*H+V*G,
together with G=D*G1, shows that ker L_G on K is exactly ker L_D.
Because D divides H, D has nonzero constant coefficient. Thus L_D has
degree 3^c and nonzero derivative D(0); it has exactly 3^c distinct roots
in an algebraic closure. Writing H=D*H1 shows that every such root also
annihilates L_H, hence belongs to K. The kernel is F_3-linear and has
dimension c. This proof remains valid when 3 divides m and H has repeated
factors; semisimplicity of the Frobenius operator is not assumed.

Every constant y in F_3 is in this kernel because G(1)=3=0. Removing
these three invalid values proves the bound 3^c-3. In particular c=1
gives no valid bad parameter.

If D divides T^d-1, every root of L_D satisfies y^(3^d)=y. Hence
y,a,b belong to F_(3^d). If d is a proper divisor of m, its nonzero
multiplicative group is smaller than S, so <a,b> cannot equal S.
SC-013 then rules out a sufficient single orbit.

One useful boundary is k=1+3^r+3^(2r): its operator is
L=(F^r-1)^2, so roots lie in F_(3^gcd(3r,m)). This excludes connected
bad seeds only if gcd(3r,m)<m. When m divides 3r the argument stops;
relative trace/norm behavior can occur. For m=3,r=1 the exponent is
N=13, a constant frequency, illustrating why blanket exclusion is false.

## 3. Six normalizations and differential fibers

Let A be the valid normalized parameter set. The transformations
s(a)=-1-a and t(a)=1/a preserve A: the second replaces b by b/a,
which is again square. They generate the six re-normalizations of an
unordered triple. They also preserve B_k, since
P_k(1/a)=a^(-k)*P_k(a) and interchanging a,b changes nothing.

This S_3 action is free. The transposition fixed points are conjugates of
a=1 or solutions a²=1, all excluded; the three-cycle equation is
a²+a+1=(a-1)²=0, again excluded. Therefore |B_k| is a multiple of six.

For a positive even lift e of k, badness is
(a+1)^e+a^e=-1. The unrestricted equation already has the invalid
root x=1. If it has at most six roots, a nonempty six-element B_k is
impossible. For an odd lift, the equation is (a+1)^e-a^e=1, with
the three invalid roots 0,-1,1; at most eight unrestricted roots likewise
leave fewer than six valid roots. Low differential-uniformity theorems
can supply such fiber bounds, with the parity and exact equation checked.
The argument uses the stated fiber only, so a global maximum bound is
sufficient but not necessary.

The prior-art gate records the exact overlap with ternary cyclic
minimum-distance equations and c-differential literature. It does not
mistake those theorems for a sparse cyclic-generator existence theorem.

## 4. A targeted odd-degree construction

Choose m=13 and the cubic frequency k=1+3+81=85. The symbol is
G=1+T+T^4, and direct polynomial division gives

`gcd(T^13-1,G)=G=(T-1)*(T^3+T^2+T+2)`.

Thus ker(y+y³+y^81) has dimension four. Unlike the preceding proper-
subfield case, it is not confined to a proper subfield of F_(3^13).
The only proper subfield is F_3, and G does not divide T-1.

The chosen field polynomial X^13+2X+1 is proved irreducible by Rabin:
X^(3^13)=X modulo it, and gcd(X³-X, X^13+2X+1)=1. Since 13 is
prime, this is the complete proper-degree exclusion. Trial division of
N through floor(sqrt(N))=892 proves N is prime.

In this field set

`y=X²+X³+X^9`,

`a=2X^5+2X^11+X^12`,

`b=2+X^5+X^11+2X^12`.

Exact reductions verify

`y+y³+y^81=0`, `a*y=y+1`, `b*y=y-1`,

`a^N=b^N=1`, `1+a+b=0`, `1+a^85+b^85=0`.

The vertices are distinct and nonzero. Since a!=1 belongs to the
prime-order group S, it generates S. The seed is therefore connected.

An explicit basis of the four-dimensional root space is

`1`, `X+2X³+X^5`, `X+X^6`, `X²+X³+X^9`.

The certificate verifies its independence and all 81 linear combinations.
Every one of its 78 elements outside F_3 passes the square filter. By
the identity in Section 1, this is the complete B_85 parameter set, not
merely a sample. It is not a classification of all bad frequencies or
all seed orbits in this field.

There is also a structural explanation for why one successful parameter
forces all 78 to pass. The 78 transformations

`y -> epsilon*y^(3^j)+c`, `epsilon in {1,-1}`, `0<=j<13`, `c in F_3`,

form a group preserving U=ker L and its subset U minus F_3. Its action
on K minus F_3 is free. Indeed, if y^(3^j)+c=y and j!=0, iterating
13 times gives 13c=c=0; then y is fixed by a nontrivial power of
Frobenius and lies in F_3, since 13 is prime. For j=0 only c=0
fixes a point. If -y^(3^j)+c=y, squaring this transformation gives
y^(3^(2j))=y. For j!=0 this again forces y into F_3; for j=0 the
original equation does so directly. Thus only the identity can fix an
element outside F_3. Since U minus F_3 has exactly 78 elements, it
is a single orbit of this group.

The square filter is invariant: translation by F_3 permutes the three
arguments y-1,y,y+1; negation multiplies all their characters by the same
chi(-1); and Frobenius preserves each character value. Therefore checking
the single displayed y proves that all 78 nonconstant kernel elements
pass. The complete finite check independently corroborates this orbit
argument. This specialized transitivity uses both prime degree 13 and
the equality 3^4-3=78; it is not asserted for arbitrary linearized kernels.

The six seed re-normalizations group these 78 parameters into 13
multiplicative edge orbits. In y-coordinates the two generators a -> -1-a
and a -> 1/a become y -> -y and y -> -y-1. Thus re-normalization is exactly
the six-element subgroup y -> epsilon*y+c. Factoring the transitive
78-element action by this subgroup leaves the order-13 Frobenius action,
so all 13 seed orbits form one Frobenius orbit. Direct field arithmetic
independently checks the same partition. This is complete for B_85 only.

## 5. The missing equations and a lower bound, not an exact rank

The orbit of 85 under multiplication by 3 modulo N is

`85,255,765,2295,6885,20655,61965,185895,557685,`

`78733,236199,708597,531469`.

It has length 13 and is disjoint from the affine frequencies
`0,1,3,...,3^12`. Each of these 13 extra characters annihilates every
scaled copy of E. Scalar extension of the incidence matrix preserves
kernel dimension; the distinct characters u^j on S are independent
because a nonzero polynomial of degree <N cannot vanish on all N points.
The constant character, 13 affine characters and 13 extra characters
therefore give a sparse kernel of dimension at least 27 over F_3.
SC-009 gives dimension 14 for the full hypergraph. No upper bound proving
exactly 27 is claimed.

Concretely let f(u)=Tr_(K/F3)(u^85). For any t in S,

`sum_(u in tE) f(u)=Tr(t^85*(1+a^85+b^85))=0`.

Another true square edge is {1,a',b'}, where

`a'=1+X+X³+X^4`, `b'=1+2X+2X³+2X^4`.

Its f-values are 1,1,0, with sum 2. Hence f is not an affine restriction:
an affine restriction sums to zero on every zero-sum triple. The universal
trace identity covers all 797161 scaled sparse edges; these were not
individually enumerated. The certificate checks the root identity and the
explicit separating edge directly.

## 6. Research decision and limits

This construction arose from a degree-four Frobenius-symbol gcd and an
81-element linear kernel, not a sweep through all 1594323 field elements.
The small m=7 census was a control for an explicit odd-degree hypothesis;
it did not justify that hypothesis. The degree-13 example now refutes it.

The general existence problem is still open. A useful next operation is to
combine the proven empty bad sets with the exact linearized B_k for cubic
frequencies, then control higher digit weights or derive a genuine
all-frequency covering obstruction. The 78 parameters of B_85 do not show
that all seeds are bad. More positive degree tables alone do not answer
that question. Sources, manual proof, exact computation, independent AI
review, human review, Lean and priority remain separate.

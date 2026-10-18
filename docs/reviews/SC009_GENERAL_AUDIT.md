# PM-CYCLE6-E independent adversarial audit

Reviewer: actual task-scoped AI researcher /root/weil_completion_review.
Date: 2026-10-18. Scope: mathematical correctness of SC-009 Section 6 and its
implication for the SC-008 quotient conjecture. Read-only research checkout;
no shared research files edited or pushed. Historical novelty is not assessed.

## Verdict

ACCEPT the stated general proof for q=3^m >=243. No algebraic gap, missing
sign, characteristic-three degeneracy, or unproved extension step remains.
The q=27 and q=81 incidence-rank bases were independently recomputed with a
separate short modular row-elimination loop using the existing exact field
class. The general quotient classification therefore follows for all m>=3,
conditional only on the explicitly invoked classical Weil and Carlitz theorems
and the finite exact linear-algebra base cases. This is not a Lean certificate.

## Four-edge identity and all repeated cases

Suppose u+v=w+z, with all four elements in S. If u=w or u=z, the multisets
{u,v} and {w,z} agree, so the desired f identity is immediate. Otherwise set
b=-u-a, c=-w-a, d=u+a-z. Then
u+a+b=w+a+c=b+z+d=c+v+d=0.
Subtracting the first two f equations gives f(u)-f(w)=f(c)-f(b).
Subtracting the last two gives f(z)-f(v)=f(c)-f(b). These imply
f(u)+f(v)=f(w)+f(z).

An important characteristic-three point: no parameters need exclusion because
one of these triples has repeated entries. If x+x+y=0 then y=-2x=x;
all three entries coincide, and its equation is 3f(x)=0 automatically.
Thus edge equations extend to every zero-sum ordered triple of S.

The four affine forms a,-u-a,-w-a,u+a-z have roots
0,-u,-w,z-u. Their six possible collisions are:
* 0=-u or 0=-w: forbidden original zero vertex;
* 0=z-u: u=z, a trivial relation;
* -u=-w: u=w, a trivial relation;
* -u=z-u: z=0, forbidden;
* -w=z-u: z=u-w, and then u+v=w+z=u, so v=0, forbidden.
This explicitly covers every collision, including u=v or w=z.

## Character count

Extend the quadratic character chi by chi(0)=0. For affine forms ell_i with
four distinct roots define P(a)=product_i(1+chi(ell_i(a))). Away from their
roots, P/16 is exactly the indicator that all four forms are nonzero squares.
At any root exactly one factor equals1; the other three are each0 or2, so
0<=P<=8. Consequently deleting all four roots subtracts at most32 from sum P.

Expand sum P over all subsets of the four forms. The empty term contributesq;
each singleton sum is0. For two distinct affine roots, the product is a
nonzero scalar times a monic squarefree quadratic, whose character sum is
minus the character of its leading coefficient. Thus every pair sum has
absolute value1. Every three-factor product is squarefree of degree3, and
the four-factor product is squarefree of degree4. The standard multiplicative
Weil bound gives absolute values at most2sqrt(q) and3sqrt(q), respectively.
Nonmonic factors cause only a unit-modulus character scalar. These are
multiplicative character sums of order2; there is NO assumption that degree
be coprime to characteristic3. Distinct roots guarantee squarefreeness,
even for a cubic in characteristic3.

Hence N4 >= (q-6-8sqrt(q)-3sqrt(q)-32)/16
          = (q-38-11sqrt(q))/16.
For q=243 its numerator is positive (sqrt243<16 gives243-38-176=29>0).
The function q-38-11sqrtq increases for q>=243, so positivity holds for all
larger q. The affine slopes are1,-1,-1,1. Their quadratic signs are1,eta,eta,1,
eta=chi(-1). The exact six-pair contribution is -6 if eta=1 and +2 if eta=-1;
the uniform bound -6 is valid for either parity of m. No missing eta factor
can invalidate the conservative bound.

A first-party seminar source explicitly states this exact multiplicative
Weil version in Theorem3.2: DominiqueGuillot, IISC Bangalore eigenfunctions
seminar notes, https://dominiqueguillot.github.io/iisc-eigen.pdf, p12.
Freshly read on2026-10-18 via web ref turn49view2, lines1093-1125.
Its theorem allows any nonzero scalar times a monic polynomial with d distinct
roots which is not a square; our nonempty squarefree products satisfy it.

## Difference representation and extension

For x!=0, N2(x)=|{b:b,b+x in S}| can be evaluated exactly:
N2(x)=(q-3-(1+eta)chi(x))/4.
Indeed sum(1+chi(b))(1+chi(b+x))=q-1; removing b=0,-x subtracts
2+(1+eta)chi(x). This is positive for everyq>=9. The difference0 has the
obvious representations. Thus S-S=K.

Define L(x)=f(a)-f(b) whenever a-b=x. If also c-d=x, then a+d=c+b;
the established Freiman equation proves representation independence.
It immediately gives L(0)=0 and L(-x)=-L(x).

For x,y,x+y allnonzero, the three forms b,b+x,b+x+y have distinctroots.
Expanding their indicators yields q from the emptyterm,0 fromsingletons,
-3 exactly fromthe three pairterms, and at least-2sqrtq fromthe cubic.
Each of thethree roots contributes at most4 beforedeletion. Hence
N3 >= (q-15-2sqrtq)/8 >0 forq>25, inparticularq>=27.
Choose suchb. Then
L(x+y)=f(b+x+y)-f(b)
      =[f(b+x+y)-f(b+x)]+[f(b+x)-f(b)]
      =L(y)+L(x).
If either argument is0 the identity is immediate; ifx+y=0 use antisymmetry.
Thus L is additive and therefore F3-linear. For u,b inS,
f(u)-f(b)=L(u-b)=L(u)-L(b), so f(u)=L(u)+c onS.

Conversely every affine F3-valued restriction satisfies theedgeequations.
Restriction is injective becauseS-S=K, hence this spacehasdimensionm+1.
This proves dimkerM=m+1 for everym>=5.

## Independent finite bases

Using existingexact Field arithmetic but a separate simple Python rowloop,
I obtained:
q9: vertices4,edges0,rank0,nullity4;
q27: vertices13,edges13,rank9,nullity4;
q81: vertices40,edges120,rank35,nullity5;
q243: vertices121,edges1210,rank115,nullity6.
These are exact integer operations modulo3, without float ranks or heuristic
search. The q9 row shows the incidence kernel is NOT generally affine there;
the necessary exception is retained.

## Classification step audited independently

For an automorphism pi:S->S, each coordinate of pi belongs to the incidence
kernel. Under dimkerM=m+1, coordinatewise affine extensions give
F(x)=A(x)+t with A:F3-linear. Injectivity onS implies A is invertible:
otherwise |F(S)|<=q/3<|S| forq>3. Since S is a multiplicative subgroup of
size>1, sumS=0; and |S|=(q-1)/2 is1 modulo3. Summing F over S forces t=0.
Then A permutes squares and nonsquares, so forx!=y,
chi((A(x)-A(y))/(x-y))=1. Its slope set is contained in S.

This is precisely the d=2 case of classical Carlitz. Freshly inspected
primary research source: Csajbok, Extending a result of Carlitz and McConnel
to polynomials which are not permutations, FiniteFieldsAppl108(2025)102683,
Result1.1; authorPDF
https://real.mtak.hu/225482/1/Extending%20a%20result%20of%20Carlitz%20and%20McConnel%20to%20polynomials%20which%20are%20not%20permutations.pdf
webrefs turn49view1/turn50view0, lines51-66.
It gives A(x)=s*x^(3^j), s inS, with no extra finite-field-size assumption.
Since A(0)=0, thetranslation inthat classical conclusion iszero.
Converse preservation is immediate. Distinct j modulo m and s give distinct
restrictions because S-S=K. Thus |Aut(H)|=(q-1)m/2 for allm>=3.
The full ternary orderpreserver is the previously proved sign-kernel
semidirect product. The small m=2 exception is Aut(H_F9)=S4; m=1 must be
kept separately because the original ternary label is entirely degenerate.

## Limits

Correctness of this specific route is accepted. This review makes NO claim
that the incidence-kernel extension theorem or resulting hypergraph
classification is historically new. Neither character sums, Freiman
extension, incidence-code reconstruction nor Carlitz is a new method here.
No human review or formalization occurred. The independent finite check
shares existing field arithmetic and should be described accurately.

## Published primary character-bound source additionally checked

Kim--Yip--Yoo, Explicit constructions of Diophantine tuples over finite
fields, RamanujanJournal65(2024)163--172, DOI10.1007/s11139-024-00888-5,
Lemma2.1 states precisely the multiplicative character bound used here.
I independently opened and read the published source on2026-10-18:
https://link.springer.com/article/10.1007/s11139-024-00888-5
webrefs turn63view0/turn63view1 lines98-102. A nonzero scalar times each
monic squarefree split product meets every hypothesis. Lemma2.2 also records
the classical prescribed-character-pattern estimate, reinforcing that this
counting technology is established prior art.

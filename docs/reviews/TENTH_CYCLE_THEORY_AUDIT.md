# PM-CYCLE10-A: low ternary digitweight and power-image exclusions

Date: 18 October 2026. Research-only handoff; no repository files changed.
Starting material read: SC-009/FOURIER_PROOF.md, SC-013/RESULTS.md,
research/literature/SINGLE_ORBIT_GATE_20261018.md.

These are elementary spectral exclusions, not a solution of PM-QUESTION-0001.
Quadratic and repeated-cubic identities were derived independently before
coordinator feedback. The coordinator then proposed the general cubic
linearized identity; this note independently verifies it, including the
possibly inseparable cyclic-polynomial case, and develops bounds and limits.
No historical novelty, human review or formal verification is asserted.

## Set-up and valid seeds

Let K=F_(3^m), m>=3, S=(K*)^2, N=(3^m-1)/2. A valid normalized seed is
E={1,a,b}, where a,b in S, b=-1-a, and 1,a,b are distinct. Thus a is not
0,-1,1. Set P_k(a)=1+a^k+b^k. Frequency k is taken modulo N.
The seed is connected when <a,b>=S. By SC-013, connectivity is necessary
for a single orbit to span the full row code.

Power-of-three exponents can always be reduced modulo m when applied to
field elements. Thus identities with exponent sums apply whenever the
frequency residue has the indicated power-of-three representation.

## 1. Every valid seed excludes every quadratic digitweight frequency

For A=3^r and B=3^s, write a=1+h and b=1-h. Frobenius gives

P_(A+B)(a)
 =1+(1+h^A)(1+h^B)+(1-h^A)(1-h^B)
 =-h^(A+B).

Since h!=0, this is nonzero. Repetitions r=s are allowed. Hence none of
these frequencies can be an extra kernel frequency for ANY valid seed.
This removes an infinite family from a simultaneous-avoidance argument.

## 2. Repeated cubic digitweight frequencies have only subfield bad seeds

For Q=3^r, direct expansion gives

P_(Q+2)(a)=(a-1)(a^Q-a).

If a!=1, vanishing is equivalent to a in F_(3^gcd(r,m)). After applying
inverse Frobenius, the same statement holds for
k=2*3^u+3^v: badness is equivalent to a in F_(3^gcd(v-u,m)).
When u!=v modulo m this is a proper subfield. Then b=-1-a is in that
same proper subfield, so <a,b> is proper in S. Therefore every connected
seed excludes all repeated-cubic frequencies with u!=v modulo m.
When u=v modulo m the frequency is Frobenius, and must not be excluded.

The properness assertion uses |S|=(3^m-1)/2>3^d-1 for every proper
subfield F_(3^d) of K: d<=m/2 and m>=3.

## 3. General cubic digitweight is a linearized root-space problem

Let A=3^r, B=3^s, C=3^t and k=A+B+C, allowing repeated powers. With
h=a-1!=0 and y=h^(-1), expand the two products:

P_k(a)
 =1+(1+h^A)(1+h^B)(1+h^C)
     +(1-h^A)(1-h^B)(1-h^C)
 =-(h^(A+B)+h^(A+C)+h^(B+C))
 =-h^k*(y^A+y^B+y^C).

Thus badness is exactly L(y)=0 for the F_3-linear operator
L=F^r+F^s+F^t, where F(y)=y^3. The map a -> y=1/(a-1) is injective.

Let

c=deg gcd(T^m-1,T^r+T^s+T^t) in F_3[T].

A normal basis makes K a cyclic F_3[T]-module F_3[T]/(T^m-1), with
T acting as F. Multiplication by G=T^r+T^s+T^t has kernel dimension c.
This remains true if 3 divides m: squarefreeness is NOT required.
Indeed, with D=gcd(H,G), H=T^m-1, write H=D*H1, G=D*G1 and
gcd(H1,G1)=1. The congruence G*f=0 mod H is equivalent to H1|f;
the solutions f=H1*u modulo H are parametrized by u modulo D.

The root space always contains F_3, because L(c0)=3*c0=0 for c0 in F_3.
Of these roots, y=0 has no finite seed and y=1,-1 give a=-1,0,
respectively, which are invalid. Therefore the number of valid normalized
bad seeds is at most

3^c-3.

This bound ignores the two square conditions, so may be strict. In
particular, if gcd(T^m-1,G)=T-1, there are no valid bad seeds at all.
The criterion excludes a frequency for every valid seed, without choosing
seeds individually. It is therefore safe to combine with simultaneous
avoidance, unlike a separate existential rejection of each frequency.

For repeated powers this recovers Section 2: G=2*T^u+T^v=T^v-T^u,
and its kernel is the corresponding fixed subfield.

## 4. Arithmetic-progression cubic exponents and a real boundary

For k=1+3^r+3^(2r),

L=1+F^r+F^(2r)=(F^r-1)^2.

Every root of L also satisfies (F^(3r)-1)y=0. Hence all bad seed
parameters a lie in F_(3^gcd(3r,m)). If gcd(3r,m)<m, every such seed is
disconnected, and connected seeds exclude this frequency.

Do not silently extend this conclusion to m|3r. If m=3g and r=g, then
k=1+3^g+3^(2g) is the norm exponent to F_(3^g). The operator L is the
relative trace K -> F_(3^g), with kernel dimension 2g. Its bad parameter
space can span K, so the proper-subfield argument has genuinely stopped.
The square conditions and generation requirement must be treated afresh.

For example, m=3,r=1 gives k=N=13, the constant frequency, and indeed
all valid seeds are bad. This prevents a false blanket assertion that
all cubic digitweight frequencies are excluded. For m=6,r=2 the image
has order four, which Section 5 excludes by a separate argument; the
linearized bound alone does not capture that exclusion.

## 5. A power-image obstruction for connected bad seeds

Let k not congruent to zero modulo N and let L0=N/gcd(N,k)>1. The power
map x -> x^k sends S onto mu_(L0). If a connected seed is bad, then
{1,a^k,b^k} is a distinct zero-sum triple generating mu_(L0).

To prove distinctness, if any two entries coincide, the equation forces
all three entries to equal 1 (characteristic three). Then a^k=b^k=1;
as a,b generate S the power map is trivial, contradicting L0>1. Generation
of the image follows because images of generators generate the image.

Consequently, every connected seed excludes any frequency whose image
group admits no connected distinct zero-sum triple. In particular:

* L0=2: a two-element group has no distinct triple.
* L0=4: with i^2=-1, the only nontrivial candidates x=+-i give
  y=-1-x with y^4=-1, so y is not in mu_4; x=-1 gives y=0.
* L0=p>=5 prime and ord_p(3)=p-1: Phi_p=1+T+...+T^(p-1) is irreducible
  over F_3. A relation 1+zeta^i+zeta^j=0 with distinct exponents would
  make Phi_p divide a nonzero polynomial of degree at most p-1 and with
  exactly three nonzero coefficients. This is impossible, since a scalar
  multiple of Phi_p has p nonzero coefficients.

Examples of the last condition include p=5 and p=7. No unproved statement
about infinitely many such primes is used. This is an obstruction, not a
classification of image groups admitting connected triples.

## 6. Scope and precise next lemma

These results eliminate selected frequency families for all seeds, or for
all connected seeds. They do not address all frequency residues, and do
not prove existence of one good seed in every degree. In particular,
high ternary digitweight frequencies are not bounded here. The known
connected F_729 extra frequency 34 has ternary digitweight four, consistent
with all the exclusions above.

The cubic identity gives a useful exact next step: for each residual cubic
Frobenius orbit, analyze the square-restricted rational image of ker L
under y -> 1+1/y, and its subgroup generation. A simultaneous union bound
using 3^c-3 would be valid only after also bounding every higher-weight
frequency family. Summing the cubic bounds alone cannot resolve the
original question.

All derivations above are symbolic; no new positive-instance enumeration
was performed. Independent low-degree polynomial verification by the
coordinator or a separate reviewer is appropriate before integration.

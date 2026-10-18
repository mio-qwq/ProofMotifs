Archive note: the first section records the initial read-only exploration. The later degree-13 result was subsequently integrated into the three assigned SC-014 files and independently accepted; see TENTH_CYCLE.md. Temporary paths below identify the original scratch commands, not durable delivery locations. The bounded m6/m7 exploration is not an all-degree theorem.

# PM-CYCLE10-B computation and interpretation

Scope: repository read only; own `/tmp` scripts and generated JSON. No shared
edits, commits, refs or external messages. All arithmetic is exact in F3.

## Initial bounded task

Command: `python /tmp/pm_cycle10_b_cover.py --output /tmp/pm_cycle10_b_cover.json`

The complete m6 and m7 multiplicative edge-orbit censuses contain 30 and 91
orbits. Every gcd degree is checked three ways: pre-existing bitplane Euclid,
direct field-root enumeration, and a newly written ordinary coefficient-list
Euclid in this script. The field representation and orbit normalization use
the pre-existing repository code; this is not wholly independent field code.

All 91 m7 seeds are connected and have nullity8. This finite result does not
prove any odd-m assertion. The three connected m6 bad seeds are
`{0,25,311}`, `{0,75,205}`, `{0,26,139}`. They form one Frobenius seed orbit
of length3 and all share precisely the extra frequency orbit
`{34,102,306,190,206,254}`. Thus the 21 connected m6 seeds have a single
nonempty forbidden-factor blocker, supported on exactly3 of them. This
blocker does not cover the other18 seeds.

General explanation for spectral invariance along Frobenius seed orbits:
cubing all seed exponents replaces p(Z) by p(Z)^3 modulo Z^N-1, while
normalizing the seed multiplies by a monomial. On Nth roots, neither operation
changes its zero set. This is an identity, not an experimental inference.

An algebraic explanation of the m6 triple is available. Normalize its
F27-conjugate pair as E={1,u,v} with v=u^27 and u+v=-1. Writing n=uv gives
`u^34+v^34=n*(u^6+v^6)=n*(1+n)^3`. Hence the k34 obstruction is
`n^4+n+1=(n-1)*(n^3+n^2+n+2)=0`. The root n=1 is the degenerate seed.
The remaining cubic is irreducible over F3 and has three conjugate roots
in F27. Their norm is1, while Norm(1-n)=2, so n is square and 1-n is
nonsquare in F27. The quadratic T²+T+n consequently has two distinct roots
in F729, both square there. In the displayed primitive-gamma presentation,
the pair representatives u exponents25,75,225 give the three orbit classes
(the third class requires normalization at the vertex gamma^139).

## Targeted degree13 test requested after the initial census

Command: `python /tmp/pm_cycle10_b_degree13.py --output /tmp/pm_cycle10_b_degree13.json`

This is independently implemented coordinate-polynomial field arithmetic:
no imports from project code, no full power/log table, no order-N gcd.

Result: the conjecture that every connected seed works when m is odd is
false already at the explicit checked degree13. We do not claim degree13
is the first odd failure. The field and seed are

* K=F3[X]/(X^13+2X+1), q=1594323, N=797161.
* N is prime by integer trial division through floor(sqrt(N))=892.
* The modulus is irreducible by the prime-degree Rabin criterion:
  X^(3^13)=X modulo the modulus and gcd(X³-X,modulus)=1.
* alpha=X is primitive: alpha^(2N)=1, alpha^N=2, alpha² !=1.
* y=X²+X³+X9.
* a=2X5+2X11+X12, b=2+X5+X11+2X12.

The program verifies y+y³+y81=0, a=(y+1)/y, b=(y-1)/y, and
1+a+b=1+a85+b85=0. It also verifies a^N=b^N=1. The three vertices are
distinct. Since N is prime, a!=1 alone implies <a,b>=S, so the seed is
connected.

Root's/A's linearized identity supplies the symbolic mechanism:
for h=a-1, y=1/h and k=1+3+81=85,
`1+a^k+(-1-a)^k=-h^k*(y+y³+y81)`.
This script verifies the resulting field identity, but the proof is not
attributed to this computation task.

The F3 matrix of L(y)=y+y³+y81 has nullspace dimension4, with basis

1; X+2X³+X5; X+X6; X²+X³+X9.

All81 kernel elements are checked; all78 outside F3 give valid square
seeds. This latter count is an exact finite arithmetic result; no conceptual
proof of its uniformity beyond this field is claimed.

The k85 Frobenius orbit modulo N is
85,255,765,2295,6885,20655,61965,185895,557685,78733,236199,708597,531469.
It has length13 and is disjoint from {0} and the affine k1 orbit. Thus the
extra trace family Tr(c*u85), c in K, supplies13 independent additional
kernel functions. Independence follows by evaluating distinct monomial
characters on the Nth roots: a nonzero polynomial of degree<N cannot
vanish at all N points. Therefore the sparse kernel dimension is at least
27, whereas the complete kernel is14. **No exact dimension27 is claimed.**

The explicit nonaffine witness is f(u)=Tr(u85). It satisfies all seed
translates by the verified power identity. An omitted real full edge is
{1,a',b'}, where a'=1+X+X³+X4 and b'=1+2X+2X³+2X4. The code verifies
both vertices square and f-values (1,1,0), whose sum is2.

The existence question for one GOOD orbit at each m remains open. This
counterexample only refutes a stronger odd-degree sufficiency conjecture.
No exact incidence rank, exhaustive m13 census, originality, human review
or formal verification is claimed. Independent review remains required.

Suggested next conceptual step: explain when a small Frobenius-kernel
subspace U has the square-ratio property for every y outside F3, and whether
this yields a reusable transfer of old cyclic spectral factors to sparse
obstructions in new degrees. Avoid enumerating 797161 incidence rows.

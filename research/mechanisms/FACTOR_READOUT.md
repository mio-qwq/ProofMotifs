# From a cancellation representation to an effective readout
19 October 2026, Asia/Singapore. Manual proofs, classical finite-algebra
methods, independent AI challenges and exact checks. NOT a new factorization
algorithm, priority claim, human review, Lean or AI-causal explanation.

## 1. Frozen external transfer

Public protocol765fa48b0eb907c4c6fc30541dbfafc42ca9d29c selected previously
unread family142 from catalogue metadata. Statement-level decision
3a7ffa9098fd024ff44df3aa0704f4faab4ed143 was publicly saved BEFORE proof
access. The finite representation candidate FAILED the uniform complete
factor-readout contract. The TRANSFER142 documents retain the exact exposure,
input, grammar, baseline and cost. This is neither a source refutation nor a
factoring lower bound. The following work is post-decision/source-informed,
NOT a successful pre-proof transfer.

The useful question is precise: evaluating a proposed cancellation test
cheaply is different from finding tests whose surviving labels separate every
unknown component. Renaming factors as small auxiliary objects may leave
the entire discovery problem unsolved.

## 2. PM-READOUT0001: certified known-small-codomain readout

Input: p PROMISED prime, monic squarefree f in F_p[X] of degree n>=1,
dense coefficients. Set A=F_p[X]/f, Phi(a)=a^p, B=ker(Phi-I), r=dim B.
No roots or factors are supplied. Additional proposed tests c_1,...,c_t in A
are represented by degree<n polynomials. Each comes with an explicit
nonempty set S_j of distinct known scalars in F_p. Require finite identities

    product_(a in S_j)(c_j-a)=0 in A.                       (1)

These imply c_j^p=c_j: the support polynomial divides T^p-T. Thus a separate
fixedness promise is unnecessary, even before using that A is reduced.

Compute r; verify(1); start with block f. For each j replace each H by all
nonconstant monic gcd(H,c_j-a), a in S_j. At every stage blocks are pairwise
coprime and have product f. If the final count is m, then

    m = dim_(F_p) F_p[c_1,...,c_t] <= r.                    (2)

COMPLETE means m=r, exactly irreducible factors; otherwise PARTIAL is a
certified outcome. The algorithm does not enumerate scalar tuples or perform
an implicit F_p scan; it iterates only the supplied label lists and charges
their total length K. A caller explicitly listing all of F_p pays for it.

Proof: use the UNKNOWN irreducible factorization f=product_i f_i only for
CRT, which gives A=product_i F_(p^deg f_i) and B=F_p^r. Identity(1) puts
each coordinate c_j(i) at a label in S_j. Gcds select precisely the relevant
coordinate fibres. Joint tuples therefore partition r components into m
nonempty blocks; all are singletons iff m=r. Polynomial functions of the
tuple are constant on each fibre. Conversely to isolate one fibre v,
for each other fibre w choose a distinguishing coordinate j and multiply
(Z_j-c_j(w))/(c_j(v)-c_j(w)). This gives its indicator, proving(2).
Those unknown labels occur ONLY in the existence proof, not the algorithm.

Compute X^p mod f by binary powering, generate Frobenius columns
1,(X^p),...,(X^p)^(n-1), and eliminate Phi-I. Cost is
O(n^2 log p+n^3) field operations. Let K=sum|S_j|. Support validation
costs O(Kn^2). For each label, reduction/gcd across blocks of total degree n
costs O(n^2), since sum(deg H)^2<=n^2. Total readout-only cost is
O(n^3+n^2 log p+Kn^2). Supplied circuits require their additional
O(Ln^2) quotient work; their lengths and expanded input size are charged.

An independent dimension check starts with1, expands each retained vector
by every c_j, and retains independent vectors. Genuine quotient congruence
makes discarded linear combinations safe. At most tm<=tr products are
offered, not exponentially many monomials. Incremental elimination and dense
quotient arithmetic cost O((1+tr)n^2), including the seed when t=0.
The prototype RECOMPUTES this closure
and checks its dimension equals the gcd-leaf count, adding that cost. It
does not trust supplied status/rank telemetry. Its deque may hold O(1+tr)
vectors of length n; no optimal storage claim. A finite border certificate
could instead check independence, every product in the span, and B containment.

Schoolbook prime-field arithmetic gives polynomial bit cost in log p.
Primehood is an INPUT PROMISE, not sqrt(p) trial division hidden in the
claimed bound. The code enforces degree<n test lists. All of this is
classical Berlekamp/CRT/interpolation infrastructure, not a missing new tool.

## 3. PM-READOUT0002: binary-test synthesis is the factorization problem

For idempotents e_j^2=e_j, take S_j={0,1}. Each CRT coordinate is a bit;
completeness means all r binary codewords are distinct. The exact minimum
existential number is ceil(log_2 r), with zero when r=1.

Necessity is r<=2^t. Given factors, assign distinct t-bit codes and construct
each bit idempotent by polynomial CRT. Conversely any complete polynomial-
size idempotent family yields factors by section2. Thus synthesis from raw
squarefree f is polynomial-time Turing-equivalent to squarefree factorization,
including honest output/circuit lengths. Requesting the optimal existential
length does not change these reductions. This is not a lower bound, no proof
factoring is hard, and not an unconditional new algorithm.

For unrestricted F_p-valued algebra generators the analogous existential
minimum is ceil(log_p r). A SINGLE scalar separator exists iff r<=p.
A is monogenic but B need not be. In characteristic2 every B element is
already idempotent; its computed basis supplies usable binary tests.
The variable-p difficulty must not be transplanted to a fixed-field case.

## 4. PM-READOUT0003: rank and unknown scalar labels

Any vector-space basis of B already generates B and jointly separates
components. For b in B its minimal polynomial is the squarefree split
product over its DISTINCT scalar values. Compute it from a first linear
dependence among1,b,...,b^n. Finding its roots and taking gcd(f,b-a)
gives its coordinate fibres; declaring it split does not supply those roots.
A computably separating large-field element alone is still not factor readout.
Classical methods and the selected source explicitly distinguish these steps.

At p=1000000007 take f=(X-1)(X-4)(X^2+1), b=X^2. The quadratic is
irreducible because p=3 mod4. Thus r=3 and b's distinct coordinates
1,16,-1 generate B. Nevertheless b^((p-1)/2) has values1,1,-1,
a valid known-label test producing only TWO blocks. Adding
(b-1)^((p-1)/2), known labels0,1,-1, produces three irreducible leaves.
All support identities/products are exactly checked without an F_p scan.
These tests are SUPPLIED/source-informed, not discovered or held out.

A fixed scalar-test family h_j:F_p->S_j with product|S_j|<p has
distinct a,b with identical joint labels. On f=(X-a)(X-b), X generates B
but these tests cannot split it. This is a pigeonhole obstruction ONLY for
that fixed family, not adaptive tests depending on f or other arithmetic.

## 5. PM-ORIENTATION0001: actually construct a selector, conditionally

Source142 section02's local even splitter goes beyond checking a supplied
mask. We reproduce that operation, NOT its full driver or headline.

Input: p odd prime, monic squarefree totally split F, even degree N>=2,
and a SUPPLIED full2-primary generator u. Write p-1=2^s t, t odd.
Check u^(2^s)=1 and u^(2^(s-1))!=1. No roots, idempotents or factorization
of p-1 are supplied. Total splitting is checked by fixed dimension N.
It implies N<=p; parity then implies p>N, so that inequality is redundant
on the actual input class, not a separate obstacle needing a fake wrap control.

This auxiliary input is polynomial-time equivalent to a supplied quadratic
nonresidue v: u itself has Euler value u^((p-1)/2)=(-1)^t=-1; conversely
v^t has full order2^s whenever v^((p-1)/2)=-1. This reduction does not
discover either input. It matches the classical supplied-nonresidue interface.

Work in R=A tensor A=F_p[X,Y]/(F(X),F(Y)). Delta=X-Y,
d=Delta^(p-1) is the off-diagonal indicator. In the corner algebra dR,
whose identity is d, z=Delta^t satisfies z^(2^s)=d and is a unit of
order dividing2^s. It is NOT a unit in all of R (it is zero on the
diagonal). Recover its logarithm on that corner by s binary digit
stages. For a current mask e0, a zero equality w=0 has mask

    e0-(e0*w)^(p-1).                                       (3)

R is a product of copies of F_p, so this is exact. At stage j, with lower
logarithm bits ell, use w=z^(2^(s-1-j))-u^(ell*2^(s-1-j)).
At most N(N-1) disjoint nonempty masks remain at each level. No loop over
2^s, the numerical group order or all scalar values occurs.

Sum final masks whose logarithm is in[0,2^(s-1)). Swapping X,Y negates
z (t odd), shifting its logarithm by2^(s-1). The result e satisfies

    e^2=e,           e+swap(e)=d.                          (4)

Compute c=(id tensor Tr_(A/F_p))(e), using the ordinary multiplication
trace, NOT a normalized trace/evaluation oracle. In unknown root coordinates
c_i are integer outgoing-pair counts0..N-1, with sum N(N-1)/2. If all were
equal, that integer would be(N-1)/2, impossible for evenN. Unequal counts
remain unequal modulo p>N. Hence c is nonscalar; testing gcd(F,c-a) for
a=0,...,N-1 gives a proper factor.

Dense tensor multiplication costs O(N^4) field operations. At most
O(N^2 log p) masks each use O(log p) powering work, giving conservative
O(N^6(log p)^2) field operations for the constructor. Finite(4), partial
trace and bounded gcd verification are polynomial as well. Full-primary-
generator DISCOVERY is not performed. This elementary local proof is
accepted; odd-degree geometry/analytic dependency closure remains unchecked.

Failure controls: e=d/2 satisfies the additive equation in(4) but is not
idempotent and has constant trace(N-1)/2 in F_p. For oddN the genuine
three-cycle mask on three roots is Boolean but has constant trace1.
Both are exact executable controls. On nonreduced F5[X]/X^2 the nonzero
nilpotent X has X^(p-1)=0, so the Fermat expression is not a nonzero-support
indicator. Non-squarefree inputs are rejected. A merely order2 element
cannot replace a full2-primary generator when s>1; that order is checked.

## 6. PM-READOUT0004: adaptive branch divergence is a classical bridge

Static known-label tests are not the only legal readout. Let f be as above,
A=F_p[X]/f. A supplied deterministic scalar procedure uses field arithmetic,
zero-tests and guarded division. All varying field parameters are quotient
elements; constants and integer/control inputs are shared. It is defined
uniformly on all irreducible CRT fields. Its output is a DISCRETE string
determined only by shared integer data and its branch/control transcript.
No field serialization, field-to-integer conversion, field-degree/order
oracle or ordering comparison is allowed unless expanded into the model.

Simulate registers in A. For a zero test on a, gcd(f,a)=1 means all components
nonzero; gcd=f means all zero; a proper gcd returns a factor. Before division
test the denominator identically, inverting it by extended Euclid ONLY when
its gcd is1. An all-zero denominator is an invalid reached procedure under
the definedness promise. Inductively each scalar register is its quotient
projection and every component follows the common prefix of decisions.

If no mixed test occurs, all transcripts and hence discrete outputs agree.
Contrapositively, different component outputs FORCE a factor. If T counts
arithmetic AND zero-test steps on the longest scalar execution, the prefix
has length<=T. Dense quotient simulation costs O((T+1)n^2) field operations
with simple preprocessing; input/program/output lengths and integer/control
work are additional. No roots, factors or known scalar label lists are
needed. Polynomial-time consequences require T AND the entire auxiliary
construction to fit the original input budget.

The output grammar is essential. On f=X(X-1) over F5, 'return X' has distinct
field outputs0,1 without a branch or factor extraction. Calling those field
outputs strings via hidden encoding does not repair the theorem. A constant-
output routine need not split either; discovering a distinguishing procedure
is separate from this conditional compiler.

tools/dynamic_readout.py implements a forward acyclic arithmetic/zero-query
DAG with literal discrete returns and guarded inverses. It has no callback,
eval or field-encoding instruction. It returns SPLIT with a gcd witness or
COMMON with a common control output, not useful-routine discovery. Exact
tests cover both outcomes, unit/all-zero denominators, mixed extension-field
components and invalid raw-field-output/cycle grammars.

This is directly classical dynamic evaluation, not a newly discovered bridge.
Root and two reviewers read Poonen's original zeta-factoring paper §§2–5.
Its Theorem5.1 applies the same principle to a FIXED abelian family under
explicit Hypothesis Z, which supplies distinct zeta invariants. The proof
also describes universal program dovetailing under that hypothesis; it does
not prove the hypothesis, give a practical synthesis procedure, or a uniform
bound for arbitrary varying geometry. Even the supplied-family/discovery
distinction is already explicit in original literature.

## 7. Macro comparison, original baselines and actual limits

| Case | Legal representation | Useful readout | Discovery still charged |
| --- | --- | --- | --- |
|197 | raw hole evaluations | degree-minimal cardinal/Gram | geometry and degree legality; BM already generates the representation |
|107 | phase and local scopes | positive zero-target weights | phase/local architecture; finite dictionary/IP already covered |
|157 | shared maps, char2, symmetric pairing | six-term parity | auxiliary sharing; parity does not imply supersaturation |
|142 | quotient and fixed algebra | known small labels; conditional orientation/trace | scalar-label discovery; full primary data and its arithmetic source |

An exponent p-1 or a long expansion is not evidence of high-order
cancellation. Here it is a Boolean zero mask in a finite function algebra.
Pair orientation and integer nondivisibility force the surviving readout,
not a high-moment argument. The half-mask/odd-cycle controls are load-bearing.

The source142 large-characteristic table consumes auxiliary primes ell_q
with a non-power-residue condition; numerical E=max ell_q bounds the work.
Its O(p) scan is confined to p<=B^200000, a legitimate polynomial branch.
Increasing-q construction uses only degreeq-1 factorizations supported by
earlier entries, not an illicit factorization oracle. The small auxiliary-prime bound
imports a conductor/height-uniform companion Hecke zero-free theorem. That
companion, full odd geometry and all resource dependencies remain unchecked;
we neither accept nor refute the unconditional headline.

Classical Berlekamp/CRT covers the interface. Original Shoup gives a
stronger deterministic same-input benchmark than an O(p) straw man.
Actual primary versions/read limits are in the source ledger and reviews;
full Berlekamp1967/1970 bodies were not successfully retrieved. No failed
search establishes novelty. PM-H1..H5 remain OPEN; this is not success-rate,
enrichment, AI-cause or historical-originality evidence.

## 8. Next mathematical operation

Stop this factorization calibration after certificate/compiler audit.
No further field tables, primary-generator search, odd-curve or zero-free
constant optimization. The unresolved operation is complete useful readout
SYNTHESIS under original information and resource constraints. Next compare
107/157/142 discovery contracts: what can be generated from input, what
oracle has been supplied, and what theorem transports the discovery step
rather than an already found certificate? Freeze any new external test first;
this family is now read and cannot be reused as unread.

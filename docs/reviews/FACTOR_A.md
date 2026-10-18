# PM-FACTOR-A: quotient construction, fixed-space separation, and factor readout

Task-scoped independent mathematical view, 19 October 2026 project chronology.
Runtime actual model/effort is not independently introspectable in this task;
the parent requested GPT-6.1 Sol Ultra, which is not itself runtime evidence.

## Scope and independence receipt

Research question: given only a prime p in binary and a dense squarefree
f in F_p[X], what does the finite quotient-algebra/frontier operation actually
construct, and which factor-readout operation remains?

Read completely: repository AGENTS.md, research/RESEARCH_PROGRAM.md,
research/mechanisms/REPRESENTATION_TRANSPORT.md, and
docs/reviews/TRANSFER142_FREEZE.md. No Git commands, repo writes, peer outputs,
or selected source142 files were used for the derivation below. The first
independent result was delivered to the coordinator before receiving any
source142 mechanism description: B is F_p^r, a basis jointly separates,
scalar minimal polynomials are split, and root/value readout remains.
The coordinator then sent an unsolicited summary of source142's oriented
tensor mask and trace. That summary was not used in any proof below, but this
receipt prevents a claim of complete masking after that message. The additional
large-field scalar-separator construction was independently developed without
using that description. No unread-transfer success, historical novelty,
formal verification, human review, or AI-causal conclusion is asserted.

Output files are only this note and /tmp/PM-FACTOR-A-checker.py. The checker
uses no third-party modules and no network. The task has no child researchers.

## Contract and cost convention

Assume p is prime, n=deg(f)>=1, f is monic and squarefree. A nonmonic input
can be normalized by one field inverse. Squarefreeness is checked by
gcd(f,f')=1, with an extended-Euclidean Bezout identity as a finite certificate.
Primality is a promised input hypothesis; its validation is separate.

Use exact operations and equality in F_p, with schoolbook degree-n polynomial
arithmetic: multiplication, division and gcd cost O(n^2) field operations;
one product in A=F_p[X]/(f) also costs O(n^2). Let L=ceil(log_2 p).
All stated field-operation bounds have polynomial bit cost in L (for example,
charging O(L^3) bit operations per elementary field operation is conservative).
Coefficient storage costs L bits each. These are elementary upper bounds, not
claims of best-known complexity. No roots, factors, splitting field, oracle,
randomness, nonresidue or prelabelled idempotents are supplied.

## PM-FACTOR-A-001: what is constructible from raw f

**Statement.** In deterministic O(n^3+n^2 L) F_p operations and O(n^2) field
storage, one constructs the power-basis multiplication representation of A,
the matrix F of Frobenius Phi(a)=a^p, and a complete basis U for

    B = ker(F-I) = {b in A : b^p=b}.

If f has r distinct monic irreducible factors, then B is an F_p-algebra
isomorphic to F_p^r. In particular dim(B)=r, so reducibility and the exact
number of irreducible factors are determined in that bound. This does not
yet output the factors.

**Construction.** In basis 1,x,...,x^(n-1), x=X mod f, multiplication by x
is the companion matrix read directly from f. Polynomial remainders satisfy
multiplication congruence because (f) is an ideal. Compute w=x^p by binary
powering in O(n^2 L). The columns of F are 1,w,w^2,...,w^(n-1), obtained
with n-1 quotient products in O(n^3). Gaussian elimination on F-I costs
O(n^3). The basis may include 1 as a chosen first member.

**Proof of interpretation, not an algorithmic assumption.** Let
f=f_1...f_r be its mathematically existing irreducible factorization, with
d_i=deg(f_i). CRT identifies A with product_i F_{p^(d_i)}. In any field of
characteristic p, the equation t^p=t has exactly the p roots F_p: T^p-T
has degree p, contains every element of F_p as a root, and has derivative -1.
Therefore the fixed algebra is exactly product_i F_p. CRT and the factors
are used only to prove the interpretation, not supplied to the construction.

**Finite certificate.** Return F, U, the row-reduced matrix R of F-I and its
invertible row-operation matrix S. Verify Frobenius columns by modular
powering/recurrent products, S(F-I)=R, invertibility of S, the RREF syntax,
(F-I)U=0, rank(U)=r, and r+rank(R)=n. These finite checks certify completeness
of the kernel, not just membership of several vectors. All verification is
polynomial in n,L; with dense matrices it has the same O(n^3+n^2 L) scale.
The quotient arithmetic is checked against f, not a guessed diagonalization.

The congruence/frontier principle is valid here, but its frontier is the
already obvious 1,x,...,x^(n-1). Finite-dimensional representation discovery
does not itself discover the CRT coordinate labels.

## PM-FACTOR-A-002: exact readout from one fixed element

For b in B let m_b(T) be its monic minimal polynomial in A. If the uncomputed
CRT values are beta_i in F_p, then

    m_b(T) = product_{a in {beta_1,...,beta_r}} (T-a).       (A1)

Consequently m_b is squarefree, splits completely over F_p, divides T^p-T,
and has degree s<=min(r,p). It has degree one iff b is a scalar multiple
of 1, a condition testable directly in power-basis coordinates.

**Construction/minimality certificate.** Form 1,b,b^2,... incrementally and
stop at the first dependence. At most n quotient products and an incremental
rank computation take O(n^3) field operations. Return the first s powers,
a rank-s certificate for their coefficient matrix, and m_b(b)=0. Independence
plus the monic relation proves minimality among all degrees, not just those
tested after a heuristic plateau. Since T^p-T annihilates b, division by m_b
shows m_b divides T^p-T: a nonzero remainder would contradict minimality.
This also proves (A1), or (A1) follows directly by evaluating at the beta_i.

For every a in F_p,

    g_a(X)=gcd(f(X), b(X)-a)
          = product_{i: beta_i=a} f_i(X),                 (A2)

where an empty product is 1. Thus b is nonconstant iff at least two g_a
are nonconstant. Every root a of m_b gives a proper nontrivial g_a when
b is nonconstant. A nonconstant fixed element need not itself be a zero
divisor: all beta_i can be nonzero, so gcd(f,b)=1. Nor need one b distinguish
all factors: several beta_i may coincide.

**Useful cancellation certificate without root labels.** Suppose a nontrivial
coprime factorization m_b=u v is supplied or discovered. Extended Euclid
constructs alpha u+beta v=1. In A set

    e=beta(b)v(b),        1-e=alpha(b)u(b).

Then the exact polynomial identity

    e(e-1) = -alpha(b)beta(b)m_b(b) = 0                  (A3)

constructs an idempotent; it is not merely naming an unspecified kernel.
Both e and 1-e are nonzero. For if e=0, then the nonzero polynomial beta v
would annihilate b with degree <s, using deg(beta)<deg(u); similarly for
1-e. Equivalently use the nonempty CRT fibers. Therefore gcd(f,e) and
gcd(f,e-1) give complementary proper factors. The verified data are finite:
m_b minimal, m_b=u v, deg(u),deg(v)>0, alpha u+beta v=1, and the modular
evaluations. Horner evaluation and the rank/Euclidean checks cost polynomial
in n, specifically O(n^3) with these naive bounds.

This transports a *discovered partition of the scalar minimal polynomial*
into a certified factor of f. It does not discover that partition by itself.
The coprimality/unit requirement is explicit in the Bezout identity.

**Selectors when scalar roots are known.** For a root a of m_b, let
v_a(T)=m_b(T)/(T-a). Since m_b is squarefree, v_a(a)=m_b'(a)!=0. Then

    e_a = v_a(b)/v_a(a)
        = 1-(b-a)^(p-1).                               (A4)

Its CRT values are 1 on the a-fiber and 0 elsewhere. Therefore
(b-a)e_a=0, e_a^2=e_a, e_a e_c=0 for a!=c, sum_{a root of m_b} e_a=1,
and g_a=gcd(f,1-e_a). The equality between the two formulas follows by
their common values on all beta_i, or by reduction modulo m_b. The second
formula is an O(log p)-length powering circuit for a specified a; it is not
an O(log p)-cost procedure to find a useful a. The first formula has degree
s-1 rather than p-1 and makes the nonzero scalar inverse explicit.

## PM-FACTOR-A-003: binary idempotents are exactly factor witnesses

A nontrivial idempotent e in A (e^2=e, e not 0 or 1) yields a proper split
f=g h with g=gcd(f,e), h=gcd(f,e-1). Indeed gcd(e,e-1)=1 and f divides
e(e-1), so g,h are coprime and their product is f. Nontriviality ensures
both have positive degree. Conversely a proper split f=g h gives gcd(g,h)=1
because f is squarefree. If a g+b h=1, then e=b h mod f is a nontrivial
idempotent, by the same calculation as (A3). These conversions cost O(n^2)
field operations. Every idempotent belongs to B because e^k=e for k>=1.

Hence finding a nontrivial fixed *binary selector* is polynomial-time
equivalent to finding a proper factor. This is a precise equivalence, not
an asserted impossibility or lower bound. Computing a basis of B and
computing a nontrivial idempotent of B are different operational outputs.

## PM-FACTOR-A-004: joint separation and a complete deterministic scan

Every basis b_1,...,b_r of B is a separating *set*: for i!=j some b_k has
beta_{k,i}!=beta_{k,j}. Otherwise the two coordinate maps on B agree on a
basis and hence on all B, contradicting the coordinate idempotent whose
values are 1 at i and 0 at j. This proof does not require those coordinate
idempotents as inputs.

Starting with the single block f, process each b_k and each a in F_p,
splitting each current block h by gcd(h,b_k-a). The final blocks are exactly
the f_i, because every pair of components is separated by a processed
coordinate. For each (k,a), reductions and Euclidean gcds across the current
factor list cost O(n^2) in aggregate: the degrees of its blocks sum to n,
and each polynomial b_k has degree <n. Total cost is

    O(n^3+n^2 L + p r n^2) field operations.             (A5)

This is an explicit elementary upper bound, not the fastest classical
factorization algorithm. Since p is binary-encoded, its p dependence is not
polynomial in L. A complete output can be certified economically using the
fixed-space factor count: a product of r monic positive-degree factors equal
to f is necessarily its complete irreducible factorization. Every output
factor contains at least one of the exactly r irreducibles, so none can
contain two. Product verification plus the certified r suffices.

## PM-FACTOR-A-005: scalar separator discovery is not the whole remaining gap

A single b in B separates all r components iff deg(m_b)=r. Such an element
exists iff r<=p. Necessity is the pigeonhole principle in F_p; sufficiency
is the existence of a vector of r distinct entries in B isomorphic to F_p^r.
When r>p a basis still jointly separates; demanding a single scalar separator
would be a false additional hypothesis.

There is also a deterministic polynomial(n,L) construction of a scalar
separator whenever r<=p; one must not leave this classical primitive-element
operation as an unexamined alleged bottleneck.

**Large-p construction.** Let D=r(r-1)/2 and suppose p>D. Start b=0. For
each basis vector c=b_j, try lambda=0,1,...,D and keep b+lambda c having
largest minimal-polynomial degree, computed by the preceding Krylov method.
For the proof only, consider the distinct pairs (beta_i,gamma_i) of current
b and c values; let their number be t. Different pairs with equal gamma
never collide under (beta,gamma) -> beta+lambda gamma. Each other pair
collision excludes at most one lambda. There are at most D pair collisions.
Among D+1 distinct lambdas at least one makes the map injective on the t
pairs, giving minimal degree t; no lambda gives degree >t. Thus every
maximizer has exactly the joint partition and cannot merge any formerly
separated pair. After the full basis is processed all r components are
separated. The cost is O(r(D+1)n^3)=O(r^3 n^3), with O(n^2) reusable field
storage, plus fixed-space construction. Rank certificates verify the final
minimal degree r; no factors/roots are needed to check success.

If r<=p<=D, then p=O(r^2), so the full scan (A5) already has polynomial(n,L)
cost. Once the factors have been obtained, extended-Euclidean CRT gives
coordinate idempotents, and their weighted sum with distinct weights
0,...,r-1 gives a scalar separator. Therefore the promised r<=p case is
covered unconditionally; this is not a factorization theorem for large p,
because in the large-p case it constructs b and m_b but not the roots of m_b.

The exact remaining readout can therefore be stated as *a nontrivial
partition/value of an explicitly constructed split squarefree polynomial*,
not just 'find a nonconstant element' or 'find a separating element.'

## PM-FACTOR-A-006: exact reduction and negative boundary

Factoring squarefree polynomials over F_p reduces deterministically, with
polynomial(n,L) overhead, to finding one root of squarefree completely split
polynomials over F_p. On a reducible block compute B, choose any nonscalar
basis member b, compute m_b, obtain a root a, and use (A2) to split. There
are at most r-1 proper splits; irreducible blocks are recognized by dim(B)=1.
Recomputing the fixed algebra at every node still gives a polynomial bound
(for example O(n^4+n^3 L) overhead is ample). Every queried m_b has degree
between 2 and the block's factor count. Conversely, a factorization of a
squarefree completely split polynomial immediately yields its roots. This
is a polynomial-time reduction/equivalence of tasks, not a proof that any
particular deterministic root-finding bound is impossible.

An especially sharp uniform negative control is the entire promised-split
input class: if f is squarefree and splits over F_p, then f divides X^p-X,
so Frobenius F=I and B=A. Kernel extraction imposes no restriction at all;
it returns the whole quotient with its original f relation. It does not
provide scalar root labels for the companion matrix. Any claim that the
finite representation plus fixed-space calculation alone has completed
large-prime factorization must account for this class. Simultaneous
diagonalization is not a unit-cost linear-algebra operation when its
eigenvalues have not been supplied; their discovery is the root problem.

These boundaries do not say that B lacks the information: its algebra fully
encodes all factors. They say that a certified representation and a readout
algorithm have distinct contracts and that the omitted operation is
classically substantive. No general deterministic lower bound follows.

## Nearest primary literature: actual access and limits

1. E. R. Berlekamp, *Factoring Polynomials Over Finite Fields*, Bell System
   Technical Journal 46(8), October 1967, pp.1853–1859,
   DOI 10.1002/j.1538-7305.1967.tb03174.x.
   Original-publication host metadata/abstract and introductory extract read:
   https://www.nokia.com/bell-labs/publications-and-media/publications/factoring-polynomials-over-finite-fields/
   (web lines209–218). Wiley abstract metadata also read. The entire1967
   body was NOT successfully retrieved in this task. Wiley PDF was
   inaccessible; the mirrored full issue at
   https://ibm.retropc.se/magazines/Bell_System_Technical_Journal/BSTJ_V46N08_196710.pdf
   timed out in web retrieval and returned502 to curl. A guessed Berkeley
   PDF path returned404. None of these failures establishes any content.

2. E. R. Berlekamp, *Factoring Polynomials Over Large Finite Fields*,
   Mathematics of Computation 24(111), July1970, pp.713–735,
   DOI10.1090/S0025-5718-1970-0276200-X.
   https://www.ams.org/mcom/1970-24-111/S0025-5718-1970-0276200-X/S0025-5718-1970-0276200-X.pdf
   Official direct fetches returned403. Search retrieval of this original
   PDF supplied the abstract and page727; only those portions were read.
   Page727 explicitly treats reduction from factorization to finite-field
   roots and then prime-field split roots. The paper's abstract is a
   reduction claim; it must not be silently promoted to an unconditional
   deterministic polynomial-time solution of the remaining prime-field
   root problem. Full-page/section comparison remains incomplete here.

3. Victor Shoup, *On the Deterministic Complexity of Factoring Polynomials
   over Finite Fields*, Wisconsin CS Technical Report782, July21,1988,
   https://ftp.cs.wisc.edu/pub/techreports/1988/TR782.pdf .
   This is a primary research source, not a survey. Read by streaming the
   scan through pdftoppm and Tesseract without saving it. Actual ranges:
   printed pp1,2,3,4,5 (PDF pp3–7), with p3's character-sum argument read
   only as OCR, not independently audited in detail. Printed p4 defines
   the Berlekamp subalgebra and separating sets; p5 states that a basis of
   B is such a set, constructs it as the nullspace of a -> a^p-a, and gives
   the scalar-gcd refinement loop. It also gives a stronger deterministic
   method using quadratic-character filters, rather than requiring a full
   p scan. The summary states p^(1/2+epsilon)-type dependence for arbitrary
   epsilon>0 with its stated degree dependence. OCR corrupts exponents,
   so quote no exact asymptotic formula here without visual confirmation.

For source-derived attribution, the core fixed-space/separating-set/gcd
operation is explicitly classical in the original research literature
accessed here. The proof above is an independently written exact special-case
derivation, not an original theorem claim. The fastest-same-input baseline is
not exhausted by an O(p) Berlekamp implementation; Shoup already improves
that dependence. The full requested original1967/1970 audit is outstanding
in this subtask, and the coordinator must not mark it completed from these
limited read ranges. No claims about the current2026 open/closed status of
general deterministic factorization are based on historical sources.

## Exact computation receipt and failed attempt

Command, run from /workspace/scratch/415407b3c01b/ProofMotifs:

    python /tmp/PM-FACTOR-A-checker.py

Final exit code0; output:

    p=2: 32 squarefree monic inputs checked
    p=3: 81 squarefree monic inputs checked
    p=5: 125 squarefree monic inputs checked
    p=7: 49 squarefree monic inputs checked
    r>p boundary: r=3,p=2; maximum scalar minimal degree=2; joint readout succeeds
    split-input control: p=101,n=6,F=I; separator minimal degree=6; history=[(0, 1), (1, 6), (0, 6), (0, 6), (0, 6), (0, 6)]
    PASS: 287 exhaustive squarefree inputs plus two boundary controls; all exact identities verified

The exhaustive ranges are p=2 degrees1–5, p=3 degrees1–4, p=5 degrees1–3,
p=7 degrees1–2. These are implementation checks, not infinite theorems or
the project's research objective. An independent deliberately slow monic
divisor enumeration validates the factor lists on these finite inputs; it
is not used by the proposed constructor or its complexity analysis.

Checks include Frobenius column construction, row-operation/full-kernel
certificates, fixed-space factor counts, complete scalar-scan readout,
minimal-polynomial rank certificates, m_b | T^p-T, Lagrange/Fermat selector
agreement, orthogonality/partition, root-free Bezout transport, and the
large-field separator algorithm.

Initial test run exited1 at the r>p control because the checker mistakenly
enumerated all A elements, not B: elements outside B can have nonsplit
minimal polynomials of degree>p. The test was corrected to enumerate linear
combinations of the returned B basis. The theorem's restriction b in B was
unchanged; this failure is a useful hypothesis control, not hidden evidence
of universal scalar degree<=p. The final run above then passed.

## Conclusion for the research program

The reusable finite operation is concrete: raw f -> exact quotient/Frobenius
representation -> full fixed algebra and factor count -> minimal split
polynomials; discovered coprime scalar partitions -> Bezout cancellation ->
binary idempotents -> actual factors. It has finite certificates and explicit
costs. Classical methods already cover it. The unresolved contract under the
frozen poly(n,log p) target is the efficient discovery of a useful partition
of the constructed split scalar polynomial (or an equivalent nontrivial
idempotent), not representation existence or membership verification. Scalar
separator construction should not be conflated with scalar value readout.
All PM-H1 through PM-H5 remain open; this is a baseline clarification and
precise hypothesis-preserving synthesis, not a missing-tool result.

# PM-FACTOR-C — independent adversarial / primary-source audit

Task ID: PM-FACTOR-C. Question: isolate the auxiliary-object discovery
operation beyond finite quotient / Frobenius-fixed-space representation,
challenge resource accounting and hypotheses, and separately challenge the
coordinator's binary-idempotent proposition. Scope: read-only ProofMotifs and
public sources; own temporary notes/checker only. No repository Git operations,
external communication, children, A/B notes or source scripts were used.
Requested configuration was GPT-6.1 Sol / Ultra; actual root configuration is
not inferable here. The public pre-access freeze and statement-only decision
were read first; no successful pre-proof transfer is being claimed.

## 1. Independent objections, before receiving the integrated proposition

The representation itself does not expose factors: the basis of
Fp[X]/f is not a primitive-idempotent basis. Frobenius kernel construction
identifies B but does not diagonalize it or supply its CRT coordinates.
Even a computably separating characteristic polynomial only produces another
unknown-root splitting problem. These are distinct construction/readout tasks.

Primary generators, unknown roots, a primitive idempotent basis and an
unproved unit must not be supplied covertly. A q-th root of unity is not in
general a generator of the *full* q-primary group. Product-field procedures
must verify inverses componentwise; root extraction has both a unit hypothesis
and a power-existence promise. Finite reduced / square-free hypotheses cannot
be dropped merely because finite-dimensional quotient arithmetic is available.

Cost must retain numerical n/q/E versus binary log p distinctions. The
source's bound in numerical E=max ell is not a bound in log E. Conversely,
q<=n digit enumeration and an O(p) loop confined to p<=B^200000 are valid
polynomial-in-input branches, not counterexamples to the source bound.

## 2. Pinned source access and exact dependency comparison

All source142 files below are at openai/math commit
1581d4cbdd69a0faf34b2089614fe2a814316a6a, under
preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026/build/.
Reads were fetched through GitHub's read-only fetch/fetch_file tools. The
line numbers below are actual TeX source line numbers obtained by splitting
the returned text; metadata and source were fetched independently.

| File | Blob | Actual audit/read scope |
| --- | --- | --- |
| sections/00-introduction.tex | 24bb00b878eac7882bfb3cbb862acf1903cf2693 | lines1–230 read; source claims/history/interface only |
| sections/01-table.tex | d7d4be3c1fe9d0d0043568ffcdfaa70fb52ff5ab | all224 lines read; elementary table construction locally checked |
| sections/02-finite-fields.tex | 714682cbb142309e1fb8d7dc119cb5f48d7cf72b | all273 lines read; simultaneous execution, primary digits, root hypotheses and even splitter locally checked |
| sections/05-geometry.tex | 31ef37eace1600670063ed7cfa47aaf6538ae4d6 | lines1–100 and keyword-selected lines displayed, not a full proof audit |
| sections/07-odd-split.tex | 395cc0430fd71cf06f24ae1e5f58c80bc8d40734 | all244 lines read as dependency map; delegated norm/divisor/geometry inputs NOT closed |
| sections/08-driver.tex | 4e5bbd81999a603d8ce4488d8b84a93b2602b5c0 | all222 lines read; elementary driver/induction locally checked conditionally on splitters |
| sections/09-complexity.tex | 193697981fd7ee57af1398992eb04fd7462f9df7 | keyword-selected lines, not full complexity closure |
| sections/10-analytic.tex | 21081c288d68760167d2d94a34247ba61240dddf | all179 lines read; dependency isolation only, imported theorem unverified |
| references.tex | ed441487f299ef0ef46a1bdf4db526877b874a04 | all read to identify original sources |

Sections03,04,06 and the analytic companion were not read. This is NOT a
headline correctness/novelty/provenance audit. In particular the odd splitter,
full algebraic reduction, uniform complexity proof and analytic theorem are
not accepted or refuted by this bounded audit.

### Representation to readout

Section08 lines23–42 constructs B=ker(Frob-id) in polynomial arithmetic
and identifies B=Fp^r in the unknown CRT coordinates. Lines44–83 produce
a separating element via b(t)=sum t^j b_j when p>r^3, using at most r^3+1
trials and a square-freeness test on the multiplication characteristic
polynomial. A *supplied nontrivial factor S* of that new degree-r polynomial
then gives gcd(h,S(b(t))). Thus the separator lemma does not by itself solve
the remaining totally-split polynomial problem.

Section02 lines224–272 solve the even case with a *supplied full 2-primary
generator*. Unknown roots are not enumerated: tensor quotient arithmetic
constructs Delta, off-diagonal masks, digit partitions and partial trace.
Lines248–266 show reverse ordered pairs have complementary orientation;
the integer row scores cannot all equal (N-1)/2 when N is even.
The obstruction is pairwise/combinatorial parity, not high-order cancellation
merely because the expression uses exponent p-1. The hypothesis p>N prevents
integer-score collapse into the field; moreover it is automatically true
here because square-free total splitting over Fp gives N<=p and N even with
p odd excludes equality. Consequently an N>=p "field wrap" example would
not be a valid input counterexample to this proposition.

Section01 lines15–27 require auxiliary primes ell_q with ell_q=1 mod12q
and p^((ell_q-1)/q)!=1 mod ell_q. Lines47–96 then use the invariant algebra
Uq=R_ell^Hq. Its dimension q alone is not the field certificate: the tested
nontrivial Frobenius class in Gamma/Hq acts transitively and supplies the
field property. Lines100–171 construct full primary generators by linear
equations in these fields, with no factorization of p-1. Lines179–223 and
section08 lines185–197 give a sound common increasing-degree induction:
factoring Phi_q of degree q-1 requires only already-built entries <q.
Calling this an unconditional factoring oracle would misdescribe the source.

The irreducibility of Uq and the table data are source-derived useful
auxiliary-object constructions, but they consume integer auxiliary-prime
information absent from the frozen quotient/frontier input. Numerical
E controls the size ell_q-1 of the cyclotomic algebra and the search. An
O(log E)-bit encoding is not a same-cost substitute for this work.

Section02 lines106–117 assume q odd dividing Q-1, zeta of exact orderq,
omega generating the full q-primary subgroup, square-free H, p>h^2, and
a unit promised to be a q-th power. Lines164–176 construct a simultaneous
unit by a grid avoiding the zero loci in all components; arbitrary nonzero
kernel output would not suffice. Lines198–205 count numerical q choices per
digit, h^2+1 grid trials and O(h logQ) digit levels. Since the source uses
q<=n and polynomial-degree fields, this does not enumerate q^s or p.

Section07 lines14–30 still requires explicit K,zeta,full-primary omega_K.
Its stages use rational lambda-divisions, divisor arithmetic/circuits,
unitroot promises and geometric forced separation from other sections;
finite quotient arithmetic only performs them simultaneously and extracts a
factor when they differ. The *forcing* mechanism is not furnished by the
quotient representation. I have not checked the complete chain proving it.

Section10 lines9–18 imports a fixed-width zero-free Hecke strip for every
finite-order character of every cyclotomic field containing mu12, including
the principal character (pole permitted), uniformly in conductor and height.
Lines91–158 use it to bound ell by c0 B^20000000. The split-prime terms in
Psi_K-(1/q)Psi_M cancel linearly (lines147–154); that fact is not itself a
higher-order moment theorem. Without actually auditing the companion, the
numerical auxiliary-prime bound and headline unconditional complexity remain
unchecked. Neither unfamiliarity nor its strength constitutes a refutation.

## 3. Original classical baseline

Shoup, *On the deterministic complexity of factoring polynomials over finite
fields*, IPL33 (1990), pp261–267. The original author-hosted preprint is
https://www.shoup.net/papers/detfac.pdf, linked by
https://www.shoup.net/papers/. Read its pages1–6 visually because PDF text
extraction is corrupted; screenshots were web refs turn327view0/1/2 and
turn340view0/1/2, PDF ref turn325view2. Page2 states the worst-case
O(p^(1/2)(log p)^2 n^(2+epsilon)) field-operation bound and contrasts an
all-Fp scalar search. Page3 describes construction of the Frobenius-fixed
algebra and gcd fibre refinement; pages4–6 develop the shift/character-based
search shortening. This is stronger than treating O(p) as the only classical
same-input baseline, but remains nonpolynomial in log p in worst case.
No statement about the strongest result as of2026 is inferred from it alone.

Berlekamp1967 original full article was *not successfully read* by this
auditor. The author publication index and Nokia/Bell Labs primary record
confirm citation/interface but expose only first-page introductory text.
Original journal full-PDF retrieval through Wiley/AMS routes or the Bell
volume mirror failed/403/timed out. Do not label this a complete original
Berlekamp audit. Relevant URLs:
https://www.nokia.com/bell-labs/publications-and-media/publications/factoring-polynomials-over-finite-fields/
https://onlinelibrary.wiley.com/doi/abs/10.1002/j.1538-7305.1967.tb03174.x
https://ibm.retropc.se/magazines/Bell_System_Technical_Journal/BSTJ_V46N08_196710.pdf
https://math.berkeley.edu/~berlek/publications/articles_reviews.html

## 4. Challenge to coordinator's supplied binary-idempotent theorem

The proposed statement is sound with explicit monic square-free degree>=1,
so r>=1. In unknown CRT fields, an idempotent has coordinates0/1, hence is
Frobenius-fixed. For supplied e1,...,et their joint binary codes partition
the r components. The generated unital algebra consists exactly of functions
constant on those code classes: one inclusion is immediate; for each observed
code c, the product of e_j or (1-e_j) is that class's characteristic
idempotent. Therefore dimension=#observed codes, full B generation iff all
r codes differ, and successive gcd(e_j),gcd(e_j-1) leaves are exactly code
buckets. Under square-freeness they are all irreducible iff there are r.

No exponential dictionary needs enumeration. W0=span{1} and
Wj=W(j-1)+e_j W(j-1); retain independent vectors at each stage. The induction
includes every subset product on the first j entries, while idempotency
makes repeated factors redundant. Each Wj has dimension<=r; at most2rt
offers suffice, and dense quotient multiplication and exact Gaussian
elimination are polynomial in n,t,logp. The final dimensionr is an exact
completeness certificate, not a search procedure for the e_j.

At least ceil(log2r) entries are necessary because there are at most2^t
codes. Given factors, choose distinct binary labels and use polynomial CRT
to construct that many idempotents; r1 uses the empty family. Conversely any
polynomial-size complete supplied family yields factors by the gcd procedure.
Thus the synthesis problem and square-free factorization are polynomial-time
Turing interreducible, with polynomial output bounds specified. This is an
operational equivalence, not an unconditional hardness lower bound, a new
method or a proof that known algorithms cannot factor.

Edge cautions: degree0/r0 needs separate handling; characteristic2 is valid;
unital closure is essential for the empty r1 case. On a nonreduced quotient,
the same binary code reasoning separates primary blocks but not necessarily
their multiplicities or irreducible leaves. Distinctness must mean distinct
codes across CRT components, not pairwise distinct supplied e_j themselves.

## 5. Exact finite tests and failure mechanisms

Run: `python /tmp/PM-FACTOR-C-check.py`.
The checker uses only Python standard library and its own exact prime-field
polynomial arithmetic, Frobenius matrix rank, naive toy factor oracle, CRT,
frontier rank and gcd branching. Its naive factor/CRT enumeration is *only*
bounded checking, never the proposed complexity algorithm.

Final output:

    PASS: 270 squarefree inputs; 3960 binary families
    PASS: nonreduced f=X^2 has complete empty family but reducible leaf X^2
    PASS: nilpotent X != 0 yet X^(p-1)=0 in F5[X]/X^2
    PASS: weakened order-3 u=7 fails source02 digit step j=1 for cube a=8 over F19
    PASS: p=73,q=3,ell=37 without residue test gives U_q=F73^3, not a field

The exhaustive inputs are all monic square-free polynomials over F2 through
degree6, F3 through degree4, F5 through degree3. For each it checks all
binary families of size0,1,2 including repeated entries; it also constructs
an optimal-length label family. This finite check does not replace the
all-degree proof. Initial checker development incorrectly asserted a_q=7
in the F19 example; exact arithmetic showed a_q=11 and the assertion was
corrected before the final passing run. The actual failure remains: with
s2 and only order3 u7, the base u^3=1 cannot match final target11. No source
theorem is refuted because the source requires order9.

The auxiliary control p73,q3,ell37 satisfies the exclusions and congruence
but fails the power-residue condition. Since p=-1 mod37 belongs to the
cube subgroup, its action fixes all three cosets; U3 is F73^3, not a field.
This shows exactly why a q-dimensional fixed space alone is insufficient.

## Handoff / stop condition

Local elementary source pieces and the binary-idempotent proposition survive
the stated challenges. Complete odd splitting and the analytic companion
are outside this bounded audit and explicitly unchecked. No novelty,
high-order-cancellation prevalence, AI-cause, global headline correctness or
formal-verification claim is made. Await coordinator's actual integrated
proof/checker for a separate implementation audit if requested.

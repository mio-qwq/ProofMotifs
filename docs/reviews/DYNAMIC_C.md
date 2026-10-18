# PM-DYNAMIC-C — bounded independent dynamic-evaluation challenge

Task: adversarially check the coordinator's classical dynamic-readout bridge,
not establish a new tool or audit new geometry. I reread the already-exposed
source142 section02 principle and read the primary Poonen paper §§2–5 only
for this comparison; no new broad source audit or enumeration was performed.

## Decision and precise scope

The theorem is correct with its stated output grammar. Let f be monic
square-free of positive degree n over promised-prime Fp. Work in A=Fp[X]/f.
A deterministic scalar program uses field +,-,*,/, zero-tests, shared Fp
constants and shared integer/control inputs. Every varying field parameter
is supplied as an element of A. Its specialization is defined in every
irreducible CRT field. Its discrete output string depends only on its
branch/control transcript and shared integer data, not on raw field values,
their coordinate encodings, field order information learned externally, or
an unlisted conversion instruction. Let T count *all* arithmetic instructions
and zero-tests along the longest scalar execution, not arithmetic alone.

Then quotient simulation either returns a proper factor of f or reproduces
a common path and its common discrete output. If component discrete outputs
are not all equal, it must return a factor within at most T scalar steps.
Dense simulation costs O(T n^2) Fp operations plus construction, input and
integer/control costs. If one wants to include preprocessing when T=0,
use O((T+1)n^2) plus those costs. Polynomial factoring consequences require
T and all extra construction/control/output costs to be polynomial in the
original input; the lifting principle alone does not prove such a bound.

For general square-free f, its scalar components are finite extension fields,
not necessarily Fp. The theorem remains valid only if the promised scalar
routine is defined and obeys the same grammar uniformly on those fields.
The directly quoted source142 version instead assumes a totally split F
over Fp and a common explicitly represented extension k, so all components
are copies of k. Do not silently move between these interfaces.

## Common-prefix proof and failure attempts

CRT writes A as a product of finite fields. Maintain the invariant that each
quotient register specializes to the corresponding scalar register and all
scalar components have followed the same instruction/control transcript.
Arithmetic preserves it. At a zero-test on a, compute g=gcd(f,a): g1 means
every coordinate nonzero, gf means every coordinate zero, and a proper g
selects a nonempty proper subset of irreducible components. The first two
cases allow the common branch; the third terminates with a factor. A
division is permitted only after checking its denominator is a unit; gcd1
gives an inverse by the polynomial extended Euclidean algorithm. A mixed
denominator also gives a factor. Under the all-components-defined promise,
an all-zero denominator cannot be a valid reached scalar division.

If no mixed test occurs, induction gives an identical control transcript.
Because only shared integer data and this transcript determine the discrete
output, all outputs are identical. Contraposition proves forced splitting
when outputs differ. It also handles unequal halt times: halting is a shared
control decision, so unequal halt times themselves require earlier divergent
control. Every common-prefix instruction belongs to each scalar execution;
the first disagreement cannot exceed their maximal length T.

Quotient addition, multiplication/reduction, polynomial gcd and inversion
cost O(n^2) field operations with standard dense algorithms. Thus the
simulation overhead is as claimed. Unknown factor labels appear only in
the proof, never as algorithm input.

Attempted strengthening fails exactly at the output grammar. On
f=X(X-1) over F5, input x=X modf and program `return x` have component outputs
0 and1 without a zero-test or branch. Raw field output is not a transcript-
determined discrete string, so this is not a counterexample to the theorem;
it is a counterexample to dropping that condition. Converting x to its
canonical integer encoding would likewise be a forbidden extra instruction.
A vector-valued algebra output being nonconstant therefore does not alone
force a dynamic-evaluation branch. A legal procedure must *read it out*
through tests/control or supply an independently verified small codomain.

## Exact original-source comparison

Source142 at openai/math1581d4cbdd69a0faf34b2089614fe2a814316a6a,
sections/02-finite-fields.tex blob714682cbb142309e1fb8d7dc119cb5f48d7cf72b,
lines24–68 explicitly states simultaneous execution, gcd zero/split handling,
inversion after unit checking and polynomial/linear-algebra pivot tests.
It calls this classical dynamic evaluation and cites Della Dora,
Dicrescenzo and Duval. The above statement is its elementary product-algebra
argument with the output grammar made explicit, not a novel theorem.

Primary comparison: Bjorn Poonen, *Using zeta functions to factor polynomials
over finite fields*, author-hosted
https://math.mit.edu/~poonen/papers/fq-factoring-ams1.pdf.
Web ref turn354view0, §§2–5, PDF pages1–5, text lines25–202 were read.
Section3 explains Kayal's branch-divergence idea; §4 describes Pila's
arithmetic sequence controlled by zero queries. Section5's Hypothesis Z
supplies a fixed abelian family with distinct zeta functions; its proof
replaces those queries with gcd tests and forces a factor. This is direct
primary coverage of adaptive discrete readout, not merely a static label
analogy. However, a polynomial exponent depends on fixed geometric
presentation, and Hypothesis Z remains an explicit conditional input.
No assertion that the hypothesis holds, no uniform bound for arbitrary
varying geometry, and no audit of Pila's full algorithm follows here.

The bridge usefully distinguishes static known-label tests from adaptive
zero-query transcripts. It does not synthesize separating observables or
families, supply unproved units, establish high-order cancellation, prove
AI causality, or solve the original complete-readout discovery task.

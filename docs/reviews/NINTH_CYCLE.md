# Ninth-cycle single-orbit gate and obstruction

Date: 18 October 2026. Verified starting head:
`e35f0dfcb8e5446be3e0840d54c8f89e9967b34e`.

## Recovery and task ledger

Fresh complete fetch, branch listing, recent history and working-tree reads
found only main and research/ongoing, with no newer external increment at
recovery. The SC-011/012 predecessor's recorded hosted success was retained
as predecessor evidence, not attributed to the new tree. Shared state and
publication remained under one coordinator; no permanent agent branch was
created. The starting open question was PM-QUESTION-0001, existence of one
sufficient seed orbit for every m>=3.

| Task | Question, assumptions and initial evidence | Allowed scope and independence | Stop condition and handoff |
| --- | --- | --- | --- |
| PM-CYCLE9-A | Derive a structural obstruction for a seed {1,a,b} in the square subgroup; start with SC-009/011 and the open existence quantifier | Read-only repository, temporary proof notes; independently propose theory before cross-review | Component theorem and strict kernel lower bound; later independent coordinate-multiplication trace check; full mathematical notes preserved |
| PM-CYCLE9-B | Can exact cyclic gcd certificates resolve the next structural test? Assume the established full kernel m+1 and retain bad F_81 control | Initially independent compact field/bitplane search; later assigned only single_orbit_search.py, its test file and SC-013/COMPUTATION.md; no publishing | Connected m=6 counterexample with explicit extra mode; full m<=6 census, selected m7/8 good certificates, 13 negative-control tests |
| PM-CYCLE9-C | Does a primary cyclic-code theorem already settle the one-weight-three-generator question? | Bounded Parallel Search plus primary-source checks; only the literature gate file | Separate length q-1 cyclic results, odd-degree Hamming connection and exact unit reformulation; no matching theorem found within the bounded search |
| PM-CYCLE9-E | Challenge the component bound and B's actual polynomial/field claims | Read-only proof review; independently code ordinary coefficient-list long division without project/B imports | Accepted theorem, both m6 gcds and trace separator; independently rebuilt all m3..6 orbit sets and gcd degrees; accepted actual saved RESULTS/COMPUTATION manuscripts |

## Accepted mathematics and rejected routes

A's PM-THEOREM-0017 identifies the connected components as cosets of
H=<a,b>. The F3 span of H is a field, and averaging H puts zero in its
affine hull. Each component therefore supports d+1 independent affine kernel
functions, giving [S:H]*(d+1). The written cardinality inequality makes this
strictly larger than m+1 for H<S. E separately accepted every step; the
coordinator rechecked the affine-span argument and strict inequality.

B then refuted the proposed converse, not the original existence question.
In F729=F3[X]/(X6+X+2), gamma=X2, the seed {0,25,311} is connected but its
trinomial gcd has degree 13, not 7. E independently recovered the exact gcd
using ordinary polynomial division. A independently multiplied six-coordinate
field vectors and checked that Tr(u34) obeys all 364 sparse equations but
has values 0,0,1 on the real edge {0,5,255}. E independently reproduced
that separator as well. SC-013 gives the complete proof and polynomial
factors. These are software arithmetic reviews and manual proofs, not Lean.

Failed routes remain explicit: principal ideals give a generator, but not
necessarily one of weight three; rejecting each frequency with some seed
cannot be exchanged with selecting one seed rejecting every frequency;
connectivity alone is now disproved. The m6 counterexample has a full-length
extra Frobenius orbit, so its absolute-trace witness with coefficient one
is nonzero. For a shorter orbit one must control relative trace, rather than
automatically reusing coefficient one.

B's complete census is only m=3,4,5,6 with 1,3,10,30 orbits. E independently
rebuilt those orbit sets and every gcd degree from coefficient-list arithmetic.
The m7/8 certificates stop at a first good seed. No all-degree existence
statement or general field-level failure is claimed.

## Verification and limitations

The coordinator inspected the exact source, proof and tests, integrated the
actual independent programs and regenerated their receipts. The combined
suite passed 102 tests, with an actual saved log; 13 new tests reject corrupt
Bezout data, divisibility, gcd degree, connectivity, trace values, scan omission,
a false completeness flag and a nonprimitive modulus. The main checker uses
SC-011 polynomial arithmetic, while both independent programs import no
project modules. The separate E program requires ordinary Python without -O.
An attempted optional SymPy import in the independent scratch work was
unavailable; the accepted calculation uses the recorded independent code,
not SymPy. No failed optional import is presented as a successful check.

The command log records actual root-level executions. sc013-SHA256.json
records file hashes at this checkpoint. The workflow adds three replay steps:
full report plus verification, independent gcd/census check, independent
coordinate trace check. Hosted results must be read for the new mathematical
commit after publication; predecessor CI is not a substitute.

Classical component, affine-span, cyclic-code and trace tools are credited.
The bounded literature gate does not establish originality. There is no
human peer review, Lean formalization, final academic release or general
single-orbit existence proof. The next precise operation is the simultaneous
forbidden-frequency avoidance/covering problem in ROADMAP, not more positive
small-field sampling.

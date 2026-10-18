# PM-DYNAMIC-C — final production audit

Scope: complete tools/dynamic_readout.py, complete
tests/test_dynamic_readout.py, and the new manuscript section6
PM-READOUT0004. No new literature, broad enumeration, Git or repository edits.
This supplements the independent mathematical audit in /tmp/PM-DYNAMIC-C.md.

## Verdict

No substantive semantic, cost, validation or hidden-execution defect found
within the stated input/program grammar. The six production tests and the
bounded direct probes below pass. This is manual scoped acceptance, not
formal verification or complete factoring/invariant-discovery acceptance.

## Actual inspected SHA-256

| File | SHA-256 |
| --- | --- |
| tools/dynamic_readout.py | 58f15528be1d509fc7d050fdc76019c13fbdf6d358c27b659b4d7935ecd10a1b |
| tests/test_dynamic_readout.py | 8bce653d5553744eb1233892ab95307eebf2d4b742c372ea60cbb523ce7ddbdc |
| research/mechanisms/FACTOR_READOUT.md | 2a5a512d823babfd5d507446b133477e5d4e3a9d7f398006af851bd226bf4161 |

## Semantic/cost challenge

`validate` accepts only seven listed instruction forms, requires literal
string return labels, and validates each non-return successor as an exact
integer strictly between the current index and program length. Thus booleans,
back edges, self edges, out-of-range edges and cycles are rejected. All
finite paths terminate at a return: a last-index non-return instruction
cannot satisfy the successor check. Register operands/destinations and
constants have exact permitted types. Uninitialized registers are checked
when reached, which is appropriate for path-dependent initialization.

There is no eval, callback, field-to-integer conversion, field comparison
other than gcd zero-tests, or raw-register return operation. Python arbitrary
object/security hardening is outside this literal JSON-like data grammar.
The supplied program itself may embody costly prior discovery; this compiler
does not claim to synthesize it.

Input representatives have degree<n and remain so: constants are reduced
modp, sums/differences preserve degree, products and inverses are reduced
modf. Each quotient register therefore specializes correctly in every CRT
field, including mixed extension degrees. A gcd1 test means every component
nonzero, gcdf means every component zero, and a proper gcd is an exact
nontrivial factor. The `inv` instruction checks its denominator before
extended Euclid; the inverse's final scalar normalization and reduction are
correct. All-zero inverse inputs raise ValueError. A mixed inverse can yield
a valid factor even when the original unguarded scalar routine would be
undefined somewhere; this is a valid extra guarded behavior, not evidence
that such a routine satisfies the theorem's all-components-defined premise.

`COMMON` follows only after a common PC/control transcript reaches a literal
return label. Field registers cannot leak into that label. It correctly does
not claim that the procedure distinguished anything or that no other useful
procedure exists. A mixed test may return SPLIT even if both successors
eventually have the same literal output; the theorem promises differing
outputs imply splitting, not the converse.

Each arithmetic/gcd/inverse instruction costs O(n^2) Fp operations with
standard dense quotient/extended-Euclidean arithmetic. Forward paths visit
at most the program length and the simulation follows a common scalar
prefix until a split. Square-free preprocessing costs O(n^2), giving the
stated O((T+1)n^2) bound when T includes zero-tests. Validation of all nodes,
input register loading, integer/control work, literal/visited output lengths
are extra input/control/output cost, as the manuscript expressly says.
Primehood is promised and no hidden field enumeration or primality trial
division is introduced.

New manuscript section6 preserves all these hypotheses, rejects the raw
`return X` strengthening, charges auxiliary construction, and treats the
Poonen/Hypothesis Z comparison as classical and conditional. Its scope agrees
with the audited production DAG, which is a restricted finite literal-output
implementation of the more general common-prefix theorem.

## Commands and actual results

From /workspace/scratch/415407b3c01b/ProofMotifs:

    python -m unittest discover -s tests -p 'test_dynamic_readout.py' -v

Result: all6 tests pass: mixed/common output, mixed/all-zero inverse handling,
unit inverse identity, mixed-degree CRT components, forbidden raw-output and
cycle grammar, missing registers and nonreduced input rejection.

A bounded standard-library direct probe imported the production module and
checked its inverse of X modulo (X-1)(X^2+1) over F3 by multiplying/reducing
to1; checked an immediate literal return gives COMMON; rejected successor
values True,-1,0,2,1.0 in a two-node const/return DAG; and accepted the valid
forward successor1. Its final output was:

    PASS: mixed-extension inverse, branchless literal COMMON, invalid and valid successors

The first development version of that probe mistakenly included valid
successor1 in its invalid list and raised its own assertion. Correcting the
probe, not production, gave the passing result. No new exhaustive panel was
run, and no mathematical correctness inference rests solely on finite tests.

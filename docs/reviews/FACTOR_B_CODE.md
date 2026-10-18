# PM-FACTOR-B-CODE — independent root implementation audit

Scope: read-only audit of tools/factor_readout.py,
tools/orientation_readout.py, tests/test_factor_readout.py and
tests/test_orientation_readout.py. All four files were read fully. No root
implementation or test file was edited, and no Git operation was used. The
only authored file for this follow-up is this handoff. The preceding
independent mathematics remains /tmp/PM-FACTOR-B.md and its exact checker.
No source142 proof was read for this follow-up: the orientation operation
below was verified directly from the implementation's arithmetic.

## Decision

Mathematical correctness: PASS for the stated promised-prime contracts.
Small-label readout is a certificate verifier and induced-partition extractor,
not label/test discovery. Orientation construction is root-free conditional on
a supplied full 2-primary generator, whose order it validates. It does not
discover that generator and does not satisfy the original input-only transfer.
Two cost-contract caveats are given below; neither changes mathematical
correctness on supported inputs.

## Small-label and closure audit

`checked_input` validates an integer p>=2, explicitly PROMISED prime, and a
positive-degree monic squarefree modulus. It contains no trial-division or
other hidden primality test. Composite-modulus behavior is outside its
contract; primehood metadata is accurate.

`readout` reduces each observable b modulo f and verifies the exact identity
W(b)=0 for W(T)=product_{a in labels}(T-a), where labels are distinct canonical
Fp elements. This implies b^p=b because W divides T^p-T. Thus no missing
Frobenius-fixed hypothesis is being silently assumed.

Each gcd block is exactly one nonempty label fibre, so the product invariant
and m<=r hold, where r=dim ker(Frobenius-I). The output is COMPLETE iff m=r;
otherwise its blocks are a certified coprime partition. No tests or label
roots are synthesized. The raw X^2 example correctly demonstrates that full
observable-algebra rank is not itself a known-small-label readout certificate.

`generated_basis` is correct: it starts from1, keeps independent original
vectors with normalized echelon reducers, and offers each accepted vector
times each generator. When the queue empties the accepted span contains1,
contains the generators and is invariant under all generators; hence it is
exactly the unital generated algebra. Reducing newly offered vectors against
the existing pivot rows is valid even when a new pivot occurs before an old
pivot: normalized old rows have zero entries before their pivots. Distinct
pivots certify independence. If there are s generators and m accepted basis
vectors, the implementation offers exactly s*m products, with m<=r for
validated labels. No subset-product/field-label enumeration is hidden here.

For normalized degree<n observable inputs, its FIELD-OPERATION bound is

  O(n^3+n^2 log p+K n^2+s r n^2),

where K is the total number of supplied labels, and s the number of tests.
The last term accounts for generated-algebra closure and reductions rather
than pretending the implementation only performs gcd branching.

Cost caveat1: `pending.pop(0)` on a Python list adds O((s*r)^2) worst-case
pointer/bookkeeping work. For an actual bit/runtime bound with the stated
linear dependence on s, use a deque or a head-index queue. The field-operation
count itself is correct. This can matter when the user supplies many repeated
tests, even with n=1.

Cost caveat2: the API accepts arbitrary-length observable coefficient lists,
then reduces them. An n-only cost must either require degree<n input or add
input scanning/reduction costs, for example O(n*sum_j len(poly_j)) field
operations for the unreduced polynomials. The mathematical theorem already
uses degree<n representatives. The modulus has the analogous ordinary
encoding/canonicalization cost. Missing test dictionary keys or non-dictionary
tests may raise KeyError/TypeError rather than ValueError; they are rejected,
but a stricter public API error-type contract would require extra validation.

## Orientation audit

Let N=deg F, with p promised odd prime, F monic squarefree totally split,
N even>=2, p>N. Tensor coefficients represent the faithful power basis of
Fp[X,Y]/(F(X),F(Y)). `Tensor.multiply` first convolves then reduces descending
X degrees and descending Y degrees. Although discarded high-degree cells are
not explicitly zeroed, all their contributions are propagated before the next
lower degree is processed and they are never returned, so this is correct.
`swap` transposes X and Y. The setup checks total splitting by dim B=N.

Let delta=X-Y, off=delta^(p-1), p-1=2^s*t with t odd. On the unknown root-pair
grid, off is the off-diagonal indicator. The supplied canonical u is checked
by u^(2^s)=1 and u^(2^(s-1))!=1. Since p is promised prime, this is precisely
full order2^s, not just a vaguely nontrivial element.

Set z=delta^t. Off diagonal, z=u^k for a unique k modulo2^s. Inductively each
nonempty mask in `parts` selects positions whose k has the recorded lower j
bits ell. At digit j, raising z to exponent2^(s-1-j) and comparing it with
u^(ell*exponent) distinguishes bit0 from bit1. Multiplying the difference by
the old mask before taking its (p-1)-st power gives the indicator of its
nonzero positions WITHIN that mask. Hence zero and one are disjoint Boolean
submasks, and their union is the old mask. Pruning an all-zero coefficient
list is a legal faithfulness test, not a root/evaluation oracle.

There are at most N(N-1) nonempty disjoint masks; this bound is on actual
root-pair support, not on all p values or all2^s possible logs. At the end
the selected masks have k<2^(s-1). Replacing delta by -delta changes z to -z
because t is odd, adding2^(s-1) to k; this flips the top bit. The constructed
e therefore satisfies e^2=e and e+swap(e)=off, with zero diagonal.

`verify_orientation` independently checks those finite tensor identities.
Its partial trace is the trace of multiplication in the SECOND quotient
factor: the code computes Tr(M_(Y^j)) by summing the diagonal coefficients
of Y^(j+k) mod F for k=0,...,N-1. In the split algebra this equals the sum
over second-coordinate roots. Thus c=(id tensor Tr)(e) has the tournament
row counts as its values, each an integer in0,...,N-1. If all row counts
were d, then Nd=N(N-1)/2, forcing d=(N-1)/2, impossible for even N.
Because p>N these distinct integer counts stay distinct modulo p, so c is
nonconstant. Scanning the N KNOWN labels0,...,N-1 finds a proper gcd factor.
This is an N-sized readout, not a p-sized search. The odd cyclic tournament
and half-off-diagonal non-Boolean tests correctly isolate the two key gates.

A conservative implementation bound is O(N^6 (log p)^2) field operations,
with naive O(N^4) tensor multiplication, O(log p) digit levels, at mostN(N-1)
masks and O(log p) multiplications per Fermat-zero test. Storage is O(N^4)
field elements for all masks. This is conditional polynomial time, not
full-generator discovery. Internal `Tensor.power` assumes its internal
nonnegative integer exponents, which the public constructor/verifier ensure.

## Actual commands and results

Executed from /workspace/scratch/415407b3c01b/ProofMotifs:

  python -m unittest tests.test_factor_readout tests.test_orientation_readout -v

Result: all18 tests passed; exit0; reported0.018seconds.

Then two separate in-process instrumentation scripts were run with
PYTHONDONTWRITEBYTECODE=1; they imported the ROOT modules without modifying
their files, counted tensor multiplications/powers, constructed F from fixture
roots, and called only construct(p,F,u). Fixture roots were not passed into
the constructor and were used after return to independently verify every
tensor grid value, orientation/diagonal/transpose, partial-trace row counts,
the exact gcd factor and complementary factor product.

Audit1:

  p=65537, N=6, fixture roots=[1,2,3,4,5,6], u=3
  F=[720,63773,1624,64802,175,65516,1]
  digit_levels=16; maximum_nonempty_masks=10
  row_counts=[3,3,2,3,2,2]
  factor_label=2; factor=[65447,63,65523,1]
  tensor_multiply=1179; tensor_power=71; max_power_bits=17
  measured constructor time=0.175seconds; exit0

Audit2 saturates the support-mask bound because the ordered nonzero
differences among powers of2 are distinct:

  p=65537, N=6, fixture roots=[1,2,4,8,16,32], u=3
  F=[32768,1025,41664,54377,1302,65474,1]
  digit_levels=16; maximum_nonempty_masks=30=N(N-1)
  row_counts=[1,4,3,3,1,3]
  factor_label=1; factor=[16,65520,1]=(X-1)(X-16)
  tensor_multiply=2167; tensor_power=123; max_power_bits=17
  measured constructor time=0.401seconds; exit0

The second script additionally checked the independent Lucas primality
certificate pow(3,65536,65537)=1 and
gcd(pow(3,32768,65537)-1,65537)=1, using the known complete factorization
65536=2^16. This was an audit-only check OUTSIDE the solver, not hidden
primehood validation. Neither numerical script loops through Fp.

A final deterministic closure audit used p=65537 and F=X^8-1, comparing
expected algebra dimensions for zero, constant, X^2, X^4, (X^2,X^4),
(X^2,X^3), and duplicated/constant-augmented generators. Expected dimensions
were1,1,4,2,4,8,4. All seven passed; every accepted-basis/generator product
was separately rechecked by rank recomputation, and every offer count was
exactly s*m. The full case (X^2,X^3) checks that closure is iterated rather
than stopping after the initially supplied span.

These are exact implementation checks plus an independent argument, not a
formal proof assistant certification, source142 analytic dependency audit,
novelty finding, or claim of uniform deterministic factoring from f alone.

## Final snapshot recheck after coordinator fixes

The earlier18-test run and its caveats above are preserved as the actual
earlier audit. I did not personally run the intermediate19-test state.
I subsequently reread all four final code/test files, read the FULL
research/mechanisms/FACTOR_READOUT.md, and reran

  PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_factor_readout tests.test_orientation_readout -v

Actual result:20 tests passed, exit0, reported0.019seconds. The coordinator
replaced the list queue by deque/popleft, enforced degree<n observable lists,
and added explicit malformed-test ValueErrors. Both earlier cost caveats are
therefore RESOLVED for the final supported contract. Negative tensor powers
are now explicitly rejected and tested as well.

Accepted mathematical proof scope in FACTOR_READOUT.md: sections2–4 and the
local conditional orientation proof in section5, including support identities,
closure, completeness, optimal existential lengths, scalar-label distinction,
supplied-nonresidue equivalence, corner-algebra unit condition, mask digit
refinement, ordinary trace and even-N count argument. I agree that p>N follows
from total splitting, squarefreeness and odd-p/even-N parity. Section6's source
and prior-art/dependency statements were read but not independently accepted
as a full source142/analytic or primary-literature audit; the section properly
marks that dependency closure unchecked. No source142 proof was read here.

Content SHA256 values of the audited final snapshot:

  tools/factor_readout.py
    14ea390f2ae5fe335918a5b62872c9fb659b64d5f6935bbbfe6e8be2c0e5718f
  tools/orientation_readout.py
    eff066d4527133173d1ef6cab63e66670217f808ba19b460d7b248d96d25def8
  tests/test_factor_readout.py
    ede7368c29a37eff15123ed71b22186c3fa738ddadc996a474af997e80c4cdb5
  tests/test_orientation_readout.py
    35dd245859d9719d555e30d80e6c3d3d292ea2ec7d2e63d7882f1253df7549d6
  research/mechanisms/FACTOR_READOUT.md
    ed41e6b3ea47ada88535205adbe5657b29845a23e8ffb40761a83388cf42a42c

Saved repeatable high-primary audit as /tmp/PM-FACTOR-B-orientation.py and ran

  PYTHONDONTWRITEBYTECODE=1 python /tmp/PM-FACTOR-B-orientation.py --repo /workspace/scratch/415407b3c01b/ProofMotifs

Exit0, JSON statusPASS. Both fixtures reproduced exactly the row counts,
factors, mask maxima and operation counters reported above. Unlike an
independent constructor, this script tests the production constructor; its
grid/trace/factor oracle is independent local polynomial/Horner arithmetic
and fixture roots. It does not call production arithmetic for the oracle or
pass roots into the constructor. This independence scope is explicit in its
docstring and JSON. No further enumeration research was performed.

Final additional bounded compiler audit: new tools/dynamic_readout.py,
tests/test_dynamic_readout.py and manuscript section6 were read; independent
dynamic proof and production review are in /tmp/PM-DYNAMIC-B.md. The separate
6 dynamic tests and combined26-test suite both passed (combined0.027seconds).
This does not supersede the preserved actual18-test/20-test earlier snapshots.
I accept the compiler proof, but have NOT read Poonen; source attribution is
outside this review. Updated manuscript SHA256 after section6 addition is
2a5a512d823babfd5d507446b133477e5d4e3a9d7f398006af851bd226bf4161.
Replay script SHA256 is
704ca271bce6bae2664a3a2c646375ff940dc6c1fa86635f4cf917b547c076fc.

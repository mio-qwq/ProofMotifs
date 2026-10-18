# PM-FACTOR-A addendum: source-informed production audit

Read-only review after delivering the independent derivation in
/tmp/PM-FACTOR-A.md. This is an independent mathematical/code review, not an
unread transfer. No selected source142 file was read; the coordinator supplied
its oriented-mask summary before this addendum. No peer research notes or
Git commands were used. Only this own /tmp addendum was written.

## Reviewed scope and disposition

Read completely:

- research/mechanisms/FACTOR_READOUT.md (whole manuscript);
- tools/factor_readout.py;
- tools/orientation_readout.py;
- tests/test_factor_readout.py;
- tests/test_orientation_readout.py.

The manuscript's PM-READOUT0001–0003 and conditional PM-ORIENTATION0001 are
mathematically sound under the stated promised-prime/squarefree/known-label
or supplied-primary-data contracts. The production algorithms implement those
scoped operations without a root list or field scan. The readout algorithm
does NOT synthesize useful tests; the orientation constructor DOES synthesize
a useful mask, conditionally on the supplied multiplicative datum. Neither
result certifies the selected source's unconditional factorization headline.

One substantive domain wording issue was found and immediately reported:
z=Delta^t is zero on the diagonal, so it is NOT a unit of the whole tensor
algebra and cannot globally have multiplicative order dividing 2^s. The
coordinator repaired the text to work in the off-diagonal corner dR with
identity d, where z^(2^s)=d. The code always began with mask d and did not
use a z inverse, so no algorithmic change was needed for that correction.

## Independent proof of the conditional constructor

Let F be monic squarefree totally split, of even degree N>=2, over F_p for
odd prime p. There are N distinct roots, so N<=p; since N is even and p
odd, N<p. Thus the p>N input check is redundant but harmless, not an
independent mathematical obstacle. The code certifies total splitting by
fixed-space dimension N; this implies Frobenius is the identity on A,
equivalently F divides X^p-X. These facts do not require roots to be supplied.

For proof only, identify R=A tensor A with F_p-valued functions on the N^2
ordered root pairs. Delta=X-Y vanishes exactly on the diagonal, hence
d=Delta^(p-1) is the Boolean off-diagonal indicator. Write p-1=2^s t with
t odd, and suppose u has exact order 2^s; the code checks precisely this by
u^(2^s)=1 and u^(2^(s-1))!=1. On the off-diagonal corner every
z=Delta^t is a power u^k with a unique residue k mod 2^s, and z^(2^s)=d.

Maintain disjoint nonzero Boolean masks indexed by the known lower j bits
ell of k. Initially j=0, ell=0, and the mask is d. At level j define
E=2^(s-1-j). On a mask with k congruent ell mod 2^j, equality

    z^E = u^(ell E)

is equivalent to k congruent ell mod 2^(j+1), exactly that the next bit is
zero. For a Boolean current mask q and any w, the expression

    q - (q w)^(p-1)

equals 1 exactly where q=1 and w=0, and equals 0 elsewhere. Its complement
inside q is the next-bit-one mask. This is exactly the code's difference,
zero and one construction. Booleanity, disjointness and union d therefore
hold by induction. A nonzero mask contains at least one of the N(N-1)
off-diagonal pairs, so at most N(N-1) masks survive at every level. Testing
whether a mask is zero by its normal-form coefficient list is exact because
the displayed quotient basis is faithful.

At level s the masks are exact logarithm fibers. Let e be the union of
fibers with 0<=k<2^(s-1). Swapping X,Y sends Delta to -Delta and z to -z,
because t is odd. Since -1=u^(2^(s-1)), swap shifts k by 2^(s-1), swapping
the selected and unselected halves. Thus e^2=e and e+swap(e)=d.

For any supplied tensor satisfying those two identities, total splitting
and p odd imply it is a tournament orientation: on a diagonal pair the
additive identity says 2e=0, hence e=0; at every off-diagonal pair its
idempotent value is 0 or 1, and exactly one of the two directions is 1.
The code's partial_trace is the ordinary trace of multiplication in the
second A factor. In root coordinates it is therefore the row sum c_i,
the ordinary integer outdegree interpreted modulo p. Each lies in
{0,...,N-1}, and their integer sum is N(N-1)/2.

If c were scalar in A, all integer outdegrees would be congruent modulo p.
Since 0<=c_i<N<p, they would actually be equal as integers. Their common
value would be (N-1)/2, impossible for even N. Thus c is nonscalar. Scanning
only the known labels a=0,...,N-1 must find a nonempty proper fiber, and
gcd(F,c-a) gives a proper factor. There is no scan of F_p and no root
enumeration in this proof or implementation. The proof necessarily uses
total splitting, Booleanity, swap symmetry, even N, and p>N (the latter is
automatic on the input class).

## Input-strength comparison: primary datum equals a nonresidue

The supplied full 2-primary generator is polynomial-time equivalent in
strength to a supplied quadratic nonresidue. If v is any nonsquare, put
u=v^t; writing v=g^k in the mathematically existing cyclic group F_p^*, k
is odd, so u has exact order 2^s. Conversely any u of exact order 2^s obeys
u^((p-1)/2)=(u^(2^(s-1)))^t=(-1)^t=-1, so u is itself nonsquare.
These conversions and checks use O(log p) scalar powering operations; they
do not discover a nonresidue from raw p.

This matches the auxiliary-input scope of the original Rónyai1988
*Factoring polynomials over finite fields*, Journal of Algorithms9,
pp391–400, DOI10.1016/0196-6774(88)90029-6: its primary publication abstract
states an even-degree completely-split local factor result given a quadratic
nonresidue. Only that abstract was accessed, not the article body, so no
complete proof identity or priority adjudication follows here.

## Code and cost audit

Tensor multiplication correctly convolves bidegrees then reduces descending
X and Y degrees with the monic F relation. It costs O(N^4) field operations;
the unreduced high coefficient cells need not be zeroed because subsequent
steps only consume the appropriate lower-degree cells. The swap is exactly
coefficient transpose. In partial_trace, for each j the code computes the
sum over k of the x^k coefficient of x^(j+k) mod F, precisely
Tr(M_(x^j)); linearity gives the required partial multiplication trace.

Binary powering uses O(log p) tensor products for every exponent that
appears. There are s<=log_2 p levels and O(N^2) masks per level, hence the
stated conservative O(N^6(log p)^2) field-operation bound is correct. The
extra scalar powers u^(ell E) have exponent of bitlength O(log p), not
numerical length 2^s. The masks cost O(N^4) field storage (old plus new
levels); this is polynomial but not O(N^2). A verifier supplied with e
recomputes d, Booleanity/symmetry, partial trace and bounded-label gcds in
O(N^4 log p) field operations, with the squarefree/fixed-space setup
dominated by that bound. Each field operation has polynomial bit cost in
log p under the prime promise; all input integer lengths are charged.

The generic readout verifies each support product over distinct canonical
known labels. That product dividing T^p-T implies fixedness even without
reducedness; squarefreeness is separately used for the component/factor
interpretation. Every gcd stage partitions current blocks, and finite
coordinate interpolation proves the claimed equality of leaf count and
generated-algebra dimension. The independent deque closure expands only
retained independent vectors and is safe because quotient congruence
preserves discarded combinations under multiplication. At most t*m product
candidates are offered, with O(t*r*n^2) closure cost. Its queue storage is
correctly disclosed as potentially O(t*r*n) fields. Degree<n inputs and
all explicit labels/circuit lengths are charged. No rank telemetry or
COMPLETE label from the caller is trusted.

For the generic binary-test theorem, the minimum existential family length
ceil(log_2 r) and the polynomial-time factorization/synthesis equivalence
are correct, including r=1 and characteristic2. For p-valued generators,
ceil(log_p r) is likewise only an existential generator count; it must not
be read as known scalar-label discovery. The manuscript distinguishes this.
The fixed-family pigeonhole obstruction is correctly restricted to that
fixed family and does not establish an adaptive-algorithm lower bound.

The public Tensor.power method originally lacked a negative-exponent guard;
public construct/verify_orientation never called it negatively, so this
was not a mathematical input-contract failure. During review the coordinator
added its guard and a regression test. No remaining production-code defect
was found in the reviewed supported input domain.

## Exact test receipt and reviewed versions

Command run read-only with bytecode writes disabled:

    python -B -m unittest discover -s tests -p 'test_*readout.py' -v

Exit code0, final output:

    Ran 20 tests in 0.019s
    OK

The tests include complete/partial known-label readouts, sharp binary-length
fixtures, characteristic2, empty-family irreducibility, degree/type/support
rejections, raw-generator rank not being label readout, conditional mask
construction, full-primary order rejection, tensor-product/grid agreement,
half-offdiagonal non-Booleanity, odd-three-cycle constant trace, nonsplit/
nonreduced rejection, corrupted masks, and the tensor power guard. They are
exact finite implementation controls, not a proof of the source headline.

SHA256 values read after the full test run (not Git identifiers):

    0b309c271855c9e5f75db7d61c407faede96aa526675f30b34afe8cdd54f3b3a  research/mechanisms/FACTOR_READOUT.md
    14ea390f2ae5fe335918a5b62872c9fb659b64d5f6935bbbfe6e8be2c0e5718f  tools/factor_readout.py
    eff066d4527133173d1ef6cab63e66670217f808ba19b460d7b248d96d25def8  tools/orientation_readout.py
    ede7368c29a37eff15123ed71b22186c3fa738ddadc996a474af997e80c4cdb5  tests/test_factor_readout.py
    35dd245859d9719d555e30d80e6c3d3d292ea2ec7d2e63d7882f1253df7549d6  tests/test_orientation_readout.py

The repository was concurrently edited by its coordinator. The two reported
repairs are visible in these reviewed versions; this review does not silently
extend to later edits. No Lean compilation or formal dependency audit was
performed. Full original Berlekamp1967/1970 bodies, full Rónyai1988 body,
the selected source's odd-degree/analytic dependencies, and its headline
remain outside the accepted scope. No further mirror retry was attempted
after the coordinator's stop request.

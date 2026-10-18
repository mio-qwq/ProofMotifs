# PM-FACTOR-C code audit addendum

Task ID PM-FACTOR-C, follow-up: audit production readout/orientation semantics,
validation and cost. Scope was read-only repository plus own temporary notes
and checker, no Git, production edits, children or external writes. Input p is
promised prime; failure to trial-divide is deliberate and correct for that
contract. This audit neither discovers supplied generators nor validates the
full source142 odd splitter, analytic companion or headline factorizer.

## Audited versions

All four files were read fully in
/workspace/scratch/415407b3c01b/ProofMotifs. SHA-256 at audit:

| File | SHA-256 |
| --- | --- |
| tools/factor_readout.py | a235bfa57c394dad97211f0acb3821b72da90a8c1453e88871b3f1000a846b5d |
| tools/orientation_readout.py | 1bb64f48ccdedef477bfba8d96fe2687cd040e72a33a7b8c080b30816caf670d |
| tests/test_factor_readout.py | bcdfb632789c8869276ad017ebd0d2d9e4b0b858e3a1c587d160c22da8f401d3 |
| tests/test_orientation_readout.py | e629ca6ad327b7ed3024b81b545226e11afc0427967f33239b92fb20f1908fa8 |

## Result

No substantive within-contract semantic or cost bug found. This is a scoped
manual argument plus exact finite tests, not formal verification or a
production-hardening/security audit.

### factor_readout.py

Lines110–120 validate positive-degree monic square-free input, without
pretending to prove primehood. The derivative coefficient ordering is
correct. Lines123–133 construct Frob-id columns on the standard quotient
basis and transpose them before taking the kernel; this is the correct
Berlekamp fixed-space dimension.

Lines169–183 verify the actual finite-label relation
product_(c in S)(b-c)=0 modulo f with distinct canonical c in Fp. Every
irreducible-component value of b must therefore equal a member of S,
so b belongs to the Frobenius-fixed algebra. Extra unused supplied labels
are harmless; missing labels are rejected rather than inferred. This
certificate is stronger than an unsupported assertion that an arbitrary
raw quotient generator is suitable for readout.

Lines185–201 compute exactly the common fibre partition of all supplied
observables. Distinct scalar labels give disjoint gcd factors; the verified
annihilator relation makes their product the current block. Thus the final
blocks are coprime and multiply to f. Each is a union of irreducible factors;
having precisely r blocks is equivalent to all of them being irreducible.
The independent generated-algebra dimension check agrees with this count.

The closure at lines136–155 enqueues products only from retained independent
vectors. This is sound: after termination their span contains1 and is
stable under every supplied multiplication operator. Every accepted vector
is a generated word, so the span is exactly the generated unital algebra.
Normalized reducer rows have zeros before their pivot; insertion of a new
pivot before an old pivot does not invalidate subsequent forward reduction.
At most n basis vectors are accepted and at most tn product offers are
made. Using raw accepted vectors rather than their reduced remainders is
valid, since reduction proves independence and raw products remain in the
same generated algebra.

Cost caveats that must remain explicit in the theorem: count the supplied
test/label descriptions and any unreduced polynomial input lengths. The
algorithm is polynomial in these explicit data and n,logp; a caller listing
all p labels supplies an input of size at least p, not a hidden poly(logp)
factorization. No claim of discovering the observables follows from its
certificate checks or dimension closure.

### orientation_readout.py

Lines76–83 check even N>=2, odd promised prime p>N, square-freeness, and
dim(B_F)=N. For square-free degreeN, the last equality means every irreducible
factor has degree1, hence total splitting. No roots are computed.

The flattened tensor indexing is i*N+j for X^iY^j. Lines29–49 correctly
multiply and reduce in Fp[X,Y]/(F(X),F(Y)). High rows/columns are not cleared,
but after descending monic reduction they are never read into the returned
low-degree rectangle; leaving them populated is not a bug.

Lines114–119 extract only v2(p-1) by repeated division by2 and certify
ord(u)=2^s by u^(2^s)=1 and u^(2^(s-1))!=1. No factorization of the odd part
of p-1 and no generator search occur. The inspected demo supplies u28 mod97,
whose order32 is correctly checked; a removed transient comment does not
affect the audited delivered code.

Let z=Delta^t. At digit j, each mask carries the already-determined low-j
logarithm ell. The equality z^(2^(s-1-j))=u^(ell*2^(s-1-j)) exactly tests
whether the next binary digit is0. On that mask, the Fermat power of the
difference is1 exactly where the difference is nonzero and0 otherwise.
Consequently lines131–138 create complementary idempotent submasks with the
correct updated digits. Outside the mask both terms are0. Dropping zero
coefficient tensors is a valid nonemptiness test because the quotient's
standard tensor monomials are a basis.

There are at most N(N-1) nonempty disjoint masks on off-diagonal root pairs.
Selecting final logs in the lower half gives exactly one orientation per
unordered pair, because t is odd and log(-1)=2^(s-1). All computation is in
the tensor quotient: the only explicit enumeration is of digits/masks and
bounded row labels, not unknown roots.

Lines63–73 compute ordinary multiplication trace of Y^j by summing its
matrix diagonal in the monomial basis, then apply it to the second tensor
factor. In a split reduced algebra this is the unnormalized sum over roots,
so the resulting polynomial's coordinates are integer row scores modp.
Lines95–96 independently check e^2=e and e+swap(e)=off; since p is odd,
these imply zero diagonal and one orientation of each off-diagonal pair.
Even N forces nonconstant integer scores in [0,N-1]. Since p>N, those scores
remain distinct whenever their integers differ. The labels0,...,N-1 suffice
to find a proper gcd. The returned factor is monic and properly divides F.

The O(N^6 L^2) Fp-operation bound, L=ceil(log2p), matches this implementation:
dense tensor multiplication costs O(N^4); each power costs O(L) such
multiplications; each of at most L levels treats at most N(N-1) masks.
Other tensor additions, generator modular powering, trace O(N^4), fixed-space
computation O(N^3+N^2L), and at most N final gcds are dominated. Integer
exponents have O(L) bits even though 2^s itself has large numerical value.
This is a field-operation bound; bit cost includes polynomial-in-L scalar
arithmetic. It is not a cost bound for finding u.

No genuine field-wrap counterexample fits the checked hypotheses:
square-free total splitting implies N<=p and even N with odd p excludes
N=p. The p>N guard is consistent and redundant, not evidence of an omitted
valid-input case.

## Validation nits outside substantive correctness

Malformed per-test objects at factor_readout.py line170, e.g. a missing
dictionary key or a non-dictionary item, cause KeyError/TypeError instead of
the otherwise-used ValueError. They are rejected and do not yield a false
factor/certificate; uniform error typing would be optional API hardening.
Tensor helper methods assume valid fixed-size tensors and nonnegative
integer exponents; direct use with a negative exponent can fail to terminate.
Public construct/verify entry points never supply such exponents. Do not
advertise those raw helpers as independently validated general APIs.

## Tests actually executed

From the repository:

    python -m unittest discover -s tests -p 'test_factor_readout.py' -v
    python -m unittest discover -s tests -p 'test_orientation_readout.py' -v

Result: 11 readout tests and7 orientation tests, all pass. Tests distinguish
manufacturing fixtures with known roots from passing roots into the solver.
The half-offdiagonal example correctly fails idempotency while satisfying
transpose symmetry; the odd3-cycle correctly shows a regular tournament
outside the even-input contract.

Independent reproducible check:

    python /tmp/PM-FACTOR-C-code-check.py

It imports my separate standard-library arithmetic from
/tmp/PM-FACTOR-C-check.py, then compares production readout against an
independent CRT/factor oracle. Across all270 square-free inputs in the
earlier bounded panel, all3992 single-observable Fp-valued assignments pass,
including nonbinary alphabets and mixed irreducible degrees. Expected
partitions, rank, completeness status and closure offer bound are checked.

The separate orientation oracle manufactures F using independent polynomial
arithmetic, calls the production constructor with only coefficients and a
supplied generator, then evaluates its output on the known root grid
*outside the solver*. All173 cases pass: exhaustive small-prime even root
subsets plus deterministic varied samples at primes11,...,257, N2/4/6.
The oracle checks Booleanity, zero diagonal, complementary transpose,
ordinary-trace row scores, nonconstant scores and proper divisibility using
independent division. The fixture's brute generator search is not called by
production and is not part of its claimed complexity.

Final independent output includes:

    PASS independent CRT-value oracle: 3992 general finite-label production readouts
    PASS independent point-value oracle: 173 root-free constructor cases, varied 2-valuations, N2/4/6

Finite testing does not prove infinite correctness; the preceding manual
invariants explain the code's semantics. No repository changes were made.

# PM-FACTOR-C — final mathematical/production acceptance audit

Task ID PM-FACTOR-C, final follow-up. I read the complete coordinator
manuscript research/mechanisms/FACTOR_READOUT.md and the complete current
production/test files, compared against my earlier read and SHA-256 records,
and reran the existing checks. No repository writes, Git operations, new
primary-source access or expanded enumeration were performed.

## Decision

The local mathematical claims PM-READOUT0001, PM-READOUT0002,
PM-READOUT0003 and conditional PM-ORIENTATION0001 pass this independent
manual adversarial audit under their explicit hypotheses. Production
semantics/cost pass the scoped code audit. This is not formal verification,
novelty acceptance, human specialist review, source142 headline verification,
an acceptance of the odd splitter or analytic companion, or AI-causal evidence.

The initial manuscript ambiguously assigned multiplicative order to
z=Delta^t in the full tensor algebra R, where it vanishes on the diagonal.
I objected; the inspected revision now explicitly uses the corner dR with
identity d, proves z^(2^s)=d, and states that z is not a unit in all R.
The implementation already had the correct masks. This resolves the actual
unit/representation issue rather than silently assuming an inverse.

I also requested the t=0 closure seed be counted; the revision uses
O((1+tr)n^2). Two final literal boundary phrasings were reported separately:
the deque starts with1 even when t=0 (storage O(1+tr), not O(tr)); and the
allowed explicit label set S_j can equal Fp, so the algorithm must be described
as avoiding an *implicit* field scan while charging its supplied label lists.
These do not change the main theorem or stated K-dependent algorithmic bound.

## Claim-by-claim challenge

- PM-READOUT0001: the square-free support polynomial divides T^p-T, so the
  finite support identity forces Frobenius fixedness in any commutative
  Fp-algebra. Under square-free f, CRT gives product fields and B=Fp^r.
  The gcd partition exactly matches joint scalar-value fibres. Fibre
  interpolation proves generated-algebra dimension equals the nonempty
  fibre count; no unknown coordinate value is used by the algorithm.
  The readout-only bound O(n^3+n^2 logp+Kn^2) is valid with explicit
  degree<n observables. Reduction of a degree<n b modulo a block H costs
  O(n degH), whose sum is O(n^2); subsequent gcd costs sum(degH)^2<=n^2.
  Thus the per-label bound is justified even for many small blocks.

- Closure prototype: each accepted raw word is independent; rejecting a
  dependent word does not lose its future products because multiplication
  respects quotient congruence and linear combinations. At most m accepted
  vectors give tm product offers. Incremental exact elimination and dense
  quotient multiplication give O((1+tr)n^2) field-operation work. The
  production code recomputes rather than trusts the telemetry. Honest circuit
  and explicit label lengths remain charged; no generator synthesis follows.

- PM-READOUT0002: binary coordinate codes require r<=2^t and are sufficient
  by CRT interpolation. The minimum ceil(log2r) includes r1/t0. Factorization
  constructs such an optimal family in polynomial time; any complete
  polynomial-output-size family supplies factorization by gcd readout.
  Requiring optimal length does not break either reduction. This is an
  equivalence of tasks, not a proved hardness lower bound. The analogous
  unrestricted Fp-valued minimum ceil(log_p r) is correct. A single scalar
  separator exists iff r<=p; monogenic A need not make B monogenic. In
  characteristic2 every fixed element is idempotent and a fixed-space basis
  supplies complete binary tests. No variable-p obstruction is asserted for
  this fixed-field case.

- PM-READOUT0003: the first linear dependence in1,b,...,b^n computes the
  minimal polynomial. For b in B it is the product of its distinct scalar
  values, but a claim that it splits does not enumerate those values. The
  large-prime example and supplied power-test labels have the stated partial
  and complete partitions. The fixed-test-family pigeonhole obstruction is
  limited correctly to a fixed family with product of label counts<p;
  it does not forbid adaptive input-dependent tests or a different algorithm.

- PM-ORIENTATION0001: total splitting plus square-freeness gives N<=p;
  odd p/even N imply N<p automatically. The supplied full2-primary generator
  is checked, not discovered. Its equivalence to a supplied quadratic
  nonresidue is valid: u has Euler value-1, and v^t has full2-primary order
  for a nonresidue v. The corner-unit digit mask invariant, transpose-half
  orientation, ordinary partial trace and bounded row-label gcd readout all
  check. Dense O(N^4) tensor multiplication over at most O(N^2 logp) masks
  with O(logp) powering work gives O(N^6(logp)^2) field operations. This
  does not charge a numerical2^s loop or supply a primitive-root oracle.

- Controls/limits: d/2 meets transpose symmetry but not Booleanity; an odd
  genuine three-cycle is Boolean with constant trace; X in F5[X]/X^2
  invalidates Fermat nonzero masking. No invalid N>=p counterexample is
  portrayed as satisfying the even splitter hypotheses. The macro table
  depends on pre-existing197/107/157 project audits, not a fresh source audit
  by this reviewer. The142 conditional mechanism is pair orientation and
  integer nondivisibility, not high-order cancellation merely because a
  p-1 exponent appears. The text keeps all PM-H questions, causal inference,
  original-source retrieval limits, odd geometry and companion acceptance
  separate; those limitations are appropriate.

## Production changes verified since earlier code audit

factor_readout.py now imports deque, uses popleft, rejects malformed per-test
objects uniformly with ValueError, and enforces degree<n coefficient-list
length. Those changes do not alter the proved generated-algebra/readout
semantics. orientation_readout.py now explicitly rejects negative or
noninteger tensor exponents, fixing the earlier raw-helper hardening issue;
no internal algorithm ever depended on a negative exponent.

Final production/test SHA-256:

| File | SHA-256 |
| --- | --- |
| tools/factor_readout.py | 14ea390f2ae5fe335918a5b62872c9fb659b64d5f6935bbbfe6e8be2c0e5718f |
| tools/orientation_readout.py | eff066d4527133173d1ef6cab63e66670217f808ba19b460d7b248d96d25def8 |
| tests/test_factor_readout.py | ede7368c29a37eff15123ed71b22186c3fa738ddadc996a474af997e80c4cdb5 |
| tests/test_orientation_readout.py | 35dd245859d9719d555e30d80e6c3d3d292ea2ec7d2e63d7882f1253df7549d6 |

The initial full manuscript read was SHA-256
eeefa42b898dfb587d1b0294b0e64c726ddf74ef707fa45e077907cc2bd803e7.
The inspected revision with the corner-unit clarification, closure seed
time and nonresidue equivalence was
0b309c271855c9e5f75db7d61c407faede96aa526675f30b34afe8cdd54f3b3a.
See final-update entry below for any final wording-only revision.

## Actual verification commands/results

From /workspace/scratch/415407b3c01b/ProofMotifs:

    python -m unittest discover -s tests -p 'test_factor_readout.py' -v
    python -m unittest discover -s tests -p 'test_orientation_readout.py' -v
    python /tmp/PM-FACTOR-C-code-check.py

All20 current production tests pass:12 readout,8 orientation. Existing
independent checks rerun unchanged:270 square-free inputs/3960 binary
families,3992 general finite-label readouts,173 point-grid orientation
checks, and the named negative controls all pass. This is a rerun of the
previous fixed panels, not new broad enumeration. Exact finite checks are
supporting evidence; the preceding invariant proofs provide the all-input
reasoning under the stated contracts.

## Final-update entry

The explicit-label scan sentence has been corrected and inspected: the
algorithm avoids an implicit Fp scan, iterates supplied label lists, and
charges their total length K. That revision's manuscript SHA-256 is
ed41e6b3ea47ada88535205adbe5657b29845a23e8ffb40761a83388cf42a42c.
The coordinator is aware of the remaining t=0 deque storage wording
O(1+tr) in place of O(tr). No unresolved mathematical or production blocker
remains. The production/test hashes above are unchanged and were rechecked.

The separately requested bounded classical dynamic-evaluation bridge audit
is in /tmp/PM-DYNAMIC-C.md. It accepts only transcript/control-determined
discrete outputs, shared integer inputs and properly charged tests/control;
raw field-output variation alone is explicitly insufficient. Primary
Poonen §§2–5 supplies the direct adaptive-readout comparison with Hypothesis Z
kept conditional. This does not expand acceptance to its geometric hypotheses
or full source142 dependencies.

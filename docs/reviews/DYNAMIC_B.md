# PM-DYNAMIC-B — bounded dynamic zero-query compiler

Task: independently challenge the classical passage from a componentwise
arithmetic branching algorithm to gcd factor readout. This is a self-contained
proof and bounded exact check, not an audit of Poonen's HypothesisZ or any
source142 analytic claim. No new source proof was accessed. Only this handoff
was authored for the dynamic task; no repository or Git write was used.

## PM-DYNAMIC-B-001: precise valid statement

Let p be promised prime and f in Fp[X] monic squarefree of degree n>=1.
Let f=product_i f_i be its unknown irreducible factorization and
K_i=Fp[X]/(f_i). Work with a deterministic program P whose field registers
initially contain projections of explicit known elements of A=Fp[X]/(f),
in particular X if desired. All supplied Fp constants and all initial
integer/control inputs are shared across components. Any initialization
outside elementary operations is separately constructed and costed.

Allowed field instructions are elementary +,-,*, ordinary guarded division,
and equality-to-zero queries (equality of two registers is a zero query on
their difference). Integer/control computation can use shared integers and
the zero-query answers. It may not inspect or serialize field representations,
convert a register to an integer, ask a component-degree oracle, or branch
on any other field-dependent primitive. The source program is defined and
terminates on EVERY component, using at most T such FIELD INSTRUCTIONS,
INCLUDING ZERO QUERIES, on each component. A division is defined only if its
denominator is nonzero on the component's actual execution path.

The output is a discrete finite string determined by the shared control/
integer state, not a raw field register or its serialization. It may vary
between components only because zero-query branches diverged. Let I_max
bound the actual integer/control bit work, including constant generation and
output writing, on a component path.

Then a deterministic quotient simulation does one of the following:

1. returns a proper nonconstant divisor of f; or
2. returns the common discrete output together with a common-path certificate
   proving that every component follows that path and has that output.

The field cost is O((T+1)n^2), plus initialization and ordinary integer/control
cost I_max. If discrete outputs are not all equal, alternative1 necessarily
occurs no later than the first divergent zero-query instruction, within T
source field instructions. This is not an algorithm for discovering P or
proving that P separates components.

## Algorithm and proof

Keep every field register as a degree<n residue polynomial modulo f. Lift
shared constants diagonally into A; simulate shared integer/control operations
literally. Addition/subtraction and multiplication are quotient arithmetic.

At a zero query of residue a, compute d=gcd(f,a), monic. If d=1, a is nonzero
in every K_i, so take the nonzero branch. If d=f, a=0 in A and every K_i,
so take the zero branch. If 1<deg d<n, return d. For squarefree f, this last
case occurs exactly when some components have a=0 and others do not.

Before a division by b, perform the same gcd. A proper gcd is already a
factor and is returned. If gcd(f,b)=1, extended Euclid constructs b^{-1}
mod f, and quotient division correctly projects to every component. The
case gcd(f,b)=f would mean b=0 on all components of the shared path. This
cannot occur for an executed division under the defined-on-all-components
promise. A guard that avoids division when b=0 is simulated as an ordinary
zero-query branch. A promise violation should be reported, not repaired by
an invented inverse or silently deleted component.

Invariant: until a proper gcd is returned, every simulated register projects
to the corresponding register on every component, and every component has
the same integer/control state and program counter. Initially this is true by
the shared-input condition. Quotient congruence preserves arithmetic; extended
Euclid preserves defined divisions; the two full gcd cases certify uniform
zero answers; shared integer operations preserve the common state. Induction
therefore proves the invariant through the simulated path.

If no proper gcd occurs, all components halt at the same instruction and
return the same control-state string. Contraposition proves that differing
strings force a proper gcd. Equivalently, their first control divergence must
be a zero query by the programming model, and at that point all earlier
registers have a common quotient lift. Its gcd is proper. The common prefix
is a prefix of every component execution, so has at most T field instructions
and at most I_max integer/control work. This also covers loop-count or halt-
time divergence: a deterministic common control state cannot halt or loop
differently without an earlier permitted query branching differently.

Classical dense modular multiplication, polynomial gcd and extended Euclid
cost O(n^2) field operations each. Addition and constant lifts cost O(n).
Thus O((T+1)n^2) is valid, with honest input/control costs and polynomial
dependence on log p in the bit model. Exponentiation is not a free primitive:
its elementary powering operations or O(log exponent) work must be charged.
T can equivalently count arithmetic instructions alone IF the number Q of
zero-query instructions is charged separately, giving O((T+Q+1)n^2).

A finite common-path certificate can contain the straight-line arithmetic
residues, the zero-query gcd outcomes, and Bezout inverse identities for each
division. A verifier checks those modular identities and replays control/
integer steps. This is classical dynamic gcd detection, not a new primitive.

## Important challenges and rejected stronger readings

1. **Raw field output is not enough.** On f=X(X-1), P(x)=return x uses no
   zero query or denominator, but its component outputs differ. The quotient
   simulation returns X, not a proper gcd. More generally returning X is the
   original representation-to-readout problem, not its solution.

2. **Syntactically discrete is not enough.** If one permits `return str(x)`
   or a canonical field-to-integer conversion, the same program has distinct
   strings with no branch query. Such inspection must be excluded; output
   must be genuinely control-state/branch dependent. Likewise a component-
   degree or field-order oracle is not shared integer control.

3. **The source budget must count queries.** Counting only +,-,*,/ while
   allowing arbitrarily many zero-query instructions does not justify an
   O(Tn^2) simulation bound. Charge Q separately or include queries in T.

4. **Definedness is a real hypothesis.** Unguarded 1/(x-a) is undefined on
   the a-component. Its partial denominator gcd may still produce a useful
   factor, but one cannot cite the defined-on-all-components theorem without
   the corresponding guard/promise. No extension, random choices, hidden
   roots, discrete-log primitive or other oracle is silently supplied.

5. **Uniform outputs do not imply no factor.** A source algorithm may branch
   differently and later return the same string; the compiler can detect a
   proper gcd before those branches reconverge. The theorem gives sufficient
   separation from different outputs, not a necessary condition for success.

6. **No uniform factoring conclusion follows.** Providing a polynomial-time
   separating discrete program is substantive input. If such a program uses
   an unproved hypothesis or analytic oracle, the compiler does not discharge
   that hypothesis. In particular this proof does not assume Poonen's
   HypothesisZ is true or audit its conditional existence consequences.

## Actual bounded exact check

Executed an inline PYTHONDONTWRITEBYTECODE=1 Python script using the independent
stdlib-only arithmetic implementation from /tmp/PM-FACTOR-B-check.py, not a
new broad enumeration or an external factorization package.

Fixture: p=101, f=(X-2)(X-3)(X-5)=[71,31,91,1]. Check d=X+1 gives
gcd(f,d)=1; extended Euclid constructs y=d^{-1} mod f; d*y-1=0 mod f
gives full gcd f, a uniform zero branch. Then the delayed query y-34 yields
gcd(f,y-34)=X-2=[99,1], and independently evaluating components gives the
control outputs ['A','B','B']. A guarded division by X-3 is intercepted at
its zero guard with factor X-3=[98,1]. The raw-register return has values
[2,3,5] and zero zero-query instructions, as the counterexample predicts.

Actual output, exit0:

  {'p': 101, 'f': (71, 31, 91, 1), 'uniform_unit_denominator_gcd': [1],
   'uniform_zero_gcd': (71, 31, 91, 1), 'delayed_query_factor': (99, 1),
   'discrete_outputs': ['A', 'B', 'B'], 'guarded_division_factor': (98, 1),
   'raw_return_x_values': [2, 3, 5], 'raw_return_x_zero_queries': 0}
  DYNAMIC-B EXACT CASES PASSED: uniform guarded division, uniform zero,
  delayed discrete divergence, raw-value counterexample

Acceptance: PASS with the explicit model and budget gates above. This is an
operational compiler for a supplied discrete distinguisher, not discovery of
the distinguisher, a factorization lower bound, or a new factoring theorem.

## Production implementation follow-up

After the independent argument above, I read tools/dynamic_readout.py and
tests/test_dynamic_readout.py fully, plus the new manuscript section6.
The production grammar is a bounded subset of the proved model: an explicit
forward acyclic instruction DAG, arithmetic registers, const/add/sub/mul/inv,
zero tests, and literal string returns. Every non-return target must be an
integer strictly later in the finite DAG. There is no callback, eval, raw
register return, field serialization or field-order primitive. Register
inputs are degree<n polynomials. All-zero inverses and reached undefined
registers are rejected. Mixed inverse-denominator support yields a valid
factor even when the corresponding unguarded scalar inverse would violate
the theorem's definedness promise; this does not invalidate the factor.

The extended Euclidean inverse routine is correct on normalized unit inputs,
including nonmonic intermediate gcd normalization. Before every tested
inverse the implementation computes its gcd, so it cannot silently invert
a zero divisor. The register arithmetic preserves degree<n, hence its COMMON
output is justified by the common-control induction. The validation scan of
all nodes is additional program-input work, as the manuscript explicitly
charges. I found no mathematical correctness defect under promised primehood.

Actual command:

  PYTHONDONTWRITEBYTECODE=1 python -m unittest tests.test_dynamic_readout -v

All6 tests passed; exit0; reported0.001seconds. They cover proper mixed test,
COMMON output, unit inverse, all-zero inverse rejection, mixed linear/quadratic
components, forbidden output/cycle grammar, undefined registers and nonreduced
input rejection. I then ran the combined26-test readout/orientation/dynamic
suite: all26 passed, exit0, reported0.027seconds. The prior20-test and original
18-test observations remain distinct earlier states, not retrospectively
inflated counts.

An additional explicit production DAG reconstructed the independent p=101
delayed case: const1; denominator=X+1; inverse; const34; query=inverse-34;
zero-test returning literalA/B. It returned factor[99,1] at instruction5,
visited[0,1,2,3,4,5], exactly the independently derived X-2. The same prefix
ending in a literal unit return instead yielded COMMON/unit. Actual output:

  {'delayed_factor': [99, 1], 'split_instruction': 5,
   'visited': [0, 1, 2, 3, 4, 5], 'uniform_inverse_status': 'COMMON',
   'uniform_label': 'unit'}
  PRODUCTION DYNAMIC ADDITIONAL EXACT CASES PASSED

Audited SHA256 snapshot:

  tools/dynamic_readout.py
    58f15528be1d509fc7d050fdc76019c13fbdf6d358c27b659b4d7935ecd10a1b
  tests/test_dynamic_readout.py
    8bce653d5553744eb1233892ab95307eebf2d4b742c372ea60cbb523ce7ddbdc
  research/mechanisms/FACTOR_READOUT.md (after section6 addition)
    2a5a512d823babfd5d507446b133477e5d4e3a9d7f398006af851bd226bf4161

I accept section6's self-contained compiler proof and its conditional/discrete
output limits. I have NOT read Poonen's paper and do not attest its exact
primary-source comparison; I warned the coordinator not to include reviewerB
in a count of reviewers who read its sections2–5. This audit does not assume
HypothesisZ or any headline factoring claim.

The production orientation high-primary replay is saved as
/tmp/PM-FACTOR-B-orientation.py, SHA256
704ca271bce6bae2664a3a2c646375ff940dc6c1fa86635f4cf917b547c076fc.
It independently verifies returned grids/traces/factors on two p=65537,N=6
fixtures, including saturation at30 masks; it is explicitly NOT an independent
constructor. It ran successfully against the final audited production state.

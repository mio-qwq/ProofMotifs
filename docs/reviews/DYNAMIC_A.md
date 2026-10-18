# PM-DYNAMIC-A: dynamic evaluation and branch-divergence extraction

Independent bounded formalization/check, after the completed PM-FACTOR-A
work. No Git commands, child agents, broad search or repository writes.
Only this own /tmp note is written. This is classical dynamic evaluation,
not a new factorization algorithm, novelty claim or formal verification.

## Precise machine contract

Let p be prime, f in F_p[X] monic squarefree of degree n>=1, and
A=F_p[X]/(f). Write the mathematically existing irreducible factorization
f=f_1...f_r and K_i=F_p[X]/(f_i), so A is the product of the K_i. The
f_i and their roots are NOT inputs. Component-varying parameters are supplied
only as explicit degree<n polynomial representatives a_1,...,a_m in A.

Let P be a deterministic, uniform field-register program with:

- shared discrete initial inputs, integer registers and control;
- shared F_p scalar constants, interpreted identically in every K_i;
- field instructions +, -, multiplication, copying, and guarded inversion;
- branching on zero tests of previously computed field registers;
- all other integer/control/output instructions determined solely by shared
  discrete data and previous Boolean branch answers.

Each scalar run P_i means the SAME program over K_i with parameter inputs
a_j mod f_i. Assume each such run is legal, terminates, and uses at most T
charged scalar field instructions/zero queries. In particular, every inverse
encountered on each actual scalar path has nonzero operand. If integer
controls depend on a field's degree, that degree must be shared input;
one may not silently supply distinct component degrees.

The output is a finite discrete string produced by the control state, NOT
by printing/encoding/ordering/hashing a field register. Discreteness alone
does not establish this restriction. Field-to-integer conversion, comparisons
other than equality-to-zero, coordinate inspection, hidden factorization
oracles and unexpanded black-box subroutines are outside the grammar.
Equality of two field registers is allowed via subtraction and a zero test.
Tuple/polynomial/matrix computations must expand into charged scalar
instructions, including their zero tests.

## PM-DYNAMIC-A-001: extractor theorem

There is a deterministic simulation over A which either returns a proper
factor of f within T scalar-simulation steps, or reaches a common halt and
returns the common discrete output of all P_i. In particular, if two P_i
have different output strings, a proper factor is returned within T steps.

With schoolbook quotient arithmetic, the field-operation overhead is
O(T n^2) in F_p. More precisely, this is the simulation cost after the
degree<n parameter representatives are prepared. Input reading/reduction
and shared integer/control bit work, including string writing, are separately
charged. If T is a total scalar bit-time bound, the quotient simulation has
that shared control cost plus O(T n^2 poly(log p)) bit overhead. No claim
that arbitrarily long integer work is free is intended.

### Algorithm

Store field registers as normal forms modulo f. Simulate +,-,* in A.
At a zero query on z compute the monic g=gcd(f,z):

1. If g=f, z is zero on every component; follow the zero branch.
2. If g=1, z is nonzero on every component; follow the nonzero branch.
3. Otherwise return g, a proper nontrivial factor of f.

Before an inverse, likewise compute g. If g=1, extended Euclid produces
the inverse of z modulo f. If 1<deg(g)<n, returning g is always a valid
factor witness. The case g=f indicates an illegal inverse on every current
component and is impossible under the legal-run hypothesis. In fact, before
the first divergent query a partial-zero inverse is also impossible under
that hypothesis, but its guard is useful for robust implementations.

No branches or inverses of nonunits are guessed. Computing f/g costs
O(n^2) if the complementary factor is requested. Merely returning g needs
no factor oracle.

### Proof

Inductively, as long as no proper factor has been found, all scalar runs
have the same discrete/control state, and every simulated register projects
to the corresponding register of every scalar run. This is true initially.
Arithmetic respects the projections A->K_i. A guarded unit inverse also
does. At a query, f_i divides z exactly when its component value is zero.
Thus g=f means all zero predicates are true, g=1 means all are false, and
a proper gcd is precisely a nonempty proper zero subset. The first two cases
preserve the induction; the third terminates with a valid factor.

If no factor is returned, the common path must halt within the scalar bound
T: it is the path of every scalar run. Its output-control state is shared,
so the output strings agree. Contrapositively, different outputs force a
first query with differing zero answers. Its proper gcd is encountered no
later than T. The same argument also rules out different halting times along
an uninterrupted common control path. It does NOT require computing all
component outputs separately.

Each quotient product, gcd or extended-Euclidean inverse costs O(n^2)
F_p operations. Additions, zero/one comparisons and scalar embeddings cost
no more. At most constantly many such operations replace a charged scalar
instruction. This proves O(T n^2). The gcd computation is a deterministic
Euclidean algorithm, not an invocation of the desired factorization problem.

**Finite verification.** A returned factor has the certificate f=g h with
0<deg(g),deg(h)<n, checked by multiplication. A no-factor execution can
carry its finite trace of normal-form register identities: zero-query
witnesses are z=0; nonzero-query/inverse witnesses are Bezout identities
u f+v z=1. These certify uniform answers on every component without roots.
The trace length and verification cost are polynomial in its explicit size,
with O(n^2) quotient/Euclidean work per field instruction. This supplies a
concrete compiler/verifier interface, not just a kernel characterization.

## Necessary output restriction and scope challenges

For p=5 and f=(X-1)(X-2), the one-instruction program 'return x' has different
raw field outputs 1 and 2 on the two components but performs no query.
It therefore follows a common path and returns x in A without partitioning
the components. Both values are nonzero, so even gcd(f,x)=1 is uninformative.
Calling their binary encodings 'discrete outputs' does not fix the claim:
encoding a raw field register is exactly the forbidden output operation.

The theorem applies to arbitrary squarefree f only when the same field
program is defined over all K_i. An algorithm specified solely for prime
fields is not automatically an algorithm over their extension fields.
Alternatively, restrict f to totally split inputs, as the cited application
does, and then all K_i are F_p. A heuristic promise that component outputs
usually differ is not sufficient for a worst-case factorization algorithm.
One must construct parameter families that force divergence within the
resource budget. Likewise, rational-family discriminants/denominators must
be units on every input component, or a failed-unit gcd must be handled
explicitly; 'run as though A were a field' is not a sufficient contract.

This extractor does not synthesize the component-distinguishing observable.
It is compatible with a common output even when f is highly reducible.
Conversely, it may find a factor before any final output differs. No lower
bound, complete factorization, general separator existence or poly(log p)
factoring theorem follows from the extractor alone.

## Primary-source receipt and macro comparison

Read Poonen, *Using zeta functions to factor polynomials over finite fields*,
author-host PDF https://math.mit.edu/~poonen/papers/fq-factoring-ams1.pdf,
7 pages; §§2–5 completely, PDF pp1–5, extracted lines25–202. The retrieved
file carries no version/date in those sections; identify this exact author
URL rather than inventing a version number. No inaccessible image placeholder
was treated as a read; this retrieval supplied coherent text.

Poonen §4 specifies arithmetic guided by zero queries; §5 substitutes gcd
queries in the quotient. Hypothesis Z supplies distinct fiber zeta functions,
hence divergence, and is a separate conditional discovery premise. The local
extractor is unconditional under its machine contract; the polynomial-time
global factoring conclusion remains conditional in that source. The
program-dovetail argument does not prove Hypothesis Z or construct a family
with the required separation. These observations are prior-art coverage,
not a new common cancellation tool or evidence about AI causality.

Source citation reference from this task: turn353view0. Directly relevant
ranges are §4 lines122–132 and §5 lines173–202; §§2–3 lines25–105 give the
Schoof/Kayal setup and legal discriminant context. The formal statement,
proof, output counterexample and cost accounting above were checked
independently rather than treating the source's prose as a proof oracle.

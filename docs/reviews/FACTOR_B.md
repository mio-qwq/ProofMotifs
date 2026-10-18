# PM-FACTOR-B — independent representation-to-readout view

Task ID: PM-FACTOR-B. Research question: exactly which additional observable
certificate converts legal quotient/Frobenius-fixed arithmetic into factors,
and where does a representation-only inference stop? Assumptions: binary prime
p; explicit squarefree nonconstant f in F_p[X], normalized monic, degree n;
no roots, factors, randomness or oracle in the original input. Scope: read-only
repository and primary web evidence; only this handoff and my own checker
written under /tmp. No children, Git commands or external writes were used.

## Independence and exposure

I read AGENTS.md and research/RESEARCH_PROGRAM.md in full, and the freeze and
statement-only decision in full. I did not access source142's proof, source
tree, or introduction. My independent derivation of the small-codomain
criterion, joint-separation/generated-algebra equivalence, scalar-root-label
gap and Euler collision was communicated to the coordinator before cross-
review. The coordinator subsequently supplied its binary-idempotent proposal;
the binary specialization below agrees and my additional checks challenge it.
The task requested GPT-6.1 Sol/Ultra explicitly; I do not independently attest
the runtime's actual setting or the main agent's setting.

Repository evidence inspected: docs/reviews/TRANSFER142_FREEZE.md lines24–51
fix allowed input and costs; lines53–67 delimit the decision. The decision file
lines11–17 records the source claims, lines19–32 the failed candidate transfer.
The fixed freeze hash is 765fa48b0eb907c4c6fc30541dbfafc42ca9d29c; parent records
the outcome commit as 3a7ffa9. I did not independently query Git.

## PM-FACTOR-B-001: legal infrastructure and the exact missing coordinate map

Write f=product_{i=1}^r f_i for its distinct monic irreducible factors and
d_i=deg(f_i). This factorization is used in the proof, not supplied to an
algorithm. Let A=F_p[X]/(f), Phi(a)=a^p, and B=ker(Phi-I).

CRT gives A ≅ product_i F_{p^{d_i}}. On each component the fixed field of
the p-power map is F_p. Consequently B ≅ F_p^r as F_p-algebras, and
dim_Fp B=r. Quotient multiplication is legal and faithful. Computing B is
also legal: compute z=X^p mod f by repeated squaring, form the columns
1,z,...,z^{n-1} for Phi in the power basis, and take the nullspace of Phi-I.
With classical dense polynomial arithmetic this costs
O(n^2 log p+n^3) field operations and O(n^2) field elements of storage.
Every claimed field-operation bound below becomes a polynomial bit bound:
for example the conservative bound O(F (log p)^2) bit operations suffices
for F field operations with standard modular arithmetic. No O(p) loop is
included or hidden in this construction.

But an ordinary basis of B is not its coordinate/primitive-idempotent basis.
In fact ANY F_p-basis of B already generates B as an algebra and jointly
separates its r CRT coordinates. Thus 'full generated-algebra rank' of an
arbitrary observable list is not by itself the missing readout operation.
One still needs a tractable way to distinguish their scalar coordinate values.

## PM-FACTOR-B-002: certified small-codomain readout

Additional input: c_1,...,c_t in A, represented by degree<n polynomials,
and explicit nonempty lists S_j of distinct elements of F_p, such that

  (i) Phi(c_j)=c_j;
  (ii) product_{a in S_j}(c_j-a)=0 in A.

These hypotheses are verified, not assumed from notation. The c_j may instead
be produced by supplied arithmetic circuits from legal quotient data; let L
be the total number of quotient operations in those circuits. Put
K=sum_j |S_j|. The lists of known labels are substantive additional data.
They are NOT automatically available by computing a minimal polynomial.
In fact (i) is redundant: because S_j consists of distinct elements of F_p,
its displayed support polynomial divides T^p-T, so (ii) implies (i) in any
F_p-algebra. Checking (i) separately is a transparent optional consistency
check, not a necessary stronger input hypothesis.

Algorithm: start with the one block f. For each j, replace each current block
H by the nonconstant monic gcd(H,c_j-a), for a in S_j, dropping unit gcds.
This does not enumerate all scalar tuples or all F_p. It maintains at most r
nonempty blocks. Compute r beforehand by B-001, validate (i) by applying the
known Frobenius matrix, and validate (ii) by quotient multiplication. At the
end let m be the number of blocks. Their product is f and they are pairwise
coprime, so the output is a certified partial factorization. It is complete
into irreducibles if and only if m=r.

Proof: in CRT coordinates write c_j=(lambda_{j,1},...,lambda_{j,r}). Condition
(i) makes every lambda scalar, and (ii), since every component is a field,
makes lambda_{j,i} lie in S_j. The gcd with c_j-a is exactly the product of
those irreducibles f_i in the current block with lambda_{j,i}=a. Induction
therefore identifies final blocks with the nonempty fibres of the tuple map
i |-> (lambda_{1,i},...,lambda_{t,i}). In particular m<=r, and equality holds
exactly when every fibre is a singleton. This proves both correctness and
the completeness criterion without irreducibility guesses.

The equivalent algebra criterion is dim_Fp F_p[c_1,...,c_t]=r. More generally
that dimension equals m: polynomial functions of the tuple are constant on
each fibre, giving the upper bound m. For any chosen fibre v, for every other
fibre w choose a coordinate j(v,w) in which they differ and multiply the
linear factors

  (Z_j-lambda_{j,w})/(lambda_{j,v}-lambda_{j,w}).

The resulting polynomial is one on v and zero on every other fibre, so all
m fibre indicator functions lie in the algebra. This interpolation is an
existence proof; the gcd algorithm constructs the fibre factors without
assuming the unknown lambdas or expanding exponentially many tuples.

Cost: support validation costs O(K n^2), Frobenius-fixed validation O(t n^2),
and circuit evaluation O(L n^2). For each j and each a, classical gcd plus
reduction over blocks of total degree n costs at most O(n^2), since the sum
of their squared degrees is <=n^2. Thus the total including B is

  O(n^3+n^2 log p+(L+K)n^2) field operations.

Here t<=K. This bound is deliberately conservative rather than optimized.
If K,L are polynomial in n,log p, this is deterministic polynomial time.
There is no claim that suitable c_j/S_j are synthesizable at this cost from
f alone. The exact useful operation is: validate a proposed readout family,
return the factors it actually separates, and report COMPLETE or PARTIAL
with the numerical obstruction m<r.

## PM-FACTOR-B-003: binary idempotents and optimal existential length

The coordinator's idempotent proposal is the specialization S_j={0,1}.
Checking c_j^2=c_j also implies c_j^p=c_j (every positive power of an
idempotent equals itself), in every characteristic. Therefore t supplied
binary idempotents admit factor readout and completeness validation in
O(n^3+n^2 log p+t n^2) field operations. Their generated algebra is B iff
their r binary CRT codewords are all distinct iff gcd branching has r leaves.
No enumeration of 2^t subset products is necessary.

The minimum possible number is ceil(log_2 r), with zero for r=1. Necessity
is r<=2^t. Sufficiency: label the r irreducible factors by distinct t-bit
strings and use CRT to construct one idempotent for each bit. This is an
existence statement. Given factors, extended Euclid constructs all required
idempotents in polynomial time. Conversely a polynomial-length complete
idempotent family yields the factors by B-002. Hence polynomial-time
synthesis of such complete families from squarefree f is polynomial-time
equivalent to squarefree factorization. This is a precise reformulation and
certificate, not a factorization lower bound or a new factoring algorithm.

Cross-review: the coordinator's criterion and binary optimum are correct
under the stated squarefree input and honest output-length/circuit costs.
Verifying generated dimension r is useful specifically because the generators
are idempotents with known labels; it does not license general rank-to-factors
inference for arbitrary B generators.

## PM-FACTOR-B-004: single observables, minimal polynomials and scalar labels

For b in B with scalar coordinates beta_i, its minimal polynomial in A is

  mu_b(T)=product_{a in {beta_i}} (T-a).

Indeed q(b)=0 iff q(beta_i)=0 for every i; the displayed squarefree product
is exactly the monic polynomial of least degree with those roots. It can
be computed from the first linear dependence among 1,b,...,b^n by ordinary
linear algebra in polynomial(n,log p) time. Its degree s is the number of
distinct b-values, not necessarily r.

If the roots a of mu_b are supplied or found, gcd(f,b-a) gives exactly the s
fibres, in polynomial overhead. If b has r distinct values, these are the
irreducible factors. But 'mu_b splits over F_p' does not give an efficient
list of its roots. Passing to mu_b replaces the readout by rootfinding for
an explicitly split squarefree polynomial, not by linear algebra alone.

A single b can generate B/separate all coordinates iff r<=p. Necessity:
there are only p possible values. Sufficiency: CRT with r distinct scalar
labels. More generally the minimum number of unrestricted F_p-valued
generators is ceil(log_p r), by the identical coding argument. For r>p the
missing single separator is structurally impossible inside B, although
multiple observables and binary idempotents remain possible. A itself is
monogenic, but its subalgebra B need not be.

One can reduce arbitrary squarefree factorization to rootfinding for split
squarefree polynomials by taking an ordinary basis b_1,...,b_r of B,
computing the split minimal polynomial of each b_j, finding its scalar roots,
and applying all resulting gcd refinements. The basis jointly separates,
so this finishes. An intentionally loose overhead is O(n^4) field operations
plus at most n calls to a split-root subroutine of degree<=n. Conversely a
uniform extractor operating on these quotient/fixed-algebra presentations
already includes the split-polynomial case: if f splits squarefree, A=B
and 1,X,...,X^{n-1} is the ordinary legal input representation. Such an
extractor would solve that factoring/rootfinding case. This equivalence
does not establish an unconditional hardness result.

## PM-FACTOR-B-005: exact collision and nonreduced controls

For odd p and b in B, c=b^((p-1)/2) has known codomain {0,1,-1}, computable
with O(log p) quotient multiplications. It is a legal B-002 test and can
be useful without enumerating the field. It is not always a separator.

Example at p=1000000007 (p=3 mod4):

  f=(X-1)(X-4)(X^2+1), b=X^2 mod f.

The quadratic is irreducible because -1 is nonsquare. Thus r=3 and b has
distinct CRT values 1,16,-1, so b generates B. Nevertheless Euler's test
has values 1,1,-1 and leaves the two linear factors merged. A second test
(b-1)^((p-1)/2) distinguishes the first value (zero) from the second
(nonzero) and finishes. Both tests and their support identities are checked
exactly; no p-scan is used. This separates 'observable generates B' from
'the chosen cheap scalar test reads out all factors'.

Restricted obstruction: given fixed maps h_j:F_p -> S_j with known finite
codomains, if product_j |S_j|<p then two distinct a,b have the same joint
labels, by pigeonhole. On f=(X-a)(X-b), the element X generates B but these
fixed tests cannot split the components. This applies to the specified fixed
test family; it is NOT a lower bound against algorithms that choose new
tests depending on f, adaptively or using other arithmetic.

Nonreduced control: for f=X^2, A has nonzero nilpotent X but its Frobenius-fixed
algebra is just F_p. In particular r=dim B=1 counts distinct components, not
degree or multiplicity. Evaluation into residue fields kills the nilpotent.
This does not obstruct the squarefree theorem, but prevents transplanting its
factor/multiplicity conclusions without squarefree decomposition. The checker
explicitly rejects this input rather than treating its fixed dimension as a
complete multiplicity readout.

## Exact independent implementation checks

Command run from /workspace/scratch/415407b3c01b/ProofMotifs:

  python /tmp/PM-FACTOR-B-check.py

Exit code0; actual output:

  large-prime mixed-degree case: p=1000000007, n=4, fixed_dimension=3
  observable X^2 generates B; Euler alone: 2 leaves; shifted Euler: 3 exact irreducible leaves
  binary-certificate case: r=9, minimum_bits=4; four supplied bits give9 leaves; first3 give8
  characteristic2 mixed-degree case: n=4, r=3, two binary idempotents give3 leaves
  negative controls: false small-codomain certificate rejected; nonreduced input rejected
  exact counters: {'pow_calls': 36, 'pow_mults': 1358, 'scalar_tests': 62}
  ALL ASSERTIONS PASSED; no loop over F_p, no random choices, no factorization package

The stdlib-only checker independently implements modular polynomial arithmetic,
Euclidean gcd/extended Euclid, modular powering, RREF/nullspace, Frobenius B,
generated-algebra closure, support validation, and gcd partition. It checks
pairwise coprimality, exact factor products, correct codomain identities,
generated dimensions and returned factor equality. The r=9 fixture constructs
four bit idempotents from nine fixture roots for testing only; their synthesis
is not claimed possible from unknown factors. Its first three bits yield
rank8/eight leaves, validating the incomplete-certificate branch. The F_2
fixture f=X(X+1)(X^2+X+1) has r=3>p, so is a structural no-single-generator
example. This is exact computational evidence for selected examples, not a
finite proof of the general statements or a compiled formal proof.

## Primary-source comparison and limitations

Berlekamp's original 1970 paper, 'Factoring Polynomials Over Large Finite
Fields', Math. Comp.24,713–735, DOI10.1090/S0025-5718-1970-0276200-X,
has an original AMS search-index abstract explicitly describing a deterministic
polynomial(degree,log field-size) reduction to finding roots over F_p of other
polynomials. This matches the independently derived B-004 operational boundary.
URL:
https://www.ams.org/mcom/1970-24-111/S0025-5718-1970-0276200-X/S0025-5718-1970-0276200-X.pdf
Direct open returned403, so I did not read full primary-paper pages/ranges.
The 1967 original Wiley abstract was inspected, DOI
10.1002/j.1538-7305.1967.tb03174.x, but supplies only abstract-level evidence.
No claim of detailed original-paper coverage is based on a survey or search
absence. The coordinator should use its independent original-source audit
for exact page-range citations. The mathematics above has a self-contained
proof, and is deliberately labeled classical structural/certificate synthesis,
not novelty, a source142 proof validation, or held-out transfer success.

Decision: the frozen representation operation still fails its uniform
factor-readout contract. The useful strengthened result is an exact validator
and partial/full-readout algorithm for supplied bounded-codomain observables,
with explicit costs and failure certificates. Producing those observables
from f alone is a separate operation; for complete idempotents it is already
equivalent to factoring. All PM-H1–H5 remain open.

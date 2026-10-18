# PM-Q-C: independent adversarial review and exact arithmetic

Date: 2026-10-18 UTC. Scope: repository read-only; this report and its standalone
checker are in `/tmp`. No Git changes, external publication or historical
novelty claim. No other delegated researchers' new notes were inspected.

## Verdict

ACCEPT the exact equivalence for **linear independence of all word series over
K(z)**, with the empty word included, q of infinite multiplicative order, and
each rational b_i regular and zero at 0. ACCEPT normalized split-pole residue
selection and the exact-r-subset weighted matroid algorithm within their
stated input contract. No counterexample to these corrected statements found.

Do not turn failure of this strong contract into an impossibility theorem for
ordinary K-linear word encoding or faithful K-operator evaluation. The explicit
unary seed b=z refutes that broader interpretation.

## Independent proof of the equivalence

Put F=K(z), sigma(f)(z)=f(qz), Delta=sigma-1. Infinite order gives
q^n-1 != 0 for every nonzero integer n. Thus Delta is invertible on zK[[z]],
and the sigma-fixed subfield of K((z)) is exactly K by comparison of Laurent
coefficients. Define h_empty=1 and Delta(h_iw)=b_i h_w, h_iw(0)=0.

Necessity: if sum_i c_i b_i=Delta f with c_i in K not all zero, comparison
of negative Laurent coefficients shows f has no pole at 0. Subtract f(0).
Now sum_i c_i h_i-f is sigma-invariant and zero at 0, hence zero. This is a
nontrivial F-linear relation among the length-one and empty words.

Sufficiency: suppose a nontrivial finite relation R=sum_w a_w h_w=0 exists.
Choose its maximal word length m as small as possible, and then its number
of nonzero length-m coefficients as small as possible. m cannot be 0.
Normalize one length-m coefficient to 1. In sigma(R)-R, length-m coefficients
are Delta a_w, and the normalized coefficient is zero. Any nonzero coefficient
vector would give either a relation of smaller maximal length or a relation
with fewer length-m coefficients. Consequently that entire coefficient vector
is zero. Therefore each length-m a_w is in K. For a tail v of length m-1,
the coefficient equation is

    Delta a_v + sum_i a_iv b_i = 0.

Independence of [b_i] in F/Delta F forces every a_iv=0, contradicting maximal
length m. This proof uses no division by an integer and survives characteristic
p without changes.

This is independence of a family of scalar series over F. It should not be
called a representation of a free F-algebra by the J_i: J_i is K-linear, not
F-linear. Its usual K-operator-faithfulness consequence follows by applying
an asserted operator identity to 1.

## Split-pole quotient and exact finite chain

Write phi_(alpha,k)=(1-z/alpha)^(-k)-1, alpha != 0. Then
sigma(phi_(alpha,k))=phi_(alpha/q,k) exactly in every characteristic. At each
nonzero q-orbit and each positive pole order k, sum the coefficients in this
normalized basis. These orbit/order sums vanish for every rational difference.

Conversely, write the support in one orbit as alpha_j=beta q^j and b's
coefficients as c_j. Set r_j=sum_(ell<j)c_ell. If sum_j c_j=0, r_j has finite
support and c_j=r_(j+1)-r_j, so sum_j r_j phi_(alpha_j,k) is an exact rational
antidifference. Missing indices must be filled with zero; skipping gaps would
give an incorrect witness. Positive polynomial terms z^d have antidifference
z^d/(q^d-1). The normalization b(0)=0 removes the remaining constant term.

For necessity, a hypothetical rational antidifference with poles outside the
split support cannot evade this argument: along every unrelated nonzero orbit,
finite support has an uncancellable endpoint pole. It cannot have a pole at 0
because Delta scales every negative Laurent coefficient by a nonzero scalar.
Thus the finite split-pole criterion does not secretly assume that a sought
antidifference is supplied in split form.

Repeated poles do not mix orders under sigma; collapsing all orders in one
orbit is unsound. Distinct pole locations in the same orbit do not give
independent classes. These two common implementation errors are separately
tested.

## Strongest scope counterexamples and boundaries

1. **Strong versus base-field faithfulness.** For one seed b=z,
   h_(1^n)=z^n/product_(s=1..n)(q^s-1). All these series are K-linearly
   independent, and J's powers are K-linearly independent after application
   to 1. Yet [b]=0 in F/Delta F and h_1=z/(q-1) is rational. Quotient rank
   zero is an obstruction only to the strong F-linear independence contract.
2. **Infinite order is essential to this construction.** At q=-1 over Q,
   Delta(z^2)=0, so Delta has no inverse on zK[[z]]. With b=z, h_1=-z/2 but
   the equation for h_11 asks Delta h_11=-z^2/2 and has no solution.
3. **Characteristic p is not a counterexample to linear independence.** Over
   K=F_p(t), q=t, choose b_1=phi_(1,1), b_2=phi_(1,p)=b_1^p. Their residue
   vectors are independent (orders 1 and p), but h_2=h_1^p by Frobenius and
   uniqueness of the normalized antidifference. Thus an algebraic-independence
   strengthening is false, while the linear-word theorem is consistent.
4. **Nonzero value at 0.** Mere regularity is insufficient: Delta g always has
   zero constant coefficient. The b_i must vanish at 0 for the stated recursion.
5. **Non-split inputs.** For example z/(1+z^2) over Q is outside the executable's
   split-rational-pole contract. It must be rejected, not assigned rank zero.
   The abstract word theorem itself does not require splitting.
6. **Selection grammar.** Minimum-cost exact-r subset selection is a weighted
   linear matroid problem. Its rank obstruction also applies to K-linear
   combinations from the same supplied span. It does not settle a grammar
   allowing new pole locations, rational multipliers, different composition
   rules or a different cost functional. Exactly r and at least r differ if
   negative costs are allowed; the root executable rejects negative costs.

## Primary-source normalization check

Chen and Singer, *Residues and telescopers for bivariate rational functions*,
Adv. Appl. Math. 49 (2012), 111-133, section 2.3, Definition 2.7, Lemma 2.9
and Proposition 2.10, give the characteristic-zero rational q-summability
criterion with standard partial fractions and a separate infinity constant:
https://singer.math.ncsu.edu/papers/YAAMA1465.pdf . Section 2 explicitly assumes
characteristic zero. This source therefore directly covers the executable's
Q setting, not by citation alone the any-characteristic statement proved above.

In that source's coordinates, the order-k orbit residue is
sum_j q^(-jk) A_j for terms A_j/(z-beta q^j)^k. Substituting
A_j=c_j(-beta q^j)^k makes it (-beta)^k sum_j c_j. Hence the normalized phi
rows differ only by nonzero row scalings. For b(0)=0, the source's infinity
constant is -sum_(orbit,k) rho_(orbit,k), so that row is redundant rather
than missing from the proposed test.

## Independent arithmetic and code audit

Run:

    python /tmp/pm-q-c-check.py

It uses only the Python standard library. The initial arithmetic and selection
tests are independent implementations. The final audit imports root's
`tools/q_seed_synthesis.py` only to exercise its public construction and checks
the returned results using independently constructed raw rational functions.

Observed exit code: 0. Final status: PASS.

- 80 independently generated gapped/repeated-pole rational-difference controls,
  each verified by full polynomial cross multiplication; adding a fresh
  orbit/order obstruction is rejected in every control.
- 720 exact independent greedy-versus-exhaustive panels, including zero
  vectors, tied and negative weights, target rank zero, and infeasible ranks.
- A specific order-3 chain with gaps and a positive polynomial part verified
  as a complete rational identity.
- Q, q=2, two independent pole orbits: the seven words of length <=2 have
  coefficient-jet rank 7 (a finite positive control, not the infinite theorem).
- F_3(t), q=t: a separately implemented exact rational-function coefficient
  field gives jet rank 7 for the seven words of length <=2, including the
  Frobenius-related seeds at orders 1 and 3. The identity h_2=h_1^3 is also
  checked through the ten-coefficient jet. No numeric finite-field element
  is treated as having infinite order.
- Unary polynomial b=z: seven word jets have K-rank 7 while quotient rank
  is zero, independently checking the strong/basic boundary.
- Root cross-audit: 280 raw rational decompositions and 280 complete raw
  rational Delta-antidifference identities, not just equality of normalized
  coefficient dictionaries; 40 selection panels compared with all subsets.
- Twelve invalid inputs rejected: non-split denominator, absent factor,
  wrong root, wrong order, duplicate root, zero root, Boolean order,
  negative or Boolean cost, a pole at 0, nonzero value at 0, and float input.
- Empty dictionary/target zero succeeds; empty dictionary/target one reports
  only strong-rank insufficiency. A zero rational numerator with an uncancelled
  denominator certificate is accepted and correctly has quotient rank zero.

Root source SHA-256 at audit time:
`1380ea953df50a63be0e79a4bf78d86ebafaf25b8fa2912d54d497cc2cd7c648`.
Checker SHA-256 after the recorded run:
`4677fff0748ca05ed5b9df16ae43fcd8119544cf651c322667ee2a22d8a584ef`.

Two narrow code-hardening observations were sent to root:

- `telescoper(dec)` currently discards `dec['poly'][0]` without rejecting a
  nonzero constant if the helper is called directly. `synthesize` is sound
  because its fresh decomposition guarantees the helper precondition.
- Before expanding declared pole powers, check that the sum of declared
  orders equals the raw denominator degree. Valid expanded-input complexity
  is unaffected, but a gigantic binary-encoded invalid order otherwise incurs
  unnecessary expansion before its factor certificate is rejected.

No soundness defect was found in the audited `synthesize` path. These tests
are exact implementation controls and proof challenges, not formal verification,
a universal input fuzzer, a benchmark superiority result or a novelty finding.

## Follow-up resolution and standalone verifier audit

The coordinator hardened both initial observations: `telescoper` now rejects
a nonzero normalized constant, and `decompose` checks the total declared pole
degree against the expanded raw denominator degree before constructing powers.
`seed_from_parts` also validates nonzero poles and positive integral orders.
Both original hardening observations are therefore RESOLVED.

The new `verify(seeds,target,certificate)` was inspected independently. It does
not call `synthesize`; it reparses raw input, recalculates quotient columns,
checks the reported rank/greedy selection/cost, checks basis coordinates, and
verifies each dependency witness with a full raw rational cross-product
identity. Shared polynomial and linear-solve primitives are explicitly
disclosed. No soundness defect was found in these checks.

Two initial certificate-format gaps were identified during that inspection:
the contract label was not checked, and adding an arbitrary constant to an
antidifference was permitted. The latter still gives a mathematically valid
antidifference, but fails the promised zero-constant canonicalization. The
coordinator now enforces the exact strong-contract string and zero constant.
Both format observations are RESOLVED.

The extended independent checker was rerun on the hardened source. All previous
controls still PASS. Additional regressions PASS:

- A declared pole order of `10**100` against a degree-one denominator is rejected
  **before any power construction**. The test temporarily replaces the power
  function with an immediate-failure trap, so this tests ordering of validation
  without risking a huge allocation.
- The telescoper helper rejects a nonzero constant. The seed constructor rejects
  Boolean, zero, negative and nonintegral orders.
- Valid certificates and genuine JSON serialization/deserialization round trips
  are accepted; both feasible and infeasible empty-input certificates verify.
- Ten mathematically false certificates are rejected: corrupted cost, rank,
  status, basis, selection, quotient columns, decomposition coefficient,
  quotient coordinate, rational telescoper coefficient and polynomial
  telescoper coefficient.
- A misleading broader contract label and a noncanonical added telescoper
  constant are rejected. These are separate asserted regressions, not just
  logged observations.

Final commands, both exit 0:

    python /tmp/pm-q-c-check.py
    python -m unittest tests.test_q_seed_synthesis

The second command ran all eight current root unit tests successfully. The
first command reported status PASS and all new verification/hardening fields
true. This supersedes the earlier snapshot hashes above.

Final audited root source SHA-256:
`c1319720283f1d058ff1e78e38cba9899e98b270d08bc32e9822f49b3030da59`.
Final independent checker SHA-256:
`68e6abab14b855bcf7c566ee15d357fbbb09019fc751f69b7ce189909f76a4f9`.

The coordinator may integrate the independent checker by changing only its
fixed root-module path to a sibling-file `Path` lookup. Such packaging does
not change its arithmetic; its integrated-file hash will necessarily differ.

# Startup research discussion and audit

Date: 2026-10-18. Coordinator: PM-ROOT-20261018.

**Execution mode:** sequential analysis by the same coordinator. No genuine subagent invocation, independent researcher review, human review or Lean replay took place. The views below are separate analytical passes, not separate agents.

## SC-001

Algebraic pass: propose cancellation-order additivity by the binomial moment identity.
Adversarial pass: the leading coefficient can vanish in positive characteristic. F_2 supplies a zero product; F_4 supplies a nonzero order jump.
Revised statement: exact additivity holds precisely when the leading binomial coefficient is nonzero, over a field. Check infinity, support collisions and 0^0 explicitly.
Literature pass: binomial algebra, Lucas congruences and divided powers already explain the statement. Classify as Level 0.
Decision: retain the proof and implement exact regression checks; do not market a new framework.

## SC-002

Structural pass: each saturated factor counts a prime-field line. Pushforward multiplicities should determine the product.
Challenge: dependent directions, including repeated or zero directions, cause total annihilation rather than a smaller-order uniform measure. Empty products need a separate convention.
Revision: prove the dependence/independence dichotomy, then compute exact ordinary order via Lagrange interpolation and a subspace polynomial.
Cross-check: fiber counting, convolution, moments, root product and Moore determinant agree in all tested cases. They share finite-field tables; algorithmic agreement is not independent authorship.
Literature pass: subspace-polynomial and finite-difference literature already contains the essential ingredients. Level 0.
Decision: keep as infrastructure; investigate unsaturated exponents instead of generalizing it without evidence.

## SC-003 proposal and challenge

Candidate question: does the characteristic, exponent vector and F_p-rank determine ordinary moment order?
Challenge obtained by exact search: in F_27, three independent first-difference directions can give order 5 or 7. This invalidates a rank-only rule.
Next requirement: save an exact witness and prove a field-independent ternary classification using the first potentially nonzero moments. Compare with higher-order derivatives, functional degree and polarization identities. No novelty elevation before this comparison.

## Remaining audit gaps

Independent mathematical reviewer; independently implemented field arithmetic; Lean kernel verification; complete historical priority search; a genuinely held-out transfer application. None is replaced by fluent exposition or a finite search. Upstream proof status and this project's status are kept separate.

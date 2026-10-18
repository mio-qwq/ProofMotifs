# PM-MIX-B — independent structural gate

## Task ledger

- TASK ID: PM-MIX-B.
- RESEARCH QUESTION: Is the ordinary constant-field free-algebra representation with A=J_z and B=J_(z/(1-z)) faithful on all K[[z]]?
- KNOWN ASSUMPTIONS: K is any field; q in K* has infinite multiplicative order; sigma(f)(z)=f(qz); D=sigma-1; J_b=D_0^(-1)M_b, with the zero-constant inverse defined coefficientwise on zK[[z]]. Composition is rightmost first.
- AVAILABLE EVIDENCE: Read AGENTS.md, research/RESEARCH_PROGRAM.md, research/mechanisms/Q_WORD_SEED_SYNTHESIS.md, and docs/reviews/Q_POLYNOMIAL_C_ADVERSARIAL.md. Supplied evidence includes the polynomial-alphabet obstruction and the polynomial quantum-plane example. The strong rational-word quotient for this pair has rank one and does not decide this weaker target.
- EXPECTED OUTPUT: An exact structural identity or faithfulness proof; no finite rank scan treated as a theorem.
- ALLOWED SCOPE: Read-only repository, own /tmp/pm-mix-b.md and own /tmp checker; no Git, no children, no external communications or external-source lookup. Parent coordination/handoff only.
- INDEPENDENCE REQUIREMENT: No current /tmp/pm-mix-a* or /tmp/pm-mix-c* notes read. Main identity and first proof below were derived independently before parent sent its matching proof. The abstract proof appendix is explicitly a later audit of a supplied parent proposal.
- STOP CONDITIONS: One bounded structural gate. A nonzero all-series identity resolves nonfaithfulness; no full presentation or minimal-degree search attempted.
- HANDOFF: Complete assumptions, two proofs, direct generalization, controls and actual commands/results below.

## Verdict and nonzero free polynomial

**PM-MIX-B1.** The representation is not faithful. On all K[[z]],

    AB - q BA = (1-q)(B^2 + BAB).

Consequently the nonzero free polynomial

    P(X,Y)=XY-qYX-(1-q)Y^2-(1-q)YXY

lies in its kernel. The four displayed free monomials are distinct and the
coefficient of XY is 1. Thus P is nonzero in every characteristic. Infinite
order implies q!=1, but nonzeroness of P does not need that extra observation.

## Independent direct proof without inverse antiderivatives

Write E=M_z, D=sigma-1, and R=(1-E)^(-1), the well-defined formal
multiplication operator by 1/(1-z). Then B=AR and E commutes with R, so

    BE=B-A.                                             (1)

The zero-constant q-antiderivative satisfies DA=E. Also sigma A=q A sigma:
this follows coefficientwise on z^m and hence on every formal series. Expanding
sigma=1+D gives

    q AD=E+(1-q)A.                                      (2)

Since DB=ER, right multiplication of (2) by B gives

    EB+(1-q)AB=q ADB=q AER=q BE=q(B-A).                 (3)

Left-multiply (3) by B. On the other hand, (1) directly gives
BEB=(B-A)B=B^2-AB. Equating the two expressions for BEB yields

    B^2-AB=qB^2-qBA-(1-q)BAB,

which is exactly the asserted identity. No inverse of A or B, division by
an integer, convergence, or characteristic-zero argument is used.

All operations above are actual endomorphisms of all K[[z]]. Multiplication
by 1/(1-z) is coefficientwise well-defined; A and B increase valuation by
at least one. Each fixed output coefficient uses finitely many input
coefficients. Equalities first checked on monomials therefore extend to all
formal series, and the derivation itself already consists of all-series
operator equalities.

## Second independent verification by output bands

For input z^m and output shift s>=2, put u_j=1/(q^(m+j)-1), 1<=j<s.
After factoring out 1/(q^(m+s)-1), the output coefficients of AB, BA,
B^2, BAB are respectively

    u_(s-1), u_1, sum_(j=1..s-1)u_j,
    sum_(j=1..s-2)u_j*u_(j+1).

The local identity

    (1-q)u_j*u_(j+1)=q*u_(j+1)-u_j

follows by clearing the two nonzero denominators. Summing it and adding
(1-q)sum u_j telescopes to u_(s-1)-q*u_1. This proves the same operator
identity at every band, for every m, in every characteristic. Shifts below
two vanish. This is an exact formula, not interpolation from samples.

## Directly justified generalization

**PM-MIX-B2.** Let u=a*z^r, where a in K* and r>=1, put Q=q^r, and take
any lambda in K. Define A=J_u and B=J_(u/(1-lambda*u)). Then

    AB-QBA=(1-Q)(B^2+lambda*BAB).                       (4)

Proof: repeat the preceding argument with E=M_u, R=(1-lambda E)^(-1),
and Q in place of q. We have sigma A=Q A sigma and hence
QAD=E+(1-Q)A. Therefore

    EB=QBE-(1-Q)AB,
    lambda*BE=B-A.

Multiplying the first equality by lambda B on the left and using the
second on both resulting products gives

    B^2-AB=QB^2-QBA-lambda*(1-Q)BAB.

No division by lambda occurred, so lambda=0 is included and simply gives
B=A. Since q has infinite order, Q!=1 and every inverse denominator used
in defining the operators is nonzero. This is a negative criterion for
a geometrically resummed monomial-seed family, not a classification of
arbitrary rational seed alphabets.

## Exact positive and negative controls

1. Each generator separately is faithful: A^n(1) and B^n(1) have order n
   and leading coefficient 1/product_(j=1..n)(q^j-1). The distinct orders
   make their powers linearly independent after evaluation on 1. Thus the
   joint obstruction does not arise from a zero or algebraic unary operator.
2. Deleting the cubic term does not give an identity. Exactly,

       AB-qBA-(1-q)B^2=(1-q)BAB.

   On input 1 its leading coefficient at z^3 is

       -1/((q^2-1)(q^3-1)),

   nonzero in every admissible field. At q=2 this is -1/21.
3. The supplied polynomial-pair relation is a distinct control, not the
   proof of this rational identity. This work does not infer the rational
   pair from a finite polynomial truncation of its second seed.

## Appendix: audit of parent-supplied abstract proof

After I sent the independently derived identity and direct proof to the
parent, it supplied a matching parameter version and this abstract algebra
argument. I checked it independently; it is valid.

In any unital associative algebra, suppose

    ZA-QAZ=(Q-1)A^2,

and 1-lambda Z is invertible. Set B=A(1-lambda Z)^(-1), and put

    P=AB-QBA+(Q-1)B^2+lambda*(Q-1)BAB.

Using B(1-lambda Z)=A and the stated base relation,

    P(1-lambda Z)
      = A^2-BA+lambda*B*(QAZ+(Q-1)A^2)
      = A^2-BA+lambda*BZA
      = A^2-B*(1-lambda Z)*A
      = 0.

Right multiplication by the invertible factor gives P=0. The lambda=0
case is covered without a limit or division. In the operator realization
Z=M_u, Q=q^r, the base relation holds coefficientwise:

    Z A-Q A Z=(Q-1)A^2.

The formal multiplier 1-lambda Z has inverse sum_(j>=0)lambda^j Z^j,
which is coefficientwise defined since ord(u)>=1. Thus no extra topology,
analytic convergence, or inverse of A/B is silently assumed.

The parent also supplied a classical Jackson-integral source comparison;
I did not retrieve it under this scope. No historical originality claim
is made for the base relation, the resolvent closure, or the resulting identity.

## Commands, results, limits

Read commands: pwd; rg --files with AGENTS/program/seed patterns; sed over
the four repository documents listed in the ledger. No current A/C notes
were opened. No repository changes or Git commands were made.

Wrote own checker with apply_patch, then ran:

    python /tmp/pm-mix-b-check.py

The checker uses only Fraction arithmetic from the Python standard library.
It verifies 432 exact generalized monomial-action controls, the omitted-cubic
negative control, unary leading-term controls, and 378 output-band telescoping
controls. Finite checks are sanity checks for the preceding all-length,
all-characteristic proofs, not their justification. No rank scan was used.

Limitations: no complete presentation, no lowest-degree identity assertion,
no all-rational-seed obstruction, no novelty claim, no Lean verification,
and no held-out transfer or causal AI-performance claim. The specific
ordinary-faithfulness gate is resolved negatively by a structural certificate.

# PM-MIX-A: a cubic operator obstruction for the mixed rational pair

Task-scoped independent result. Repository access was read-only. I read
`AGENTS.md`, `research/RESEARCH_PROGRAM.md`, and
`research/mechanisms/Q_WORD_SEED_SYNTHESIS.md`, including the accepted
polynomial obstruction and quantum-plane calculation, but no other current
child notes. No Git operation, child delegation, literature search, or external
communication was performed. The requested model label was GPT-6.1 Sol Ultra;
the actual execution configuration is not independently exposed/verified here.

## Result: PM-MIX-A-001

Let K be any field and let q in K* have infinite multiplicative order. On
V=K[[z]], set sigma(f)(z)=f(qz), Delta=sigma-1, and

    J_b(f) = sum_{n>=1} [z^n](bf)/(q^n-1) * z^n.

Set A=J_z and B=J_(z/(1-z)). Composition is rightmost first. Then the
following exact identity holds on **all** V:

    AB - q BA + (q-1) B^2 + (q-1) BAB = 0.                 (1)

Consequently K<X,Y> -> End_K(V), X |-> A, Y |-> B, is NOT faithful.
Indeed the free polynomial

    XY - q YX + (q-1)Y^2 + (q-1)YXY

is nonzero: the coefficient of the distinct word XY is 1. This argument
includes every allowed positive characteristic and has no specialization
assumption beyond the stated infinite order.

## Full-series proof, with no inverse of A or B

Let M be multiplication by z and let R be multiplication by 1/(1-z).
Both are continuous K-linear endomorphisms of V; I-M is invertible, with
inverse R. The definitions immediately give

    B = A R,      B(I-M)=A,      BM=B-A.                  (2)

The key elementary identity is

    MA - q AM = (q-1)A^2.                                (3)

For completeness, write f=sum_{j>=0} f_j z^j. For n>=2, the z^n
coefficients on the three terms MA, AM, A^2 applied to f are respectively

    f_(n-2)/(q^(n-1)-1),
    f_(n-2)/(q^n-1),
    f_(n-2)/((q^(n-1)-1)(q^n-1)).

The claimed coefficient equality follows by clearing the two nonzero
denominators and using

    (q^n-1) - q(q^(n-1)-1) = q-1.

All coefficients in degrees 0 and 1 are zero. Thus (3) is already proved
on arbitrary series, not only on monomials or polynomials. This calculation
does not divide by an integer, so it is characteristic-free.

Define P to be the left side of (1). Using (2), associativity, and then (3),

    P(I-M)
      = A^2 - q BA(I-M) + (q-1)BA + (q-1)BA^2
      = A^2 - BA + q BAM + (q-1)BA^2
      = A^2 - BA + B[ q AM + (q-1)A^2 ]
      = A^2 - BA + BMA
      = A^2 - BA + (B-A)A
      = 0.

Right-composing with the actual endomorphism R=(I-M)^(-1) proves P=0
on all K[[z]]. No partial inverse, cancellation of a noninvertible operator,
exchange of infinite sums, or extension from a finite truncation occurs.

## Structural interpretation and certificate size

The auxiliary operator C=M+A satisfies CA=qAC by (3). Thus the obstruction
comes from a q-plane-type relation together with the genuine multiplication
unit I-M and the fractional substitution B=A(I-M)^(-1). This explains why
the infinite Taylor support of the rational seed does not evade all
ordinary operator relations. Strong K(z)-word rank 1 is not used as a
necessary condition and does not supply this conclusion by itself.

The certificate has four noncommutative monomials and maximum word length
3. Its construction and symbolic verification take a constant number of
operator rewrites, independent of any jet bound or target word count.
Applying A or B to a jet through degree N can separately be done in O(N)
field operations using q powers, denominators, and prefix sums; that finite
computation is only a sanity check, not the infinite proof.

No exact presentation of the full generated algebra, minimality of relation
degree/support, historical priority, formal Lean verification, or new general
instrument is claimed. The explicit identity resolves the assigned ordinary
faithfulness question negatively.

## Checked commands and limitations

1. `pwd` and `rg --files -g 'AGENTS.md' -g 'RESEARCH_PROGRAM.md' -g
   'Q_WORD_SEED_SYNTHESIS.md'` located the permitted instructions/definition
   files in `/workspace/scratch/415407b3c01b/ProofMotifs`.
2. `sed` read the three permitted files completely for the portions relevant
   to the task. No current B/C note was inspected.
3. An attempted Python/SymPy symbolic check failed immediately because the
   default Python lacks SymPy (`ModuleNotFoundError`). Nothing was installed.
4. A replacement built-in-Python exact check verified the cleared numerator

       (q^2 T - 1) - q(qT-1) - (q-1) = 0

   in Z[q,T], by coefficient dictionaries. It also checked (1) using
   `fractions.Fraction` at q=2 for six arbitrary rational-coefficient inputs
   through degree 13. Output:

       Universal cleared numerator in Z[q,T]: PASS.
       Exact q=2 coefficient sanity checks: PASS (6 inputs, 14 coefficients).

   These computations are explicitly supplemental; the coefficientwise
   proof and invertible right factor above establish the full result.

## Failure mechanism avoided

A tempting derivation uses A^(-1), B^(-1), because on their positive-order
images B^(-1)=A^(-1)+1-sigma. They are not invertible endomorphisms of all
K[[z]], so unrestricted use could leave a boundary defect. The proof above
eliminates that issue: only I-M is inverted, and it really is an invertible
endomorphism on the full intended space.

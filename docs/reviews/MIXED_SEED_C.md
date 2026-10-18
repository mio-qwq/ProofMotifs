# PM-MIX-C — independent adversarial/prior-art handoff

## 1. TASK ID

PM-MIX-C. Scoped subagent `/root/mixed_seed_c_ultra`. Requested configuration in
the task: GPT-6.1 Sol Ultra; actual runtime model/effort metadata was not exposed
or independently verified. No human review or formal-assistant compilation is claimed.

## 2. RESEARCH QUESTION

Is the K-algebra map K<X,Y> -> End_K(K[[z]]) sending X to A=J_z and Y to
B=J_(z/(1-z)) faithful? Challenge any affirmative claim by a primary-source
comparison and an independent structural derivation.

**Verdict: not faithful, in every allowed field.** The nonzero free polynomial

    P(X,Y)=XY-qYX+(q-1)Y^2+(q-1)YXY

satisfies P(A,B)=0 on **all** K[[z]], not just on 1.

## 3. KNOWN ASSUMPTIONS

K is any field; q in K* has infinite multiplicative order; sigma fixes K and
sends f(z) to f(qz). Delta_0^-1 divides the coefficient of z^r by q^r-1
for r>=1 and returns zero constant. All operators act rightmost first.
The optional parameter c below is any scalar in K, including zero.

Infinite order ensures every denominator used on positive powers is nonzero.
No characteristic-zero hypothesis is used. In characteristic p, q=t in F_p(t)
is a legitimate control; a fixed nonzero element of a finite field is not.

## 4. AVAILABLE EVIDENCE / PRIMARY-SOURCE COMPARISON

Repository material actually read, without inspecting other current child notes:
AGENTS.md; research/RESEARCH_PROGRAM.md; research/mechanisms/Q_WORD_SEED_SYNTHESIS.md
in full (the last through its final section). No git command was used.

### Bell–Rogalski: nearest free-subalgebra criterion

Primary published PDF: Jason P. Bell and Daniel Rogalski, *Free subalgebras of
quotient rings of Ore extensions*, Algebra & Number Theory 6:7 (2012), 1349–1368,
DOI 10.2140/ant.2012.6.1349.
<https://msp.org/ant/2012/6-7/ant-v6-n7-p03-p.pdf>

Read published pp.1349–1356 (PDF indices 1–8), especially Notation2.1,
Theorem2.2 and its proof, Theorem2.3, Lemma2.4. Theorem2.2 works over arbitrary
characteristic: in D(x;sigma,delta), let psi=sigma-1+delta and E=ker psi.
If b is not in sigma(E), and psi(u) in sigma(E)+sigma(E)b forces u in E,
then b(1-x)^-1 and (1-x)^-1 freely generate. These are specified generators,
not every rationally transformed pair. Its hypotheses and generator form
were not established for our A,B. The paper explicitly warns that quadratic
growth before localization does not control subalgebra growth after division
localization (pp.1349–1350). Neither ambient Ore membership nor ambient free
subalgebra existence proves our particular pair free or nonfree.

Version check: <https://arxiv.org/abs/1101.5829> reports v1 30Jan2011,
v2 2Oct2011, with changes to main-theorem statements/proofs. The actual theorem
comparison above uses the published PDF, not its abstract. No assertion about
unread subsequent sections is needed.

### Lorenz: ambient existence is not specified-pair freeness

Primary preprint MPI/SFB84-60, Martin Lorenz, *On free subalgebras of certain
division algebras*:
<https://archive.mpim-bonn.mpg.de/2907/1/preprint_1984_60.pdf>

Read theorem statement, Lemmas1–2 and their proofs, and opening proof/proposition
through printed p.9 (PDF indices1–9); later closing lines were exposed but not
needed. The theorem says Q(k(t)[X;alpha]) contains a noncommutative free
k-subalgebra when alpha has infinite order. The proof chooses a primitive
element a satisfying a pole-orbit condition and proves freeness of
a,a(1-X)^-1. This does not identify our A,B. The retrieved object is the
1984 preprint; the 1986 journal version was not independently read here.

### Díaz–Pariguan: closest explicit operator relation

Opened on the coordinator's later audit request, not used to generate the
independent candidate relation. Rafael Díaz and Eddy Pariguan, *On the
q-meromorphic Weyl algebra*, arXiv:0804.0183, retrieved PDF stamped
**v2, 23Jun2009**:
<https://arxiv.org/pdf/0804.0183>

Read §3 from its opening through Theorem6 and Lemma7 (printed pp.6–8;
PDF indices5–7), plus initial title/version context. Definition4 gives
MW_q=C<x,y>[q]/(yx-qxy-x^2), with formal q. The analytic discussion fixes
real 0<q<1. Theorem6 represents x by Jackson integration and y by multiplication;
Theorem5 is the q-derivative representation. **The integral result is Theorem6,
not Theorem7 in this retrieved version.** With I=(q-1)A and y=Z, its defining
relation becomes ZA-qAZ=(q-1)A^2. Our coefficient proof supplies the
all-field/formal-series extension; their analytic hypotheses alone do not.
The target A,B cubic follows by elementary elimination of invertible
multiplication S=1-cZ. No historical-priority conclusion is drawn for that
specialized cubic. A direct version-suffixed PDF fetch failed; the successful
unversioned PDF visibly identifies its version.

One structural search query was used, then primary documents were opened.
No absence-of-search claim or exhaustive literature claim is made.

## 5. EXPECTED OUTPUT / PROOF

### PM-MIX-C-1: all-series commutator

Write Z=M_z. For every m>=0,

    (ZA-qAZ)(z^m)
      = [1/(q^(m+1)-1)-q/(q^(m+2)-1)] z^(m+2)
      = (q-1) A^2(z^m).

Each output coefficient depends on finitely many input coefficients, so the
identity extends to all K[[z]]. Equivalently this is coefficientwise, and no
topological assumption on K is involved.

### PM-MIX-C-2: universal rational-seed obstruction

For any c in K, let S=1-cZ and B_c=A S^-1. Here S is genuinely invertible on
all K[[z]]: its inverse is multiplication by 1/(1-cz). Also B_c=J_(z/(1-cz))
and B_c S=A. Define

    P_c=AB_c-qB_cA+(q-1)B_c^2+c(q-1)B_cAB_c.

Using only the previous commutator and B_c S=A,

    P_c S
      = A^2-B_cA+cB_c[qAZ+(q-1)A^2]
      = A^2-B_cA+cB_cZA
      = A^2-B_c(1-cZ)A
      = 0.

Since S is a unit, P_c=0 as an operator. For c=1 this is the requested
counterexample. The free polynomial is nonzero because the distinct word XY
has coefficient1. At c=0, B_c=A, and the formal polynomial is still nonzero;
its operator evaluation vanishes, as it should. No division by c occurs.

### Independent coefficientwise audit of PM-MIX-C-2

Let d_k=q^k-1. For n>=m+2 put M=m+1 and N=n-1. The coefficient of z^n in
P_c(z^m) is c^(n-m-2)/d_n times

    1/d_N-q/d_M
       +(q-1) sum_(k=M)^N 1/d_k
       +(q-1) sum_(k=M)^(N-1) 1/(d_k d_(k+1)).

It vanishes by the exact local identity

    (q-1)/(d_k d_(k+1)) = 1/d_k-q/d_(k+1)

and finite telescoping. For n<m+2 every term is zero. This proves all
matrix entries, for arbitrary m,n, and hence all series coefficientwise.
It is not a finite matrix rank argument.

### PM-MIX-C-3: universal noncommutative polynomial certificate

Over Z[q,c]<A,B,Z> define S=1-cZ,

    R0=ZA-qAZ-(q-1)A^2,
    R1=BS-A,
    H=A+(q-1)B+c(q-1)BA,
    P=AB-qBA+(q-1)B^2+c(q-1)BAB.

Exact free-polynomial expansion verifies

    P S + R1 A + c B R0 - H R1 = 0.

Thus the elimination uses no inverses of A or B, no domain cancellation,
and no hidden relation beyond R0,R1 and the genuine unit S.

## 6. ALLOWED SCOPE / ACTUAL ACTIONS

Repo was read-only. Only this note and /tmp/pm_mix_c_checker.py were written.
No Git operation, child researcher, or external communication was performed.
Web retrieval was primary-document research, not outbound correspondence.

Commands actually run included:

    pwd && rg --files -g 'AGENTS.md' -g 'program*' -g 'Q_WORD_SEED_SYNTHESIS.md'
    rg --files -g '*program*' -g '*PROGRAM*' -g 'AGENTS.md'
    sed -n '1,260p' AGENTS.md
    sed -n '1,300p' research/mechanisms/Q_WORD_SEED_SYNTHESIS.md
    sed -n '300,450p' research/mechanisms/Q_WORD_SEED_SYNTHESIS.md
    sed -n '1,240p' research/RESEARCH_PROGRAM.md
    python /tmp/pm_mix_c_checker.py

An initial inline Fraction q=2,N=9 check on1 returned zero. An initial checker
importing sympy failed with ModuleNotFoundError; it was replaced completely by
a dependency-free implementation. Runtime/path diagnostics found no sympy;
no package was installed. All edits used apply_patch.

Final checker command exited0 in about0.32s. It verified the universal
noncommutative certificate over Z[q,c], the universally cleared telescoping
kernel, every input monomial modulo z^18 at Q,q=2,c=1, modulo z^12 at
Q,q=3,c=0, and modulo z^9 over F_p(t),q=t,c=1 for p=2,3,5.
All arithmetic is exact; finite tests are explicitly secondary regressions.

## 7. INDEPENDENCE REQUIREMENT / LATER AUDIT

The initial candidate cubic was sent to the coordinator **before** receiving
their proof. It was independently obtained by fraction-ring heuristic:
c0=A^-1, d0=B^-1 yield a q-Weyl relation and suggest the cubic after formal
denominator clearing. This was not accepted as an all-series proof.

**Critical domain warning:** A and B raise order, so neither is invertible on
all K[[z]]. A Jackson derivative has constants kernel. Expressions A^-1,B^-1
cannot silently be treated as two-sided inverse operators there. The accepted
proof above removes those symbols altogether.

The coordinator subsequently supplied the same cubic and the direct S-proof.
I audited its signs, the parameter c, characteristic2, c=0, rightmost-first
composition, and full-domain extension; no defect was found. The independent
coefficient telescoping argument and the universal certificate give distinct
checks. No coordinator code had been supplied/read at handoff time.

## 8. STOP CONDITIONS

The bounded structural/literature gate is complete. No rank scan was used as
proof, no general Ore growth assertion was made, no presentation or growth
classification is claimed, and no wider rational-seed impossibility theorem
is inferred. It is appropriate to stop this neighboring case and resume the
program's cross-mechanism representation-discovery question.

## 9. HANDOFF

Accept the universal nonfaithfulness relation and direct all-series proof.
Keep correctness separate from historical novelty: the ambient theory and
base Jackson commutator are classical; the bounded search does not establish
priority for the specialized eliminated cubic. A strong-rational-word rank
defect alone still does not imply ordinary operator nonfaithfulness; here an
actual nonzero free polynomial has been produced.

### Later coordinator source audit

On the coordinator's explicit request, read in full and audited read-only:

    tools/resolvent_certificate.py
      SHA256 8c419aa95faacd98376685908bc3c8a1bebd7a7c7940cdbdc67354ba5916cc26
    tests/test_resolvent_certificate.py
      SHA256 fc121cd26cc7b43fc3bb8faa5f1123aff43e8b4ece7e0a5a940d4cad98bdd1c8

Commands:

    sed -n '1,320p' tools/resolvent_certificate.py
    sed -n '1,320p' tests/test_resolvent_certificate.py
    sha256sum tools/resolvent_certificate.py tests/test_resolvent_certificate.py
    PYTHONDONTWRITEBYTECODE=1 python -B -m unittest discover -s tests -p 'test_resolvent_certificate.py' -v

All six tests passed, including mod-p final-remainder reduction, malformed-row
rejection, omitted/corrupted relation rejection, c=0, and lack-of-unit
counterexample. The explicit no-unit example q=2,c=1,A=0,B=Z=1 has
R0=R1=S=0 but P=1, correctly displaying the cancellation hypothesis.

An additional inline python -B program loaded the coordinator source and my
independent checker with runpy, converted the flattened coordinator polynomial
payload into my nested polynomial representation, and verified its universal
certificate with my independent arithmetic engine; AB coefficient1 was also
checked. It passed. PYTHONDONTWRITEBYTECODE=1 avoided repo cache writes.

No mathematical or arithmetic defect found at those exact hashes. Important
API scope: verify(data) checks only the supplied equality. It accepts all-zero
polynomials, as a generic equality verifier should. It does not establish that
the payload is the canonical theorem, that P is nonzero, or that S is invertible.
The demo separately checks its canonical P is nonzero; the mathematical
application separately supplies the actual S unit and R0=R1=0. A stronger
public validator is unnecessary for this demonstration, but if arbitrary
untrusted certificates are later accepted, either name the API verify_identity
or add a separate canonical-theorem validator with explicit hypotheses.
Its characteristic argument permits any modulus>=2; this is harmless for
ring-polynomial equality and must not be read as certifying a field.

Source/checker audit completed. Stop this bounded gate.

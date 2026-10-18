# Eleventh-cycle normal-character gate and quartic boundary

Date: 18 October 2026. Starting verified research head:
`10c06a57d5b4795c69fec819c832f141a0c8e863`.

## Recovery and independent task ledger

The full Git fetch and GitHub all-branches endpoint found only main and
research/ongoing, at the expected heads, with a clean working tree and no
other active task. The coordinator read the governance/recovery files and
continued SC-014's precise normal-element gate. Only the coordinator edited
shared state, accepted the results and published the checkpoint.

| Task | Research question and starting evidence | Allowed scope and independence | Stop condition and accepted handoff |
| --- | --- | --- | --- |
| PM-CYCLE11-A | Can a normal element meet the three-character filter, giving simultaneous cubic avoidance? | Initially independent read-only theory and temporary notes; no shared edits | Full classical CRT/Fourier/Kloosterman count, repeated-factor treatment and all-large-degree range; exact source review; no connectivity claim |
| PM-CYCLE11-B | What equation replaces a linearized kernel at quartic digitweight? | Independent read-only algebra and bounded targeted counter-search; temporary code/notes only | K-valued quadratic equation, multiplicity factorization, normality exclusion of2+2; exact normal but disconnected m8 boundary, then stop searching |
| PM-CYCLE11-C | Do primary normal/primitive AP results already imply this exact filter? | Two Parallel Search rounds plus primary documents; temporary notes only | Checked classical indicator/mixed-sum overlap, exact bound independently matching A, and nonmatching theorem limits; no novelty inference |
| PM-CYCLE11-D | Resolve only the degrees3/4/5/8 not settled by the bound, with3 already structurally impossible | Initially read-only targeted4/5/8 arithmetic; later only normal_pattern_certificate.py, its tests and SC-015/COMPUTATION.md | Found actual degree4 impossibility, pure polynomial factor/annihilator proof and positive5/8 witnesses; standalone Bezout certificate and9 corruption tests; files frozen |
| PM-CYCLE11-E | Independently challenge the count, endpoints, repeated factors, degree range, small exceptions and quartic claims | Read-only derivation/source review and own coordinate code; no project/B imports | Accepted final proof; exhaustive m3/m4 coordinate audit; independent targeted m8 quartic witness with Rabin/rank/character/trace checks |

The coordinator independently obtained the same pairwise-character indicator
and local-CRT Fourier coefficient norm before seeing the complete notes,
checked the finite range and all hypotheses, inspected exact code and tests,
and integrated the final proof. E's verdict and independent implementation
are actual scoped AI work, not human peer review or a proof assistant.

## Accepted mathematics and revised assumptions

PM-THEOREM-0019 proves the exact normal-filter existence classification in
the range m>=3: existence iff m>=5. The initial sufficient bound alone
did not decide3/4/5/8. Degree3 has a constant-frequency obstruction. D
found that degree4 is genuinely impossible, rather than merely difficult
to search, and supplied a three-input polynomial Bezout certificate whose
two factors obey different low-degree Frobenius annihilators. An attempt
to use only the degree-three annihilator for all eighteen points was
rejected: six points require the separate F9 factor. Explicit degree5/8
witnesses complete the positive proof.

The normality Fourier calculation retains every P^e module factor when3
dividesm. Its nonprincipal absolute coefficient mass is Theta*(W-1), not
an assumed semisimple expression. The raw character-filter formula can
have nonzero values at0,+-1, but the normality indicator vanishes there;
this removes the boundary correction exactly. Additive-twisted quadratic
sums reduce to nondegenerate finite-field Kloosterman sums. A and E read
the author-hosted Conrad primary paper, including the2sqrt(q) bound; the
coordinator checked the specialization and primary-source retrieval. No
integer-modulus Kloosterman estimate is substituted.

One normal parameter excludes every nonaffine cubic-representable frequency
simultaneously. PM-THEOREM-0020 shows that quartic frequencies instead give
Q(y)=-1, a K-valued quadratic constraint; normality removes2+2 repetitions
but not all remaining patterns by the stated argument.

PM-COUNTEREXAMPLE-0009 supplies the necessary warning. In F6561, y4863 is
normal and passes the square filter; its seed has connectivity index4 and
a surviving four-distinct quartic frequency820. The component theorem gives
kernel at least36 versus complete9, and an explicit trace function violates
a true omitted edge. E independently reconstructed the witness without B
arithmetic. This refutes normality alone as a sufficient replacement, not
the possible criterion requiring both normality and connectivity. Exploratory
failures to find a connected normal quartic counterexample are not theorem
evidence and were stopped; no large-degree table is used in acceptance.

## Sources, execution and limits

The literature gate records primary normal-unit counting, normal-character
indicators, mixed sums and consecutive primitive-element results. Generic
primitive-normal and consecutive-primitive theorems do not imply that their
witness sets intersect. Extraction dates are not treated as original paper
dates. No bounded search outcome establishes historical priority. The
normal-character bound is a classical-tool application, conservatively
recorded as infrastructure with novelty unverified.

The integrated local suite passed120 tests; actual log sc015-tests.log.
Nine new tests reject corrupt gcd, Bezout, annihilator, field, normal basis,
character/seed, count and scope claims. Five new outputs regenerated
byte-identically. The main certificate's generation/check paths share its
polynomial arithmetic. B's and E's coordinate programs were independently
written but use the same field presentation and classical algorithms.
The independent E audit enumerates only m3/m4; its m8 check is targeted.
The main basecase verifier uses no field enumeration. Bound arithmetic
checks finite factor counts and induction anchors, not an infinite scan.
Actual commands and the snapshot manifest accompany the reports.

Four new replay steps bring the workflow to22 deterministic replay steps.
Read the hosted run at its actual new mathematical SHA before reporting
success; the preceding f363f13 run cannot certify this tree. Old manifests
remain historical snapshots when later receipt metadata changes.

Next exact subproblem is PM-QUESTION0002, normal filtered AND connected
parameters in every m>=5. Forcing (y+1)/y to have orderN, rather than
orderq-1, is a sufficient route; compare2-primitive normal rational-image
literature first. Genuine2+1+1/four-distinct quartic and higher-frequency
control still lies beyond the normal count. PM-QUESTION0001 remains open.
No human review, Lean compilation, final academic release or priority
claim accompanies this checkpoint.

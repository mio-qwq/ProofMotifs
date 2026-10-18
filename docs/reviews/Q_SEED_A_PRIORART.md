# PM-Q-A: original q-multiplicity comparison

Task handoff, 18 October 2026 UTC. Repository read-only; no Git operations or children. Read `AGENTS.md`, `research/RESEARCH_PROGRAM.md`, `docs/reviews/SUCCINCT_CHECKPOINT.md`, the existing `SUCCINCT_C_ADVERSARIAL.md`, and the existing source ledger. Did not read new B/C task notes. The parent identifies this child as the specifically configured GPT-6.1 Sol / Ultra researcher; that is not evidence about the coordinator's runtime settings.

## Decision

**No historical or missing-tool gap is proved.** Actual journal full text now replaces the earlier slides-only comparison. More importantly, Amou--Matala-aho--Vaananen (2007) already explicitly proves a q-multiplicity theorem in arbitrary characteristic. Consequently, “q-difference multiplicity in every characteristic” is not a defensible novelty description. The exact degree-only bound under a regular invertible fundamental matrix is not displayed in the inspected older statements. That is a statement-level coverage observation, not proof that the bound or argument is new.

The two remaining requested originals have exact access limits: the 2007 Bertrand chapter was identified in an actual contents scan, but its text was not obtained; the original Moura JDCS2003 article remains subscription-only in the accessed publisher record. Neither was silently replaced by slides or by the different hyperelliptic paper.

## 1. Target and exposure

Source116 revision `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, `sections/order.tex`, blob `ab18a99256085b49fddba4c4d8ee2963016733de`, all 156 lines read directly from the pinned raw source:

https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/build/sections/order.tex

Its Order Bound theorem, lines18--32: any field K, infinite-order q in K*, sigma(z)=qz, H in GL_m(K[[z]]), sigma(H)=AH, A=P/Q with Q(0) nonzero and numerator/common-denominator degrees at most nu; constant u,v; nonzero uHv has order at most nu*binom(m,2). Proof read through line148, including constant-span/Casoratian construction, rational-row degree bound, and unit-minor invariance. Also read all164 lines of pinned `words.tex`, blob `882cb46e0e824041ecddcd051aa97a20d96cd050`.

## 2. Theorem-to-hypotheses/access table

| Primary source/version | Actual text inspected | Statement and comparison | Access limit |
|---|---|---|---|
| Bertrand, *Multiplicity and vanishing lemmas...*, FPM16(5)(2010),19--30, original Russian journal PDF | Intro p21; complete q sections4--5, printedpp24--28; PDF extraction218--420, especially256--292 and339--341 | Theorem4.1: complex q, 0<|q|<1; regular singular at0 with quasi-unipotent local type; polynomial row degree L; a weighted multi-point vanishing bound with system-dependent c(Psi). Corollary4.1 gives finite ord(s.Y)<=r L+c(Psi). Printedp27 explicitly says effectivity of c(Psi) from A is not known. No nu*binom(m,2) displayed. | Actual original full PDF obtained, not slides. Relevant theorem and proof sections read; unrelated irregular-period section6 not audited. |
| Bertrand, JMS180(5)(2012),542--549, DOI10.1007/s10958-012-0652-3 | Publisher abstract, references, translation metadata | Publisher confirms translation of FPM2010. | English full PDF unavailable; no separate English theorem pagination claimed. |
| Bertrand2007, *Multiplicity estimates for q-difference operators*, CRMSeries4,65--71 | Actual book contents scan, PDFp3/contentspVI, lines44--48 | Confirms final chapter title, §1 statement p65, §2 proof of Theorem1.1 p68, referencesp70. The journal bibliography instead calls it “Multiplicity estimates for values of q-difference equations”; do not treat these title variants as separately read papers. | Chapter text not obtained. Publisher book page offers print edition, not chapter full text. Author research page links 2007 slides, not this chapter. |
| Moura, JDCS9(1)(2003),73--88, DOI10.1023/A:1022155217548 | Original publisher title, abstract, bibliographic record | Differential system, nonsingular point, polynomial restricted to a solution. | Full PDF inaccessible; original theorem numbers/constants and exact proof overlap remain unverified. |
| Moura, *On the multiplicity of the hyperelliptic integrals*, arXiv:math/0312323v1,17Dec2003 | §2 printedpp3--6, extraction86--231; referencespp17--18, especially1120--1121 | Different paper. Theorem1 recalls a differential flatness bound attributed to JDCS2003; the derivative-row/minor and fundamental-matrix/Wronskian mechanism is explicitly explained. Confirms the conceptual derivative baseline, not an all-characteristic shift theorem or independent access to JDCS2003. | Hyperelliptic-specific later proof not fully audited; not a substitute for original JDCS text. |
| Amou--Matala-aho--Vaananen, *On Siegel--Shidlovskii's theory for q-difference equations*, ActaArith127(4)(2007),309--335, publisher PDF | §2 printedpp310--312; relevant §3--4 pp313--317; note added in proofp334. Extraction36--140,204--264,330--528,1894--1906 | Explicitly any characteristic, infinite-order q. Theorem2.1 assumes components of a formal solution are K(z)-linearly independent; polynomial initial row degree n; shift-row rank r; ord(L1)<=r n+O_system(1). Lemma4.1 gives rational shift-Krylov closure and system-uniform dependence-degree control. | These statements do not display target's degree-only constant; rational independence is extra and cannot be inferred from regular fundamental H. Full 27-page PDF available; arithmetic application sections5--10 not audited. |

Primary URLs:

- Bertrand2010 journal record: https://www.mathnet.ru/eng/fpm1334 ; actual original PDF: https://www.mathnet.ru/php/getFT.phtml?jrnid=fpm&option_lang=eng&paperid=1334&what=fullt . Web references `turn247view1`, `turn249view1`, `turn249view2`. Screenshots of pages25/27 timed out; the PDF's extractable text was available.
- Bertrand2012: https://link.springer.com/article/10.1007/s10958-012-0652-3 (`turn246view2`).
- Bertrand2007 actual contents: https://toc.library.ethz.ch/objects/pdf/e01_978-88-7642-206-5_01.pdf (`turn262view1`); publisher https://link.springer.com/book/9788876422065 (`turn261view0`), https://edizioni.sns.it/prodotto/diophantine-geometry/ (`turn262view0`). Author index https://webusers.imj-prg.fr/~daniel.bertrand/Recherche/recherche.html (`turn252view0`).
- Moura JDCS2003: https://link.springer.com/article/10.1023/A:1022155217548 (`turn248view3`). Direct publisher PDF request also failed (`turn275view0`).
- Moura separate hyperelliptic2003: https://arxiv.org/pdf/math/0312323 (`turn273view0`, `turn274view0`).
- AMV2007 publisher full text: https://www.impan.pl/shop/en/publication/transaction/download/product/83675 (`turn253view0`, `turn256view0`, `turn256view1`, `turn256view2`). Its p334 note expressly says Bertrand independently obtained an analogue of Theorem2.1; it is not independent access to his chapter.

## 3. Exact mathematical conclusions from the comparison

### PM-Q-A1: target local condition is strictly stronger than regular singularity

This is a direct calculation, not an attribution. From sigma(H)=AH and H(0) invertible, evaluation at0 gives H(0)=A(0)H(0), hence **A(0)=I**. In fact the system is formally gauge-trivial via H. Merely assuming A regular and invertible at0, or regular singular/quasi-unipotent, is weaker.

The scalar example H=z^N, A=q^N, N>0, has a regular invertible constant coefficient matrix A and an analytic solution, but H is not a unit at0. A=P/Q has degree0 while ord(H)=N. Therefore a uniform degree-only estimate ord(y)<=nu*binom(m,2) is false under just that weaker local system hypothesis, already for m=1. A system-dependent constant may absorb N. This proves a concrete hypothesis boundary; it does **not** establish historical novelty of the stronger-hypothesis theorem.

Complex |q|<1 theorems cannot be directly cited for arbitrary infinite-order q. Unit-circle q and formal, potentially nonconvergent solutions are additional mismatches. AMV2007 removes this characteristic/analytic restriction, so comparisons must include it, not only Bertrand.

### PM-Q-A2: AMV rational independence is not automatic

Take H=I+z E12, A=I+(q-1)z E12, over any field with infinite-order q, and v=e2. Then H is invertible over K[[z]], degree parameter nu=1, and Hv=(z,1)^T. Its two components are K(z)-linearly dependent. Thus source116's inputs need not satisfy AMV Theorem2.1 in the supplied coordinates. Choosing a rationally independent subsystem introduces rational changes of coefficients; no degree-preserving reduction to the displayed explicit target bound has been proved here. Conversely, failure of that direct substitution is not a theorem that AMV's machinery cannot derive it.

### PM-Q-A3: source116 is an explicit regular-fundamental specialization of established mechanisms

Its proof uses a constant-field span, shift Casoratian, degree-controlled dual rows, and invariance of minor valuations under a power-series unit matrix. It yields a directly computable truncation constant from (m,nu), unlike a displayed O_system(1). The needed gain is explicit **under the stronger input contract**. No new auxiliary-map discovery algorithm or strongest-baseline speedup follows from this comparison. It would be incorrect to promote these observations to “the older theory has no such tool.”

## 4. Rational summability / iterated difference words

| Primary source | Read range | Verified contribution and limitation |
|---|---|---|
| Chen--Singer, AAM49(2012),111--133, author journal copy, DOI10.1016/j.aam.2012.04.003 | §2 assumptions printedp113; §2.3 pp116--118, especially Prop2.10. Extraction143--166,345--494. https://singer.math.ncsu.edu/papers/YAAMA1465.pdf (`turn264view0`) | Rational q-summability iff q-orbit residues, including infinity residue, vanish. Characteristiczero is explicitly assumed. The proof exposes endpoint survival/weighted residue telescoping. Source116 proves its simpler disjoint-single-pole obstruction in every characteristic. No unrestricted positive-characteristic residue theorem was inferred. |
| Schneider, *Parameterized Telescoping Proves Algebraic Independence of Sums*, arXiv:0808.2596v1,19Aug2008 | §2 pp2--3, §3 Theorem3.1 and proof pp4--5; extraction73--149,252--291. https://arxiv.org/pdf/0808.2596 (`turn269view0`) | Nonexistence of nonzero constant combination sum c_i f_i=sigma(g)-g iff a constant-preserving tower of independent Sigma* adjunctions with sigma(t_i)=t_i+f_i exists. Difference-field statement, not only ordinary shifts; characteristiczero explicitly imposed in footnote1 p2. This is a strong obstruction-to-independence baseline, not the identical recursive all-word theorem. Karr1981 is credited there, but its original proof was not independently read. |

The prior differential-word reference remains DDMS arXiv:1101.4497v3, previously read by reviewerC, not newly reaudited here. It must not be called the same difference theorem.

### PM-Q-A4: precise reusable difference-word certificate (source-derived, no priority claim)

Let E be a difference field with automorphism sigma and constant field K. Let L contain E and carry an extending automorphism. Suppose b_1,...,b_n lie in E and elements h_w in L satisfy h_empty=1 and

    sigma(h_iw)-h_iw = b_i h_w.

If the classes [b_i] are K-linearly independent in the additive quotient E/(sigma-1)E, then all h_w are E-linearly independent. The proof is valid in arbitrary characteristic: assume a finite relation, minimize maximum word length then top-level support, normalize one top coefficient to1, apply sigma and subtract. All transformed coefficients must vanish by minimality. Top coefficients are in K; at the next level the assumed quotient independence kills every top coefficient, contradiction.

If additionally const(L)=K, the converse holds: sum c_i b_i=sigma(R)-R gives sigma(sum c_i h_i-R)=sum c_i h_i-R, so this expression lies in K and produces a dependence among1,h_1,...,h_n. Thus, in the same-constant realization, **all-word linear independence is equivalent to a length-one parameterized telescoping obstruction**. Source116's orbit-endpoint proof is one exact certificate of that obstruction. This packages its argument; it is not asserted as a new theorem.

The difference product rule is accounted for: the transformed coefficient of h_w is sigma(R_w)-R_w+sum_i b_i sigma(R_iw). No derivation rule was used. All constant-field hypotheses and the recursive realization must be checked; bare failure of an algorithm to find g is not an obstruction certificate.

## 5. Handoff / next operation

1. Update the old source ledger: Bertrand2010 is no longer slides-only; English2012 remains unread; add AMV2007's explicit all-characteristic theorem and its actual hypotheses.
2. Keep exact historical overlap unresolved until a legal full scan of Bertrand2007 and MouraJDCS2003 is supplied or retrieved. The identified publisher/catalogue records provide exact acquisition targets; do not contact authors or purchase without separate authority.
3. Treat (m,nu)-computable regular-fundamental truncation as the exact local input/output contract, and parameterized telescoping classes as the word-encoding certificate. Compare legal representation generation under equal input/cost rather than relabel these mechanisms as missing.
4. No computation, formal verification, publication, or historical priority claim was performed. PM-H4/H5 remain open. No residual missing-tool gap was proved.

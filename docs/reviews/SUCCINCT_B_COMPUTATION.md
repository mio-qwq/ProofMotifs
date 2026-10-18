# PM-SUCCINCT-B — independent exact reachable-space verification

## Task ledger and independence

- TASK ID: PM-SUCCINCT-B.
- RESEARCH QUESTION: Given explicit exact matrices for the noncommutative series `s(w)=lambda A_w gamma`, independently verify the proposed bounded reachable-row basis / closure certificate and short witness, and challenge their hypotheses.
- KNOWN ASSUMPTIONS: A specified field; finite alphabet; stationary `r x r` transition matrices; explicit initial/final vectors; exact field operations. Code covers Q and prime fields Fp.
- AVAILABLE EVIDENCE: Repository `AGENTS.md` and `research/experiments/succinct-transfer-protocol.json`; task-supplied frozen revision `2b8dd9e` (not independently resolved, because this task prohibits Git); primary literature listed below; executable exact checks below.
- EXPECTED OUTPUT: Independent implementation, distinct certificate checker, full small expansions, genuine path cancellation, field specialization/rank change, malformed closure challenges, and a succinct exponential-word family.
- ALLOWED SCOPE: Repository read-only; only `/tmp/pm-succinct-b*` deliverables written, with apply_patch. No Git commands or child agents.
- INDEPENDENCE REQUIREMENT: No family116 manuscript, scope, proof, or agent-A notes read. Only its title and frozen protocol were visible. The construction/proof was independently reasoned out before reading the primary weighted-automata reference. Source-level target transfer was deliberately not evaluated.
- STOP CONDITIONS: Stop after exact executable independent controls and mathematical handoff; no novelty, black-box conversion, or LP-performance claim inferred from success.
- HANDOFF: `/tmp/pm-succinct-b.py` and this document.

## Mathematical statements and proofs

### PMB-1: exact finite basis and short witness — proved; classical reproduction

Let K be any field, Sigma a finite alphabet, `lambda in K^(1 x r)`, `gamma in K^(r x 1)`, and `A_a in K^(r x r)` for every letter a. Put `A_empty=I` and multiply transitions in word order. Let

`V = span_K {lambda A_w : w in Sigma*}`, with `d=dim V <= r`.

There exists a basis of V consisting of at most r actual reachable rows, with representing words of length at most `d-1` when d>0. The series is identically zero iff every row of that basis annihilates gamma. Otherwise there is a word w with `|w| <= d-1 <= r-1` and `lambda A_w gamma != 0`. When lambda=0, d=0 and the series is zero; the empty word is a legitimate witness for a nonzero constant coefficient.

Proof: Let `V_j=span{lambda A_w: |w|<=j}`. Then `V_(j+1)=V_j + sum_a V_j A_a`. Equality at one stage makes V_j invariant under every transition, so it equals V. If lambda is nonzero, `dim V_0=1`; before stabilization every inclusion strictly raises dimension. Thus `V_(d-1)=V`. Choose a reachable-row basis from those words. A linear functional `v -> v gamma` vanishes on V exactly when it vanishes on that basis. This proves both identity and witness claims over every field, without assumptions on characteristic, positivity, or lack of path cancellation.

Algorithm: Initialize a queue with lambda if nonzero, annotated by the empty word. For each accepted basis row b, offer `b A_a` to incremental exact elimination; retain it and enqueue its annotated word only if independent. At most d rows are retained and at most `1+|Sigma|d` rows offered. At termination the retained span contains lambda and is closed under every A_a, hence equals V. Retained word ancestors are also retained, so their lengths are at most d-1. Breadth-first processing is used in the implementation.

Tightness: For r=D+1, take both letter matrices equal to the superdiagonal shift S, `lambda=e_0`, and `gamma=e_D`. Every word of length D has coefficient 1, and every other length has coefficient 0. Therefore the shortest witness has length `D=r-1`: replacing r-1 by r-2 is false, even over F2.

### PMB-2: compact local zero certificate — proved; invariant-subspace packaging

The certificate consists of `B in K^(m x r)`, `alpha in K^(1 x m)`, and one `C_a in K^(m x m)` per letter satisfying

1. `lambda = alpha B`;
2. `B A_a = C_a B` for every a;
3. `B gamma = 0`.

These equations imply `lambda A_w gamma = alpha C_w B gamma = 0` by induction on the word. Independence and reachable-word provenance of B are **not needed for soundness of a zero certificate**. They are needed if one additionally certifies that B is an actual basis and that m equals the reachable rank. The implementation verifies these stronger properties using word replay and a separately coded full Gaussian rank check. It also checks all shapes, all alphabet letters, field tag, output values, and claimed nonzero witness.

Completeness follows from PMB-1 by choosing B to be a reachable basis. An empty B is valid precisely when lambda=0. A positive certificate is simply a word and its nonzero coefficient, independently checked by exact sequential multiplication. Zero-certificate scalar size is `mr + |Sigma|m^2 + m`, plus O(m) output values in the implementation. Word annotations cost at most O(m^2) letters. This is polynomial in the supplied transition representation, not in the number of words.

### PMB-3: resource and field qualifications

Incremental elimination and dense multiplication give `O((|Sigma|+1)r^3)` field operations for synthesis, including final closure coefficients, and polynomial representation/certificate size. An efficient checker for only the three invariant equations has the same cubic bound. **This executable's stronger checker deliberately replays each basis word independently**, which can cost `O(r^4+|Sigma|r^3)` field operations; do not report the implementation as a cubic verifier without optimizing shared prefixes. Positive witness verification costs O(r^3) with the short bound.

Over Fp with a promised prime modulus, field operations have polynomial bit cost in log p. The executable validates p by trial division solely for the small test primes; **that primality validator is not polynomial in log p**, so the whole Python entry point is not an arbitrary-prime bit-complexity implementation. Over Q, binary rational input bit length must be counted. A common input denominator delta makes each length <=r reachable row a scaled integer matrix product; its numerator/denominator bit lengths are polynomial in r and total input bit length. Coordinates are ratios of bounded-order minors, so fraction-free or ordinary exact elimination has polynomial-size rational values. Unit-cost field counts alone are not a rational bit-cost argument.

Specialization is field-sensitive. A rational input can be reduced modulo p only if all input denominators are invertible modulo p. Even then reachable rank and zero/nonzero status can change. A characteristic-zero basis or elimination pivot is not automatically valid in every positive characteristic. The checker rejects basis reuse after rank drops.

### PMB-4: fixed-length/layered distinction and input boundaries

For a layered representation `lambda A_(1,a1)...A_(D,aD) gamma`, each layer can independently keep at most its width many reachable-row generators. The local equations become `B_(j-1) A_(j,a)=C_(j,a) B_j`, with initial containment and final annihilation. Induction gives the same sound negative certificate; a retained nonzero output produces a word of length exactly D. Uniform width w and explicitly supplied layers admit O(D |Sigma| w^3) field-operation synthesis.

The stationary short bound uses **total stationary state dimension r**, not maximum layered width. Width 1 and D arbitrary already contradict `w-1` as a fixed-length witness bound. Unfolding the degree-D shift example uses total dimension D+1, restoring `r-1`. If D is binary encoded and the required output is an explicit length-D word, output size alone rules out polynomial time in log D without compressed-output conventions. No arbitrary black-box circuit/formula-to-small-transition representation is provided here. Scalar evaluation oracles are insufficient to recover noncommutative formal coefficients, as the explicit commutator control shows. These are failure boundaries, not repairs to an incompatible target contract.

## Executable checks and exact outputs

Command run from the read-only repository working directory:

```sh
python /tmp/pm-succinct-b.py
```

Exit status 0; final status `ALL EXACT CHECKS PASSED`. The final run reported 9.605289 seconds, recorded only as a reproducibility observation, **not a benchmark**. No LP or other same-input performance comparison was run.

| Control | Exact result |
|---|---|
| Seeded exact models over Q, F2, F3, F5; r=1..4 | 384 models: 86 zero, 298 nonzero; 11,136 full word coefficients through length r+1; all decisions/witnesses agree |
| Exhaustive all two-state/two-letter binary inputs | All 4,096 choices of initial/final vectors and two 2x2 matrices; 1,984 zero and 2,112 nonzero; all 61,440 coefficients through length 3 agree |
| Cancellation | Four-state xy has exactly two nonzero path weights +1 and -1; reachable basis words empty,x; rank 2; all 127 word coefficients through length 6 are zero |
| Specialization | `lambda=(1,0)`, `A_x=[[0,2],[0,0]]`, `gamma=(0,1)` gives rank 2 and witness x over Q/F3; rank 1 and zero series over F2 |
| Scalar-oracle boundary | Over F3, xy-yx has formal coefficients 1 and 2; all 9 scalar evaluation points return 0; exact transition algorithm returns nonzero |
| Huge implicit family | Over F2, D=96 shift family: 97 states, 18,818 dense matrix entries, 97 retained basis rows, 195 row offers, 18,818 closure scalars, witness x^96 coefficient 1 |
| Huge family's word count | Exactly `2^96 = 79228162514264337593543950336` distinct nonzero degree-96 words by the shift proof; **large full expansion not performed** |
| Small family full controls | D=0..7: exactly 1,2,4,8,16,32,64,128 nonzero words; every word through D+1 checked (3,7,15,31,63,127,255,511 entries) |
| Edge cases | Zero lambda gives empty rank-0 basis; empty alphabet handles both zero and nonzero constant; empty word nonzero witness; denominator 1/2 modulo 2 rejected |

The finite enumerations verify the implementation only for their stated finite domains. PMB-1/2 prove the unrestricted field statements; the large family's exponential word count is proved from its explicit matrices, not inferred from a finite sample or claimed full expansion.

### Adversarial certificate results

All 11 deliberately malformed certificates were rejected:

| Mutation | Rejection |
|---|---|
| Wrong closure scalar | closure identity |
| Omitted letter | closure alphabet |
| False initial containment | initial containment |
| Forged reachable row | basis word provenance |
| Missing closure row | closure height |
| Forged output | output identity |
| Field mismatch | version/field |
| Q basis reused after F2 rank drop | dependent basis |
| Annihilating rows but nonclosed span | closure identity |
| False nonzero witness | witness coefficient |
| Duplicate/dependent purported basis rows | dependent basis |

The central closure trap uses the nonzero polynomial `(x+y)^2` with `lambda=e_0`, `gamma=e_2` and both transitions the three-state shift. The fake certificate lists only B=[e_0], so every listed row annihilates gamma, and initial containment holds, but it falsely declares both closure scalars 0. The checker rejects `e_0 S != 0 B`. The real witness is xx with coefficient 1. Merely checking that a small sampled set of rows has zero output would falsely accept this trap.

## Nearest primary art and novelty classification

1. Stefan Kiefer, *Notes on Equivalence and Minimization of Weighted Automata*, arXiv:2009.01217v1, 2020, Section 2, Algorithms 1/2 and Propositions 2.1/2.2, PDF pages 2–4: https://arxiv.org/pdf/2009.01217 . This explicitly gives the same forward-space basis operation, the d-1 word bound, cubic arithmetic complexity, and nonzero witness. Bibliographic remarks trace equivalence to Schuetzenberger and Tzeng. Retrieved primary PDF lines 82–205.
2. Ran Raz and Amir Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative Models*, primary author-hosted PDF: https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf . Its abstract explicitly includes deterministic polynomial-time identity testing for noncommutative algebraic branching programs. Consult for ABP-specific formulations rather than claiming a new general PIT algorithm here.
3. Stefan Kiefer et al., *On the Complexity of Equivalence and Minimisation for Q-weighted Automata*, primary paper: https://arxiv.org/pdf/1302.2818 . Retrieved as supplementary primary context; no novel theorem is inferred from it.

Assessment: **Level 0 / reproduction of known mathematics, with independent executable certificate/control packaging.** Correctness, novelty, and target transfer are separate. No new general linear-algebra instrument is established. The certificates demonstrate exactly what supplied white-box transition data make possible; they do not establish a black-box-to-white-box conversion, a characteristic-uniform hitting set, a new model-capability result, or performance superiority to explicit LP. No target transfer verdict is given because independence forbade reading the selected family116 statement/proof.

## Trust and remaining limitations

Implementation separation is real: the checker does not call the synthesizer, its incremental span class, row multiplication helper, or dot helper. It recomputes provenance, rank, initial containment, every closure identity, and outputs. Both still trust the same Python interpreter, Fraction/modular field primitives, and model parser; this is not a separately compiled formal proof. Input primes were small and explicitly validated. The large family is a structured exact instance, not an arbitrary-model performance benchmark. All results above concern formal word coefficients, not scalar functional identity.

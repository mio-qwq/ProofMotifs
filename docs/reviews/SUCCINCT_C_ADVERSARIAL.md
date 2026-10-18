# PM-SUCCINCT-C — prior art and released-source adversarial review

Date: 2026-10-18 UTC / 2026-10-19 Asia/Singapore. Reviewer is the actual task-scoped subagent `/root/succinct_priorart_ultra`, not a simulated review. No children, repository edits, or Git operations were used.

## Task ledger

- ID: PM-SUCCINCT-C.
- Question: Does incremental span closure of rows `lambda A_w` supply a genuinely missing succinct cancellation tool, and does it meet the frozen family116 interface?
- Assumptions: Exact effective field; explicitly supplied finite transition matrices; distinguish all-length representations from fixed-length layered ABPs; no formula supplied to the target generator.
- Evidence: Read `ProofMotifs/AGENTS.md` and `research/experiments/succinct-transfer-protocol.json`; independently retrieved primary automata/ABP sources; after explicit coordinator release, read the five pinned family116 sections listed below.
- Expected output: Exact prior-art overlap, field/cost/access qualifications, independent mathematical objections, and source-exposure record.
- Scope: Repository read-only; this `/tmp/pm-succinct-c.md` internal handoff only.
- Independence: Primary-source retrieval and mathematical inspection performed independently; no family116 content was retrieved/read before the coordinator's release. The reviewer read the coordinator's saved statement decision before opening the released proofs.
- Stop: Initial search stopped after strong exact primary closure/ABP coverage; later review limited to the released proof chain and directly relevant dependency checks, not an exhaustive priority search or full Lean audit.
- Handoff: Coordinator owns integration, claim status, publication, and resolution. This report establishes no historical priority and issues no whole-project or formal-verification certification.

## 1. Prior-art result: the fixed operation is classical

### C-PA1: Exact reachable-span overlap

Primary source: S. Kiefer, A. S. Murawski, J. Ouaknine, B. Wachter, J. Worrell, *Language Equivalence for Probabilistic Automata*, CAV 2011 author manuscript, https://www.cs.ox.ac.uk/andrzej.murawski/papers/cav11.pdf . Read §2–§2.1, printed pp.3–5, especially Definition 1, Proposition 2, and Figure 1. Browser extraction lines75–149 and159–186 identify the exact objects and worklist.

The representation is `alpha M(w) eta`. Their backward algorithm computes a basis of columns `M(w) eta`, queues only independent successors, and retains words for counterexamples; the stated forward version transposes matrices and exchanges endpoints. This is precisely the dual of the proposed row closure, not merely a thematically related algorithm. They obtain `O(|Sigma| n^3)` arithmetic complexity by maintaining a basis; Figure 1 includes direct counterexample extraction. Their implemented orthogonal/QR membership test is over the reals and later permits floating tolerances. It must not be copied as a positive-characteristic exact algorithm.

### C-PA2: Known short witness, with original-access qualification

Primary source: the same authors, *On the Complexity of the Equivalence Problem for Probabilistic Automata*, arXiv:1112.4644v2, 6 January 2012, https://arxiv.org/pdf/1112.4644v2 (the successfully retrieved canonical PDF was https://arxiv.org/pdf/1112.4644 and its header identifies v2). §3, printed pp.4–5, Definition and Proposition 1, extraction lines144–193: a nonzero `n`-state rational weighted automaton has a nonzero word of length at most `n-1`. The proposition explicitly attributes the result to Tzeng1992. Direct-sum subtraction reduces equivalence to zeroness with summed state dimensions.

Original primary publisher page: W.-G. Tzeng, *A Polynomial-Time Algorithm for the Equivalence of Probabilistic Automata*, SIAM J. Comput.21(2),216–227, April1992, DOI10.1137/0221017, https://epubs.siam.org/doi/10.1137/0221017 . The abstract, extraction lines64–68, states `O((n1+n2)^4)`. Full text was not accessible: the PDF link redirected to the access page. Therefore no Tzeng theorem number, proof page, or arbitrary-field hypothesis is asserted from an unread full article.

### C-PA3: Exact white-box ncABP coverage

Primary source: R. Raz and A. Shpilka, *Deterministic Polynomial Identity Testing in Non-Commutative Models*, Computational Complexity14(1),1–19(2005), DOI10.1007/s00037-005-0188-8; numbering below is the 16-page author version, https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf . Read §1.1 and §2 in full relevant range.

Definition1, printedp.4, defines layered ncABPs. Lemma2, pp.5–6, reduces supplied size-`s` formulas to homogeneous ABPs of size `O(s^2)`, with total `O(s^3)` arithmetic construction time. Claim3 and the span construction, pp.8–9, compress prefix-coefficient vectors by a basis before reducing ABP depth. Theorem4,p.9, states `O(s^5+s n^4)` ABP identity testing; Theorem5,pp.9–10, gives polynomial formula PIT. §1.1,p.3, explicitly says the methods use internal circuit structure, not only evaluations. The ambient coefficient object is a field, and the displayed linear-algebra argument imposes no characteristic-zero or field-cardinality restriction. These are field-operation bounds, not an automatic bit model for every effective field.

### Historical Schützenberger attribution, not a fabricated read

Located original: M. P. Schützenberger, *On the Definition of a Family of Automata*, Information and Control4(2–3),245–270(1961), DOI10.1016/S0019-9958(61)80020-X. Primary scanned reprint URL: https://igm.univ-mlv.fr/~berstel/Mps/Travaux/A/1961-4DefinitionFamilyAutInfCtl.pdf ; collected works URL: https://www-igm.univ-mlv.fr/~berstel/Mps/Oeuvres-Completes/tome05.pdf . Search exposed original opening/scattered pages, but full fetches returned502/timeouts; ScienceDirect's PDF fetch was disabled. I do not label the original proof independently read. The CAV2011 primary paper explicitly connects polynomial equivalence/minimisation with Schützenberger1961, but exact original theorem numbering remains unverified.

### C-PA4: Independently checked field-sensitive formulation

For `R_t=span_K{lambda A_w: |w|<=t}`, `R_t=R_(t+1)` implies invariance and hence finality. If `lambda!=0`, `dim R_0=1`; there are at most `r-1` strict dimension increases. A breadth-first basis therefore has representatives of length at most `r-1`. All outputs vanish exactly when basis rows annihilate `gamma`. Gaussian elimination, rather than orthogonality, makes this valid over every exact field, including characteristic2. This proof uses neither positivity nor analytic approximation.

A sound zero certificate needs equations `lambda=cB`, `BA_i=C_iB`, and `B gamma=0`. Independence of rows or reachable representatives is not needed for soundness. If representatives and nonzero output are claimed, their products must separately be checked. A fixed-length layered model needs per-layer spaces or a block-state embedding: treating all lengths as the same unrestricted language silently changes the question. Rational bit bounds require denominator/pivot-growth accounting; reducing a rational certificate at a bad prime is invalid without rechecking its equations and pivots in that field.

Conclusion: the candidate is a faithful reproduction/implementation of classical white-box tools. A succinct exponential word count alone does not establish a new algorithm, missing theorem, or transfer success.

## 2. Released family116 exposure record

The coordinator explicitly released proof access after saving `research/experiments/succinct-statement-decision.md`. All following material was first retrieved after that release, at `openai/math` revision `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, directory `preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026/build/`.

| File | Blob | Read range |
|---|---|---|
| `sections/introduction.tex` | `4a798efdc42349bfbe378eede3862750b5cd91b7` | all154 lines |
| `sections/words.tex` | `882cb46e0e824041ecddcd051aa97a20d96cd050` | all164 lines |
| `sections/systems.tex` | `ac918c8eb6ea0603b8509377c98697454da26a02` | all179 lines |
| `sections/order.tex` | `ab18a99256085b49fddba4c4d8ee2963016733de` | all156 lines |
| `sections/construction.tex` | `1f8cca2bd8dca8026b18dbc332617465a23af9d9` | all258 lines |
| `references.bib` | `b265844a98039fd53ead3af26edec1e61c493908` | whole file |

Canonical source links use `https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/` followed by the directory and file above. Full tool responses were stored in tool memory; truncated displayed responses were supplemented by a complete numbered print of `construction.tex`. No scope document, Lean proof, companion-paper proof, or other116 section was read.

## 3. Adversarial proof-chain checks

### C-AUD1: Pole obstruction and minimal relation

`words.tex`52–82: the poles `alpha_i=(1+t)^(-i)` have infinite, disjoint `t`-orbits. For an alleged equality `(1+t)^(i-i')=t^a`, valuations at `t=0,-1` force `a=0,i=i'`, even when the characteristic divides an exponent. If a rational function has a finite nonempty pole set on an orbit, its shift-minus-itself retains two distinct endpoint poles. Interior cancellations do not remove the endpoints. Poles on other orbits cannot help. This proves the displayed obstruction without characteristic-zero residue machinery.

`words.tex`117–153: applying the shift to a normalized shortest/maximal-length minimal relation gives exactly `sigma(R_w)-R_w + sum_i b_i sigma(R_iw)`. The normalized top coefficient disappears and no new top support occurs. Minimality forces every new coefficient to vanish. Top coefficients are shift constants, hence belong to `F(t)`; the length-one-lower equations then contradict the pole obstruction. I find no order-of-multiplication or difference-versus-derivation gap in these steps.

### C-AUD2: Coefficients and system

`systems.tex`24–106: scalar-only paths are summed by `S=I+E0+...+E0^(m-1)`. Unique path decomposition gives `u=e_src^T S`, `B_i=X_i S`, `v=e_snk`, with `f_w=uB_wv`. All `B_i` are simultaneously strictly upper triangular. Acyclicity, central scalar labels, and counting scalar leaves are essential. The two-vertices-per-formula-node construction is legitimate because formula subtrees are disjoint; it would not justify the same bound for arbitrary shared arithmetic circuits.

`systems.tex`113–173: the finite sum `H=sum_w B_w h_w` has `H(0)=I`; prefix recursion yields `sigma(H)=(I+sum_i b_i B_i)H`, not reversed multiplication. A common denominator in `z` has degree at most `n`. This is a standard coefficient representation feeding a different analytic-algebraic operation; it is not the reachable-basis algorithm.

### C-AUD3: Uniform order bound

`order.tex`18–148 independently checked: distinct-order basis construction uses finite-dimensional coefficient-functional kernels. The Casoratian leading coefficient is a Vandermonde in `tau^(c_i)`, hence nonzero when `tau` has infinite order in any characteristic. Shifted rational rows have numerator degree at most `j nu` and unit denominators at zero. Cauchy–Binet gives one valuation inequality for minors of `MH`; applying it to `M=(MH)H^(-1)` gives the converse. Thus the minimum minor order is bounded by `nu binom(k,2)`, and the claimed `nu binom(m,2)` bound follows. This is a substantive uniform truncation argument, not an inference from finitely sampled words.

Necessary-hypothesis attacks: removing invertibility allows `m=1,H=z^M,A=tau^M,nu=0`; removing infinite order allows `tau=1,H=I+z^M E12,A=I,nu=0`; permitting nonconstant `u,v` allows trivial arbitrary-order factors. These attacks fail against the stated hypotheses and explain why those hypotheses must be preserved in any extracted tool.

### C-AUD4: Descent and bit model

`construction.tex`13–58: the rational operator tuple depends only on `p,n,s`; all nonzero size-bounded formulas are detected through the order bound. The formula-specific coefficient representation is used only in the proof of the simultaneous guarantee, not as generator input.

`construction.tex`62–88: every nonzero product-entry summand follows a strictly increasing chain of row indices. Thus each denominator factor occurs at most once *by its index*, and `D=prod_(r=1)^(N-1)(t^r-1)` clears every word. Repeated irreducible factors at small primes are harmless because divisibility follows from subproducts, not coprimeness. Numerator exponent telescopes to at most `n(N-1)`.

`construction.tex`100–157: reduction to `F[t]/t^E` preserves a nonzero cleared numerator of degree `<E`; multiplication on this ring is injective because its value at1 recovers the multiplier. The entrywise regular representation is a unital algebra embedding and respects every extension `F/F_p` and scalar `aI`. No nonexistent infinite-order shift on the finite ring is assumed.

`construction.tex`172–224: explicit truncated geometric inverses and schoolbook arithmetic give polynomial binary cost in `n+s+log p`; output itself is polynomial and dense. The stated exponents are loose upper bounds but internally consistent. Constant and `m=1` boundary cases in the path-program corollary are handled.

Review result: no concrete defect found in this read of the displayed proof chain. This is a mathematical source audit, not a machine-checked proof or full independent certification of the headline, historical novelty, or repository formalization.

## 4. Relevant primary dependency checks and remaining priority uncertainty

- Chen–Singer, *Residues and Telescopers for Bivariate Rational Functions*, Adv.Appl.Math.49(2012),111–133, author copy https://singer.math.ncsu.edu/papers/YAAMA1465.pdf . §2.3, especially Proposition2.10, printedp.117 (extraction345–494), gives the rational `q`-summability obstruction by orbit residues. Its field assumptions are characteristic zero (§2,p.113). This verifies the nearby mechanism, not a ready-made all-characteristic theorem. The source's finite-endpoint proof independently supplies its special case.
- Deneufchâtel–Duchamp–Hoang Ngoc Minh–Solomon, *Independence of Hyperlogarithms over Function Fields via Algebraic Combinatorics*, author version arXiv:1101.4497v3 (canonical successfully retrieved https://arxiv.org/pdf/1101.4497), Theorem1,printedp.3, extraction177–198; minimal-relation proof pp.4–5. It concerns a derivation with constant field `k`, characteristic zero, and equates word-coefficient independence with an obstruction to exact derivatives. The shift adaptation cannot be cited as the identical theorem.
- Bostan–Dumas, *Wronskians and Linear Independence*, author PDF https://mathexp.eu/dumas/publications/Bostan_Dumas_2010_WLI.pdf , Lemma2,p.3 and Lemma3,pp.3–4; Theorem2,p.2. Distinct-order elimination works over a field; the ordinary Wronskian nonvanishing step requires characteristic zero and explicitly fails for `1,x^p`. The source replaces exponent Vandermonde values by infinite-order shift powers.
- Additional prior-art lead not listed in116 references: D.Bertrand, *Multiplicity and vanishing lemmas for differential and q-difference equations in the Siegel–Shidlovsky theory*, FPM16(5)(2010),19–30 / J.Math.Sci.180(5)(2012),542–549, DOI10.1007/s10958-012-0652-3. Author material https://webusers.imj-prg.fr/~daniel.bertrand/Recherche/rpdf/MOCKBA_07.pdf is **January2007 lecture slides, not the journal paper**. Slides10–13 give complex-analytic `q`-multiplicity bounds with system-dependent constants, regular-singular/quasi-unipotent hypotheses, and discuss ineffectivity of a general bound. This is enough to require a serious comparison before calling a `q`-multiplicity tool new, but not enough to assert the exact explicit all-characteristic `nu binom(m,2)` theorem was previously proved there. Journal metadata: https://www.mathnet.ru/eng/fpm1334 . Related earlier title “Multiplicity estimates for q-difference operators” remains a follow-up, not read evidence.

No theorem of Moura2003 or the characteristic-zero companion was independently fetched/read in this task; their exact overlap must not be silently marked verified.

## 5. Adjudication for ProofMotifs

1. The frozen candidate's headline transfer remains **failed at input and quantifier order**, exactly as saved before proof exposure. Source inspection does not retroactively improve that prediction.
2. The source's missing operation relative to that candidate is a **formula-independent injective word encoding with a uniform finite-jet bound**, followed by degree-controlled descent. Its universal tuple is built without the particular transition matrices. A supplied representation is a proof witness for the uniform bound, not generator input.
3. Cancellation is load-bearing at a precise location: linear combinations of independent word series can cancel many initial coefficients, and the Casoratian/minor estimate bounds how late a nonzero combination may begin. Interior pole cancellation is tolerated while endpoint poles force an obstruction. These are two different cancellation mechanisms and should not be collapsed into one motif.
4. A portable instrument could package hypotheses and certificates for such structured finite-jet bounds. That is a useful **candidate extraction direction**, not evidence of a novel general linear-algebra method or a surviving priority gap. Compare `q`-zero estimates and difference-module multiplicity literature first; require a second genuinely unread same-input transfer before promoting general utility.
5. Honest present status: classical baseline reproduced; failed target transfer preserved; relevant external mechanism mathematically inspected with no defect found; exact novelty and formal verification unresolved. Search failure is not used as evidence of novelty.

## 6. Follow-up adversarial audit of source-derived DAG jet code

After the preceding review, the coordinator requested review of newly written `tools/acyclic_jet.py` and `tests/test_acyclic_jet.py`. I read both files in full; I made no repository edits.

### C-CODE1: Mathematical contract

The common-DAG bound is sound for explicitly represented rational edge labels `num/prod_j q_j^e_j`, where every `q_j(0)` is nonzero in the actual field. Each expanded word-entry summand follows a DAG path. For every listed denominator independently, its total exponent on that path is bounded by the longest-path maximum `M_j`. Therefore `D=prod_j q_j^M_j` clears each summand, without any pairwise-coprimeness assumption and with arbitrary parallel edges. Its cleared degree is bounded by `deg(D)` plus the path sum of `deg(num)-sum_j e_j deg(q_j)`. Allowing empty paths and starts at every vertex computes the required nonnegative maximum, including the scalar constant term. The implementation's `best=[0]*m` and topological sweep do exactly this even with signed degree excesses.

Normalization takes place before path bounds, so leading coefficients and entire edges killed by characteristic reduction disappear before degrees are measured. Shared irreducible factors, including identical or repeated denominator polynomials, merely overestimate the bound. The regular representation block orientation is consistent with coefficient columns. A faithful compilation of the **evaluation algebra** is not a theorem that the map `f -> f(V)` is injective. The fixed-bound theorem depends on the common DAG: the cyclic scalar tuple `V=[t]` and `f=x^E` defeats truncation at `t^E`.

### C-CODE2: Independent exact stress checks

Executed an ephemeral independent script (no file created) with seed11631. It generated80 small DAG instances over `Q,F_2,F_3,F_5,F_7`, with2 variables,2–4 vertices, parallel edges, numerator degrees0–2, exponent vectors in `{0,1,2}^2`, and deliberately noncoprime denominators `1+t` and `(1+t)^2`. For each word through length equal to the vertex count, independent path enumeration formed the full cleared numerator by multiplying the missing denominator factors. Independent polynomial arithmetic checked its degree `<E` and equality to `D` times the production word jets modulo `t^E`. It also checked640 random linear combinations of word evaluations for preservation of zero/nonzero status. Outcome: **PASS,1408 word checks and640 polynomial checks**. These are finite controls, not the proof.

### C-CODE3: Input-validation objection sent to coordinator

`scalar(x,p)` currently uses `int(x)%p` for prime fields. If rational or floating coefficients are accepted as input, this silently changes their value: with `p=3`, numerator `Fraction(1,2)` becomes0 instead of2. Either restrict prime-field input coefficients to exact integers and reject other types, or use rational numerator times inverse denominator and reject bad specializations. Similarly, integer types should be required for dimensions and edge indexes; e.g. `variables=1.5` can be accepted by `analyze` before failing later during compilation. These do **not** refute the theorem on the intended integer-residue input domain, but that domain should be explicit and enforced before marking the implementation accepted.

No mathematical counterexample found under the stated DAG/unit/actual-field/integer-residue contract. No strongest-baseline advantage or novelty claim is justified by comparison only with repeated global denominators.

## 7. Persisted reproducibility panel and corrected-parser rerun

The exact earlier stress-panel generation code was recoverable from this task's tool-call history. It is now persisted as `/tmp/pm-succinct-c-check.py`, written using `apply_patch`, with a documented runnable command. The seed, iteration order, field order, random-draw order, path enumeration, and polynomial-combination loops were preserved; code was expanded for readability and wrapped in functions. Parser regressions were added separately and do not consume the stress panel's random generator. Deterministic result data are saved as `/tmp/pm-succinct-c-results.json`.

Rerun command:

```sh
python /tmp/pm-succinct-c-check.py --repo /workspace/scratch/415407b3c01b/ProofMotifs
```

Exit status0; result:

```json
{
  "corrected_parser_checks": 16,
  "fields": [0, 2, 3, 5, 7],
  "instances": 80,
  "parallel_edges": true,
  "random_polynomial_checks": 640,
  "result": "PASS",
  "seed": 11631,
  "shared_non_coprime_denominators": true,
  "word_checks": 1408
}
```

The coordinator corrected the original C-CODE3 objection before this rerun: rational coefficients now specialize by numerator times inverse denominator, undefined prime specializations are rejected, floating coefficients are rejected, and dimensions/edge indexes/exponents require genuine integer types. Independent checks cover `Fraction(1,2)` and the exact string `"1/2"` overF3, rational retention overQ, both floating-field paths, bad-prime rejection through both scalar and instance parsing, and noninteger/bool dimensions and edge indexes. All16 corrected-parser checks passed. C-CODE3 is therefore **resolved for the tested exact-input contract**, not an outstanding arithmetic bug.

SHA256 snapshots taken with `sha256sum` immediately after the successful run:

| File | SHA256 |
|---|---|
| `/tmp/pm-succinct-c-check.py` | `76056f7a34790907cf3997dbf61997880bc83a665e48ada5e3bc80acdb0394d4` |
| `tools/acyclic_jet.py` | `2aff3c7020dee05e3357c376f79fe47abd57998a1533ebcaac45ece7fdd308c3` |
| `tests/test_acyclic_jet.py` | `d95043ca0cce255ed10464fb75fc6892ab6db597fed7f5ae2d19045a2d65dbd2` |

These hashes identify the reviewed snapshot without performing any Git operation. The panel explicitly asserts the expected `(80,1408,640)` totals. Its independent arithmetic validates DAG bounds and the zero/nonzero-preserving jet map on the listed finite controls; it does not claim exhaustive verification, formal proof, or a new general theorem.


## C8. Independent challenge of the finite-algebra/faithful-jet proposition

The coordinator proposed the following source-derived extension for mathematical review, explicitly without a novelty claim. I inspected the argument independently; this section is not an audit of its subsequently implemented code.

### C8.1 Precise statement and necessity

Let `K` be a field, `N>=1`, and let the supplied matrices `V_1,...,V_n` have entries in the local ring `K[t]_(t)` of rational functions regular at zero. Let `A=K<V_1,...,V_n,I_N>` be the **unital K-algebra**, inside `Mat_N(K(t))`. A fixed positive jet length `E` preserves zero/nonzero for every polynomial evaluation if and only if the entrywise reduction `pi_E` is injective on `A`.

If such an `E` exists, `A` injects K-linearly into `Mat_N(K[t]/(t^E))`, whose K-dimension is `N^2 E`. Hence `dim_K A` is finite. It is essential that the algebra be generated over **K**, not over `K(t)`: every subalgebra generated over the latter field has dimension at most `N^2` over that larger field, including the counterexample `V=[t]`.

### C8.2 Sufficiency

If `A` is finite-dimensional, the subspaces

`J_E = {a in A: every entry has t-order at least E}`

form a descending chain. Their intersection is zero because rational functions embed injectively into their formal expansions at zero. A descending chain of subspaces of a finite-dimensional space eventually stabilizes; its stabilized value is its intersection, hence is zero. Therefore some `pi_E` is injective. The usual faithful multiplication representation of `K[t]/(t^E)` then converts this jet map into ordinary matrices over K.

This argument also works for matrices of arbitrary formal series for the abstract existence direction. Rationality supplies effective common-denominator and degree certificates, not the abstract descending-kernel equivalence.

### C8.3 Checkable certificate, not necessarily a basis

Suppose a finite supplied family `B=(B_1,...,B_r)` satisfies actual **K-constant** equations

- `I_N` lies in `span_K B`;
- every `B_j V_i` lies in `span_K B`;
- one polynomial `q(t)` with `q(0)!=0` clears all entries of all `B_j`, and every nonzero entry of `q B_j` has degree `<E`.

Then induction on word length puts every polynomial evaluation in `span_K B`. If such an evaluation is nonzero, its product by q has a nonzero polynomial entry of degree `<E`; that entry survives reduction. Consequently the evaluation survives the jet and the regular representation. No independence, minimality, or reachable-word provenance for the supplied B is required for **soundness**. Those properties matter only if one claims dimension or a basis. Right closure suffices because words are built by appending generators. Merely supplying K(t)-linear closure is unsound.

### C8.4 Promised dimension and explicit length

Under the promise `dim_K A<=d` with `d>=1`, let `A_l` be the K-span of words of length at most l. It starts with dimension1, and a plateau `A_l=A_(l+1)` implies right-generator invariance and finality. Therefore A has a spanning word family of lengths at most `d-1`.

Choose a polynomial `delta` regular and nonzero at zero that clears every input entry. Put

`b=max(deg(delta), max degree of the nonzero entries of delta V_i)`.

For a length-k basis word, `k<=d-1`, multiplication by `delta^(d-1)` yields the polynomial matrix

`delta^(d-1-k) (delta V_i1)...(delta V_ik)`.

Every entry has degree at most `(d-1-k)deg(delta)+k b <= (d-1)b`. Thus `E=1+(d-1)b` suffices for all evaluations, by the certificate argument. The `d=1` case correctly gives `E=1`: the algebra then consists only of K-scalars times identity. Zero entry degrees should be omitted or treated as minus infinity; b is nonnegative because delta is nonzero.

The degree estimate clears the **spanning word family**, not arbitrarily long products term by term. Extending it to all evaluations relies exactly on the K-constant closure relations. No unconditional termination or general finiteness decision algorithm follows: word-space closure is guaranteed to stop under the finite-dimension promise, or when an explicit valid closure certificate is found. Binary-encoded degree/dimension parameters still require output-size accounting.

### C8.5 Coefficient-field extensions: necessary convention

For every field extension `F/K`, interpret the source matrices in `Mat_N(F(t))` with a **fresh parameter t transcendental over F**. A K-basis of A remains F-linearly independent: clear a common denominator, stack all polynomial coefficients into a finite matrix over K, and use persistence of a nonzero rank minor under field extension. The same common-denominator/degree certificate then proves the jet guarantee simultaneously for F-coefficient polynomials. Scalar coefficients act as scalar identity blocks after the unital regular representation.

Do not instead absorb the original parameter into the coefficient field. For example `V_1=t E12,V_2=E12` generates a finite K-algebra. If F is taken to contain that **same** t as a coefficient, `x_1-t x_2` vanishes before compilation but its jet-block evaluation need not vanish. This does not contradict the standard scalar extension `K(t)->F(t)` with fresh formal t; it identifies an interpretation that must be excluded explicitly.

### C8.6 Counterexample attempts and classical baseline

- A diagonal support cycle does not imply infinite algebra: `P=[[1,t],[0,0]]` satisfies `P^2=P`; its algebra is `span_K{I,P}`. In fact `E=1` already preserves this algebra because constant diagonal entries distinguish I and P, although the displayed coarse bound gives2.
- `V=[t]` generates infinite-dimensional `K[t]`; for every E, `x^E` is nonzero on V but killed by the E-jet.
- Algebra dimension alone cannot bound E: `V=t^M E12` generates the dimension-two algebra `span_K{I,V}`, but needs `E>=M+1`. The proposed bound with `delta=1,b=M,d=2` is sharp on this example.
- Individual polynomial relations for generators do not certify finite joint algebra: `V_1=t E12,V_2=E21` both square to zero, but `(V_1 V_2)^k=t^k E11` gives an infinite independent family. The proposed full right-closure certificate correctly excludes this case.

The strongest same-input baseline is the classical **K-linear word/Krylov closure of the generated algebra**, testing exact rational-matrix equality after denominator clearing, then finite-dimensional linear algebra and faithful regular representation. This generalizes the earlier DAG sufficient condition to finite evaluation algebras with cycles; it does not supply formula-independent injective encoding and does not repair the frozen family116 transfer. The abstract kernel-chain proof, invariant-span certificate, and basis-word bound are elementary finite-dimensional mechanisms already adjacent to the primary automata/ABP closure sources in §1. No priority claim for this formulation, tightness in general, or strongest-baseline speedup is established here.

### C8.7 Reproducible finite controls

Persisted independent script: `/tmp/pm-succinct-c8-check.py`. Run:

```sh
python /tmp/pm-succinct-c8-check.py
```

Exit status0, **PASS220 exact checks over Q,F2,F3,F5,F7**. The script independently checks the idempotent identity, its one-coefficient diagonal distinction, arbitrary delays `M=1,2,5,9` for the dimension-two square-zero example, and the square-zero-generator/infinite-joint-algebra obstruction through nine powers. It uses its own standard-library polynomial and matrix arithmetic, no production arithmetic. These controls are finite illustrations; C8.1–C8.5 provide the general argument.

Review disposition: the proposition and explicit promised-dimension bound are mathematically sound under the local-ring, unital **K**-algebra, exact K-closure, and fresh-parameter extension conventions. No novelty or unpromised algorithmic termination is certified.

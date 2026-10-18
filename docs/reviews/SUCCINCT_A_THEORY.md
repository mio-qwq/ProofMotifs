# PM-SUCCINCT-A — exact reachable-span certificates

## Task ledger and exposure boundary

- Question: can supplied exact transition matrices generate polynomial-size cancellation certificates without enumerating all words, and what is the safe composition interface?
- Assumptions: explicit row `lambda`, square transition matrices `A_i`, and column `gamma` over an exact field; in the computational claims the field is `Q` with binary rational entries or a supplied prime field `F_p`.
- Read: repository `AGENTS.md` and `research/experiments/succinct-transfer-protocol.json` only. The parent supplied the protocol-freeze commit `2b8dd9e`; I did not independently verify that remote commit. No family116 source, scope document, proof, or other agents' notes were read. No repository writes or Git mutations were made.
- Independence: theorem and objections below were derived independently; the parent subsequently supplied a proposed acyclic rational-jet statement for a separate, explicitly post-statement-decision audit, in the final section.
- Output scope: this file only. Mathematical claims are proved below; they have not been Lean-formalized and are not independently reviewed merely because this is a delegated report.
- Conclusion: **yes for supplied white-box linear representations; the core is classical weighted-automata equivalence / noncommutative ABP identity testing, not a new general algorithm. No black-box-to-transition conversion follows.**

## A1. Field-parametric theorem

Let `K` be any field, `Sigma={1,...,n}` with `n>=1`, and `d>=1`. Let

`lambda in K^(1xd), A_i in K^(dxd), gamma in K^(dx1)`.

For a word `w=i_1...i_l`, put `A_w=A_i1...A_il`, with `A_empty=I_d`, and let `f(w)=lambda A_w gamma`. Define the reachable row space

`R = span_K {lambda A_w : w in Sigma*}`, `r=dim_K R <= d`.

**Claim A1.** One can construct a matrix `B in K^(rxd)`, a row `a in K^(1xr)`, matrices `T_i in K^(rxr)`, and `g in K^(rx1)` such that

1. the rows of `B` are an independent list of actual reachable rows `lambda A_wj`;
2. if `lambda!=0`, every retained word has length at most `r-1`;
3. `lambda=aB`, `BA_i=T_iB` for every `i`, and `g=B gamma`;
4. consequently `lambda A_w=a T_w B` and `f(w)=a T_w g` for every word `w`.

Moreover exactly one of the following valid outputs can be produced:

- a word `w`, of length at most `r-1 <= d-1`, together with its directly checkable nonzero value `lambda A_w gamma`; or
- the finite zero certificate `(B,a,(T_i))` satisfying

  `lambda=aB`, `BA_i=T_iB` for all `i`, and `B gamma=0`.

When `lambda=0`, take `r=0` and empty matrices of the indicated shapes; the zero certificate remains well-defined. The witness alternative is absent in that case. No characteristic restriction is used.

### Proof and construction

If `lambda=0`, the assertions are immediate. Otherwise initialize the immutable retained-row list with `v_1=lambda`, word `w_1=empty`, and put index 1 in a queue. Keep a second, echelon-form basis for exact membership tests.

Pop each queued row `v_j` once. For each letter `i`, compute `v_j A_i`. If it is outside the current span of retained rows, append it as a new retained row, with word `w_j i`, and enqueue the new index. Otherwise discard this candidate. Retain a parent index and letter rather than copying the entire word.

Every addition strictly increases dimension, so at most `d` rows are retained and the queue empties. Each retained row is reachable by induction on its parent pointers. At termination each retained row times each `A_i` belongs to the final span `S`; thus `S A_i subset S`. Since `lambda in S`, induction on word length gives `R subset S`. The reverse inclusion follows because every retained row is reachable. Therefore `S=R`, and the retained independent list has length `r`.

Each appended row has a parent with a strictly earlier index. Thus the depth of the `j`th retained word is at most `j-1`, and all depths are at most `r-1`. Since the retained rows form a basis, `lambda=aB` and `BA_i=T_iB` have unique solutions (indeed `a=e_1` in this construction). Their equations imply `BA_w=T_wB` by induction, so `lambda A_w=aT_wB` and `f(w)=aT_wg`.

If some retained row has nonzero scalar product with `gamma`, its retained word is the requested witness. If every retained row annihilates `gamma`, then `B gamma=0`, and all values `f(w)` vanish. This proves both completeness and soundness. In particular, testing basis outputs, not all word outputs, is sufficient. QED.

### A1a. What the zero verifier really needs

The three displayed zero-certificate equations alone imply `f(w)=0` by induction. **Neither full row rank of `B`, nor minimality, nor reachability/provenance of its rows is required for zero-soundness.** Any finite invariant overapproximation of the reachable space that annihilates `gamma` is a sound zero certificate.

If the stronger advertised output is an *exact reachable-span basis*, verify full row rank and reachability as well. The construction permits cheap provenance: `B_1=lambda`, and for every later retained row `B_j=B_parent(j) A_letter(j)` with `parent(j)<j`. These equations, closure, and full rank prove exactly the claimed reachable basis; no exponential table is needed.

### A1b. Witness-length bound is sharp

On a one-letter alphabet let `A` be the `dxd` matrix with ones at `(j,j+1)` for `1<=j<d`, zeros elsewhere, and let `lambda=e_1`, `gamma=e_d^T`. Then `f(a^k)=0` for `k<d-1` and `f(a^(d-1))=1`. Therefore one cannot replace `d-1` by `d-2` in general. The proof and example work over every field.

## A2. Arithmetic cost and encoded size

For dense matrices a candidate row product costs `O(d^2)` field operations; an incremental echelon membership test and update also costs `O(d^2)`. There are at most `n r` candidate products. Coordinate recovery for all `T_i` can be performed in one final pass using the echelon basis (or tracked incrementally). Thus generation uses `O(n d^3)` field operations, with lower-order initialization/output work included since `n>=1`.

The zero certificate has

`r d + r + n r^2 = O((n+1)d^2)`

field entries, in addition to the supplied input. Provenance adds `O(r)` parent/letter pairs; explicit retained words, if preferred, use at most `O(d^2)` letters. A nonzero certificate uses at most `d-1` letters, plus an optional claimed field value; verifying that claim simply recomputes `lambda A_w gamma`.

To verify the zero certificate, multiply both sides of each `BA_i=T_iB` and check every entry, and check the seed and output equations. The cost is

`O(n(r d^2+r^2 d)+r d)=O(n d^3)`

field operations. Optional full-rank and parent-equation checks also fit this bound. A verifier must check all letters, all relevant matrix entries, and the seed; testing only `B gamma=0` is unsound.

### A2a. Bit cost is not the field-operation count

For `F_p`, with `p` supplied and promised prime, exact field operations have bit cost polynomial in `log p`; canonical residues give certificate bit size `O((n+1)d^2 log p)` up to indices. Hence generation and verification are polynomial in the explicit input encoding. No field extension or large-characteristic hypothesis is needed.

For `Q`, assume explicit binary numerators and nonzero denominators. The arithmetic bound alone does not prove a bit bound. Here a polynomial bit implementation is available for a concrete reason. Let `S` be the total scalar input encoding length, and let `D` be the product of its positive denominators, so `log_2 D=O(S)`. After multiplying each input scalar by `D`, the resulting integer entries have `O(S)` bits. A row `lambda A_w` for `|w|=l` has denominator `D^(l+1)` and integer numerators with

`O((l+1)(S+log d))`

bits: each coordinate is a sum of at most `d^l` products of `l+1` scaled entries. Retained rows have `l<=d-1`, and candidate rows have `l<=d`. Therefore all retained and tested raw rows have polynomial-size exact encodings.

Choose an invertible pivot-column submatrix of `B` to compute closure coordinates. Clear each row's denominator separately. Cramer's rule and the determinant bound `|det C| <= r! (max|C_ij|)^r` show that each coordinate numerator/denominator has `O(d^2(S+log d))` bits, a deliberately coarse polynomial bound. The same applies to `a` and `g`. Fraction-free exact elimination, or denominator-controlled rational linear algebra, realizes polynomial bit time for the span tests and these solves. This does **not** promise that an arbitrary unnormalized rational implementation avoids avoidable coefficient swell.

There is no encoding-independent bit complexity claim for an arbitrary abstract field, or when a matrix entry is itself a black-box/circuit description of an enormous rational.

## A3. Explicit layered noncommutative ABPs

Let there be `L` layers of transitions, with widths `d_0,...,d_L <= W`, explicit matrices `A_(k,i) in K^(d_(k-1) x d_k)`, initial row `lambda`, and terminal column `gamma`. The coefficient of `i_1...i_L` is

`lambda A_(1,i_1)...A_(L,i_L) gamma`.

This is the homogeneous ABP model with linear edge labels; constants/epsilon edges or affine labels require their own normalization and are not silently included.

**Claim A3.** Bases of the exact prefix spaces

`R_0=span{lambda}`, `R_k=sum_i R_(k-1) A_(k,i)`

can be generated stage by stage. Write their basis matrices as `B_k`, of ranks `r_k<=d_k`. There are exact local certificates

`lambda=a B_0`, `B_(k-1) A_(k,i)=C_(k,i) B_k`.

The degree-`L` polynomial is identically zero iff `B_L gamma=0`. Otherwise a retained terminal basis row with nonzero output gives a word of length exactly `L`.

**Proof.** Generate each `B_k` by reducing the `n r_(k-1)` candidate rows `B_(k-1),j A_(k,i)`. Their span is exactly the defined `R_k`, and every retained row has a retained actual prefix as parent. Iterating the local equations expresses every length-`L` coefficient row through `B_L`; conversely every row of `B_L` is a length-`L` reachable prefix. The output criterion follows in both directions. QED.

Dense arithmetic cost is

`O(n sum_(k=1)^L d_(k-1)[d_(k-1)d_k+d_k^2]) = O(n L W^3)`,

plus initialization/terminal work (relevant when `L=0`). Certificate size is

`O(sum_k r_k d_k + n sum_(k=1)^L r_(k-1)r_k) = O((L+1)(n+1)W^2)`

field elements. A local verifier has the same polynomial arithmetic bound. Parent/letter provenance uses `O(sum_k r_k)` pairs. The rational-height argument above uses path length `L` in place of `d`, and is polynomial in `L` and explicit scalar encoding size.

These are polynomial bounds in an **explicit layer list**. If `L` or a transition generator is exponentially succinctly encoded, they do not imply a polynomial bound in `log L` or in the generator description alone. For a bounded-length question one must retain layers or otherwise track length; unrestricted invariant closure answers a stronger all-word question and cannot replace the layered contract without justification.

### Exponential-support and cancellation controls

For `(x_1+...+x_n)^L`, take width one, every transition scalar equal to 1, and both endpoint scalars equal to 1. There are `n^L` nonzero coefficients but only one retained row per layer. Thus this construction genuinely avoids writing an exponential coefficient table.

For the cancellation polynomial `(x_1+...+x_n)^L-(x_1+...+x_n)^L`, use width two, `lambda=(1,-1)`, every transition `I_2`, and `gamma=(1,1)^T`. Each prefix space is the one-dimensional span of `(1,-1)`, each closure scalar is 1, and the terminal product is 0. This remains valid in characteristic 2, where `-1=1` and `1+1=0`. This is exact cancellation of two path contributions for every word; no individual-path nonzero test would prove the output nonzero.

## A4. Composition-safe interfaces, and boundaries that are not safe

**Claim A4.** The equations in A1 preserve every continuation made from the certified alphabet: for any word `u`, reachable coordinate row `c`, and output column `delta`,

`(cB) A_u delta = c T_u (B delta)`.

This follows directly from `BA_u=T_uB`; it is an equality of full state rows before applying the output. Consequently a summary retaining the embedding `B` can be used with any supplied downstream linear map `H` by replacing it with `BH`. It need not rerun all prefix words.

For fragments with multiple admissible input rows, put those rows into a seed matrix `U`. Generate the invariant row space of **all** seed rows and check `U=P B` and `BA_i=T_iB`. Then

`U A_w H=P T_w (BH)`

for every word and downstream matrix `H`. This is a clean contract for stateful composition: every possible incoming boundary row must be covered, and the outgoing embedding must remain available. A certificate for only one chosen input row does not claim correctness on arbitrary new incoming states.

Two other standard forms of composition are safe:

- Direct sums certify sums/differences of scalar series.
- For synchronized products (coefficient-wise/Hadamard products), use Kronecker products: `B=B_1 tensor B_2`, `a=a_1 tensor a_2`, `T_i=T_(1,i) tensor T_(2,i)`. The identity `(B_1 tensor B_2)(A_(1,i) tensor A_(2,i))=(T_(1,i) tensor T_(2,i))(B_1 tensor B_2)` proves safety. These rows need not be a minimal reachable basis, but they are a sound invariant cover.

Scalar-series equality is also preserved under ordinary concatenation/Cauchy products: the coefficient at `w` is the finite sum `sum_(uv=w) f(u)h(v)`. Thus replacing an entire scalar series by an equal one inside scalar algebra is sound. This should not be confused with rewiring internal state boundaries, or with a polynomial-size guarantee under an unbounded sequence of tensor products; product dimensions may grow multiplicatively.

### A4a. Failed composition claims

1. The scalar equation `v gamma=0` alone cannot prove a zero outgoing state: `v=(1,-1)`, `gamma=(1,1)^T` gives 0, but the new output `delta=(1,0)^T` gives 1, over every field. To change outputs retain `B` and check `B delta`.
2. Closure under old transitions does not cover a new transition. Let `lambda=e_1`, all original transitions be zero, and `gamma=e_2^T` in dimension 2. The represented series is zero and the space `span{e_1}` is certified invariant for the original alphabet. Adding a new transition `C=E_12` yields `lambda C gamma=1` and breaks that invariance.
3. A one-seed summary does not cover arbitrary external input. A fragment with transition `diag(0,1)` certified only from seed `e_1` has reachable span `span{e_1}`. Incoming row `e_2` is not represented by that interface and cannot be passed through it as though it were.

These are concrete reasons that a local scalar cancellation test is not by itself a composition-safe module summary.

## A5. Characteristic specialization: theorem versus certificate reuse

**Claim A5.** The construction and proof hold separately over every field, including every prime characteristic. They do not assert that rank, a chosen basis, or a nonzero witness is characteristic-independent.

### A5a. Nonzero can specialize to zero, and rank can drop

Fix a prime `p`, take dimension two, `lambda=e_1`, `A=p E_12`, and `gamma=e_2^T`. Over `Q`, `f(a)=p!=0`, the reachable basis is `(e_1,p e_2)`, and the reachable rank is 2. Over `F_p`, `A=0`, the entire series is zero, and the reachable rank is 1. Thus a characteristic-zero nonzero witness is not automatically a nonzero witness modulo every prime; testing only modulo `p` cannot prove nonzero or zero over `Q` without further arithmetic information.

For integral input, specialization cannot increase reachable rank: all reachable rows are already spanned by words of length at most `d-1`; a finite matrix of those rows has zero `(r+1)`-minors over `Q`, hence zero integer minors, which remain zero modulo `p`. The example shows strict decrease is possible.

### A5b. A rational certificate may not have a defined reduction

In dimension three take `lambda=e_1`, `A_a=pE_12`, `A_b=E_12`, and `gamma=e_3^T`. The series is zero over every field. If BFS processes `a` before `b`, it can choose the actual-word basis rows `e_1,p e_2` over `Q`. The closure equation for `e_1 A_b` uses coefficient `1/p`. This valid rational certificate cannot be reduced modulo `p`. Indeed the reduced displayed rows span only `e_1`, while the reduced `b` transition reaches `e_2`.

The conclusion remains true in this example, but that particular basis/certificate has no valid specialization. Recomputing the span over `F_p` gives a valid certificate. The issue is divisibility in coordinates, not failure of the field-parametric theorem.

### A5c. Exact safe specialization statement

If the input and a certificate's equations are defined over a localization `Z[1/D]`, then for every prime `p` not dividing `D`, reduction is a ring homomorphism, and the equations remain true. In particular, a zero certificate remains sound even if the reduced rows of `B` become dependent. To preserve a *basis rank* claim, one must additionally keep a verified nonzero pivot minor nonzero modulo `p`. To preserve a *nonzero output* claim, its numerator must remain nonzero modulo `p`. Input denominators also have to be invertible.

An integral representation that is the zero series over `Q` is the zero series modulo every prime, since each word coefficient is the same integer zero. This semantic fact does not guarantee that every rationally normalized certificate specializes at every prime.

### A5d. Formal identity is not a scalar-function identity

The noncommutative polynomial `xy-yx` has nonzero word coefficients over every field, including characteristic 2, but vanishes on every scalar substitution in a commutative field. Over `F_p`, the one-variable formal polynomial `x^p-x` is also nonzero but zero as a scalar function. The theorem decides coefficient/formal zero, not merely scalar functional zero. Matrix-evaluation black boxes require a separate evaluation/input contract.

## A6. What is not supplied by this theorem

- It does not infer `lambda,A_i,gamma` from an arbitrary output-only black box, build a uniform matrix hitting set, or provide one evaluation point that works across all primes. Such results need separate hypotheses and proofs.
- Even a promise of a small linear representation does not make a coefficient-query oracle sufficient for this algorithm. For each hidden word `u` of length `L`, the singleton series `f_u(w)=1` iff `w=u` has a dimension-`L+1` path representation. Among the `n^L` possibilities, any deterministic coefficient-query zero tester making fewer than `n^L` relevant queries has an unqueried `u` and cannot distinguish `f_u` from zero. Queries of other words give zero. This lower bound is for coefficient/membership queries only; it is **not** a lower bound for richer matrix-evaluation black boxes or gate queries.
- General arithmetic circuits, rings without field linear algebra, hidden transition generators, and arbitrary nonlinear state compositions are not covered by the polynomial resource claim.
- The generated reachable dimension need not equal the Hankel rank/minimum scalar representation dimension: reachable states can still be unobservable at `gamma`. Reachable reduction alone is not full minimization.
- The certificate is exact. Numerical tolerances/approximate rank are a different problem.

## A7. Primary prior-art pointers and classification

This is reproduction/packaging of known tools, not a novelty claim. Sources checked online during this task:

1. M. P. Schutzenberger, **On the definition of a family of automata**, *Information and Control* 4 (1961), 245–270, DOI `10.1016/S0019-9958(61)80020-X`. Original journal page: <https://www.sciencedirect.com/science/article/pii/S001999586180020X>. Original-paper scan indexed at <https://www-igm.univ-mlv.fr/~berstel/SiteSchutzenberger/Travaux/A/1961-4DefinitionFamilyAutInfCtl.pdf>; the browser's PDF-open failed, so I do not claim a fresh full-text verification of that scan.
2. W.-G. Tzeng, **A Polynomial-Time Algorithm for the Equivalence of Probabilistic Automata**, *SIAM Journal on Computing* 21(2) (1992), 216–227, DOI `10.1137/0221017`. Publisher abstract checked: <https://epubs.siam.org/doi/10.1137/0221017>. It explicitly supplies a polynomial equivalence algorithm (stated quartic in total states).
3. R. Raz and A. Shpilka, **Deterministic polynomial identity testing in non-commutative models**, *Computational Complexity* 14(1) (2005), 1–19; author manuscript checked: <https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf>. The abstract and ABP sections establish the directly relevant noncommutative ABP identity-testing baseline; section 1.1 explicitly describes the method as non-black-box.
4. V. Arvind, P. Mukhopadhyay, and S. Srinivasan, **New results on Noncommutative and Commutative Polynomial Identity Testing** (2008), <https://arxiv.org/abs/0801.0514>. The authors explicitly connect automata theory and noncommutative PIT. Their black-box ABP reconstruction statement assumes queries at every given gate, illustrating why oracle details cannot be omitted.
5. S. Kiefer, **Notes on Equivalence and Minimization of Weighted Automata** (2020), <https://arxiv.org/html/2009.01217v1>. This is a primary author exposition explicitly claiming no new results, not the original historical discovery. It gives **the exact core algorithm and bounds here**: Algorithms 1–2 and Proposition 2.1 compute actual-word forward bases with retained length at most reachable dimension minus one and cubic arithmetic cost; Proposition 2.2 gives zero testing/nonzero witnesses; section 3 gives the same intertwining equations for forward conjugates. Its bibliographic remarks trace the history to items 1–2 and cubic refinements. This match prevents presenting A1–A2 as a new missing theorem.

For parent citation reuse, retrieved references include `turn214view0` (Raz–Shpilka PDF), `turn214view1` / `turn230view1` (Tzeng publisher), `turn214view3` / `turn230view3` (Arvind et al.), and `turn238view0` (Kiefer exact-match text). The parent must reopen sources before using delegated citation references in a user-facing answer.

## A8. Separate post-decision audit: parent's acyclic rational-jet proposal

This section audits only the explicit statement supplied by the parent after the frozen-operation comparison. It is not pre-proof evidence of transfer and does not use any family116 source.

Let `V_1(t),...,V_n(t)` be `hxh` rational-function matrices over `K`, supported on a common directed acyclic graph on the matrix indices. For each nonzero labelled edge `(i,e)`, suppose its entry is supplied as

`a_(i,e)(t) / product_j q_j(t)^e_(i,e,j)`,

where `a_(i,e)` and `q_j` are nonzero polynomials, all exponents are nonnegative integers, and `q_j(0)!=0`. Parallel choices of labels on the same underlying edge are separate edges for weighted path maximization. Include empty paths (at any vertex) in every path maximum. Let

`M_j=max_P sum_(labelled edges in P) e_(i,e,j)`,

`D=product_j q_j^M_j`,

`c_(i,e)=deg a_(i,e)-sum_j e_(i,e,j) deg q_j`,

`L=max(0,max_P sum_(labelled edges in P) c_(i,e))`,

and `E=1+deg D+L`.

**Claim A8.** For every noncommutative polynomial `F` whose scalar coefficients lie in any extension field `K'/K`, each entry of `D F(V_1,...,V_n)` is a polynomial in `K'[t]` of degree at most `deg D+L`. Moreover

`F(V)!=0` iff its image in `Mat_h(K'[t]/(t^E))` is nonzero.

Thus entrywise substitution into the regular representation of `K'[t]/(t^E)` by multiplication matrices of size `E` preserves the zero/nonzero status of `F(V)`. Over the base field the resulting matrices have size `hE`; extension-field coefficients can be handled by scalar extension of the same construction.

**Proof.** An entry of a word in the `V_i` is a finite sum over labelled directed paths. Common acyclicity bounds path length by `h-1`; the identity word corresponds to empty paths. For a path `P`, let `s_j` be its summed denominator exponent. Then `s_j<=M_j` for each `j`, and multiplying its rational term by `D` gives the polynomial

`(product_edges a_(i,e)) product_j q_j^(M_j-s_j)`.

Its degree is exactly `deg D + sum_edges c_(i,e)` and hence at most `deg D+L`. Multiplying by scalar coefficients and adding terms cannot increase this bound. Shared factors among numerators or denominators, and cancellations between different paths, can only decrease the resulting degree, so no coprimality or irreducibility assumption is needed for this upper bound.

Every `q_j`, and therefore `D`, has a nonzero constant term, so it is a unit in `K'[[t]]` and modulo `t^E`. If `F(V)` has zero `E`-jet, so does `D F(V)`. An entry of `D F(V)` is a polynomial of degree at most `E-1`; having zero `E`-jet forces that polynomial to be zero. Since `D` is a nonzero rational function, `F(V)=0`. The converse is immediate. Finally the multiplication-map representation `z -> (u -> zu)` of the quotient ring is injective because a zero map sends `1` to zero; it is a unital algebra homomorphism, so polynomial evaluation commutes with it. QED.

Negative edge costs do not harm this argument; the longest-path computation must permit a path to start and stop anywhere and include the empty path. Longest paths can be computed on the labelled DAG for each of the exponent weights and once for the degree costs. No enumerated path list is needed.

**Resource caveat.** Dynamic programming on the DAG uses polynomially many integer arithmetic operations in the number of labelled edges and denominator factors. Its *numeric* outputs `M_j`, `deg D`, and `E` can be exponentially large if exponents are binary encoded. Constructing expanded `D`, the jets, or an `hE`-dimensional regular representation is polynomial in those expanded degrees / `E` and explicit polynomial encoding, not necessarily in the binary exponent input length. An assertion of polynomial cost must state this distinction.

**Cyclic counterexamples.** Without acyclicity there is no fixed truncation length based only on a fixed tuple that detects every polynomial evaluation. The scalar tuple `V=[t]` gives the nonzero evaluation `F(V)=t^E` for `F=x^E`, whose `E`-jet is zero. Even a regular rational loop `V=[1/(1-t)]` fails uniformly: `F=(x-1)^E` gives `t^E/(1-t)^E`, again nonzero with zero `E`-jet. Any stateful composition that creates a directed cycle invalidates the DAG hypothesis and must be re-audited globally.

This proves an upper bound, not optimality. Distinctness/irreducibility and separately selectable paths would matter to sharpness claims; no such claim is made. No claim about injection on all noncommutative words, multiplicities, hitting sets, or novelty follows from A8 alone.

## Handoff

The frozen reachable-span operation is mathematically complete for supplied exact transitions and has polynomial-size independently checkable certificates. Its central algorithm, word bound, cubic arithmetic bound, and intertwining summary are explicitly classical. The open transfer question is solely whether the external problem actually supplies or legitimately constructs this representation within its promised resources; I have not inspected that target. Characteristic specialization and boundary composition have explicit sound contracts and counterexamples above. The parent's later acyclic rational-jet proposal is sound as an upper-bound statement with the stated expanded-degree resource caveat and common-DAG requirement.


## A9. Further focused audit: finite evaluation algebras and faithful fixed jets

The parent subsequently supplied the proposal in this section for independent challenge. The same exposure boundary applies: no family116 source or other agents' notes were read. The conclusions below are elementary proved statements, not priority claims.

### A9a. Exact equivalence

Let `K` be any field, `h>=1`, and let `V_1,...,V_n in Mat_h(K(t))` have all entries regular at `t=0`. Let

`A=K<V_1,...,V_n>`

mean the **unital K-algebra** they generate, that is, the `K`-linear span of all word evaluations, including `I_h`. For an integer `E>=1`, let `j_E` be entrywise truncation at zero into `Mat_h(K[t]/(t^E))`. Regularity makes `j_E` a well-defined unital `K`-algebra homomorphism on every matrix in `A`.

**Claim A9.1.** The following are equivalent:

1. Some fixed `E>=1` is faithful on `A`: for every noncommutative polynomial `F` with coefficients in `K`, `j_E(F(V))=0` if and only if `F(V)=0`.
2. `dim_K A` is finite.

**Proof, 1 implies 2.** Condition 1 says precisely that the restriction `j_E|A` is injective. Its target has `K`-dimension `h^2 E`, so `dim_K A<=h^2 E`.

**Proof, 2 implies 1.** Let `D=dim_K A<infinity`, and set `N_E=ker(j_E|A)`. These are descending `K`-subspaces. Their intersection is zero: a nonzero rational function regular at zero has finite order of vanishing, so a nonzero matrix has a nonzero entry detected by some finite jet. Since `A` is finite-dimensional, the descending chain has only finitely many strict dimension drops and is eventually constant; its eventual value is its intersection, hence zero. Therefore `N_E=0` for some `E`. QED.

**Stopping-test caution.** The equality `N_E=N_(E+1)` at one stage does not prove future stabilization. A chain can have a long plateau before a later drop. Finite-dimensionality proves eventual stabilization, not that the first equality is a certified stopping point. The explicit degree certificate below avoids this gap.

This equivalence concerns injectivity on the **evaluation algebra**, not injectivity of the free algebra: distinct polynomials may already have identical evaluations at the rational tuple. No word-injection or multiplicity assertion follows.

### A9b. An independently checkable sufficient certificate

Supply finitely many regular rational matrices `B_1,...,B_r`, constants `a_j,C_(j,i,k) in K`, a polynomial `H(t) in K[t]` with `H(0)!=0`, and an integer `E>=1`, satisfying

`I_h=sum_j a_j B_j`,

`B_j V_i=sum_k C_(j,i,k) B_k` for every `j,i`,

and, for every `j`, `P_j=H B_j` is a polynomial matrix with every entry of degree strictly less than `E`.

**Claim A9.2.** These conditions imply that `j_E` is faithful on `A`.

**Proof.** Let `R=span_K{B_1,...,B_r}`. The seed equation and the closure equations imply by induction that every evaluated word lies in `R`, hence `A subset R`. For any `X in R`, the matrix `H X` is polynomial and has every entry of degree less than `E`, because its coefficients in the displayed span are constants in `K`. If `j_E(X)=0`, then `j_E(H X)=0`; the degree bound forces `H X=0`. Since `H` is nonzero in `K(t)`, `X=0`. Thus `j_E` is injective on `R`, and in particular on `A`. QED.

Neither independence nor actual-word provenance of the `B_j` is needed for this sufficient certificate. They are needed only for an assertion that the list is an exact basis of `A` of dimension `r`. Exact rational identities can be checked after denominator clearing; the polynomial identities `H B_j=P_j`, constant-term condition on `H`, and coefficient degree checks are finite exact checks.

The requirement that the closure coordinates lie in **K rather than K(t)** is essential. For `h=1`, `V=t`, and `B_1=1`, the rational-coordinate equation `B_1 V=t B_1` holds, and `H=1` gives a degree-zero displayed basis element. Nevertheless the algebra is `K[t]`, and no fixed `E` is faithful. Allowing rational coordinates would incorrectly replace an infinite-dimensional `K`-algebra by a one-dimensional `K(t)`-space.

### A9c. Conditional generation and an explicit degree bound

Suppose `delta in K[t]`, `delta(0)!=0`, clears the tuple: every `M_i=delta V_i` is a polynomial matrix. Define

`b=max(deg delta, max_(i,u,v) deg (M_i)_(u,v))`,

using `deg 0=-infinity`. Since `delta` is nonzero, `b` is a nonnegative integer. Assume a supplied positive integer `D` is promised to satisfy `dim_K A<=D`.

**Claim A9.3.** A queue construction, starting at `I_h` and extending retained word matrices on the right by the `V_i`, returns a `K`-basis `B_1,...,B_r` of `A`, with `r<=D` and retained word lengths at most `r-1<=D-1`. For

`H=delta^(D-1)` and `E=1+(D-1)b`,

the certificate in A9b holds with this basis and its constant closure coordinates. In particular this `E` is faithful.

**Proof of generation.** Keep a list of `K`-independent evaluated words and a queue of newly accepted entries. An exact `K`-span test decides whether a candidate extends the span. Each accepted matrix increases its `K`-dimension, so at most `D` matrices are accepted. At exhaustion, the list's span contains `I_h` and is closed under every right multiplication by `V_i`; it therefore contains every word evaluation. The reverse containment holds by provenance. Each accepted word has a strictly earlier retained word as parent, giving the same index/depth bound as A1.

**Proof of the degree bound.** If a retained word has length `l<=D-1`, then

`B_j=delta^(-l) M_(i_1)...M_(i_l)`.

The numerator matrix has entry degrees at most `l b`. Hence

`H B_j=delta^(D-1-l) M_(i_1)...M_(i_l)`

is polynomial with entry degrees at most

`(D-1-l)deg delta + l b <= (D-1)b = E-1`.

This includes `l=0`, the identity word. Since `delta(0)!=0`, also `H(0)!=0`; the exact constant closure coordinates exist because the list is a `K`-basis of `A`. A9b now applies. QED.

The promise can be an upper bound, not the exact dimension. If the algebra has dimension one, then it equals `K I_h`, and `E=1` suffices; the formula handles `D=1` exactly, even if the initially chosen common denominator was needlessly nonconstant.

### A9d. What a K-linear dependence test entails

Rational matrices must be viewed as vectors over **K**, not over `K(t)`. For any finite list and candidate, multiply all entries by one common nonzero polynomial denominator, then flatten all polynomial coefficients across all `h^2` matrix entries. A constant-coordinate relation among rational matrices is equivalent to an ordinary `K`-linear relation among these finite coefficient vectors. Exact Gaussian elimination therefore decides the required dependence test.

Even finite-dimensional examples can have more `K`-dimension than `K(t)`-dimension: in `Mat_2(K(t))`, the matrices `I_2,E_12,t E_12` form a `K`-basis of a dimension-three algebra (all products of the two nonidentity generators are zero), but are dependent over `K(t)`. Thus using the ambient bound `h^2` for a `K(t)`-space does not establish a correct `K`-basis or this faithful-jet conclusion.

With the promised bound `D`, every retained word has length at most `D-1`, and its one-step candidates have length at most `D`. One may use the single denominator `delta^D` for every tested matrix. Their cleared polynomial matrices have entry degrees at most `D b`, so the flattened coefficient space has dimension at most

`N=h^2(D b+1)`.

There are at most `nD` candidate products before closure. Dense polynomial matrix multiplication and denominator alignment are polynomial in `h,D,b`; incremental elimination in a space of dimension `N` against at most `D` basis vectors is also polynomial. For example, elementary schoolbook arithmetic gives the coarse field-operation bound

`O(nD [h^3(D b+1)^2 + D h^2(D b+1)])`,

plus polynomial preprocessing to obtain `delta` and the `M_i` from explicit rational entries. No sharp complexity claim is intended. The certificate has `r+n r^2` constant coordinates and at most `r h^2((D-1)b+1)` polynomial coefficients for the cleared basis, together with the common denominator representation and provenance. These sizes are polynomial in the displayed numeric parameters.

Over `F_p`, this yields polynomial bit cost with the usual polynomial-in-`log p` exact coefficient arithmetic. Over `Q`, polynomial matrix products of at most `D` explicit factors have polynomially bounded rational coefficient heights in `D`, the dense degrees, and input coefficient bit lengths; polynomial-size determinant bounds control the constant-coordinate linear solves. Thus a denominator-controlled/fraction-free implementation gives polynomial bit time in those parameters. Unit-cost field arithmetic is not itself a bit-complexity proof for arbitrary encoded fields.

These claims are polynomial in **D and expanded degree b**, not in `log D`, sparse-degree encodings, or binary exponents alone. There is no claim of unconditional termination when `A` is infinite-dimensional. A finite budget can instead stop upon exhibiting `D+1` independent words, which certifies only `dim_K A>D`, not infinite-dimensionality.

### A9e. Extension fields and examples

Let `K'/K` be any field extension, keeping `t` as an indeterminate over `K'`, and let `A'=K'<V_1,...,V_n> subset Mat_h(K'(t))`. Every finite list of base-field rational matrices has the same linear rank over `K` and over `K'`: clear denominators and use the rank of the finite coefficient matrix, whose nonzero minors stay nonzero under field extension. Therefore a finite basis of `A` remains a basis of `A'`, with the same dimension. If `A` is infinite-dimensional, every finite independent sublist stays independent, so `A'` is also infinite-dimensional.

In the finite case the rank of each jet map on a base-field basis is likewise unchanged. Consequently both existence of a faithful fixed jet and the least faithful `E` are invariant under scalar extension. The certificate in A9b and the explicit bound in A9c therefore work uniformly for polynomials with coefficients in any extension field. This is scalar extension with an independent rational-function parameter, not an operation that identifies the parameter `t` with a newly adjoined scalar or specializes it to a scalar value.

1. **Finite non-DAG algebra.** The matrix `P(t)=[[1,t],[0,0]]` satisfies `P^2=P`. Its evaluation algebra is `span_K{I_2,P}`, of dimension two, despite a self-loop in its support. In fact `E=1` is already faithful because `I_2` and `P(0)=diag(1,0)` are independent. The general bound with `delta=1,b=1,D=2` gives the valid but nonsharp bound `E=2`. Thus acyclicity is sufficient for one kind of degree certificate, not necessary for a faithful fixed jet.
2. **Infinite algebra.** The scalar tuple `V=[t]` generates `K[t]`. For every fixed `E`, the nonzero evaluation `V^E=t^E` has zero `E`-jet. This proves the failure in the infinite-dimensional case directly and also refutes a `K(t)`-rank substitute.
3. **Dimension alone is insufficient to bound E.** For any integer `M>=1`, let `V=t^M E_12`. Then `V^2=0`, so its algebra has the fixed dimension two in fixed ambient size two. An element has form `a I_2+c t^M E_12`. For `E<=M`, `V` lies in the jet kernel. For `E=M+1`, its diagonal constant coefficient determines `a` and the degree-`M` off-diagonal coefficient determines `c`, so the jet is injective. Thus the least faithful truncation is exactly `M+1`, unbounded at fixed algebra dimension. The degree-aware formula in A9c is sharp on this family (`delta=1,b=M,D=2`). If `M` is sparse/binary encoded, this example also explains the expanded-degree cost caveat.

**A9 verdict.** The proposed equivalence, constant-coordinate certificate, conditional basis-generation theorem, degree formula, and extension-field uniformity are correct with the definitions above. The principal pitfalls are replacing K-linear span by K(t)-linear span, claiming that one kernel plateau is a stopping certificate, omitting the dimension promise for algorithm termination, or describing a degree-dependent construction as polynomial in binary degree encodings. No source-level transfer or novelty assertion is made.

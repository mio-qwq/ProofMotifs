# PM-Q-D — independent second mathematical view

## Task ledger and status

- TASK ID: PM-Q-D.
- RESEARCH QUESTION: characterize when iterated zero-constant multiplicative-q sums of a rational alphabet are linearly independent over the rational-function field; audit split-pole certificates and minimum-cost alphabet selection.
- KNOWN ASSUMPTIONS: K is a field, q is in K^× and has infinite multiplicative order, z is a fresh indeterminate, σ fixes K and sends z to qz, and every alphabet letter b_i belongs to zK[[z]] ∩ K(z).
- AVAILABLE EVIDENCE: read repository AGENTS.md and research/RESEARCH_PROGRAM.md only. Family 116 is already-read calibration, not an unseen transfer test. No other current-task agent notes were read. The proofs below are self-contained; normalized q-discrete-residue language is established mathematics, and no novelty claim is made.
- EXPECTED OUTPUT: a full proof or obstruction, with characteristic, scalar-extension, and algorithmic qualifications.
- ALLOWED SCOPE: this internal /tmp/pm-q-d.md note; repository read-only; no Git operations or children.
- INDEPENDENCE REQUIREMENT: an independent mathematical derivation, not reconstruction of another agent's proof.
- STOP CONDITION: a complete proof or a genuine obstruction, plus an explicit distinction between rational-coefficient word independence and constant-coefficient faithfulness.
- HANDOFF STATUS: complete. All substantive results are elementary proved statements, not formal-verification claims.

## Definitions

Put Δ = σ − id. For g = ∑_{n≥0} g_n z^n, define

    J_i(g) = ∑_{n≥1} [z^n](b_i g)/(q^n − 1) · z^n.

Thus J_i(g) is the unique zero-constant formal series satisfying ΔJ_i(g) = b_i g. Let ε denote the empty word and set

    h_ε = 1,       h_{iw} = J_i(h_w).

Every finite word is included, including ε. Independence of an infinite alphabet or word family always means finite-support linear independence. Rational coefficients act in K((z)), so they need not be regular at 0.

## PM-QD-001 — inverse and constants

**Claim.** Δ maps zK[[z]] bijectively to itself. Its kernel on K((z)), and hence on K(z), is K. These statements hold in every characteristic.

**Proof.** On each Laurent monomial z^n, Δ acts by multiplication by q^n − 1. Infinite multiplicative order makes this multiplier nonzero for every integer n ≠ 0. Therefore the displayed coefficientwise inverse exists in positive degrees, and a Δ-invariant Laurent series has only its degree-zero coefficient. ∎

## PM-QD-002 — exact rational-word-independence criterion

**Theorem.** The following are equivalent:

1. The family {h_w : w a finite word} is linearly independent over K(z).
2. The classes [b_i] in the K-vector space K(z)/ΔK(z) are linearly independent over K.

The theorem is valid in arbitrary characteristic under the infinite-order hypothesis on q.

### Necessity

Suppose there is a finite relation ∑_i c_i b_i = Δr with c_i in K, not all zero, and r in K(z). Since the left side is regular at 0 and has zero constant term, r is regular at 0: a pole of order m > 0 would contribute a nonzero leading term multiplied by q^(−m) − 1 to Δr. By uniqueness of zero-constant primitives,

    ∑_i c_i h_i = r − r(0).

Consequently

    ∑_i c_i h_i − (r − r(0))h_ε = 0

is a nonzero rational-coefficient word relation. This proves (1) ⇒ (2).

### Sufficiency: a minimal-relation argument

Assume (2), but suppose a nonzero finite relation

    ∑_w f_w h_w = 0,                 f_w in K(z)

exists. Among all such relations, minimize the largest supported word length n, and then minimize the number m of supported words of length n. The case n = 0 is impossible since h_ε = 1. Divide by one length-n coefficient so that f_u = 1 for some word u of length n.

Using σh_{iv} = h_{iv} + b_i h_v, apply σ to the relation and subtract the original relation. The resulting coefficient of h_v is

    g_v = Δf_v + ∑_i b_i σ(f_{iv}),

where absent coefficients are zero. The largest possible length is still n, and g_u = Δ1 = 0. If the coefficient vector g were nonzero, it would give either a relation with maximum length less than n, or a relation with maximum length n and fewer than m supported top words. Both contradict the choice of relation. Thus every g_v is zero as a rational function.

For |w| = n this gives Δf_w = 0, so PM-QD-001 gives f_w = c_w in K. For each |v| = n − 1, the identity g_v = 0 now gives

    Δf_v + ∑_i c_{iv} b_i = 0.

Independence of the classes [b_i] forces every c_{iv} to vanish. Every length-n word has the form iv, so all top coefficients vanish, contrary to their choice. This proves (2) ⇒ (1). ∎

**Important scope.** This is linear independence of the word series over K(z), not algebraic independence of those series. No shuffle identity, factorial division, characteristic-zero differential argument, or transcendence theorem is used.

## PM-QD-003 — split-pole q-residue certificate

Let B_split be the K-vector space of rational functions regular at 0, vanishing at 0, whose finite poles are all nonzero and split over K. For α in K^× and k ≥ 1, put

    φ_{α,k}(z) = (1 − z/α)^(−k) − 1.

Every b in B_split has a unique finite expansion

    b = P(z) + ∑_{α,k} c_{α,k} φ_{α,k}(z),       P in zK[z].

This is ordinary partial fractions with the constant term absorbed by subtracting 1 from each principal-part basis element. The normalized basis is useful because

    σφ_{α,k} = φ_{α/q,k},
    Δφ_{α,k} = φ_{α/q,k} − φ_{α,k},

with no coefficient scaling and no mixing of pole orders.

Let O range over multiplicative orbits K^×/q^Z. Define the finite-support residue coordinates

    R_{O,k}(b) = ∑_{α in O} c_{α,k}.

**Claim.** For b in B_split,

    b in ΔK(z)  iff  every R_{O,k}(b) is zero.

More precisely,

    B_split / (B_split ∩ ΔK(z))  ≅  ⨁_{O,k≥1} K,

and B_split ∩ ΔK(z) = ΔB_split.

### Sufficiency and explicit certificate

Each positive-degree polynomial monomial is exact:

    a_n z^n = Δ( a_n z^n/(q^n − 1) ).

Fix an orbit representative a and write φ_n = φ_{q^n a,k}. On this orbit/order block, let c_n be the finitely supported coefficient sequence of b. If ∑_n c_n = 0, define

    d_n = ∑_{j<n} c_j.

The sequence d is finitely supported, and d_{n+1} − d_n = c_n. Since σφ_n = φ_{n−1},

    Δ(∑_n d_n φ_n) = ∑_n c_n φ_n.

Doing this on all finitely many blocks and adding the polynomial primitive constructs a rational zero-constant primitive in B_split.

### Necessity, including nonsplit potential telescopers

If b = Δr with arbitrary r in K(z), work over an algebraic closure solely to split the poles of r. A finite principal-part coefficient array on each nonzero q-orbit/order block is transformed by Δ into a difference of neighboring entries; its total sum is zero. This remains true if r originally had nonsplit poles. The coefficients of b on its K-rational pole orbits are precisely the displayed c_{α,k}, so every R_{O,k}(b) is zero. A possible pole at 0 is excluded as in the necessity proof of PM-QD-002. Thus no unmentioned nonsplit rational telescoper defeats the certificate.

Finally, R is surjective because a single φ_{a,k} realizes a coordinate unit vector. The kernel is exactly as proved, giving the quotient assertion. ∎

**Normalization warning.** The unweighted coefficient sum is correct in the φ_{α,k} basis. In a basis (z − α)^(−k), σ introduces q^(−k), and the corresponding residue formula needs weights. One must not silently mix the two conventions.

**Characteristic boundary.** This certificate works in positive characteristic as written: partial fractions and the shift identity are characteristic-free, and q^n − 1 is invertible by assumption. Pole orders divisible by the characteristic cause no additional exception. The coefficient of the constant polynomial in a general rational function would be an additional obstruction; the restriction b(0) = 0 and the normalized φ expansion remove this separate coordinate here.

## PM-QD-004 — minimum-cost finite dictionary selection

Suppose a finite dictionary b_1,…,b_N in B_split is supplied, with exact residue-coordinate columns M_1,…,M_N. Only finitely many rows (O,k) occur. Give element j an additive cost a_j in an ordered domain with effective comparison, and fix an integer r ≥ 0.

**Problem.** Choose r dictionary elements, with minimum total cost, so that all word series on the chosen alphabet are K(z)-linearly independent.

**Reduction.** By PM-QD-002 and PM-QD-003, feasibility means exactly that the chosen columns of M are independent. These subsets form the linear matroid represented by M. Thus the problem is the minimum-weight basis problem in its rank-r truncation.

**Algorithm.** Sort elements by nondecreasing cost, breaking ties arbitrarily but consistently. Scan in that order; retain a column if it is outside the span of the retained columns, and stop after r retentions. If fewer than r columns can be retained, report infeasibility. Zero classes are loops and are never retained.

**Proof of optimality.** After any scanned prefix, before reaching r, the retained columns form a basis for the span of that prefix: a rejected column was already in the retained span. For an arbitrary independent size-r competitor, let its elements in scan order be t_1,…,t_r. By the time t_k has been scanned, that prefix contains k independent columns. Hence greedy has already retained its kth element g_k, so a(g_k) ≤ a(t_k). Summing over k proves minimum total cost. This also proves the full-rank minimum-cost basis assertion by setting r = rank(M). ∎

### Algorithmic and cost qualifications

1. This is a finite-dictionary, additive-cost, fixed-cardinality/rank result. It is not a structural generator for arbitrary rational alphabets, a minimum description-length theorem, or a solution to nonadditive operator/DAG/composition costs.
2. Negative costs are harmless for the stated fixed size r problem. If the objective is only “rank at least r,” permits redundant elements, or allows arbitrary cardinality, negative costs change the problem. If “word-free” is retained, independence itself forces rank to equal cardinality.
3. A finite field-operation count requires the split partial fractions and correct q-orbit identifications. Testing α/β in q^Z is an additional orbit-membership problem; abstract field arithmetic does not supply a uniform effective decision algorithm for it. Supplying orbit labels, and integer shift witnesses when an explicit primitive is required, makes the algebraic procedure precise.
4. With D supplied coordinate rows, ordinary incremental elimination needs polynomially many exact field operations (for example O(NDr) for testing against at most r retained columns), plus sorting and preprocessing. This is not an unconditional bit-complexity bound. Factoring, orbit decisions, expression swell, and numeric cost comparisons must be included in any concrete complexity model.
5. An explicit telescoper can have support spanning a very large orbit-index interval. Its expanded output size can therefore greatly exceed the input's sparse pole count or the bit length of shift witnesses. The selection test needs the summed coordinates, not an expanded primitive, but a claimed small certificate must specify its encoding.

## PM-QD-005 — strong criterion is not necessary for K-faithfulness

Take the one-letter alphabet b = z over any allowed (K,q). For the unique word a^n of length n,

    h_{a^n} = z^n / ∏_{j=1}^n (q^j − 1),        h_ε = 1.

This follows by induction directly from the defining recurrence. The denominators are nonzero, and these are nonzero scalar multiples of pairwise distinct monomials. Hence the word series are linearly independent over K. In particular the cyclic word map K⟨a⟩ → K[[z]], a^n ↦ h_{a^n}, is injective; it also implies that the associated one-generator operator representation a ↦ J is faithful, because any operator relation could be applied to 1.

Nevertheless

    z = Δ(z/(q − 1)),

so [b] = 0 and the rational-word-independence criterion fails. Indeed h_a = (z/(q − 1))h_ε is already a nonzero K(z)-linear relation. Thus a minimum-cost selector based on residue independence solves a strictly stronger target than basic K-coefficient faithfulness; it is not automatically an optimal selector for that weaker target.

## PM-QD-006 — honest constant extension and fresh variable

The convention “z is fresh” is essential: q and every element of the coefficient field are fixed by σ, while σz = qz. One cannot promote a series in the same z to a σ-fixed coefficient while retaining this action.

There is also a genuine invariance statement, not merely a convention:

**Claim.** Let E/K be any field extension, keep q and the rational letters from K(z), and take z to be a fresh indeterminate over E. Then independence of the classes [b_i] over K in K(z)/ΔK(z) is equivalent to independence of those classes over E in E(z)/ΔE(z). Consequently the word-independence theorem survives this constant extension.

**Proof.** Only preservation needs proof. Suppose a finite relation ∑_i e_i b_i = Δr holds in E(z), with e_i in E. Every finite pole of the left side is algebraic over K. Over an algebraic closure of E, consider any nonzero q-orbit of poles of r. Its finite pole support has an extreme point; under the shift z ↦ qz, one boundary pole is not canceled in σr − r. Thus this orbit contains a pole of the left side. Every pole of r in that orbit is a q^integer multiple of an element algebraic over K and is therefore algebraic over K. A pole at 0 is already algebraic over K (and in the present regular-at-0 setting is absent).

There are only finitely many poles of r. Choose H in K[z] whose roots, with sufficient multiplicities, include them all. Then Hr lies in E[z], and r is a finite E-linear combination of elements z^j/H(z) in K(z). Hence r belongs to the natural injected E-vector space E ⊗_K K(z) inside E(z). The relation therefore holds already in this tensor product, where Δ is the scalar extension of the original K-linear map.

Passing to its quotient by Δ gives a relation among 1 ⊗ [b_i] in E ⊗_K (K(z)/ΔK(z)). K-linearly independent vectors remain E-linearly independent under extension of scalars, so all e_i vanish. The converse follows immediately because a K-relation is also an E-relation. ∎

This proof does not require K to be perfect, algebraically closed, or characteristic zero. In the split-pole case the same result is immediate from the residue matrix, which has entries in K and the same orbit labels after constant extension.

## PM-QD-007 — sharp order boundary for q

If q has finite multiplicative order d, then Δ annihilates z^d, has extra zero-constant invariants, and cannot map any formal series to z^d. Thus the stipulated unique zero-constant inverse on all zK[[z]] does not exist. The alphabet b = z^d already prevents the first primitive from existing. Even the alphabet b = z, whose initial primitives exist for d > 1, reaches the obstruction at the word of length d. Therefore replacing “infinite order” by merely q ≠ 1 is invalid.

Positive characteristic itself is not an obstruction: for instance K = F_p(t) and q = t satisfy every hypothesis. Finite coefficient fields do not, because their nonzero elements all have finite multiplicative order. Any argument introducing ordinary factorial denominators would add an unnecessary characteristic restriction absent from the result proved here.

## Adversarial checks and limits

- Rational telescopers with poles at 0: ruled out by the leading Laurent term, not assumed away.
- Nonsplit poles in a potential telescoper: covered by orbitwise partial fractions over an algebraic closure in PM-QD-003.
- Possible nonconstant σ-fixed rational coefficients in a minimal relation: ruled out by PM-QD-001.
- Positive-characteristic Frobenius phenomena: do not affect this linear theorem; no algebraic-independence claim is made.
- Polynomial letters: all positive-degree polynomial letters have zero residue class, yet can support K-faithful word maps, as PM-QD-005 shows.
- Infinite dictionaries: the independence criterion remains a finite-relation statement, but the finite weighted-greedy algorithm does not silently extend to an unenumerated or infinite search space.
- Prior-art/transfer status: these results provide exact classical-style q-difference synthesis and a finite linear-matroid consequence. They do not by themselves establish a missing mathematical tool, novel priority, or successful held-out transfer.

### Exact computation log

A symbolic-package sanity check could not start because the default Python lacks SymPy; no symbolic-computation result is claimed. A replacement using only Python's exact Fraction arithmetic checked 32 series coefficients of the primitive formula at q = 2, pole order 2, with orbit coefficients c_{−2} = 3, c_0 = −5, c_3 = 2 and d_n = ∑_{j<n}c_j. It also checked the b = z recurrence through word length 8. Both passed. These are finite implementation/sign checks, not substitutes for the infinite proofs above.

## Handoff summary

The proposed iff statement is correct, including in positive characteristic, under the stated infinite-order and fresh-variable hypotheses. The shortest robust proof is the two-level minimal-relation argument of PM-QD-002. Split-pole normalized residue sums exactly decide the classes, and finite additive-cost rank-r selection is precisely weighted linear-matroid greedy. The central caution is target strength: b = z gives an explicit K-faithful alphabet rejected by rational-word independence. Algorithmic claims must expose partial-fraction/orbit-membership inputs and certificate encoding. No obstruction to the theorem was found; its scope is narrower than general representation discovery or constant-coefficient faithfulness optimization.

# Bounded follow-up: polynomial alphabets and operator faithfulness

This continuation was independently assigned after the preceding handoff. Its scope remains this note only, with no other current-task notes read, repository edits, Git operations, or children. The first classification and the identities below were derived independently. The coordinator then supplied the proposed change C = B + A² and its quantum-plane formula; PM-QD-010 is an independent verification of that supplied deduction, not an independent proposal of it. These are classical growth/Ore-algebra mechanisms, with no novelty claim.

## Definitions for the weaker target

For n formal letters, let

    ρ : K⟨X_1,…,X_n⟩ → End_K(K[[z]]),       X_i ↦ J_i,

be the unital K-algebra homomorphism defined by operator composition. Composition is read rightmost first. “Basic K-operator faithfulness” means that ρ is injective. The cyclic word map instead sends a polynomial P to ρ(P)(1). Cyclic injectivity implies operator faithfulness, but these are distinct definitions in general.

## PM-QD-008 — complete classification for polynomial seeds

**Theorem.** Suppose q has infinite multiplicative order and every b_i is in zK[z]. Then:

- For no letters, the scalar representation is faithful.
- For one letter, the operator representation and cyclic word map are faithful if and only if its seed is nonzero.
- For at least two letters, neither the operator representation nor the cyclic word map is faithful.

This holds over every characteristic. In the last case there is a nonzero operator identity homogeneous in word length.

### One nonzero letter

Let ν ≥ 1 be the least degree in b with nonzero coefficient a_ν. Induction on k gives

    J_b^k(1) = [a_ν^k / ∏_{j=1}^k(q^(jν) − 1)] z^(kν)
               + terms of larger degree.

The displayed coefficients are nonzero. In a finite nontrivial linear combination ∑_k c_k J_b^k(1), the smallest k having c_k ≠ 0 contributes the unique least-order term and cannot cancel. Thus the cyclic map is injective, and applying an alleged operator identity to 1 proves operator faithfulness. This one-letter argument actually works for every nonzero b in zK[[z]], not only polynomial b. If b = 0, the nonzero free polynomial X maps to zero.

### At least two letters: polynomial-growth obstruction

It suffices to use any two letters. A zero letter already gives a length-one relation. Otherwise choose d ≥ 1 bounding the degrees of the finitely many polynomial letters under consideration, and write

    b_i = ∑_{s=1}^d a_{i,s} z^s.

For m ≥ 0 put T = q^m. The elementary action is

    J_i(z^m) = ∑_{s=1}^d a_{i,s} z^(m+s)/(q^s T − 1).

Consider a word operator of length L. In chronological order of application (rightmost letter first), select shifts s_1,…,s_L, each between 1 and d. Put S_j = s_1 + ⋯ + s_j. Its corresponding term on z^m has coefficient

    ∏_{j=1}^L a_{i_(L+1−j),s_j} / ∏_{j=1}^L(q^(S_j)T − 1)

and output exponent m + S_L. The partial sums S_j are distinct integers in {1,…,dL}. Therefore every denominator divides

    D_L(T) = ∏_{r=1}^{dL}(q^rT − 1).

The quotient D_L by a term's denominator has degree dL − L. Grouping by final shift S gives

    ρ(w)(z^m) = ∑_{S=L}^{dL} [P_{w,S}(T)/D_L(T)] z^(m+S),

where each P_{w,S} is in K[T] and has degree at most (d − 1)L. There are (d − 1)L + 1 possible shifts and the same number of numerator coefficients per shift. Thus all length-L word operators lie in the image of a K-vector space of dimension at most

    ((d − 1)L + 1)².

For n ≥ 2 there is an L such that n^L exceeds this number. Linear algebra then supplies scalars c_w, not all zero, for which every polynomial ∑_{|w|=L} c_w P_{w,S} is zero. Consequently ∑ c_w ρ(w) vanishes on every monomial z^m: D_L(q^m) is nonzero because every m + r is positive and q has infinite order. The corresponding nonzero free polynomial is homogeneous of word length L.

Finally, each J_i raises z-adic order by at least one and is continuous. A finite word operator is continuous; a finite linear combination that vanishes on all monomials vanishes on all polynomials and hence all formal series by truncation. Equivalently, the finite-band formula shows directly that every output coefficient depends on only finitely many input coefficients. Therefore this is an identity in End_K(K[[z]]), not only an identity on polynomial inputs. Applying it to 1 also disproves cyclic injectivity. ∎

**Bounds and qualifications.** The condition n^L > ((d − 1)L + 1)² is a sufficient, not minimal, identity-length bound. For a coarse completely explicit choice, L = 8d suffices whenever d ≥ 1 and n ≥ 2: ((d − 1)8d + 1)² ≤ 64d⁴ < 256^d = 2^(8d). The latter inequality starts at d = 1 and is preserved because the ratio of right sides is 256, whereas ((d + 1)/d)^4 ≤ 16. A polynomial identity can thus be constructed by finite linear algebra on the displayed numerator coordinates, provided field arithmetic is effective. This does not claim minimal identity size or a bit-complexity bound. The same proof applies to an infinite alphabet by restricting to two letters.

**Filtered growth refinement.** The span of all words of length at most L has dimension at most (dL + 1)². Indeed the same D_L clears the denominators of every shorter word; its numerator degree is at most dL, and its output shift is between 0 and dL. The empty word is represented by numerator D_L at shift 0. Thus the finitely generated operator algebra has at most quadratic word-filtration growth (Gelfand–Kirillov dimension at most 2), not merely a quadratic bound on each separate homogeneous-length image. This is a standard growth obstruction to containing the given two-or-more-generator free algebra faithfully.

## PM-QD-009 — explicit identities for seeds z and z²

Put A = J_z and B = J_(z²). Directly on z^m, with T = q^m,

    BA(z^m) = z^(m+3)/[(qT − 1)(q³T − 1)],
    AB(z^m) = z^(m+3)/[(q²T − 1)(q³T − 1)],
    A³(z^m) = z^(m+3)/[(qT − 1)(q²T − 1)(q³T − 1)].

The elementary numerator identity

    (q²T − 1) − q(qT − 1) = q − 1

therefore proves the operator identity

    BA − qAB = (q − 1)A³.

Continuity extends the monomial calculation to all K[[z]]. This is a nonhomogeneous identity in ordinary word length, but is homogeneous for weights wt(A) = 1 and wt(B) = 2. Taking its right-A multiple minus its left-A multiple also gives the homogeneous length-three identity

    BA² − (q + 1)ABA + qA²B = 0.

Both identities are nonzero formal free polynomials in every allowed characteristic. They require no division by q − 1 or q + 1 in their verification.

For completeness, there is no nonzero operator relation supported entirely in homogeneous length one or entirely in homogeneous length two for this particular pair. At length one, A and B have distinct output shifts. At length two, A² and B² have unique shifts 2 and 4; AB and BA have shift 3 but are not constant multiples, since their denominator ratio (q²T − 1)/(qT − 1) is nonconstant for q ≠ 1. Infinite distinct T = q^m make this rational-function distinction an operator distinction. Thus length three is minimal for a homogeneous relation. The earlier nonhomogeneous identity also has maximal word length three.

## PM-QD-010 — exact quantum-plane algebra for z,z²

The coordinator proposed C = B + A² and the resulting PBW formula. Both are valid, with the following complete verification.

From PM-QD-009,

    CA = BA + A³ = qAB + qA³ = qAC.

Moreover

    C(z^m) = [qT/((qT − 1)(q²T − 1))] z^(m+2).

Applying C repeatedly shifts T by successive factors q². Its numerators multiply as

    ∏_{k=0}^{j−1} q(q^(2k)T) = q^(j²)T^j,

while its denominators contain each factor q^rT − 1 once for 1 ≤ r ≤ 2j. Applying A another i times proves, for all i,j,m ≥ 0,

    A^i C^j(z^m)
      = [q^(j²)T^j / ∏_{r=1}^{i+2j}(q^rT − 1)] z^(m+i+2j),
        T = q^m.

Empty products are 1. This formula is characteristic-free.

**PBW independence.** Suppose a finite combination ∑_{i,j} λ_{i,j} A^iC^j is the zero operator. Group its action on z^m by the final shift S = i + 2j. The common denominator at that shift is ∏_{r=1}^S(q^rT − 1), so for every m ≥ 0,

    ∑_{j=0}^{⌊S/2⌋} λ_(S−2j,j) q^(j²) (q^m)^j = 0.

A polynomial over a field cannot vanish at the infinitely many distinct elements q^m unless it is zero. Its coefficients therefore all vanish, proving that the operators A^iC^j are K-linearly independent.

**Exact presentation.** The relation CA = qAC reorders every word into a scalar multiple of a normal monomial A^iC^j. The abstract quantum plane K⟨a,c⟩/(ca − qac) consequently maps onto K⟨A,C⟩ and is spanned by the corresponding normal monomials. Their proved operator independence makes that map injective. Since C = B + A² and B = C − A²,

    K⟨A,B⟩ = K⟨A,C⟩ ≅ K⟨a,c⟩/(ca − qac).

Equivalently the original pair has the exact presentation

    K⟨A,B⟩ ≅ K⟨a,b⟩/(ba − qab − (q − 1)a³).

Indeed the mutually inverse triangular changes c = b + a² and b = c − a² identify the two abstract presentations. Thus the displayed cubic relation generates the full relation ideal for the original two operators; “no other relations” means no additional independent defining relation is required, not that there are no consequences such as PM-QD-009's homogeneous identity.

This exact quantum-plane description supplies a concrete classical explanation of the polynomial grammar's failure to be free. It does not generalize the two-generator exact presentation to arbitrary polynomial dictionaries without additional work.

## Follow-up handoff

The polynomial-seed conjecture is proved in its full operator form, including all-series continuity and arbitrary characteristic. A single nonzero seed is faithful; two or more polynomial seeds never are. The pair z,z² has both the explicit cubic identity and a homogeneous length-three identity, and after the coordinator's verified triangular generator change its exact generated algebra is the quantum plane. This strengthens the earlier warning: the polynomial sector can be completely classified for basic faithfulness, while the residue criterion targets strictly stronger rational-coefficient independence.

An additional exact Fraction-arithmetic sanity check passed at q = 2: both displayed A,B identities were checked on z^m for 0 ≤ m ≤ 23, and the A^iC^j formula for the same m with 0 ≤ i,j ≤ 4. The infinite statements rest on the proofs, not these finite checks.

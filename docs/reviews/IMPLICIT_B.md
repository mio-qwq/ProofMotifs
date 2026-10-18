# PM-IMPLICIT-B — implicit degree-minimal point interpolation

## Nine-field task ledger

- TASK ID: PM-IMPLICIT-B.
- RESEARCH QUESTION: Given only m distinct explicitly coordinated points H subset K^n, with no monomial dictionary or degree bound supplied, generate an evaluation-spanning polynomial/cardinal representation of minimum total degree by coordinate multiplication and pruning, polynomial in n,m rather than the ambient monomial count.
- KNOWN ASSUMPTIONS: m,n>=1; K is any field with exact effective field operations and equality; H=(h_1,...,h_m) consists of pairwise distinct K-rational points; ordinary commutative polynomials and total degree are the allowed grammar. Complexity below counts field operations and treats coordinate encodings separately.
- AVAILABLE EVIDENCE: Read AGENTS.md and research/RESEARCH_PROGRAM.md in the preceding scoped task, and now read research/mechanisms/CONSTRUCTION_CONTRACTS.md, especially PM-CONSTRUCTION-0002. Its source197 square-Gram criterion is surjectivity of ev_H on the permitted degree space, with 2d<=q-2. Existing finite-dictionary selection does not by itself supply the dictionary generation proved here.
- EXPECTED OUTPUT: Exact algorithm and proof, degree-safe pruning, early-plateau justification, degree-minimal cardinal output and checkable failure/minimality certificates, polynomial arithmetic cost, exact positive/negative controls, and a classical-baseline comparison without originality claims.
- ALLOWED SCOPE: Read-only repository, own /tmp/pm-implicit-b.md and checker; no Git, no children, no external-source lookup/communication, except parent coordination and handoff. Parent handles primary sources.
- INDEPENDENCE REQUIREMENT: This algorithm and proof were derived independently before cross-review. No current /tmp/pm-implicit-a* or /tmp/pm-implicit-c* notes were read. Repository searches were confined to existing mechanism/review/tool files, not current independent notes.
- STOP CONDITIONS: One bounded representation-generation result; no finite rank scan promoted to an infinite theorem; no general-purpose optimal representation claim outside this polynomial point-evaluation grammar.
- HANDOFF: Full statements, proofs, arithmetic/encoding costs, certificate design, actual exact checks and limits follow.

## Result

**PM-IMPLICIT-B1.** From the raw points one can compute a nested, total-degree-adapted monomial evaluation basis, the minimum degree d* for which ev_H:K[x_1,...,x_n]_(<=d*) -> K^m is onto, and m cardinal polynomials of that minimum common degree. At most n*m monomial candidates are offered, with O(n*m^3) field operations. The bound d*<=m-1 holds over every field. In fact the resulting cardinal polynomials are individually degree-minimal, not only optimal in their maximum degree.

No ambient set of binomial(n+d,d) monomials is enumerated. The output is sparse: m retained monomials and an m-by-m coefficient matrix. This is a classical evaluation-algebra/point-interpolation construction, not a new general tool claim.

## Algorithm: degree frontiers, not arbitrary spanning closure

Put v(p)=(p(h_1),...,p(h_m))^t and

    V_d = span_K{v(p): deg(p)<=d},
    D_i = diag(h_(1,i),...,h_(m,i)).

Start with retained monomial list B=[1], evaluation vector 1_m, and current frontier [1]. Maintain exact incremental elimination for the retained evaluation vectors. If m=1, stop with d*=0.

For degree d=1,2,...:

1. Start an empty next frontier.
2. For each retained monomial b in the current frontier (all have degree d-1), and each coordinate i, form only the candidate x_i*b, whose evaluation vector is D_i*v(b).
3. Reduce this vector against the cumulative retained evaluation basis. If independent, retain its original monomial and vector and append it to the next frontier. Do not replace older retained monomials by arbitrary new spanning vectors.
4. If rank reaches m, stop immediately and set d*=d. Otherwise finish the entire degree round. An empty next frontier is a stable-span certificate; under the distinct-point contract it cannot occur at proper rank. Replace the current frontier by the next one.

Store an accepted monomial by a parent index and the coordinate multiplied; construct its exponent vector only when it is accepted. A dependent candidate gets no children. Each retained monomial is expanded at most once, so there are at most n*m candidate offers, even when d* is large.

## Why pruning preserves the degree filtration

**PM-IMPLICIT-B2.** At every completed round d, the retained monomials of degree at most d form a basis of V_d. The same holds if a round stops early at full rank.

Proof by induction. For d=0 this is V_0=K*1_m. For every d>=1,

    V_d = V_(d-1) + sum_(i=1..n) D_i V_(d-1).          (1)

By induction, substitute the retained basis of V_(d-1) in the right side. Every product D_i*v(b) of an older retained monomial of degree at most d-2 was already offered in an earlier round; whether accepted or discarded, it belongs to the cumulative span. Products of the remaining retained monomials, of degree d-1, are exactly this round's candidates. Thus after the round all of the right side of (1) lies in the retained span. Conversely every retained monomial has degree at most d, so the retained span lies in V_d. Retention preserves linear independence. If rank becomes m before the round finishes, its span is already K^m=V_d, so the same conclusion holds.

This proof is the justification for discarding descendants: it does not assume that an arbitrary basis of the final closure remembers total degree. Only a cumulative degree-ordered basis has the required invariant. Equal-degree dependencies cause no problem because all retained vectors used in that round have degree at most the candidate degree.

## Early plateau and the uniform degree bound

**PM-IMPLICIT-B3.** A completed round with V_d=V_(d-1) is already full rank. Hence d*<=m-1.

If equality occurs, (1) shows D_i V_(d-1) subset V_(d-1) for every coordinate. As it contains 1_m, this subspace contains the evaluation of every polynomial, by repeated multiplication. Distinct points ensure that polynomial evaluations span all of K^m: for each j and each k!=j choose a coordinate i(j,k) in which h_j and h_k differ and form

    ell_j(x) = product_(k!=j)
        (x_(i(j,k))-h_(k,i(j,k))) /
        (h_(j,i(j,k))-h_(k,i(j,k))).

All denominators are nonzero, deg(ell_j)<=m-1, and ell_j(h_k)=delta_(j,k). This works over finite fields too and uses no generic separating linear form. The stable span must therefore be K^m.

Before full rank, dimensions consequently increase by at least one per degree. Starting at dimension one at degree zero gives d*<=m-1. The univariate family of m distinct nodes has d*=m-1, so the bound is sharp whenever such nodes exist in K.

Checking only one new arbitrary vector is not a plateau test. A genuine plateau requires all coordinate products of a spanning basis (or, as above, the complete new frontier together with previously checked older products).

## Cardinal output and exact individual degree optimality

Let the retained monomials be b_1,...,b_m with degrees w_1,...,w_m, sorted in retention order, and let

    E_(j,k)=b_k(h_j),    C=E^(-1).

Define

    L_j(x)=sum_(k=1..m) C_(k,j)*b_k(x).

Then E*C=I gives L_j(h_i)=delta_(i,j). The maximum of their degrees is exactly d*, not merely at most d*: otherwise the lower-degree cardinal evaluations would already span K^m.

More strongly, for any prescribed value vector y in K^m define a=C*y. Since the retained basis is adapted to every V_d,

    y in V_d  iff  a_k=0 for every k with w_k>d.        (2)

Thus p_y=sum_k a_k*b_k is a minimum-degree polynomial with the prescribed evaluations, of degree max{w_k:a_k!=0} for y!=0. The zero function is represented by the zero polynomial. In particular

    degree_min(L_j)=max{w_k:C_(k,j)!=0}.

The retained monomials are distinct, so their formal highest-degree terms do not cancel in the displayed sparse expression.

## Compact verification and failure certificates

**PM-IMPLICIT-B4.** The construction provides primal cardinal and dual degree-obstruction certificates without an ambient monomial list.

Primal data are the retained monomials and C; verify their evaluations and E*C=I.

For filtered-spanning verification, provide coordinate transition columns

    T_i(:,k)=C*D_i*E(:,k).

They can be verified directly against raw coordinates. The crucial degree condition is

    T_i(j,k)=0 whenever w_j>w_k+1.                    (3)

Along with b_1=1 and the monomial degree labels, (3) proves by induction that every degree-at-most-d polynomial evaluation lies in the span of retained basis columns with w_k<=d. The opposite inclusion follows from the monomial degrees. For checking minimality at d*, only transitions out of basis elements of degree at most d*-2 are needed; providing all transitions is convenient and still polynomial size.

If a proposed budget d<d* is infeasible, choose a retained basis index k with w_k>d. The row lambda=C(k,:) is nonzero because lambda*E(:,k)=1, and it annihilates V_d. This is a nonzero evaluation dependence against every degree-at-most-d polynomial, not only against a supplied dictionary.

For an individual prescribed value vector y requiring degree delta>d, choose k with w_k>d and (C*y)_k!=0. Then lambda*y!=0 while lambda annihilates V_d, certifying impossibility of a lower-degree realization. The same applies to each individual cardinal vector y=e_j.

The transition-support certificate is important: a nonzero vector annihilating an arbitrary selected basis would not by itself certify annihilation of all low-degree monomials. Here the exact degree-safe spanning invariant, or its finite transition verification, supplies that missing implication.

## Cost and output conventions

Each offered vector D_i*v(b) costs O(m) field operations. Exact incremental elimination against at most m vectors of length m costs O(m^2) per offer. With at most n*m offers, total field arithmetic is O(n*m^3); inverting E costs O(m^3) more. Checking point distinctness costs O(n*m^2) field equalities in a direct implementation.

The base algorithm can use O(m^2+n*m) field elements/label storage aside from input and output, processing one candidate at a time. The output cardinal coefficients use m^2 field elements, with m exponent vectors of n entries each, all entries at most m-1. Full optional transition certificates use O(n*m^2) field elements and can be constructed and verified in O(n*m^3) arithmetic operations.

An accepted monomial may be stored initially as a parent-coordinate pair, so rejected candidate labels do not require copying n-entry exponent vectors. Expanding only the m final monomial labels costs O(n*m) label storage. The cardinal output must remain sparse or shared in these selected monomials; expanding an ambient coefficient tensor is neither needed nor promised.

For an arbitrary effective field, effectiveness alone gives no uniform polynomial bit-time guarantee in n,m independent of field-element encodings or arithmetic cost. The result is a polynomial field-operation algorithm. Bit complexity must additionally include input sizes and the chosen exact field implementation; no factorization or field-size/generic-position oracle is used.

## Consequence for the supplied source197 contract

Over a finite field of size q, compute d* directly from the raw hole points. Within PM-CONSTRUCTION-0002's square-output/total-degree architecture, an admissible cardinal construction with 2d<=q-2 exists exactly when

    2*d* <= q-2.

If this holds, the computed cardinal map supplies the punctured Gram -I_m and zero full-line Grams by the supplied theorem. If it fails, set d=floor((q-2)/2) and return an inverse-row evaluation dependence annihilating every allowed degree-at-most-d coordinate polynomial. This closes the implicit-generation gap for this point-interpolation grammar. It does not discover a new cancellation principle or remove that contract's degree/output restrictions.

## Classical baseline and boundaries

This is the core classical mechanism of Buchberger-Moeller point interpolation and the finite evaluation algebra K[x]/I(H) isomorphic to K^m: evaluate candidate monomials, retain independent quotient classes, and use multiplication by coordinates. The present output is only a degree-filtered evaluation basis/cardinal map with certificates, not necessarily a canonical Groebner basis or a staircase for a specified term order. The simple frontier tie order is not asserted to make every selected monomial divisor-closed. A degree-compatible admissible term order and additional relation bookkeeping give the familiar stronger BM-style setting; that stronger output is not required or proved here.

Parent is handling primary-source comparison. No independent external literature retrieval was made within this scope, and no historical originality claim follows from the proof or implementation.

Limits: distinct rational points are essential to the K^m/full-rank conclusion. Repeated points without derivative data give a proper diagonal evaluation algebra and genuine early plateau; multiplicity/Hermite interpolation needs a different input contract. Arbitrary circuits/rational representations, minimal support/cost, geometric changes of grammar, numerical stability, and universal bit complexity over arbitrary effective fields are not optimized or claimed.

## Actual commands and exact controls

Repository reads: rg for Gram/evaluation/implicit terms in CONSTRUCTION_CONTRACTS and RESEARCH_PROGRAM; sed of CONSTRUCTION_CONTRACTS lines 1-180; a bounded rg over existing mechanism/review/tool/test files for Buchberger/evaluation-algebra/implicit references. No current independent A/C note was read, and no repository file was modified.

Wrote own standard-library checker with apply_patch and ran:

    python /tmp/pm-implicit-b-check.py

Observed exit code 0, with these exact controls:

- Seven small rational/prime-field panels independently checked against ambient enumeration: singleton degree 0; five collinear rational nodes degree 4; rational square degree 2; off-line four-point panel with individual cardinal degrees [2,2,2,1]; F2 cube with ranks [1,4,7,8]; and F7 good/bad geometry panels.
- F7, degree budget 2, H+={(0,0),(1,0),(2,0),(0,1)}: generated cardinal degree 2, evaluated the full punctured Gram as -I_4, and checked all 56 full affine-line Grams are zero.
- F7, same budget, H-={(0,0),(1,0),(2,0),(3,0)}: minimum degree 3 and the exact obstruction lambda=[1,4,3,6], with x-moments [0,0,0,1] through degree 3. This excludes every degree-at-most-2 interpolation, not just chosen monomials.
- Implicit stress panel n=40,m=9, points (t,...,t), t=0,...,8 over Q: minimum degree 8, 281 candidate offers, versus 377348994 ambient degree-at-most-8 monomials. The ambient dictionary was not enumerated.
- Duplicate input was rejected by the explicit distinctness check.

Finite tests are exact implementation controls, not substitutes for the filtration/plateau/minimality proofs. No Lean verification, unseen transfer, specialist review, or new-tool/novelty claim is made.

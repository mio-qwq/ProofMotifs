# Additive preserver prior-art audit — 2026-10-18

**Task:** PM-AUDIT-20261018-C. Researcher: task-scoped independent adversarial/prior-art subagent. Sources accessed 2026-10-18. This records a bounded review, not an exhaustive historical search. Correctness review, formal verification and historical originality remain separate judgments.

## Finding and scope

The scalar-times-field-automorphism conclusion is classical once full quadratic-cone preservation has been obtained. The closest verified source found is Lester (1977), substantially closer than a comparison based only on the shape of the Carlitz–McConnel conclusion. The project must isolate and assess its passage from ternary cancellation-order data, which initially controls a punctured cone, to the full cone. Historical priority of that passage, the exceptional-field analysis and the constructive extractor has not been established.

## Sources actually read

1. J. A. Lester, *Cone Preserving Mappings for Quadratic Cones Over Arbitrary Fields*, Canadian Journal of Mathematics **29**(6) (1977), 1247–1253. DOI: [10.4153/CJM-1977-124-1](https://doi.org/10.4153/CJM-1977-124-1). Read the original seven-page publisher PDF, including the main theorem on p. 1247 and the proof: [full text](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0070F79946DFD05DAB130713B1C66529/S0008414X00025323a.pdf/cone_preserving_mappings_for_quadratic_cones_over_arbitrary_fields.pdf). The journal publication date is 1977; the publisher's later online date is not its priority date.
2. Chi Hoi Yip, *A strengthening of McConnel's theorem on permutations over finite fields*, arXiv:2407.21362v3, 18 October 2024. Read the introduction, Theorem 1.2 and its proof: [versioned full text](https://arxiv.org/html/2407.21362v3).
3. Marko Orel, *On Minkowski space and finite geometry*, arXiv:1410.1979v1, 8 October 2014. Read the relevant introduction and p. 23 discussion applying Lester to affine polar graph automorphisms: [full text](https://arxiv.org/pdf/1410.1979). This was a route to Lester, not a substitute for reading Lester's original theorem.

## Exact hypothesis comparison (paraphrased)

| Item | Lester's main theorem | Project's starting condition |
| --- | --- | --- |
| Field | Arbitrary field of characteristic different from two | Field of characteristic three; SC-005 initially treats finite fields |
| Space and form | Nonsingular symmetric metric vector space, dimension at least three, with a nonzero isotropic vector | Can use V=K^3 with B(x,y)=sum x_i y_i; its form is nonsingular, and (1,1,1) is isotropic in characteristic three |
| Map | Bijection f:V to V | Additive bijection T:K to K, lifted coordinatewise to F=(T,T,T) |
| Preservation | For every vertex a, f maps the entire cone C(a) onto C(f(a)), where C(a)={x:B(x-a,x-a)=0} | Cancellation orders imply preservation of a^2+b^2+c^2=0 initially only when all three directions are nonzero |
| Conclusion | f(x)=L(x)+f(0), with a semilinear bijection L and a nonzero similarity factor lambda satisfying B(Lx,Ly)=lambda sigma(B(x,y)) | Once the full-cone hypothesis is justified, the coordinatewise restriction gives T(x)=T(1)sigma(x) |

The implication in the last row is conditional on repairing the missing cone data. If full cone preservation is available, apply Lester to F. Since F(0)=0, the translation term vanishes. Semilinearity on a coordinate axis gives T(r)=sigma(r)T(1). For finite K=F_(3^m), field automorphisms are Frobenius powers, recovering the familiar scalar-Frobenius form. This conclusion must not be presented as a new field-automorphism classification.

The elementary alternative after the project has proved square preservation is equally classical: normalize S=T/T(1), use additivity and S(x^2)=S(x)^2, and polarize (x+y)^2 to obtain multiplicativity. Lester supplies a broader geometric precedent; using that theorem is unnecessary for completing this elementary last step.

## Why Lester cannot be invoked directly from the starting hypothesis

Let K=F_9=F_3[i], i^2=-1, and define the additive bijection T(1)=1, T(i)=1+i. SC-005 proves that it preserves all ternary cancellation orders. Nevertheless,

    Q(0,1,i)=0,
    Q(T(0),T(1),T(i))=1+(1+i)^2=1-i != 0.

Thus it fails full-cone preservation. The missing zero-coordinate information is a real logical gap in any attempted direct application of Lester. This example does not contradict Lester, because its hypothesis is not satisfied.

## Project content requiring separate assessment

The project-specific chain to retain explicitly is:

1. The characteristic-three ternary ordinary-moment classification relates order five versus higher order to a^2+b^2+c^2, for nonzero directions.
2. The parameterized conic family converts the punctured-cone condition into the defect identity D_T(t)=T(1)T(t^2)-T(t)^2 at admissible parameters.
3. A finite-field polynomial root bound, or the separately reviewed arbitrary-field quadratic-defect repair, extends that identity beyond the omitted parameters; K=F_9 is exceptional.
4. The defect can be used to produce and certify a concrete order-seven to order-five witness for maps outside the scalar-automorphism class.

These are precise mathematical objects for further comparison. This audit found no source establishing their historical novelty and no source yet verified as directly containing the exact punctured-cone bridge, exceptional-field statement or extractor. An unsuccessful bounded search cannot establish originality. Retain NOVELTY_UNVERIFIED and no claim of a new general theory, public-conjecture resolution or independent publication value.

## Carlitz–McConnel / Yip relationship

Yip's Theorem 1.2 assumes a finite field F_q, a set D contained in F_q^*, and a function f such that every difference quotient (f(x)-f(y))/(x-y), for x!=y, belongs to D. Its quantitative assumption is |D D^(-1) D^(-1)| <= (q+1)/2. It concludes f(x)=a*x^(p^j)+b. A proper multiplicative subgroup D recovers McConnel's hypothesis.

The project has not independently derived this difference-quotient hypothesis from ternary-order preservation. Consequently, the similar conclusion alone does not make Yip or McConnel a direct proof of SC-005. Once square preservation is known, polarization already gives the needed algebraic classification, so a Carlitz reduction at that stage would add little.

## Relevant lead not fully inspected

B. Kuzma and M. Orel, *Additive mappings on symmetric matrices*, Linear Algebra and its Applications **418**(1) (2006), 277–291, DOI: [10.1016/j.laa.2006.02.010](https://doi.org/10.1016/j.laa.2006.02.010). Author bibliography and publisher metadata were located; the full theorem text was inaccessible through the available retrieval route. Do not assert its precise assumptions or that it directly implies the project's punctured-cone result. Rank-one symmetric-matrix preservers remain a useful follow-up search direction.

## Adversarial-review outcome and next operation

No correctness gap was found in SC-005's q>=27 root-bound proof, small-field arguments, treatment of zero directions, or distinction between formal polynomials and polynomial functions. This is independent review by an actual task-scoped AI subagent; it is not human review or Lean verification. The subsequently communicated quadratic-defect repair is consistent with the identity D_T(t+u)+D_T(t-u)=-D_T(t)-D_T(u) and with the F_9 exception.

Next: compare the exact punctured-cone extension lemma and constructive witness procedure against additive conic preservers, cone-preserver weakenings and rank-one symmetric-matrix preservers. Preserve the explicit F_9 counterexample in any such reduction. No broadening of historical-originality claims is warranted by this audit.

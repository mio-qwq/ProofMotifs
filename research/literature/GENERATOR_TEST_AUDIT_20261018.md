# Generator test: bounded mathematical and prior-art audit

Date: 2026-10-18. Task: PM-SC007-C. Independent task-scoped AI adversarial/prior-art researcher. Read AGENTS.md and SC-006 before this review. This is a bounded audit, not an exhaustive priority search or formal verification.

## Statement independently checked

Let K=F_(3^m), m>=2, and let (1,alpha,...,alpha^(m-1)) be a genuine F_3-power basis. Let T be an additive bijection, A=T(1), S=T/A, and Q(t)=A*T(t^2)-T(t)^2. The proposed 2m-3 test parameters are

    alpha;
    alpha^k, alpha+alpha^k, for 2<=k<=m-1.

If Q vanishes at all these points, S is a field automorphism. No correctness gap was found in the following argument.

Write H(x,y)=S(x*y)-S(x)*S(y). Additivity makes H F_3-bilinear. H(alpha,1)=0 follows from S(1)=1. The alpha test gives H(alpha,alpha)=0. The other tests and quadratic polarization give H(alpha,alpha^k)=0 for 2<=k<=m-1. The power basis therefore gives

    S(alpha*x)=beta*S(x) for every x in K, where beta=S(alpha).

Iterating gives S(alpha^k)=beta^k. Crucially, the last basis vector alpha^(m-1) gives the closure equality S(alpha^m)=beta^m as well. Applying S to the degree-m defining relation f(alpha)=0 yields f(beta)=0. Evaluation alpha->beta is consequently a well-defined homomorphism of F_3[X]/(f). Its values on the basis coincide with S, so S is that homomorphism, and hence an automorphism. This is the classical generator-image/defining-relation principle. The tests encode it using the project's special quadratic defect.

## Explicit closure counterexample

Use K=F_3[alpha] with alpha^3=alpha+2, so f(X)=X^3+2X+1. Put beta=alpha^2, and define S by F_3-linearity from

    S(1)=1,
    S(alpha)=alpha^2,
    S(alpha^2)=alpha^4=alpha^2+2*alpha.

The displayed images form a basis, so S is bijective. It passes Q(alpha)=0, but

    f(beta)=alpha+2 != 0.

Thus S is not a field automorphism. Merely obtaining consistent images through alpha^(m-1) does not prove that the defining relation is respected. The endpoint k=m-1 generator-row relation repairs precisely this gap. This counterexample challenges an incomplete proof, not the full proposed test.

## Necessary scope restrictions

* The power-basis hypothesis is essential. A generator of a proper subfield is insufficient: an arbitrary nonmultiplicative F_9-linear bijection fixing 1 in a larger field fixes every tested parameter when alpha belongs to F_9. For example, in K=F_9[u], u^2=d for a nonsquare d in F_9, the map x+y*u -> x+y*(u+1) is such a bijection and is not multiplicative.
* A field generator of degree m suffices; a generator of the entire multiplicative group is a stronger, unnecessary assumption.
* This is not a hitting set for general F_3-quadratic maps. For m>=4, in coordinates relative to (1,alpha,alpha^2,alpha^3,...), the nonzero quadratic form x_2*x_3 vanishes at all listed test parameters. The proof depends on the multiplicativity-defect form of Q.
* The 2m-3 bound needs m>=2. Degree one is a separate trivial case. At m=2 the single alpha test certifies the scalar-automorphism class, but an order-changing ternary witness still cannot exist in the exceptional field F_9.
* The count is a sufficient test size, not a minimality result. The listed points are distinct for a genuine power basis because equality between two would give a nonzero polynomial relation of degree less than m.

## Query model and classical direct recognition

The bound counts evaluations of Q and improves the project's previous full-quadratic-basis test in that model. It does not establish an optimal query bound for a directly accessible additive-map oracle T. Querying T on m basis vectors determines T completely. Normalize those images, compare the images of powers with powers of beta, and check f(beta)=0. That is already a linear-number-of-T-calls recognition procedure based on classical finite-field representation. Arithmetic costs, basis construction, generator validation and conversions must be accounted for separately. The new statement should be described as a concrete defect-query certificate, not unprecedented linear-time field-homomorphism recognition.

## Primary sources actually read

All URLs below were accessed on 2026-10-18. These are official computational-algebra documentation and establish classical background, not historical priority for the exact test set.

1. [Magma Handbook: finite-field creation](https://docs.magma-maths.org/BasicRings/FiniteFields/creation.html). Read `Embed(E,F,x)`, Homomorphisms, `F.1`, `Generator`, and `PrimitiveElement`. The embedding constructor requires the image of the source generator to be a root of the defining polynomial. The homomorphism constructor specifies a map by one generator image, but expressly leaves validity to the user. The documentation distinguishes a field generator from a multiplicative primitive element. It does not assert the project's exact defect-query theorem.
2. [Magma Handbook: finite-field structure operations](https://docs.magma-maths.org/BasicRings/FiniteFields/operation.html). Read `VectorSpace(F,E)`, `MatrixAlgebra(F,E)` and defining-polynomial operations. The field-vector-space correspondence uses a power basis; the field's matrix algebra is generated by the companion matrix of its defining polynomial. This supplies a classical multiplication-generator interpretation of the intertwining equation above.
3. [GAP Reference Manual, Chapter 62, section 62.10](https://gap-system.github.io/gap/doc/ref/chap62.html). Read the distinction between linear maps and algebra homomorphisms, and the checked and unchecked constructors by generator images. The checked constructor verifies generation and existence of the homomorphism; the unchecked constructor assumes both. This supports treating closure/relations as an actual condition rather than an automatic consequence of generator-image specification.

No verified source stating the exact 2m-3 Q-evaluation certificate was found in this bounded search. Absence of a retrieved match is not evidence of originality. Retain NOVELTY_UNVERIFIED; no first-result, exact-optimum, publication-value or new-theory claim follows from this source search. The additional restricted-model lower bound reviewed below is a separate mathematical conclusion.

## Independent review of a deterministic Q-only lower bound

The following adversary argument is accepted under its explicitly restricted model. The input promise is an additive bijection on K=F_(3^m), m>=3, and the decision problem is whether its defect Q is identically zero, equivalently whether it is scalar-Frobenius. Both positive and negative inputs must be permitted. A deterministic adaptive algorithm receives only values of Q at parameters of its choice, together with fixed field/generator metadata independent of the unknown map. It receives no matrix, basis images, direct T access or other map-dependent side information. The lower bound already holds in the normalized subclass T(1)=1, so disclosing that normalization does not evade it.

Run the algorithm on the identity map's all-zero transcript. After s queries t_1,...,t_s, let

    U=span_F3{1,t_1,t_1^2,...,t_s,t_s^2}.

If 1+2s<m, this span is proper. Choose a nonzero F_3-linear functional phi:K->F_3 annihilating U and define

    S(x)=x+phi(x),

where F_3 is embedded in K. Since 1 belongs to U, phi(1)=0. Thus N(x)=phi(x) has N^2=0, and I+N is a bijection with inverse I-N. S is additive and unital, and fixes U pointwise. Consequently its defect answers at all queried points are exactly

    Q_S(t_i)=S(t_i^2)-S(t_i)^2=t_i^2-t_i^2=0.

This S is not a field automorphism. Its fixed space is ker(phi), of dimension m-1, and it is not the identity because phi is nonzero. A nonidentity Frobenius power on F_(3^m) has fixed-space dimension gcd(m,j)<=m/2<m-1 for m>=3. Unitality also excludes a nontrivial scalar factor. Hence S is a valid negative input with the identical observed transcript.

Adaptivity does not invalidate the construction: once S is selected, the same earlier zero answers inductively force the same later queries and the same output. A correct recognizer cannot terminate positively on that identity transcript while 1+2s<m. Its worst-case number of Q evaluations is therefore at least

    ceil((m-1)/2)=floor(m/2).

Combined with the admissible 2m-3 upper bound in SC-007, this establishes Theta(m) deterministic Q-evaluation complexity in this model, up to constants. It does not establish an exact optimum, a randomized lower bound, bit complexity, or a lower bound for inputs supplied through T-images or matrices. The lower bound is for recognition with both answer classes possible; it cannot be transferred without another argument to a witness-only task whose promise already excludes every automorphism.

The argument was independently checked algebraically by this audit researcher. Its historical originality has not been assessed by a dedicated source search; retain NOVELTY_UNVERIFIED. The asymptotic lower bound concerns a particular oracle model and is not a new general finite-field or quadratic-map classification claim.

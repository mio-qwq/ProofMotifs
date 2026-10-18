# PM-CYCLE11-C: normal elements and three quadratic signs

Bounded literature gate, 2026-10-18. Two Parallel Search rounds, then primary-document fetches. No matching all-degree normal-plus-three-sign existence theorem was established by this search. This is not evidence of novelty.

## Sources actually read

1. Trevor Hyde, *Normal Elements in Finite Fields*, arXiv:1809.02155v1, 6 September 2018, Theorem 1 and proof.
   https://arxiv.org/html/1809.02155v1
   Counts normal elements by units in F_q[T]/(T^n-1). The factor product uses distinct irreducibles, explicitly including n=d p^a and T^n-1=(T^d-1)^(p^a). Therefore repeated factors when 3 divides the extension degree do not obstruct the ordinary normal-indicator framework. The fetch metadata incorrectly labeled the HTML as 2026; the document itself says 2018.

2. Kaustav Chatterjee, Hariom Sharma, Aastha Shukla, Shailesh Kumar Tiwari, *Arithmetic progression in a finite field with prescribed norms*, arXiv:2401.01819v1, 3 January 2024.
   https://arxiv.org/pdf/2401.01819v1
   Section 3 gives the polynomial-Mobius normal indicator; Lemma 3.2 reproduces a mixed character-sum bound attributed to Fu and Wan, *A class of incomplete character sums*, Q. J. Math. 65(4) (2014), 1195–1211, Theorem 5.6. Its constant is D1+D2+D3+D4-1, with D1 the sum of distinct irreducible-factor degrees of the multiplicative argument, D2=max(deg g,0), D3 denominator degree of g, D4 denominator factors not already counted. For split squarefree quadratic f and nonzero linear g, this is 2 sqrt(Q). The cited original Fu–Wan paper was not independently fetched. The source's general additive-degeneracy wording should not be exported without checking the original theorem; linear g has no Artin–Schreier degeneracy by its pole order.

   The paper studies arithmetic progressions with all entries primitive and at least one normal, with prescribed norms and progression length at most the characteristic. Its exhaustive characteristic-three statement is for two entries, not three. Theorem 4.1's sufficient inequality suffered missing superscripts in fetched text, so it is not used here. In particular, do not infer the desired all-m assertion from its title.

3. Arpan Chandra Mazumder, Giorgos Kapetanakis, Dhiren Kumar Basnet, *Normal and primitive normal elements with prescribed traces in intermediate extensions of finite fields*, arXiv:2510.14840v1 (2025), Section 2.2.
   https://arxiv.org/html/2510.14840v1
   Gives the standard normal indicator with polynomial Mobius coefficients, normality equivalent to full F_q-order, and count of additive characters of each order. Its trace prescription results do not prescribe three shifted quadratic characters.

4. Stephen D. Cohen, Tomas Oliveira e Silva, Tim Trudgian, *On consecutive primitive elements in a finite field*, arXiv:1410.6210v1, 22 October 2014.
   https://arxiv.org/pdf/1410.6210v1
   Three consecutive primitive elements exist for every odd prime power Q>169. There are eleven exceptions below this threshold, including Q=3,9,81. Primitive entries all have quadratic character -1, but this theorem imposes no normality. Thus it proves the unweighted sign pattern eventually, not its intersection with normal elements.

## Explicit classical bound application (independent derivation for root review)

Let Q=3^m, m>1, F=T^m-1, Theta=Phi(F)/Q, W=2^(number of distinct irreducible factors of F). For any y outside F3, the indicator of equal, nonzero quadratic signs at y-1,y,y+1 is

I(y) = [1 + chi(y(y-1)) + chi(y(y+1)) + chi((y-1)(y+1))]/4.

Every normal y is outside F3, so this identity can be multiplied by the normal indicator and summed over the entire field without deleting exceptional points. For each of the three quadratics, the untwisted sum is exactly -1. For each nontrivial additive character, the additive-linear term alone sums to zero and each mixed quadratic sum is bounded by 2 sqrt(Q). In the normal indicator, the total absolute coefficient mass of nontrivial additive characters, before the external Theta, is W-1: for every squarefree divisor D there are Phi(D) characters and coefficient magnitude 1/Phi(D).

Consequently the number R_m of admissible normal y satisfies

R_m >= Theta/4 * [Q - 3 - 6(W-1) sqrt(Q)].

This is a routine application of classical normal-character and mixed-Weil machinery; no historical originality is claimed. It handles 3|m using the radical factor count W, without asserting that T^m-1 is squarefree. It is useful exactly when the displayed bracket is positive. For m=13, T^13-1 has one linear and four cubic irreducible factors over F3, so W=32; the bracket is positive. For m=3, W=2 and the bracket is negative, so this inequality correctly makes no assertion in that obstructed small degree.

Missing steps relative to PM-QUESTION-0001: admissible normal y avoids nonzero cubic linearized obstructions, but this count neither proves connectivity of the transformed seed nor controls every higher-digit-weight frequency. It cannot prove a full-code single orbit by itself. Small degrees not certified by the bound require separate analysis, not a claim of uniform existence.

## Retrieval limitations and stopped routes

The first search included various broad character-sum and consecutive-primitive papers with no matching normality restriction. The second located the above primary candidates. Wan's author publication list and a general exponential-sums survey were fetched while seeking the original Fu–Wan theorem; the author list did not provide that paper. No additional search round was performed. Generic primitive-normal basis theorems and generic consecutive primitive-root theorems cannot be combined by assuming their witness sets intersect.

# PM-CYCLE10-C: differential spectra as a bad-frequency exclusion tool

Date: 18 October 2026. Scope: bounded primary-source comparison for
PM-QUESTION-0001. No shared repository files or remote refs modified.
Decision: no uniform single-orbit existence theorem located. There is a
concrete useful connection to differential uniformity and ternary cyclic
minimum-distance criteria. Originality remains unverified.

## Exact reduction (independently derived)

Write q=3^m, S=(F_q^*)^2, N=(q-1)/2, and

 A={a in S: b=-1-a in S, 1,a,b pairwise distinct}.

For frequency k mod N choose a positive lift e congruent to k mod N.
Let B_k={a in A: 1+a^e+(-1-a)^e=0}. Its definition is independent
of the lift because all three elements belong to S.

* For e odd, the equation is (a+1)^e-a^e=1: an ordinary differential
  equation for x^e.
* For e even, the equation is (a+1)^e+a^e=-1: the c=-1 differential
  equation for x^e.

The restrictions a,b in S matter. Unrestricted differential results
can bound this restricted set; a count for one quadratic-character
case is not automatically a count for all cases.

The transformations a -> -1-a and a -> 1/a generate the six
normalizations of the unordered triple {1,a,b}. They preserve A and
B_k (the second transformation multiplies the power sum by a^(-e)).
The action is free: transposition fixed points are excluded values;
3-cycle fixed points satisfy a^2+a+1=(a-1)^2=0. Thus

 |B_k| is divisible by 6.

This converts small differential bounds into an empty bad set:

* If e is even and the c=-1 differential uniformity of x^e is <=6,
  then B_k is empty. The unrestricted equation at output -1 already
  has the root x=1, leaving at most five admissible roots.
* If e is odd and ordinary differential uniformity is <=8, then B_k
  is empty. The unrestricted equation at output 1 already has the
  three distinct roots x=0,-1,1, leaving at most five admissible roots.

These are elementary consequences, not assertions that the cited
papers state these particular restricted-square conclusions.
In particular an odd APN or odd PN monomial cannot be used here:
those three unavoidable roots already prohibit uniformity 1 or 2.

The entirely elementary quadratic-frequency exclusion is stronger
than needing a PN condition for a single monomial:

 1+X^(3^r+3^s)+(-1-X)^(3^r+3^s)
   = -(X-1)^(3^r+3^s) in F_3[X].

Hence every nondegenerate seed avoids every frequency congruent
modulo N to 3^r+3^s. This identity follows by expanding the two
Frobenius factors and is classical quadratic-function behavior.

## Sources actually read and exact comparisons

1. Haode Yan, *On -1-differential uniformity of ternary APN power
   functions*, arXiv:2101.10543v1, 26 January 2021.
   https://arxiv.org/html/2101.10543v1

   Definition 1 uses D_c,a F(x)=F(x+a)-cF(x), and defines its
   maximum fiber cardinality. This body definition is the one used
   here; the abstract's F(cx) notation must not replace it.
   Lemma 1 reduces power-function uniformity to the a=1 fibers plus
   gcd(e,q-1). Theorem 4.1: for m odd and
   e=(3^m+1)/4+(3^m-1)/2, the c=-1 uniformity is at most four.
   Its exponent is even, so the preceding sixfold argument proves
   B_k empty for k=(q+1)/4 mod N. This is inverse 2 modulo odd N.
   This exclusion also has a short independent proof: the power
   map x->x^k is the inverse of squaring on S; a transformed
   zero-sum distinct triple would contradict the quadratic identity.

   Other bounds in this source are not transferred without checking
   parity: Theorems 2.1 and 3.1 have c=-1 bounds at most two for
   certain odd exponents, whereas odd-exponent B_k uses the ordinary
   differential, not the c=-1 differential. They cannot be inserted
   into the even-exponent criterion merely because the numerical
   bound is small.

2. Nian Li, Chunlei Li, Tor Helleseth, Cunsheng Ding, Xiaohu Tang,
   *Optimal Ternary Cyclic Codes with Minimum Distance Four and Five*,
   arXiv:1309.1218v1, 5 September 2013.
   https://arxiv.org/html/1309.1218v1

   Theorem 1, attributed there to Ding--Helleseth [5, Theorem 4.1],
   assumes e outside the 3-cyclotomic coset of 1 modulo q-1 and
   |C_e|=m. It characterizes parameters [q-1,q-1-2m,4] of the
   two-zero cyclic code by three conditions: e even; the equation
   (x+1)^e+x^e+1=0 has only x=1; and
   (x+1)^e-x^e-1=0 has only x=0.

   The second condition is exactly the unrestricted equation for
   our even-exponent B_k. Thus a source theorem verifying it proves
   a bad set empty. The differing code length q-1 versus N prevents
   importing their minimum-distance statement as the desired
   single-orbit theorem, but does NOT prevent this exact equation
   transfer. This is a more useful reading than dismissing the
   entire paper solely because the code lengths differ.

3. Gaofei Wu, Zhuohui You, Zhengbang Zha, Yuqing Zhang,
   *Several new classes of optimal ternary cyclic codes with two or
   three zeros*, arXiv:2407.07332v1, 10 July 2024.
   https://arxiv.org/html/2407.07332v1
   https://arxiv.org/abs/2407.07332

   Theorem 4: m odd, e even,
   e(3^h-1) congruent to (3^m+1)/2 modulo q-1,
   1<=h<=m-1, and gcd(q-1,3^h-2)=1 imply the code C_(1,e)
   has parameters [q-1,q-2m-1,4]. Its proof explicitly reduces
   the question to excluding solutions outside F_3 to
   (1+x)^e = plus or minus (x^e+1). The minus sign is precisely
   our bad equation. Therefore these stated hypotheses imply an
   empty restricted B_k. Neither this nor the singleton-fiber
   condition selects one seed avoiding every remaining frequency.

## Bounded search record

Parallel Search was used with model_name omitted (no trusted exact
active model slug). Session session_f6bc3270b107261625a9c12cf835feeb.
Two targeted rounds only, followed by full-content primary-source
fetches for the three versions above.

Round 1, search_f6bc3270b107261625a9c12cf835feeb:

* ternary cyclic codes monomial equation minimum distance four planar
* ternary cyclic codes weight three power mapping APN equations
* cyclic Hamming code weight three cyclic generator

Round 2, search_3230862f6baa5fb52983133068e76dbf:

* ternary Hamming code single minimum weight cyclic generator
* even like Hamming code weight three generator
* Singer orbit affine lines incidence rank cyclic ternary

The second round was weak: generic Hamming-code teaching material,
unrelated graph/code hits, and projective-plane incidence papers.
No matching one-weight-three-orbit generation theorem was found in
the inspected results. This is bounded unresolved coverage, not a
novelty conclusion. No secondary search descriptions are theorem
dependencies.

## Useful next mathematical operation

Before a simultaneous-cover calculation, remove empty B_k proved
by the quadratic identity, inverse-power equivalences, or verified
low-differential families. Group frequencies under Frobenius and
seed normalization. A claimed application of any published bound
must retain the parity of a q-1 lift and square-character restrictions.
What remains is still a simultaneous avoidance problem, not a
collection of independent minimum-distance assertions.

All mathematical reductions above were derived by this agent and
need coordinator/independent acceptance before entering CLAIMS.
No Lean formalization or human peer review is claimed.

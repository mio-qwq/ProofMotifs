# A bounded prior-art gate for a single cyclic edge orbit

Date: 18 October 2026. Task: PM-CYCLE9-C. Scope: PM-QUESTION-0001.
Decision: **the general single-orbit assertion remains unresolved here**.
No inspected primary theorem supplies it. This bounded search does not
establish historical originality, and the cyclic-code translation itself
is classical.

## Exact target and assumptions

Let q=3^m, m>=3, S=(F_q^*)^2, N=(q-1)/2, and gamma generate S.
The established full incidence code is

`C = <D> in F_3[Z]/(Z^N-1), D=(Z-1) M_gamma(Z)`.

Here M_gamma has degree m, so dim(C)=N-m-1. The question is whether
there is a distinct zero-sum triple `{1,gamma^i,gamma^j}` whose indicator
`p=1+Z^i+Z^j` satisfies `gcd(p,Z^N-1)=D`.
The question concerns existence of at least one suitable triple for every
m; it does not assert that every triple works. SC-011 already supplies a
counterexample to that stronger assertion in F_81.

This review used the repository's SC-011 proof as available evidence and
searched independently for a published theorem that settles the uniform
question. It did not rerun the repository's finite certificates, change
their acceptance status, or inspect all coding literature.

## Sources actually inspected

All links below were accessed on 18 October 2026. Author papers and
official software documentation supply the evidence; search-result
aggregators are not mathematical authorities.

| Primary source/version | Actual relevant assertion | Why it does not settle the target |
| --- | --- | --- |
| Nian Li, Chunlei Li, Tor Helleseth, Cunsheng Ding and Xiaohu Tang, *Optimal Ternary Cyclic Codes with Minimum Distance Four and Five*, [arXiv:1309.1218v1](https://arxiv.org/html/1309.1218v1), submitted 5 September 2013 | Introduction gives the principal-ideal description of cyclic codes. Sections IV/V study codes of length 3^m-1 with several prescribed zeros and minimum distance four or five. | The length and defining set differ; those distance claims exclude weight-three words in those codes. They do not provide a weight-three generator for our length-N code. |
| Minjia Shi and Denis S. Krotov, *An enumeration of 1-perfect ternary codes*, [arXiv:2110.06305v3](https://arxiv.org/html/2110.06305v3), author final version dated 8 April 2023 | Studies ternary perfect codes with Hamming length (3^m-1)/2; the check-matrix discussion uses non-collinear projective columns. | The paper concerns classification/enumeration of perfect codes and their ranks; the inspected statements do not give a minimum-weight word whose cyclic shifts generate our even-like subcode. |
| SageMath, [official CyclicCode documentation](https://doc.sagemath.org/html/en/reference/coding/sage/coding/cyclic_code.html), live documentation accessed 18 October 2026 | Defining sets describe roots of the generator; a cyclic generator is obtained as the gcd of polynomial representatives of all codewords. | Gcd of a collection is not the assertion that one member of the collection has that gcd. This is classical infrastructure, not a sparse-generator existence theorem. |

The arXiv landing page [1309.1218](https://arxiv.org/abs/1309.1218)
was separately checked for the original 2013 date: an extraction service
labelled the HTML with a 2026 date, which must not be treated as the paper's
submission date. The version identifier, not that extraction label, is
used above.

Search leads also included Bao--Zou, arXiv:2601.12427v1; Wu--You--Zha--Zhang,
arXiv:2407.07332; and Liu--Luo, arXiv:1303.0503. Their retrieved descriptions
concern other defining sets or weight distributions. They were not promoted
to theorem dependencies or claimed as exhaustive exclusions.

## Three distinctions that prevent a false positive

### 1. Principal generation does not imply a weight-three generator

Since 3 does not divide N, h=Z^N-1 is squarefree. For every valid seed,
write p=D*a. Then

`gcd(h,p)=D  iff  gcd(h/D,a)=1`.

Equivalently, a must be a unit in `F_3[Z]/(h/D)`. The fact that all valid
seeds together generate C means that their a's collectively generate the
unit ideal. It does not imply that any individual a is a unit.
For example, in the semisimple ring `F_3 x F_3`, the two elements `(1,0)`
and `(0,1)` generate the whole ring together and neither is a unit.
This abstract example is not a counterexample to PM-QUESTION-0001; it
identifies the invalid inference a general proof must avoid.

Likewise, a weight distribution counts codewords by support size, but
does not by itself identify the cyclic span of an individual word.

### 2. The Hamming-code identification depends on parity of m

If m is odd, -1 is nonsquare. Consequently S contains exactly one
representative of each pair `{x,-x}` of nonzero vectors. The m-by-N matrix
whose columns are S is a ternary Hamming check matrix, and its kernel is
the cyclic code `<M_gamma>`. Adding the all-one parity row cuts this to C.
Thus C is its even-like subcode, where "even-like" means coordinate sum
zero, not even Hamming weight.

For a word of weight three over F_3, coordinate sum zero forces the three
nonzero coefficients to be all 1 or all 2. Hence weight-three words in C
are exactly nonzero scalar multiples of the edge indicators in this odd-m
presentation. The target therefore becomes a precise sparse cyclic
generator question for this even-like Hamming subcode.

If m is even, -1 is square. S contains both x and -x when it contains x,
and misses the other projective points. Its columns are not a Hamming
check matrix: opposite columns already give a weight-two word in
`<M_gamma>`. Adding the all-one row removes that word but does not restore
the projective-column premise. An odd-m Hamming theorem cannot silently
be applied to even m.

The affine kernel is a restriction of the first-order affine evaluation
code to S. It is not automatically a standard projective Reed--Muller
code: evaluation of degree-one functions depends on the chosen scalar
representative of a projective point.

### 3. Full projective lines are different incidence blocks

An affine F_3 line has three points; a projective F_3 line has four.
Our blocks are three-element affine lines entirely contained in S.
Even in the odd-m projective representative picture, their indicators
are not the indicators of full projective lines. A theorem about a Singer
orbit of full projective lines requires an additional identification and
rank argument before it can settle this question. The present bounded
search located no theorem with those matching hypotheses.

## Search record and research decision

Two related query rounds used Parallel Search. Round one covered ternary
weight-three cyclic words, cyclic line incidence, and quadratic-residue
zero-sum triples. Round two covered even-like ternary Hamming codes and
Singer cyclic incidence ranks. An additional search-service batch was
unhelpful: it returned largely unrelated literal-word matches, so it adds
no mathematical evidence. The relevant paper versions and Sage
documentation were then fetched for actual statement comparison.

Stop condition: no matching theorem after the two substantive rounds.
This is **unresolved prior-art coverage**, not a claim of a new conjecture
or a historically new code family. No theorem of existence or nonexistence
has been accepted from this literature task, and no formal verification or
human review is asserted.

The next useful mathematical operation is to test or prove whether the
restricted family of quotients `a=p/D` contains a unit modulo h/D, rather
than reprove the principal-ideal theorem. A valid negative result must
show that every legitimate seed misses some additional spectral factor;
a valid positive proof must select one seed avoiding all such factors
simultaneously. Finite examples, collectively spanning edge sets, and
separate avoidance of each factor are insufficient substitutes. A small
negative instance with a complete factor-covering certificate would
resolve the project question and be more valuable than unguided further
enumeration of positive instances.

Handoff: coordinator integrates this single new literature file; no
shared-state files, code, commits, remote refs or other projects were
modified by this task.

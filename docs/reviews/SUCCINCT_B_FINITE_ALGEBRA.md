# PM finite-algebra bounded implementation — independent handoff

Task: implement and exactly challenge the proposed finite constant-field algebra mechanism. Repository was read-only; this task wrote only `/tmp/pm-finite-algebra.py` and this report. No family116 source/proof or agent-A/C review notes were read. This is implementation/evidence for a candidate proposition, not a novelty claim or formal verification.

## Contract and mechanism

Input: a tuple `V_i=P_i(t)/delta(t)` of explicit square univariate rational matrices over Q or a promised prime field Fp, one common polynomial denominator with `delta(0)!=0`, and an explicit positive integer budget D. Let `b=max(deg(delta),max_entry deg(P_i))` (zero polynomial represented with degree 0 for this harmless upper bound). The intended promise is `dim_K K<V_i> <= D`, with the unital algebra including I.

The code keeps **actual generator words**, starting with I. A word of length ell is stored as a polynomial matrix numerator over `delta^ell`. To test constant-field dependence among several words, it clears all denominators to `delta^L`, where L is the largest word length in that test, flattens every polynomial matrix entry into its complete coefficient vector, and solves the resulting scalar equations over K. It never computes rank over K(t). At the first D+1 independent retained words it returns `rank_budget_exceeded`. It never runs an unbounded search and never interprets that outcome as a proof of infinitude.

If the queue finishes with d words, the output contains constant coefficients for

`I = sum_k initial_k B_k`, and `B_j V_i = sum_k C[j][i][k] B_k`.

The independent checker recomputes the word matrices, uses a separately written row-rank calculation, and verifies every coefficient identity after clearing denominators. It requires C entries to be actual scalar ints/Fractions; a polynomial coefficient such as `[0,1]` representing t is rejected before any identity comparison. This matters because permitting K(t) coefficients would make scalar V=t spuriously look one-dimensional.

## Proof notes independently derived

**FA-B1, bounded closure correctness.** Every retained matrix belongs to the generated algebra. If the queue closes, its K-span contains I and is invariant under right multiplication by every generator. Thus it contains every generator word by induction, and is exactly the algebra. The independent retained matrices are a basis, and d is its K-dimension. Every retained word's prefixes were retained, so each word length is at most d-1. If D+1 independent words are found, the only warranted conclusion is `dim_K algebra > D`. The code demonstrates this outcome on an algebra of finite dimension 4 with D=3, not just on infinite examples.

**FA-B2, faithful finite jets.** For a closed d-dimensional algebra, set `Delta=delta^(d-1)` and `E=1+(d-1)b`. Multiplying any retained word B_j by Delta gives a polynomial matrix of degree at most `(d-1)b=E-1`, because its word length is at most d-1. Every element of the algebra is a constant-field linear combination of the B_j, hence has the same denominator Delta and numerator degree bound. If such an element has zero jet modulo t^E, then multiplying its formal expansion by Delta still gives zero modulo t^E. Its numerator has degree below E, so that numerator is zero. Thus truncation into `M_n(K[t]/(t^E))` is injective on the whole algebra, not merely on polynomials of bounded word length. It is an algebra homomorphism because delta is a unit at the origin.

**FA-B3, arbitrary extension.** The same argument holds after any field extension L/K: the constant basis remains independent (a finite coefficient-matrix nonzero minor stays nonzero), all closure constants remain valid, delta(0) remains nonzero, and the same numerator degree bound holds for every L-linear combination. Therefore the jet map remains injective on the extended algebra, and detects every `f(V)` with coefficients in L. This is a mathematical proof; the executable tests Q/F2/F3 only, not arbitrary extension implementations.

**FA-B4, no jet-plateau inference.** For `V=t^M E12`, the algebra is span_K{I,V}, of dimension 2. All jet orders E<=M collapse V to zero; order M+1 is necessary and sufficient. Therefore a long plateau of jet ranks does not certify closure or fidelity. Dimension d alone cannot bound the required jet order independently of input degrees.

Resource qualification: the word-generation portion offers at most `1+gD` candidates, with at most D+1 retained words, candidate lengths at most D, and cleared numerator degrees O(Db), where g is the number of generators. The exact scalar systems have polynomial dimensions in n, g, D and b. This is polynomial in the **explicit budget and dense polynomial representation**, with the usual rational coefficient bit growth accounted for; it is not asserted polynomial in log D or log b for sparse/binary-degree encodings. The test harness's additional full-word enumeration is deliberately exponential in its small test parameters and is not part of the bounded generator. The small-prime field constructor assumes primality; it is not a primality-testing implementation.

## Execution

```sh
python /tmp/pm-finite-algebra.py
```

Final run: exit 0, `ALL EXACT FINITE-ALGEBRA CHECKS PASSED`, approximately 0.56 seconds. This timing is observational, not a comparative performance benchmark.

| Exact control | Result |
|---|---|
| Scalar V=t over Q; budgets 1,2,4,8 | `rank_budget_exceeded` with respectively 2,3,5,9 independent actual words; no `infinite` verdict |
| `V=[[1,t],[0,0]]` | Closed dimension d=2, b=1, faithful order E=2 |
| `V=t^17 E12` | Closed d=2, b=17, E=18; jet ranks are 1 at every E=1..17 and 2 at E=18 |
| `V=[[1,t/(1-t)],[0,0]]`, delta=1-t | Closed d=2, b=1, E=2; denominator inversion exercised |
| Rational conjugates of E12,E21 | `S=I+t/(1-t) E12`; common delta=(1-t)^2; closed d=4, b=2, E=7; basis words empty,0,1,01 |
| Same rational conjugate algebra with D=3 | `rank_budget_exceeded` with four independent words, despite finite algebra dimension 4 |
| Exhaustive all two-generator constant 2x2 tuples over F2 | All 256 inputs close within D=4; dimension counts d=1:4, d=2:84, d=3:72, d=4:96 |
| Exhaustive idempotent offdiagonal q of degree <=2 over F2/F3 | All 8+27=35 matrices `[[1,q],[0,0]]` close with d=2; certified jet rank equals d |
| Rational/conjugate/delayed examples reduced over F2/F3 | Six exact controls pass, including characteristic-2 cancellations in delta=(1-t)^2 |
| Invalid delta(0)=0 | Rejected |

For every closed test, the harness independently computes all words through length d, performs an unpruned full coefficient-rank comparison, and checks rank d. It also independently computes the truncated rational basis and checks rank d at the stated E. These are finite checks, not substitutes for FA-B1–4.

Four malformed certificates are rejected: t-dependent scalar (`constant field scalars`), wrong constant (`coefficient identity`), false E (`jet bound`), and the central false K(t)-closure certificate for scalar t with basis I and closure coefficient t (`constant field scalars`).

## Limitations and safe interpretation

- Standalone standard-library Python, univariate t only. No repository helper imports or writes, no external dependencies, no Git actions, no child agents.
- The synthesis and checker share polynomial/field primitives but have distinct solving/rank implementations; not a fully independent formal checker.
- The field is Q or a supplied prime Fp. Denominator invertibility and coefficient interpretation are exact.
- The proven object is a finite-dimensional algebra over the **constant field K**. Ambient matrix size bounds dimension over K(t), not over K, and does not supply the required promise D.
- A failed dimension budget says only that more than D independent words were found. Both infinite and larger finite algebras can produce it.
- No claim of new finite-dimensional algebra generation, new jet theory, uniform black-box PIT, or polynomial generation absent the explicit finite-dimension/degree promises is made.

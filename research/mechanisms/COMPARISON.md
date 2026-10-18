# Startup comparison: three distinct cancellation mechanisms

Read date: 2026-10-18. OpenAI source revision: `1581d4cbdd69a0faf34b2089614fe2a814316a6a`. These are targeted calibration examples, not a neutral sample of the collection. Reading a Lean proof does not constitute recompiling it or validating an upstream headline theorem.

## 1. Finite-field polynomial summation

Source: `lean/OAI/RingTheory/DirectFiniteness/Pairing.lean`, lines 100-153, especially `sum_polynomial_eval`, `line_sum_zero` and `affine_space_sum_zero`.

For a finite field Q, a polynomial P of degree <|Q|-1 has sum_{t in Q}P(t)=0 in Q. The source expands by monomials and invokes the existing Mathlib theorem `FiniteField.sum_pow_lt_card_sub_one`. It bounds the degree after restriction to an affine line and then exchanges finite coordinate sums. The affine-space statement has a supplied coordinate i, so it does not silently assert the same fact in zero dimensions.

The constant term cancels because |Q|=0 as a field scalar. At the excluded boundary P=X^{|Q|-1}, the sum is -1, not zero. Real-valued counting would not kill the constant term. The affine line parameter may be degenerate; a zero direction still gives |Q| times one value. The basic power-sum identity is established mathematics, not evidence of an invented universal instrument.

## 2. Mean-zero density and a local analytic gain

Source: `lean/OAI/Analysis/DiskMaximal/Cancellation.lean`, lines 1-125, `integrable_lip_mul`, `lip_cancellation` and `piece_discount`.

Inputs are an integrable complex density b on C, integral b=0, an L-Lipschitz function F, and almost-everywhere support of b within distance s of z. The proof first establishes product integrability. It subtracts F(z), uses the vanishing mass, and bounds the remainder by Ls integral|b|. This is zeroth-moment cancellation with a scale gain, not by itself high-order cancellation.

Dropping mean zero fails for constant F=1 and a nonzero-mass integrable density, because L=0. Higher-order gains require stronger moment and regularity hypotheses. The subsequent `ErrorPiece` has mean zero only when its size is <1, and `piece_discount` also needs boundedness and explicit exponent/scale constraints. Those conditions must not be erased during transfer.

## 3. Join-stable chains and sign-reversing involution

Sources: `lean/OAI/GroupTheory/PChains/FinsetCancellation.lean` and the complete `lean/OAI/Combinatorics/Order/ChainToggle.lean`.

In a finite join-semilattice with bottom, assume P!=bottom, bottom is allowed, and allowed(q) implies allowed(q join P). Chains contain allowed nonbottom elements; the empty chain has sign +1. For a chain s, take the largest element not above P, or bottom when there is none, and toggle its join with P. The source proves that this element is comparable with the chain, admissible and nonbottom; toggling preserves the set of elements not above P. Thus toggling twice restores s and changes cardinality by one, so signs cancel. It ultimately uses `Finset.sum_involution`.

The group-theoretic application supplies join stability via a nontrivial normal p-subgroup. This structural certificate is not just an equation declaring the desired sum to be zero. If only bottom is allowed, there is only the empty chain and the signed sum equals 1; the join-closure hypothesis fails.

## Boundary examples and transfer policy

The three methods use different scalars and assumptions: field characteristic, analytic regularity/support, and a combinatorial closure/involution. Describing each as a kernel condition is correct but adds no mathematics. A useful transfer theorem must identify a map preserving the required hypotheses and deliver a conclusion not assumed at the input.

The separate four-circulant Gram case in `mio-qwq/math` is pinned in the index. It requires the displayed 6-by-6 block symmetry and does not prove general MUB classification. It was already inspected before this project and is not a held-out test. Its upstream verification records have not been independently rerun here.

The withdrawn Weil-classes argument is a negative *proof-validity* control: a sign reversal turns a claimed zero count into -2m. Its notice says October 6, while the repository history records the change under October 7. Keep both dates and distinguish the failed proof from falsity of its conclusion.

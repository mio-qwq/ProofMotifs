# SC-004: next research question (not an accepted theorem)

Study four first differences over a characteristic-three field:
mu=product_{j=1}^4 (delta_{a_j}-delta_0).
The exact support size is at most sixteen, so complete cancellation of moments 0 through 15 would force the zero weight by Vandermonde interpolation.

A candidate coefficient analysis predicts that below degree sixteen the only potentially first nonzero moments occur at degrees 8 and 14. The p-weight of a degree must be at least four to survive four differences, but this prediction must be checked by explicit multinomial expansion, not merely quoted as intuition.

With x_i=a_i^2 and e_j their elementary symmetric polynomials, investigate
M_8=(product a_i)e_2,
M_14=-(product a_i) sum_{i!=j}x_i^4 x_j.
On the locus e_2=0 the latter should reduce to (product a_i)e_1(e_1e_3-e_4). These formulas are an unverified working target in this checkpoint.

Exact next actions: implement integer multinomial checks through degree 15, search small fields (including rank-four examples in F_81), prove or refute the formulas, and determine whether the simultaneous vanishing locus is already described by finite-difference/polarization literature. Then assess whether any result exceeds a routine classical consequence. Do not call a new direction worthwhile merely because its algebra is longer.

A parallel theoretical question is the smallest sufficient set of field-valued invariants for fixed multiplicity patterns, and whether its size or computation can be reduced beyond full expansion. Ordinary moment order must not be confused with functional degree. A genuine new application or a sharp nontrivial complexity/structure theorem would be needed before claiming a new method.

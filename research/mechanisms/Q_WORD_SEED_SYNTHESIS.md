# Discovering q-word seeds from pole geometry

19 October 2026, Asia/Singapore. Scope: a proved **strong rational-word**
criterion, exact finite-dictionary synthesis and a polynomial-grammar
faithfulness obstruction using classical tools. Not a new general theory,
arbitrary-rational-faithfulness impossibility theorem, finite-matrix hitting
result, capability explanation or held-out transfer.

## 1. The operation being extracted

The previous reachable-space and finite-algebra tools started with a supplied
representation. Here the input is a dictionary of rational candidate seeds
and their costs. The tool computes the relevant features from their pole
geometry, chooses an independent seed family, and constructs exact difference
certificates explaining discarded directions. This is a bounded part of
auxiliary-map discovery, not discovery from an arbitrary problem statement.

The choice of q-shift/operator grammar and candidate functions remains supplied.
The dictionary's split factorization is either computed separately or supplied
as a verified certificate. No polynomial factorization or orbit-decision
algorithm over an arbitrary effective field is assumed.

## 2. Exact strong-word criterion

**PM-QSEED0001.** Let K be any field, q in K* have infinite multiplicative
order, sigma fix K and act by sigma(g)(z)=g(qz), and Delta=sigma-1. Suppose
b_i belong to K(z) intersect zK[[z]]. Define on **all** K[[z]]

\[
 J_i(g)=\Delta_0^{-1}(b_i g),\qquad
 \Delta_0^{-1}\!\left(\sum_{r\ge1}a_rz^r\right)
 =\sum_{r\ge1}\frac{a_r}{q^r-1}z^r.
\]

The inverse is the unique zero-constant antiderivative; multiplication by b_i
makes its argument positive-order even for g=1. Set h_empty=1 and
h_iw=J_i(h_w). Then

\[
 \{h_w:\text{all finite words }w\}\text{ is K(z)-linearly independent}
 \quad\Longleftrightarrow\quad
 [b_i]\text{ are K-linearly independent in }K(z)/\Delta K(z).
\]

Proof. The fixed field of sigma on K((z)) is K: coefficient comparison gives
(q^r-1)a_r=0, and infinite order excludes every r!=0. The same holds on K(z).

If sum c_i b_i=Delta(R) for constants c_i not all zero, then R is regular at0.
A negative leading Laurent exponent of R would survive Delta, contrary to
regularity of the left side. Consequently sum c_i h_i=R-R(0), since both
sides have the same difference and zero constant term. This is a nontrivial
K(z)-linear relation among h_empty,h_1,...,h_n.

Conversely take a nonzero finite formal relation sum a_w h_w=0, minimizing
first its maximum word length l and then its number of nonzero length-l
coefficients. We have l>=1. Divide by one top coefficient to make it1.
Apply sigma to the relation and subtract it. The new formal coefficient of
h_w is

\[
 \Delta(a_w)+\sum_i b_i\,\sigma(a_{iw}),
\]

where missing coefficients are zero. No top word is introduced and the
normalized top coefficient disappears. Minimality forces every transformed
formal coefficient to be zero; this is not an assumption of independence.
At length l, the coefficients a_w are therefore in K. At each length-(l-1)
word w, the displayed equation says sum_i a_iw b_i is an exact difference.
The assumed quotient independence kills every a_iw, contradicting the
nonzero top layer. This proves the equivalence in every characteristic.

This proof uses the difference product rule, not a derivation rule. Infinite
order and the full constant field K are essential. Over a finite field every
nonzero q has finite order, so an unrestricted implementation cannot simply
choose q=2 modulo a prime. For positive characteristic use, for example,
q=t in K=F_p(t), t transcendental.

### Strong freeness is not ordinary faithfulness

**PM-QSEED0002 (counterexample).** With one seed b=z, the class [b] is zero,
because Delta(z/(q-1))=z. Nevertheless

\[
 J_z^n(1)=\frac{z^n}{\prod_{r=1}^n(q^r-1)}
\]

is nonzero and these series are K-linearly independent for all n. Thus the
K-algebra representation of K[x] by J_z is faithful even though the strong
K(z)-word criterion fails. The distinction is strict. A rank-defect output
below is only impossibility **within the strong contract**, not impossibility
of an ordinary faithful representation. Strong word freeness implies that
every nonzero K-coefficient free polynomial in the J_i acts nontrivially on1;
the reverse implication is not asserted. Rational multiplication need not
commute with J_i, so no central K(z)-algebra representation is inferred.

## 3. Extracting a complete residue matrix

For alpha!=0 and integer k>=1 put

\[
 \phi_{\alpha,k}(z)=(1-z/\alpha)^{-k}-1.
\]

The subtraction is outside the power, so phi(0)=0, and
sigma(phi_alpha,k)=phi_(alpha/q),k. A rational b regular and zero at0 whose
poles split over K has the unique form

\[
 b=\sum_{r\ge1}p_rz^r+\sum_{\alpha,k}c_{\alpha,k}\phi_{\alpha,k}.
\]

This is ordinary partial fractions with constant terms removed. No division
by k or k! is required, including pole orders divisible by the characteristic.
For each q^Z-pole orbit O choose a representative alpha_O and write its poles
as q^j alpha_O. Keep the pole order k as a separate coordinate. Define

\[
 \mathcal R_{O,k}(b)=\sum_j c_{O,k,j}.
\]

**PM-QSEED0003.** For the displayed split-pole inputs, b is in Delta K(z) iff
every residue coordinate is zero. This permits a telescoper in the whole
K(z), not merely in a preselected split-pole subspace.

Proof and construction. Positive monomials are exact, with antiderivative
p_r z^r/(q^r-1). On one orbit/order let c_j have finite support in [a,b].
If sum c_j=0 set d_j=sum_(ell<j)c_ell, with zero outside [a+1,b], and take
R=sum_j d_j phi_(q^j alpha_O),k. Then the coefficient of phi_(q^j alpha_O),k
in Delta(R) is d_(j+1)-d_j=c_j. This constructs a zero-constant telescoper.

For necessity, a rational telescoper has no pole at0 by the leading-exponent
argument. Work over an algebraic closure temporarily. On any nonzero q-orbit
its pole support is finite; shifting it produces two uncancellable endpoint
poles. Therefore an orbit absent from b cannot occur in R. A pole outside K
has its entire q-orbit outside K, so none can occur when b has split poles.
Now ordinary partial fractions for R give c_j=d_(j+1)-d_j on every orbit/order,
whose finite sum is zero. Polynomial terms and constants do not change this
calculation. Shared pole locations across different orders do not mix orders.

Chen–Singer2012 §2.3/Proposition2.10 already gives rational q-summability via
q-discrete residues under characteristic-zero assumptions. Their unnormalized
(z-alpha)^(-k) coordinates have q-dependent weights and an infinity constant
obstruction. Our normalized phi coordinates remove the weights; zero-at0
makes that extra constant residue redundant. The above elementary split-pole
proof is characteristic-free, but this is not a historical originality claim.

### Orbit identification is part of the input contract

Distinct poles need not mean distinct orbits: alpha and q alpha have the same
class. Exact field arithmetic alone does not solve orbit membership for an
arbitrary field. A supplied orbit partition needs a genuine inequivalence
certificate, not merely an equality check on its representatives.

Two exact effective classes suffice here. For K=F(t), q=t, normalize a nonzero
pole alpha by t^(-v_t(alpha)) alpha; two poles are in the same orbit iff these
normalized rational functions agree. For K=Q, q=2, normalize by
2^(-v_2(alpha)) alpha, retaining its sign. Odd-numerator/odd-denominator signed
rationals then give canonical orbit representatives. These are complete
criteria, not hidden discrete-log oracles.

## 4. Minimum-cost seed synthesis and negative certificates

**PM-QSEED0004.** Let R be the matrix with one computed residue column per
candidate seed and one row per orbit/order coordinate. A size-r strongly
word-free subset exists iff rank_K R>=r. For nonnegative supplied costs, a
minimum-total-cost such subset is obtained by increasing-cost linear-matroid
greedy: accept a column iff it increases the current span, until r are accepted.

Proof of feasibility follows from0001 and0003. For optimality let A be the
already accepted greedy set and let O be a minimum-cost rank-r independent
set containing A. If the next greedy element e is absent from O, basis
exchange in the rank-r truncation supplies f in O\A with O-f+e independent.
Such f could not have appeared earlier in increasing-cost order: A+f is
independent, so it would have been accepted by that earlier stage. Thus
cost(e)<=cost(f); exchange preserves optimality and extends A. Induction
proves the result. This is classical weighted matroid optimization, not a
new optimization theorem. Costs refer to selecting listed seeds, not arbitrary
rational combinations or shared-support costs.

For a complete rank certificate retain a column basis B and coordinates
R_i=sum_j a_ji R_Bj for every candidate. If rank R<r, this proves strong
infeasibility. Every residual b_i-sum_j a_ji b_Bj has zero residues, so0003
constructs an explicit rational R_i with Delta(R_i) equal to that residual.
The resulting length-one word relation explains the obstruction. The
implementation verifies these identities directly by raw numerator/denominator
cross multiplication as well as residue arithmetic.

The matrix is generated from raw rational functions, not assumed as a supplied
residual table. The Q,q=2 implementation verifies a complete split-denominator
factorization certificate, solves polynomial coefficient equations to obtain
the normalized partial fractions, canonically groups poles, and selects seeds.
It rejects non-split or incomplete certificates; it does not factor arbitrary
input denominators. Failure of that parser is outside-contract input, not an
impossibility theorem about the original rational function.

## 5. Resource and composition boundaries

With T supplied split-pole terms and d orbit/order coordinates, residue
accumulation takes O(T) additions. Increasing-cost selection uses
O(m d min(d,m)) field operations with incremental elimination, plus sorting
and input/decomposition work. The reference uses fresh exact solves rather
than claiming this optimized implementation bound. Rational heights, dense
degrees and the chosen orbit-decision method count separately.

Expanded telescopers have their own necessary output budget. On an orbit
spanning W positions the construction can use W intermediate poles, even if
the input has two terms. Indeed

\[
 \phi_{\alpha,k}-\phi_{q^N\alpha,k}
 =\Delta\!\left(\sum_{j=1}^{N}\phi_{q^j\alpha,k}\right).
\]

The telescoper has N distinct poles of order k. Uniqueness modulo constants
forces that pole divisor for every rational telescoper, so its reduced
denominator has degree Nk. Binary/succinctly encoded N can therefore require
exponential expanded output. Fast residue-rank selection is not a promise
of equally short expanded dependence certificates. For explicit rational
poles at q=2, their binary heights already account for orbit position sizes.

Coefficient extensions keep the formal variable z transcendental. After
clearing a finite hypothetical rational relation's denominators, it is a
linear dependence of finitely many z^j h_w with coefficients in the extended
constant field. Their coefficient matrix over K has a finite nonzero rank
minor when the original words are independent; that minor stays nonzero
under extension. Thus strong freeness persists. Specializing an infinite-
order q to a root of unity is not scalar extension and can break everything.

This operator grammar is not closed under arbitrary representation changes,
finite-order shifts or a change to the scalar field used for rank. Ordinary
products of h_w are also not word concatenation: a differential shuffle rule
cannot be imported without checking the difference product rule, especially
in positive characteristic.

## 6. What the full-paper comparison changes

The actual Bertrand2010 journal q-sections were read, not just January2007
slides. Its complex regular-singular/quasi-unipotent result has a system-
dependent constant; the paper states that constant's effectivity from the
system is not known there. More importantly, Amou–Matala-aho–Vaananen2007
explicitly treats arbitrary characteristic and infinite-order q. Its
Theorem2.1 bounds ord L by r*degree+O_system(1), under rational independence
of solution components. Consequently “all-characteristic q-multiplicity”
alone is already covered by old mathematics.

The source116 explicit degree-only bound has a stronger local input:
H in GL_m(K[[z]]) forces A(0)=I. Regular-singular coefficient matrices alone
do not suffice: scalar H=z^N, A=q^N has coefficient degree0 but order N.
Nor is AMV's rational independence automatic: H=I+zE_12 gives Hv=(z,1)^T.
These are precise direct-substitution failures, not proofs that the older
machinery cannot derive the source bound or that a new tool is required.
See Q_SEED_A_PRIORART.md for actual versions/ranges and inaccessible originals.

Schneider2008 Theorem3.1 supplies a strong characteristic-zero difference-
field baseline connecting absence of parameterized telescoping with constant-
preserving independent sum extensions. It is not the identical recursive
word theorem, and it blocks a broad claim that summation obstructions had
never been organized into independence tools. No absence-of-search priority
argument is used here.

## 7. PM-QSEED0005: polynomial dictionaries cannot encode two free letters

This addresses the weaker K-operator target, not only rational independence.
For a finite alphabet b_i in zK[z], write d>=1 for a degree bound and
rho:K<X_1,...,X_n> -> End_K(K[[z]]), X_i -> J_i. Then rho is faithful
for one letter exactly when its seed is nonzero; for n>=2 it is never
faithful. The empty alphabet gives the scalar algebra. All characteristics
are allowed; q still has infinite multiplicative order.

Proof of the obstruction. Put T=q^m for an input monomial z^m. A length-L
word expands into paths of L positive shifts r_j in {1,...,d}. Their partial
sums s_j are strictly increasing and at most dL. A path contributes a
constant times z^(m+s_L)/product_j(q^(s_j)T-1). Thus the common denominator
D_L(T)=product_{r=1}^{dL}(q^rT-1) clears every path. Group by final shift
s in [L,dL]. Each numerator has degree at most (d-1)L. With M=(d-1)L+1,
the entire word is encoded by M^2 coefficients. If n^L>M^2, any M^2+1
distinct length-L words have a nonzero linear dependence of these arrays,
giving a nonzero homogeneous free polynomial that acts as zero.

The denominators D_L(q^m) never vanish for m>=0. The resulting identity
holds on all monomials. Each output coefficient of a polynomial-seed word
depends on finitely many input coefficients (its shifts lie in [L,dL]);
therefore the identity holds on all formal series, not merely on polynomials
or sampled inputs. Over all word lengths <=L, shifts lie in [0,dL] and
cleared numerators have degree <=dL. The filtered operator algebra has
dimension at most (dL+1)^2, hence GK dimension at most2. This is a classical
growth obstruction, not a novel general principle. Some Ore localizations
can contain free subalgebras; the specific dimension bound is essential.

For a single nonzero seed of order r>=1, J_b^k(1) has order kr and nonzero
leading coefficient. Distinct orders imply linear independence over K,
so no polynomial in J_b can vanish. This unary proof even holds for any
nonzero b in zK[[z]]. A zero seed supplies the relation X=0. In contrast,
two or more polynomial letters have the stronger operator obstruction just
proved, independent of any quotient-rank calculation.

Construction/cost. Increase L until n^L>M^2 and examine only M^2+1 words,
not all n^L. A polynomial dynamic program builds their cleared shift arrays,
then exact linear algebra produces an identity. For d>=2 the loose choice
L=8*ceil(log_2(d+1)) suffices: writing s=ceil(log_2(d+1))>=2 gives
M<=dL<2^s*8s and 2^(8s)>64s^2*2^(2s). For d=1, L=1 suffices.
Thus this uses polynomially many field operations in expanded degree d,
alphabet size and output; sparse binary-encoded huge degrees and rational
bit growth require separate accounting. Our reference implementation uses
the simpler M^2 array and repeated Gaussian solves, not an optimized bound.
An independent proof obtains M(M+1)/2 coordinates using per-shift denominators;
no minimal relation length/support or speedup over linear algebra is claimed.

tools/q_polynomial_obstruction.py constructs and symbolically checks these
certificates over Q,q=2. The proof above is field-general. Its verifier
rejects a zero free polynomial and proves zero rational numerators for each
shift; evaluating at finitely many m would be insufficient.

## 8. PM-QSEED0006: exact quantum-plane explanation for z,z^2

Set A=J_z and B=J_(z^2), with rightmost operator acting first. Clearing the
three factors qT-1,q^2T-1,q^3T-1 gives

    BA-qAB=(q-1)A^3.

Indeed the numerators on the left are (q^2T-1)-q(qT-1)=q-1.
Put C=B+A^2. Then CA=qAC, and direct iteration yields

    A^i C^j(z^m) = q^(j^2) T^j / D_(i+2j)(T) * z^(m+i+2j),
    D_s(T)=product_{r=1}^s(q^rT-1), T=q^m.

For C alone its numerator is qT and its shift is2. Iterating multiplies
q^(1+3+...+(2j-1))T^j=q^(j^2)T^j; the subsequent A's fill the remaining
denominator factors. This proves the formula in every allowed field.

In a finite operator relation between the A^i C^j, group by shift S=i+2j.
After multiplying by D_S, the coefficient is a polynomial in T with terms
lambda_(S-2j,j)*q^(j^2)T^j. It vanishes at every distinct T=q^m, hence is
identically zero; all lambdas vanish. The relation CA=qAC reorders every
word into a multiple of A^i C^j. These normal monomials are therefore a
basis, proving an exact presentation, not just a detected relation:

    K<A,B> = K<A,C> isomorphic to K<a,c>/(ca-qac)
            isomorphic to K<a,b>/(ba-qab-(q-1)a^3).

The second isomorphism is the invertible change c=b+a^2. Thus the full
defining ideal for the original pair is generated by the mixed cubic;
there are of course further identities that follow from it. Taking its
right-A multiple minus its left-A multiple gives the homogeneous identity

    q A^2 B-(q+1)ABA+BA^2=0.

This superficially resembles one down-up relation. The companion is false:
at q=2, (B^2A-3BAB+2AB^2)(1)=(2/1395)z^5. It would be incorrect to
identify the original pair as the corresponding down-up algebra. The
quantum-plane identification after the triangular change is proved directly.
These are classical named-algebra/growth mechanisms; no historical priority
claim is made for the specialized formulas.

## 9. Evidence and next gate

The proofs received independent mathematical derivations B/D and separate
adversarial review C, with primary-source review A. Computation is exact but
does not replace the infinite theorem. tools/q_seed_synthesis.py implements
Q,q=2 only; q_seed_independent.py preserves separate raw-rational checks,
exhaustive same-input optimization and a formal F3(t) control. No human review
or Lean completion is claimed. No new unread target was consumed this cycle.

The bounded operation now constructs a strongly faithful seed subfamily from
an explicit rational dictionary and explains defects by telescopers. The
polynomial sector is fully classified for the weaker operator target too.
The remaining macro gap is generating a useful representation grammar from
an actual problem, with the appropriate target property and resource promise;
it is not a missing residue solver, matroid optimizer or generic kernel.

This next bounded gate is now CLOSED by PM-MIX0001 in
REPRESENTATION_TRANSPORT.md: J_z,J_(z/(1-z)) obey an explicit cubic operator
identity on all formal series. Strong residue rank1 alone did not decide it.
The follow-up returned to raw-point implicit representation generation and
identified its classical BM coverage. No new unread external transfer target
was consumed. Continue the macro freeze/transfer gate, not q-seed variants,
old field scans or a claim that strong rank is necessary for all faithfulness.

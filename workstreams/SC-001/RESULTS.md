# SC-001: additive convolution and exact moment order

Claim: **PM-THEOREM-0001**. Written proof complete; exact finite tests passed. No Lean check or independent researcher review. **Level 0: classical binomial/moment algebra.**

## Definitions and statement

Let K be a field and mu, nu be finitely supported K-valued weights on K. Put

M_n(mu) = sum_x mu(x) x^n, with x^0=1 even at x=0,
(mu*nu)(z) = sum_{x+y=z} mu(x)nu(y).

Define ord(0)=infinity; for a nonzero weight, ord(mu) is the least n>=0 with M_n(mu) nonzero. Such n exists: if the distinct support nodes are x_1,...,x_t, the Vandermonde matrix (x_j^i) for 0<=i<t is invertible, so its kernel contains only the zero weight. In particular ord(mu)<=t-1.

For every n>=0,

**M_n(mu*nu) = sum_{i=0}^n binom(n,i) M_i(mu) M_{n-i}(nu).**

If mu and nu are nonzero, with orders r and s, then all moments below r+s vanish and

**M_{r+s}(mu*nu) = binom(r+s,r) M_r(mu) M_s(nu).**

Consequently ord(mu*nu)=r+s if and only if the image of binom(r+s,r) in K is nonzero. Otherwise the order is strictly larger, or the convolution is zero. In characteristic zero equality always holds. In characteristic p it holds exactly when adding r and s in base p produces no carry.

## Proof

All sums are finite. Substitute z=x+y into the moment and expand (x+y)^n by the binomial theorem; then interchange finite sums and factor each summand. If n<r+s, each index i has either i<r or n-i<s, hence its summand vanishes. If n=r+s, only i=r can remain. Since K has no zero divisors and both leading moments are nonzero, the stated equivalence follows.

For completeness, write n=sum n_j p^j. In F_p[X], (1+X)^n=product_j(1+X^{p^j})^{n_j}. Since 0<=n_j<p, coefficient comparison gives binom(n,r)=product_j binom(n_j,r_j) modulo p. This is nonzero exactly when r_j<=n_j for all j. With n=r+s, that condition is equivalent to carry-free addition. This is Lucas's classical criterion, not a new lemma of this project.

## PM-COUNTEREXAMPLE-0001: two different failure modes

Over F_2, let Delta_1=delta_1-delta_0. It has order one but Delta_1*Delta_1=0, since 1+1=0 and 2=0. This refutes unrestricted additivity in the smallest possible field.

Over F_4=F_2[a]/(a^2+a+1), Delta_1 and Delta_a each have order one. Their convolution is sum_{x in F_4}delta_x. Its moments 0 through 3 are (0,0,0,1), so it has order three, not two. In this same field Delta_1^2=0. Thus the pair of input orders (1,1) does not even determine whether the product vanishes.

These are exact symbolic counterexamples. The computer also checks their full weight vectors. They are not claimed to be historically new.

## Prior art and limits

The coefficient identity is the binomial theorem, equivalently multiplication in divided-power coordinates. See [Stacks, Definition 23.2.1](https://stacks.math.columbia.edu/tag/07GK). The relation to finite differences and group algebras is already developed in [Clark-Schauz, section 1.3](https://arxiv.org/html/2305.01304v1), building on Aichinger-Moosbauer. Formal power series divided by n! are not a characteristic-free substitute: factorials need not be units.

The proof requires finite support, or additional summability hypotheses in an infinite setting. It does not establish an analytic norm estimate. The field/no-zero-divisors assumption matters for the equivalence. A nonzero binomial coefficient alone is insufficient in a coefficient ring with zero divisors.

## Evidence

`python -m unittest discover -s tests -v` and `python tools/run_experiments.py` were actually run. The latter exhausts all 66,281 ordered weight pairs over F_2, F_3 and F_4, comparing direct convolution with a separate binomial moment calculation. This finite check supports the implementation; the general statement is proved above. See `research/experiments/startup-results.json` and `startup-tests.log`. Both implementations share field tables; there has not yet been an independent author or external-system replay.

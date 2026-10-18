# Recovery handoff

Read AGENTS, STATUS, ROADMAP and CLAIMS, then fetch live refs and recent commits. `research/ongoing` is the only daily-research branch. Last verified predecessor is `063f99f67aba436c11feeb8157c1689bd8e82961`; the containing commit is determined from the remote, not self-referential text. Preserve unexpected changes.

## Proven baseline

For finitely supported field-valued weights, M_n(mu)=sum mu(x)x^n, with 0^0=1 and ord(0)=infinity. SC-001 proves binomial convolution and exact additivity iff binom(r+s,r) is nonzero. In characteristic p this is carry-free addition. SC-002 proves that product Delta_a^(p-1) is zero for dependent directions and is the uniform subspace weight otherwise, of order p^d-1. Both are classical Level 0 results, not claimed discoveries. Full proofs are in workstreams/SC-001/RESULTS.md and SC-002/RESULTS.md.

## Exact next question: SC-003

Work over any field of characteristic 3. Let mu=Delta_a*Delta_b*Delta_c, Delta_t=delta_t-delta_0. Candidate classification uses e1=a^2+b^2+c^2 and e2=a^2b^2+a^2c^2+b^2c^2. Symbolic expansion suggests M_0,...,M_4 and M_6 vanish, M_5=-abc e1, M_7=-abc e2. If abc=0 the weight is zero. If abc!=0 and e1=e2=0, the three squares must coincide (T^3-e3 has at most one root in characteristic 3), so directions are +/-a and Delta_a^3=0. Prove every step; then classify order 5, 7 or infinity.

Explicit search leads in F_27=F_3[alpha]/(alpha^3+2alpha+1), base-3 encoding c0+3c1+9c2: directions (1,3,9) and (1,3,15) both span the entire field over F_3, but have orders 5 and 7. These correspond to (1,alpha,alpha^2) and (1,alpha,alpha^2+2alpha). A preliminary normalized scan found 432 independent triples (a=1), with 408 order-5 and 24 order-7 instances. This scan has not yet been made a permanent experiment; do so next. Cross-check direct convolutions against subset inclusion-exclusion and symbolic multinomial coefficients.

## Actual verification

From repository root: `python -m unittest discover -s tests -v` (10 tests passed), then `python tools/run_experiments.py` (66,281 pair checks, 5,606 saturated tuples, 40,000 Lucas comparisons). Expected deterministic JSON and raw unit-test log are committed under research/experiments. Verify SHA256.json before assuming unchanged inputs. No Lean compilation or independent author replay has occurred.

## Literature boundaries

See research/literature/INITIAL_REVIEW.md. Xie already discusses transfer, so transfer alone is not a differentiator. Clark-Schauz section 1.3 and 4.1 cover established functional-degree and p-weight tools; compare the prospective ordinary moment classification with those and higher-order derivatives. Croot-Mao-Yip arXiv:2609.05061 is a recent equal-power-sum lead whose full text remains unread. Do not infer novelty from unsuccessful searches.

## Transport and safety

Python/Git work locally, but direct GitHub DNS failed. Use authorized connector tree/commit/nonforced-ref operations and compare remote tree hashes with `git write-tree`. Only ProofMotifs may be written. No persistent subagent branches. Source pins: OpenAI 1581d4cbdd69a0faf34b2089614fe2a814316a6a; mio math 029e05b3f45f43690f19dd599834690bcbbf016e. Do not redistribute upstream files. Licensing awaits separate approval. A CI configuration is present; actual hosted execution still must be checked.

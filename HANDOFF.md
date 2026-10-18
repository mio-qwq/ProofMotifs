# Recovery handoff

Read AGENTS, STATUS, ROADMAP and CLAIMS first, then inspect live `main` and `research/ongoing`. Do not overwrite unexpected commits. GitHub connector writes are available; container Git networking failed. Local files may therefore be reconstructed through API content rather than cloned. Verify uploaded trees against local Git blob hashes.

## Exact mathematical starting point

K is a field. A finitely supported weight mu on K defines M_n(mu)=sum_x mu(x)*x^n, with x^0=1 including x=0. The zero weight has order infinity; otherwise ord(mu)=min{n>=0:M_n(mu)!=0}. Distinct-support Vandermonde invertibility makes this finite.

Convolution is (mu*nu)(z)=sum_{x+y=z}mu(x)nu(y). The finite binomial expansion gives M_n(mu*nu)=sum_{i=0}^n binom(n,i) M_i(mu) M_{n-i}(nu). If the first nonzero moments are r and s, all moments below r+s vanish and the r+s moment equals binom(r+s,r)M_r(mu)M_s(nu). Prove and test; do not call this original.

Challenge the false characteristic-free equality ord(mu*nu)=r+s. In F_2, (delta_1-delta_0)^2=0. In F_4 with a^2+a+1=0, (delta_1-delta_0)*(delta_a-delta_0) is the uniform weight on F_4; inspect moments 0 through 3. This distinguishes total annihilation from a finite order jump.

Next question: the product over j of (delta_{a_j}-delta_0)^(p-1) is a pushforward of uniform counting on F_p^d. If directions are independent, it is uniform on their subspace; if dependent, coefficients are multiples of p. Compare its moments with the derivative of product_{w in W}(X-w). Check all edge cases, including d=0.

## Source pins already read

OpenAI math: `1581d4cbdd69a0faf34b2089614fe2a814316a6a`.
Existing mathematical repository: `029e05b3f45f43690f19dd599834690bcbbf016e`.
Files read include OpenAI README/history, DirectFiniteness/Pairing.lean, DiskMaximal/Cancellation.lean, PChains/FinsetCancellation.lean and Order/ChainToggle.lean; also 004-mub-triplets/flat-gram-cancellation.md. Re-fetch original ranges as necessary; source inspection is not kernel checking.

## Verification and delivery

Exact Python tests will be the startup verification system; no third-party packages are required. There is no local Lean compiler and no genuine independent reviewer yet. Preserve those limitations. Before reporting a push, fetch the resulting ref, commit and recursive tree. Last verified root commit: `96ca68caf554ed5e0ed7a0315d233dffcfbe01e4`.

# Project status

Checkpoint: initialization, 2026-10-18.

Coordinator: PM-ROOT-20261018. Stable baseline: `main`; unified research branch: `research/ongoing` (to be created after governance initialization).

Last remotely verified commit: `96ca68caf554ed5e0ed7a0315d233dffcfbe01e4` (README root commit). Resolve live refs before continuing; this is a predecessor, not a prediction of this file's commit.

Initial remote inspection found a public empty repository, no branch refs, and write permission. The root commit was created and fetched through the GitHub connector. The model container has Python 3.13.5 and Git 2.47.3. Direct `git clone` failed with DNS resolution of github.com; GitHub API reads/writes work. No `lean`, `lake` or `elan` command was found. No callable independent subagent interface is present; sequential review must not be labeled independent.

Active question: for finitely supported field-valued weights mu, nu with first nonzero moments r, s, determine the first nonzero moment of additive convolution, especially when a binomial coefficient vanishes in positive characteristic.

Verified in this baseline: repository initialization only. Written proofs and exact experiments are in preparation, not yet accepted here. Formal verification, independent review and novelty are all outstanding.

Next: finish the source audit; run SC-001 exact tests and adversarial cases; commit evidence on research/ongoing; then pursue the additive-subspace boundary in SC-002.

# PM-TRANSFER142: statement-only decision

Saved after public freeze765fa48b0eb907c4c6fc30541dbfafc42ca9d29c and BEFORE
reading the target's proof sections or the rest of its introduction.

Access so far: pinned directory/build-tree metadata, README, and ONLY lines1–130
of build/sections/00-introduction.tex, blob24bb00b878eac7882bfb3cbb862acf1903cf2693.
This includes the theorem, auxiliary-prime reduction and historical context;
it does not constitute a proof or dependency-closure audit.

Actual input agrees with the frozen provisional interface: prime p in binary,
dense nonzero f, degree n, bit parameter (n+1)ceil(log2 p). Desired output is
the complete factorization including multiplicities. Claimed cost has fixed
exponent10^12, no randomness/oracles/GRH assumption. The introduction separately
identifies a companion zero-free Hecke theorem as the analytic dependency;
the algebraic reduction instead accepts auxiliary primes with numerical-value
cost. These are SOURCE CLAIMS, not accepted theorems in this project.

Direct frozen transfer: **FAILURE at the stated uniform factor readout**.
The frontier construction from explicit root points would require unknown
roots/splitting data, disallowed by the protocol. Constructing F_p[X]/(f)
from coefficients is legal and has genuine multiplication congruence, but
its canonical basis is not a factorization or a primitive-idempotent basis.
The accepted operation supplies no deterministic poly(n,log p) procedure for
discovering those idempotents or separating the components. No valid unit
transport certificate in the frozen input supplies that missing step either.

This is failure of the particular candidate transfer, NOT a factorization
lower bound, source refutation, proof that new tools are needed, or proof
that known methods cannot solve the problem. The finite representation can
still be useful infrastructure. The source's own statement-level historical
description explicitly credits Berlekamp's Frobenius-fixed-space baseline.

Post-decision work will compare this exact representation-to-readout gap
with the ORIGINAL baseline, inspect the selected dependency steps and derive
a checkable scoped theorem/counterexample or algorithm. All such work is
source-informed, not a successful pre-proof transfer. No population/cause/
novelty or formal-verification conclusion follows; PM-H1..H5 remain OPEN.

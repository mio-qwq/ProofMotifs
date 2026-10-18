# Statement-level transfer decision (before target proof exposure)

Date: 2026-10-19 Asia/Singapore. Frozen protocol was publicly committed as
`2b8dd9e15462030b944fa220b8587e81a8e1e60f` before target contents were requested.
This file records the coordinator's independent operation and decision before
reading the target proof. It is not a model-training holdout or a novelty claim.

## Source exposure and available input

Repository `openai/math`, revision
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`; selected directory
`preprints/Uniform-Matrix-Hitting-Points-in-Every-Positive-Characteristic-October-4-2026`.
Directory metadata and build/sections metadata were inspected. Then only
`build/sections/introduction.tex`, blob
`4a798efdc42349bfbe378eede3862750b5cd91b7`, lines 1–44, were exposed to the
coordinator: definitions/context 1–25 and main theorem 26–44. The fetch contained
154 lines, but a script stored it and printed only these ranges; no later
introduction text or other proof text has been read at this decision point.
The scope document `lean/docs/116.md` remains unread.

Paraphrased main contract: from a promised prime p in binary, variable count n
and formula-size bound s in unary, produce a dense n-tuple of d-by-d matrices
over F_p, with d=O(n^3 s^6), in time/output length polynomial in n+s+log p.
The tuple must detect every nonzero noncommutative size-at-most-s formula over
every field of characteristic p. The particular formula and its coefficients
are NOT supplied. Formula size counts every tree vertex, including constants;
operations are addition and ordered multiplication, without division or sharing.

## Independently checked candidate lemma

Let K be any field, lambda in K^(1 by r), gamma in K^(r by 1), and A_1,...,A_n
explicit r-by-r matrices. Put c(w)=lambda A_w gamma, with A_empty=I. Start with
lambda if nonzero, then repeatedly append the row v A_i whenever it is outside
the span of retained rows. Store a representative word for each retained row
and exact linear-combination coefficients for dependent successors. There can
be at most r accepted rows. Breadth-first generation yields word length at
most r-1: spans of words of length at most t start with dimension one (unless
lambda=0); a plateau is invariant under all A_i and hence final; every earlier
step strictly raises dimension. All accepted words therefore have that bound.

When closure is reached, the retained span R contains lambda and is invariant
under every A_i. Induction on word length gives lambda A_w in R for every w.
Conversely each retained row is reachable, so R is exactly the reachable span.
Thus all coefficients vanish iff every retained row annihilates gamma. If not,
a retained representative word is a nonzero coefficient witness. A zero-series
certificate need only supply lambda in the row span, all r-or-fewer rows'
successor decompositions, and their annihilation of gamma; these equations
suffice for soundness even without a minimal basis or word representatives.

Incremental elimination yields O(n r^3) field operations (n>=1), storage
polynomial in n and r. This is not a claim of unit-cost rational bit complexity.
It generates a word-test basis from explicit transition structure, not from a
pre-expanded table. This is the classical weighted-automata/white-box PIT route;
primary-source comparison is still being independently audited.

## Frozen decision

**Headline transfer fails at the supplied-input and quantifier interfaces.**
The candidate consumes a particular formula's transition representation and
constructs an input-dependent list of words/closure coefficients. The target
consumes only p,n,s and must output a single matrix tuple working for all
formulas and all coefficient extensions simultaneously. Even a legitimate
polynomial formula-to-ABP conversion would require the absent formula and would
not change this quantifier order. No such uniform conversion from the target's
available input has been established here. This is a failed transfer, not a
refutation of the target theorem.

Useful local scope remains: compact certificates for a supplied representation
and exact cancellation of exponentially many paths/words. A same-input
comparison is against classical reachable-space and white-box ABP PIT, not
against a black-box headline. An exponential word enumeration is only a naive
control, not the strongest baseline.

An elementary obstruction to a tempting repair: for every length-D word u on
n>=2 letters, a D+1-state chain represents the series supported only at u.
Any representation-independent set of coefficient-query words that tests all
these chains must contain all n^D such words. Adaptive structure-dependent
bases avoid this enumeration; uniform *matrix* evaluations are different and
are not ruled out by this lower bound. Characteristic specialization must be
tested in the actual field: rational denominator/pivot certificates cannot be
reduced at bad primes without an additional validity check.

Next: develop independently verified certificate code, audit classical sources,
then expose relevant target proof and record whether its actual construction
supplies a missing uniform operation. This decision precedes that exposure.

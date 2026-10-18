# Recovery handoff

Read AGENTS, STATUS, ROADMAP, CLAIMS and fresh remote refs before writing.
Last verified remote predecessor: `31f3d3936c654fc4d24c8246144c3308bb0570f7`.
Resolve the containing live head separately. Preserve unexpected work;
never force-push. Unified branch: `research/ongoing`; main stays stable.

## Strongest accepted statements

C(a,b,c) is the ordinary-moment order of the convolution of three first
finite-difference weights over a characteristic-three field. SC-003 proves:
a zero direction gives infinity; otherwise, writing u=a²,v=b²,w=c²,
equal squares give infinity, distinct zero-sum squares give 7, and all other
cases give 5. SC-005/006 classify additive preservers and retain F_9 as the
exception; the arbitrary-field additive result allows arbitrary field
automorphisms, not only Frobenius powers.

SC-007 proves <=2m-3 admissible Q evaluations with a supplied power basis
and >=floor(m/2) for deterministic decision from Q alone. Theta(m) is ONLY
that oracle model; no direct-T, randomized or bit-complexity optimality.

SC-008 gives all arbitrary preservers for finite q>3 as the independent-sign
kernel over Aut(H_K), where H_K is the distinct zero-sum triples on
S=(K*)². The sign swap on just {1,-1} in F_27 is nonadditive and preserves
all 19,683 ordered triple labels. This obstruction must not be discarded.

SC-009 now proves PM-THEOREM-0013: every incidence-kernel function S->F_3
is affine for m>=3. Combined with PM-THEOREM-0011 and classical Carlitz,

`Aut(H_K)={u -> s*u^(3^j):s in S,0<=j<m}`.

The arbitrary preserver group has order `2^((q-1)/2)*(q-1)*m/2`.
F_9 remains exceptional (384 arbitrary preservers); F_3 has S_3.
PM-CONJECTURE-0002 is proved, not still open. Read the full self-contained
proof in workstreams/SC-009/RESULTS.md before changing this status.

SC-009 also has a second uniform proof in `FOURIER_PROOF.md`. The square
subgroup diagonalizes the incidence kernel into characters `u->u^k`. Root
bounds and Frobenius-orbit dynamics leave only
`k=0,1,3,...,3^(m-1)`; a cubic Weil sum excludes the even-degree order-two
candidate. Task F independently accepted every step. This covers all `m>=3`
without finite base certificates.

SC-010 proves PM-THEOREM-0014. For an index-`d` multiplicative subgroup, the
condition `q-[6(d-1)^2+8(d-1)^3+3(d-1)^4]sqrt(q)-4d^3>0` forces the
line-incidence kernel to be affine. Its exact automorphism group is then
`Stab_GL(m,3)(H)`. Do not replace this by scalar--Frobenius for `d>2` without
a separate generalized-Paley theorem.

## Why the general proof works

The F_3 incidence kernel includes every affine restriction. If its dimension
is m+1, coordinate pullbacks under any hypergraph automorphism extend
uniquely to an affine map. Since S affinely spans K, its linear part is
invertible. Sum S=0 and |S|=1 modulo3 kill the translation. Additivity and
preservation of squares give square difference quotients, meeting Carlitz.

For q>=243, a nontrivial u+v=w+z in S has four distinct roots
0,-u,-w,z-u. A parameter a making a,-u-a,-w-a,u+a-z squares exists by
`N4 >= (q-38-11sqrt(q))/16>0`. Four zero-sum triples give the Freiman
identity. Repeated triples are automatic: characteristic three forces all
entries equal and 3f=0. Do not exclude extra diagonal parameters.

For x!=0, the exact difference count is
`(q-3-(1+chi(-1))*chi(x))/4>0`. Thus define L(x)=f(a)-f(b) for a-b=x;
Freiman relations make it well-defined. Three-square-translate intersections
are at least `(q-15-2sqrt(q))/8>0`; telescoping gives additivity, with zero
arguments and x+y=0 checked separately. Hence f is affine. Exact rank
certificates for q=27 and 81 finish the two degrees below243.

Weil's multiplicative-character version applies to distinct-root degree2/3/4
polynomials here, without a degree-coprime-to-characteristic restriction.
Primary statement: Kim–Yip–Yoo2024 Lemma2.1; final Carlitz step: Yip2024
Theorem1.2 with the square subgroup. E independently checked the complete
proof and primary sources; root accepted. No Lean or human review occurred.

## Exact certificates and commands

The rank reports are (q,vertices,edges,rank,nullity):
(9,4,0,0,4), (27,13,13,9,4), (81,40,120,35,5),
(243,121,1210,115,6). F_9 is the essential failing affine-rank control.

F_243 has exactly605 quotient automorphisms. The rank certificate supplies
matching nonzero minor and six independent kernel vectors. A separate
color certificate fixes1, yielding cell counts2,3,15,25,25; fixing(1,9)
yields3,6,121,121. The upper bound121*5*1 matches605 edge-preserving known
actions. Its checker imports no other project module and reconstructs
arithmetic from alpha^5=alpha+2 and a242-element cyclic-log table.

```bash
python -m unittest discover -s tests -v
python tools/incidence_rank_certificate.py > /tmp/incidence-rank-results.json
diff -u research/experiments/incidence-rank-results.json /tmp/incidence-rank-results.json
python tools/color_refinement_certificate.py --check research/experiments/color-certificate.json
python tools/freiman_completion.py > /tmp/freiman-completion-results.json
diff -u research/experiments/freiman-completion-results.json /tmp/freiman-completion-results.json
python tools/fourier_incidence_spectrum.py > /tmp/fourier-incidence-spectrum.json
diff -u research/experiments/fourier-incidence-spectrum.json /tmp/fourier-incidence-spectrum.json
python tools/cyclotomic_incidence.py > /tmp/cyclotomic-incidence-results.json
diff -u research/experiments/cyclotomic-incidence-results.json /tmp/cyclotomic-incidence-results.json
```

All 74 integrated tests passed; log research/experiments/sc010-tests.log.
The workflow replays all historical reports plus the SC-009 and SC-010 reports.
Mathematical commit 029a65ff5920f6f9bc05e5102ee3cd5d2f545154 was delivered
with matching local/remote tree 4afcd66a268a42f18f4fd4f7f8a09ebaba5a5298.
Hosted run39109178633/job117621402329 passed the full suite and all nine
replay steps; fresh run/job reads were inspected. See
docs/reviews/CI_INCIDENCE_CHECKPOINT.json. The containing receipt checkpoint
changes evidence/recovery metadata only. Hashes: sc009-SHA256.json. Negative tests
reject missing edges, unsafe color splits and altered Frobenius data; exact
F_9 functions and missing completions witness the true exception.

## Recovered external increment

Accepted f172123bd60e27bccbea31fb335994418d95d5d9 (SC-008),
b82c344012c4af879f6e6e4d7a5320efb77d4f8b (workflow), and
bfe32279b502fd07ec646d4a7f173808d0ad8a2a (receipt).
Fresh run 39108039870/job 117618028562 reads confirmed success; local46-test
replay, exact regenerated JSON and all saved hashes also passed.
See docs/reviews/EXTERNAL_SC008_ACCEPTANCE.md. The producing execution's
identity is not established by the shared Git author. The earlier mistaken
predecessor string was corrected to 2e990a70585e0fd7230a2c8b47d34627722a011b.

## Exact next operation and limits

The direct value audit is complete: SC-009 is provisionally Level 1 and
historical priority remains unverified. Next compare the uniform
Fourier/cyclic-code proof with defining-characteristic cyclic-code and
punctured Reed--Muller literature. Identify a direct spectral theorem or the
precise residual step. Do not optimize SC-010's sufficient bound or add more
subgroup enumeration without an application. If Lean becomes available, the
abstract completion-to-affinity lemma is the compact formalization target.

One full publicly extracted Zhihu answer was read via Parallel Search; not
all33 answers or comments. The evidence gate rejects universal cancellation
or AI/human prevalence conclusions. Source and method comparisons:
research/literature/DISCUSSION_GATE_20261018.md.

Architecture remains one coordinator with actual task-scoped subagents,
independent views, adversarial checks and a single shared roadmap. See
SEVENTH_CYCLE.md, SIXTH_CYCLE.md and SC009_GENERAL_AUDIT.md for accepted
handoffs, objections and decisions. Distinguish software certificates,
AI review, human review, Lean and historical novelty.

## Delivery and scheduling

The user authorized immediate ordinary project pushes. Terminal Git lacks
credentials; authorized GitHub API tree/commit/ref writes work. Fresh-read
the expected predecessor, match local `git write-tree` with remote tree,
create a child commit, update the ref non-forced with expected_sha, fetch and
verify live SHA. Never overwrite unexpected remote changes.

The existing 90-minute task was successfully re-enabled and updated on
2026-10-18, timezone Asia/Singapore. Its recorded last invocation is 07:34:32UTC;
this is not proof of a particular output or continuous background work.
Every research window resumes from fresh live state. No other repository,
permissions, expenses, external correspondence, DOI or final academic
release is authorized by ordinary checkpoint permission.

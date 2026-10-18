# Acceptance of the recovered SC-008 checkpoint

Date: 2026-10-18. Reviewed against live remote predecessor
`bfe32279b502fd07ec646d4a7f173808d0ad8a2a` on `research/ongoing`.

## Recovered deliverables

The branch had advanced beyond the coordinator's previous verified checkpoint.
The recovered increment is mathematical commit
`f172123bd60e27bccbea31fb335994418d95d5d9`, workflow extension
`b82c344012c4af879f6e6e4d7a5320efb77d4f8b`, and the containing CI receipt
commit `bfe32279b502fd07ec646d4a7f173808d0ad8a2a`. These commits were
fast-forwarded into a clean local checkout. The shared Git author identity does
not establish which particular execution produced them.

SC-008 supplies the independent-sign obstruction, the exact quotient by the
zero-sum hypergraph on nonzero squares, its degree formula, and complete small
field classifications for F_9, F_27 and F_81. It explicitly leaves the general
semilinear quotient classification open. No F_243 enumeration or infinite
classification was present in that increment.

## Mathematical acceptance

The coordinator checked the proof against SC-003. For nonzero directions,
the observable labels depend only on their squares: equal squares give
infinite order, three distinct zero-sum squares give order seven, and all
remaining cases give order five. In characteristic three a repeated entry in
a zero-sum triple forces all three entries to coincide. Zero is distinguished
when q>3; preservation and injectivity then force oddness. Choosing independent
orientations on opposite pairs proves the stated split sign kernel.

The degree calculation correctly removes the repeated solution r=1 and
divides by two. The enumeration's pair-incidence pruning is necessary for
every genuine automorphism, its forced third images follow from linearity of
the hypergraph, and complete maps are checked against the entire edge set.
No unjustified projective-geometry theorem is used to infer the general case.

## Actual replay

The coordinator ran `python -m unittest discover -s tests -v`: all 46 tests
passed. `python tools/nonadditive_preservers.py` reproduced the committed
`nonadditive-results.json` byte for byte. All four source/result/log hashes in
`nonadditive-SHA256.json` were verified. This repeats the original exact
arithmetic dependency rather than constituting an independent arithmetic
engine. The local test record is `research/experiments/sc008-acceptance-tests.log`.

The GitHub run and job endpoints were separately read. Run
[39108039870](https://github.com/mio-qwq/ProofMotifs/actions/runs/39108039870)
is completed/success at mathematical-workflow head `b82c344`; job
117618028562 reports successful unit tests and all six deterministic replay
steps, including SC-008. The receipt agrees with those live records.

## Decision and corrections

Accept the recovered mathematical increment and continue from its open
hypergraph problem. This does not certify historical novelty, Lean
formalization, or human review. The predecessor string beginning
`2e990a7c00899321` in the recovered STATUS/HANDOFF was not the actual commit;
the verified predecessor is `2e990a70585e0fd7230a2c8b47d34627722a011b`.
Recovery metadata and the README's missing SC-008 row are corrected in the
next integrated checkpoint. These documentation issues do not alter the
accepted proof or exact results.

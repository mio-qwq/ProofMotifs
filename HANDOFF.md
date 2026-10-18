# Recovery handoff

Read AGENTS, STATUS, ROADMAP, CLAIMS, then fresh remote refs, recent commits and working tree. Last remotely verified predecessor: 4f6db95fe5b72c12bdbfc875026f47698735f817. Resolve the live containing commit independently. Preserve unexpected changes and never force-push.

## Mathematical state and exact notation

For a finite weight mu on a characteristic-three field K, M_n(mu)=sum_x mu(x)x^n, with x^0=1; ordinary order is the first nonzero moment, infinity only for the zero weight. Vandermonde on its s support nodes detects zero using moments 0 through s-1, including over infinite fields. Delta_a=delta_a-delta_0, C(a,b,c)=ord(Delta_a*Delta_b*Delta_c).

SC-003 gives M_0,...,M_4=M_6=0, M_5=-abc*e1 and M_7=-abc*e2, where e1=a²+b²+c² and e2=a²b²+a²c²+b²c². For abc!=0, order is 5 if e1!=0, 7 if e1=0,e2!=0, infinity otherwise; the last case has directions signed copies of one another. Zero directions also give infinity.

SC-005 classifies additive bijections of finite F_(3^m): scalar Frobenius if m!=2, all GL(2,3) if m=2. Its original polynomial proof and F9 exception have now passed actual independent AI review (not human or Lean).

SC-006/RESULTS.md contains the current strongest proof. For a(t)=1-t²+t, b(t)=1-t²-t, c(t)=-1-t², one has e1=0 and e2=-(t-t³)². The zero-coordinate set E is empty unless K contains F9, in which case E=F9 minus F3. Identity: abc=-(t²+1)(t⁴+1), (t³-t)*abc=-(t⁹-t).

For additive bijective T, A=T(1)!=0 and Q(t)=A*T(t²)-T(t)². Its polar is B(x,y)=2*(A*T(xy)-T(x)*T(y)); Q(1)=0,B(1,x)=0,Q(t+r)=Q(t) for r in F3. Q(t+u)+Q(t-u)=2Q(t)+2Q(u). Transformed conic sum of squares equals Q(t). A nonzero Q-value outside E automatically gives a strict source7->target5 witness; Q vanishes on F3, so no infinity source is hidden.

PM-THEOREM-0005: for basis (1,e1,...), test Q(e_i) and Q(e_i+e_j), i,j>=1. There are N=m(m-1)/2 tests. All zero implies Q identically zero by quadratic expansion, hence T/A is a field automorphism by square polarization. Otherwise obtain t. If t in E, choose basis element u outside F9: Q(u) or Q(t+u) or Q(t-u) is a usable nonzero value. Up to3 directly checked extras (2 if last is inferred). A basis adapted to (1,i,u,...) replaces the bad test i by i-u and proves an N-test bound, but that version is NOT implemented. Costs are oracle-query counts with field/basis setup, rank validation and full verification separate.

PM-THEOREM-0006: the same repair proves the arbitrary-field classification K!=F9, T=lambda*sigma with sigma an arbitrary field automorphism. If a preserver had any nonzero Q, repair gives an admissible conic violation. Thus Q identically zero and polarization gives multiplicativity after normalization. No finiteness, perfectness or Frobenius-surjectivity assumption is used. Infinite-field sigma must NOT be restricted to Frobenius powers. F9 retains all 48 additive bijections.

## Evidence and reproducibility

python -m unittest discover -s tests -v
python tools/constructive_witness.py > /tmp/constructive-results.json
diff -u research/experiments/constructive-results.json /tmp/constructive-results.json

29 tests passed. F27 all 432 normalized bijections: 3 semilinear, 429 strict witnesses verified by complete27 moments on each side, max 3 defect queries / 6 distinct extraction T calls. Selected F81 tests are 18 transvections, not a full GL(4,3) enumeration. An even-repair example uses modulus x⁴+x²+2, columns(1,4,16,27), initial t=9 repaired to12, source(39,51,28), image(38,46,28), verified7->5 by complete81 moments. Output and hashes: research/experiments/constructive-results.json and constructive-SHA256.json. The script constructs O(q²) field tables, so it makes NO O(m²) end-to-end runtime claim.

Independent tasks A/B/C/D completed; task scopes, objections, resolution and review limits are in docs/reviews/THIRD_CYCLE.md. A accepted the manuscript and implementation and ran all 9 new tests. Root fixed A's docstring objection that q moments are sufficient rather than necessary. Mathematical correctness, independent AI review, human review, formalization and novelty remain separate. No Lean/Lake/Elan tool is available.

Historical baseline commands remain available: python tools/run_experiments.py; python tools/ternary_differences.py; python tools/order_preservers.py. Do not repeat large enumerations just to appear active. CI run 39102950233 covers 037ea1c only; verify each later run separately. The workflow now also replays constructive-results.json.

## Exact next mathematical operations

1. Read research/literature/PRESERVER_AUDIT_20261018.md. Lester 1977 DOI10.4153/CJM-1977-124-1 already classifies FULL cone-preserving bijections in isotropic nonsingular spaces dim>=3. Once full-cone preservation is established, coordinatewise(T,T,T) gives the scalar-automorphism conclusion. That conclusion is classical. The project-specific candidate is the punctured-data repair/exact exception, whose historical priority is still unresolved.
2. Search primary literature for that exact weakening and for quadratic basis identity tests, recording exact hypotheses. F9 T(1)=1,T(i)=1+i preserves ternary order but sends full-cone vector(0,1,i) off cone; direct Lester invocation before repair is invalid. Never infer originality from a failed search.
3. Decide whether the N-test adapted-basis result admits an interesting sharp lower bound, or a new target where order-loss certificates add value. Distinguish arbitrary quadratic-map testing from the restricted square defects of additive bijections. Do not assume their coefficient spaces coincide. Preserve counterexamples if a proposed lower bound fails.
4. Actual Lean formalization remains useful when a compiler is present. SC004 higher-difference formulas stay unverified/deferred. Do not upgrade uncompiled files or finite evidence to formal proof.

## Operational recovery

Only ProofMotifs/research/ongoing is writable under this charter; main remains stable. Direct clone succeeded in this window; earlier DNS failure is historical, not a permanent assumption. Check both Git and connector access afresh. Nonforced connector updates with expected predecessor remain a fallback. The existing 90-minute scheduled task was actually re-enabled and its unified coordinator/short-task/adversarial-review instructions updated. The stored first start is 2026-10-18 07:14:59 UTC (15:14:59 Asia/Shanghai). No future run or continuous between-run process is asserted. No license decision, DOI, correspondence or final paper release has been made.

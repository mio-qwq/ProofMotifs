#!/usr/bin/env bash
# Actual local verification commands for the succinct checkpoint. Run in repo.
set -euo pipefail
python3 -m unittest discover -s tests -v > research/experiments/succinct-tests.log 2>&1
python3 tools/reachable_series.py > /tmp/reachable-series-report.json
diff -u research/experiments/reachable-series-report.json /tmp/reachable-series-report.json
python3 tools/acyclic_jet.py --demo > /tmp/acyclic-jet-report.json
diff -u research/experiments/acyclic-jet-report.json /tmp/acyclic-jet-report.json
python3 tools/acyclic_jet_independent.py > /tmp/acyclic-jet-independent.json
diff -u research/experiments/acyclic-jet-independent.json /tmp/acyclic-jet-independent.json
python3 tools/finite_algebra_jet.py > /tmp/finite-algebra-jet-report.json
diff -u research/experiments/finite-algebra-jet-report.json /tmp/finite-algebra-jet-report.json
python3 tools/finite_algebra_jet_independent.py > /tmp/finite-algebra-jet-independent.json
diff -u research/experiments/finite-algebra-jet-independent.json /tmp/finite-algebra-jet-independent.json
awk '/^        run: \|/{block=1;next} /^      -/{block=0} block{sub(/^          /, ""); print}' .github/workflows/verify.yml > /tmp/pm-succinct-replay-all.sh
bash -ex /tmp/pm-succinct-replay-all.sh > research/experiments/succinct-replays.log 2>&1
python3 -m json.tool research/experiments/succinct-source-ledger.json > /dev/null
git diff --check

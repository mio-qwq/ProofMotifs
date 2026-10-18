#!/usr/bin/env bash
# Run at repository root. Logs and reports are generated outputs, not proofs.
set -euo pipefail
python3 tools/q_seed_synthesis.py > research/experiments/q-seed-report.json
python3 tools/q_seed_independent.py > research/experiments/q-seed-independent.json
python3 tools/q_polynomial_obstruction.py > research/experiments/q-polynomial-report.json
python3 tools/q_polynomial_independent.py > research/experiments/q-polynomial-independent.json
python3 -m unittest discover -s tests -v > research/experiments/q-seed-tests.log 2>&1
awk '/^        run: \|/{block=1;next} /^      -/{block=0} block{sub(/^          /, ""); print}' .github/workflows/verify.yml > /tmp/pm-q-replay-all.sh
bash -ex /tmp/pm-q-replay-all.sh > research/experiments/q-seed-replays.log 2>&1
git diff --check

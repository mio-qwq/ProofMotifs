#!/usr/bin/env bash
# Actual local verification sequence, run at repository root.
set -euo pipefail
python3 tools/resolvent_certificate.py > research/experiments/resolvent-certificate.json
python3 tools/mixed_seed_independent_b.py > research/experiments/mixed-seed-independent-b.log
python3 tools/mixed_seed_independent_c.py > research/experiments/mixed-seed-independent-c.log
python3 tools/implicit_evaluation.py > research/experiments/implicit-evaluation.json
python3 tools/implicit_independent_a.py > research/experiments/implicit-independent-a.log
python3 tools/implicit_independent_b.py > research/experiments/implicit-independent-b.log
python3 tools/implicit_independent_c.py > research/experiments/implicit-independent-c.log
python3 -m unittest discover -s tests -v > research/experiments/representation-tests.log 2>&1
awk '/^        run: \|/{block=1;next} /^      -/{block=0} block{sub(/^          /, ""); print}' .github/workflows/verify.yml > /tmp/pm-representation-replays.sh
bash -ex /tmp/pm-representation-replays.sh > research/experiments/representation-replays.log 2>&1
git diff --check

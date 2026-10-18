#!/usr/bin/env bash
# Actual local verification commands, run from repository root.
set -euo pipefail
python3 tools/factor_readout.py > research/experiments/factor-readout.json
python3 tools/orientation_readout.py > research/experiments/orientation-readout.json
python3 tools/dynamic_readout.py > research/experiments/dynamic-readout.json
python3 tools/factor_independent_a.py > research/experiments/factor-independent-a.log
python3 tools/factor_independent_b.py > research/experiments/factor-independent-b.log
python3 tools/factor_independent_c.py > research/experiments/factor-independent-c.log
python3 tools/factor_oracle_audit.py > research/experiments/factor-oracle-audit.log
python3 tools/orientation_high_primary_audit.py > research/experiments/orientation-high-primary.json
python3 -m unittest discover -s tests -v > research/experiments/factor-readout-tests.log 2>&1
awk '/^        run: \|/{block=1;next} /^      -/{block=0} block{sub(/^          /, ""); print}' .github/workflows/verify.yml > /tmp/pm-factor-readout-replays.sh
bash -ex /tmp/pm-factor-readout-replays.sh > research/experiments/factor-readout-replays.log 2>&1
git diff --check

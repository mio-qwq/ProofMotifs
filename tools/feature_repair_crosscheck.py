#!/usr/bin/env python3
"""Separated final cross-review of the coordinator's implementation."""
import random
import runpy
import sys
from pathlib import Path

sys.dont_write_bytecode = True
tool_dir = Path(__file__).resolve().parent
independent = runpy.run_path(str(tool_dir/'feature_repair_reference.py'))
primary = runpy.run_path(str(tool_dir/'feature_repair.py'))
Matrix = independent['Matrix']
own_oracle = independent['oracle']
root_oracle = primary['oracle']
root_matrix = primary['matrix']
rng = random.Random(2026101801)
checks = 0
for case in range(80):
    n = rng.randint(2, 6)
    m = rng.randint(0, 3)
    instance = {
        'omega': list(range(n)),
        'target_indices': list(range(rng.randint(1, n))),
        'base_rows': [[rng.randint(-2, 2) for _ in range(n)] for _ in range(rng.randint(0, 2))],
        'blocks': [{'name': str(j), 'cost': rng.randint(0, 4),
                    'rows': [[rng.randint(-2, 2) for _ in range(n)] for _ in range(rng.randint(0, 2))]}
                   for j in range(m)]}
    for mask in range(1 << m):
        a = root_matrix(instance, mask)
        kind, certificate = own_oracle(Matrix(a, n), instance['target_indices'])
        root_certificate = root_oracle(instance, mask)
        assert kind == root_certificate['kind'], (case, mask, kind, root_certificate)
        checks += 1
print(f'PASS: {checks} fixed-stack cross-checks on 80 separate deterministic integer dictionaries; empty feature stacks, empty optional blocks, all-target domains, dependent rows, and multi-target spans included.')

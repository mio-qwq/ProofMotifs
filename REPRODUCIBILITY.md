# Reproducibility

The startup computational environment uses the Python standard library. Exact rational and finite-field arithmetic, explicit small fields and deterministic enumeration will be used. Record the actual Python version, commands, counts, fixed random seeds when applicable, output and input/source hashes.

The first research checkpoint will provide:

```sh
python -m unittest discover -s tests -v
python tools/run_experiments.py
```

These commands are planned, not yet recorded as successful in the governance baseline. No Lean build or independent replay has occurred. A compiler, pinned toolchain/dependencies and semantic audit are required before any formal-verification claim.

Git transport: use standard Git where available. In restricted environments, the GitHub connector can create a tree and a commit followed by a non-forced ref update with an expected predecessor. Compare recursive remote blob hashes with local `git hash-object` results. A successful API mutation alone does not certify a complete upload.

Source provenance and mathematical verification are independent. Third-party source pins identify what was inspected, not whether an upstream headline theorem is correct.

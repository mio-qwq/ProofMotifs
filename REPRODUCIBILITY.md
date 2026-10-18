# Reproducibility

## Recorded environment and commands

The startup run used Python 3.13.5, standard library only. All finite fields are constructed from explicitly supplied, irreducibility-checked monic polynomials. No floating-point arithmetic or random sampling is used.

```sh
python -m unittest discover -s tests -v
python tools/run_experiments.py > /tmp/startup-results.json
diff -u research/experiments/startup-results.json /tmp/startup-results.json
```

Actual result: 10 unit tests passed; deterministic experiment output records 66,281 ordered weight pairs, 5,606 direction tuples and 40,000 Lucas checks. See `research/experiments/startup-tests.log`, `startup-results.json` and `SHA256.json`. Unit-test elapsed time is not a reproducibility target. The JSON contains only deterministic results.

The pair search is exhaustive over all K-valued weights on F_2, F_3 and F_4. Category counts for nonzero factors exclude pairs with a zero factor. Saturated tuple enumeration includes all directions, dependent/zero directions and empty products, for lengths 0 through extension-degree+1 in F_2/F_3/F_4/F_8/F_9. Field axioms are exhaustively checked over the five small fields; multiple algorithms still share their field tables and are not independent authors.

Integer encoding in F_{p^m}: c_0+c_1*p+...+c_{m-1}*p^(m-1) represents c_0+c_1*a+...+c_{m-1}*a^(m-1), not an integer modulo p^m. Ordinary moments include n=0 and define 0^0=1. The q moments through degree q-1 determine a weight by Vandermonde interpolation, so an all-zero complete moment vector really implies a zero weight in these experiments.

No Lean, Lake or Elan executable was available; no formal-verification claim is made. The CI workflow pins checkout by its verified commit but uses the runner's Python; it replays deterministic JSON. A workflow file is not evidence of a successful hosted run until the run is fetched and inspected.

## Git delivery

When direct Git works, use ordinary non-destructive commits. In this environment GitHub DNS failed in the container but the connector works. Create a tree based on the verified predecessor, compare its SHA to local `git write-tree`, create a child commit and update the branch non-forcibly with an expected predecessor. Fetch live ref and recursive tree before claiming upload completion. This verifies bytes and ancestry, not mathematical correctness.

Third-party source provenance is recorded separately in research/corpus/index.json; pinned source inspection is not an upstream theorem audit.

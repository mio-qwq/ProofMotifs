# Formal verification status

No Lean, Lake or Elan executable was found in the working container. No ProofMotifs theorem has been compiled or marked FORMAL_VERIFIED. Upstream Lean files were inspected, not rebuilt.

The startup minimum verification system is exact Python arithmetic with complete written proofs. A future Lean package must pin both the compiler and Mathlib revision, prove the actual finitely supported convolution statement (not an assumed moment identity alone), and audit its axioms and semantic correspondence. The characteristic-three polynomial identities are a smaller first formalization target. Compiler availability and a real successful run are prerequisites for a formal-verification claim.

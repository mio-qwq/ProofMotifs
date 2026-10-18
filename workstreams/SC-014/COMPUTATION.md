# Exact degree-13 forbidden-frequency certificate

Task PM-CYCLE10-B, 18 October 2026. The generator and verifier use independent
ordinary coefficient-list arithmetic over F3, without imports from earlier
project arithmetic modules. No full field power table, incidence matrix,
order-797161 polynomial gcd, or full degree-13 seed census is built.

## Reproduction

```
python tools/linearized_seed_certificate.py --output /tmp/sc014-certificate.json
python tools/linearized_seed_certificate.py --verify /tmp/sc014-certificate.json
python -m unittest tests.test_linearized_seed_certificate -v
```

The coordinator may retain the generated JSON and actual command log under
`research/experiments/`. The first command generates and verifies the same
deterministic certificate; the second checks an existing certificate.

## Exact evidence

K=F3[X]/(X^13+2X+1), q=1594323, N=797161. The program checks primality
of N by trial division through892 and irreducibility by the prime-degree
Rabin criterion: X^(3^13)=X modulo the modulus, and gcd(X³-X,modulus)=1.
The diagnostic primitive-order receipt verifies alpha^(2N)=1, alpha^N=2,
and alpha²!=1. Primitivity is convenient but is not needed to infer
connectivity once N is known prime and a nonidentity square is supplied.

For L(y)=y+y³+y81, an explicit13-by13 matrix over F3 has rank9 and
nullspace basis

* 1;
* X+2X³+X5;
* X+X6;
* X²+X³+X9.

The symbolic gcd is gcd(T13-1,1+T+T4)=1+T+T4, degree4. Matrix reduction
independently establishes the field-operator nullity without assuming a
normal-basis implementation. Since13 is prime, the only proper subfield
is F3. Checking only for proper-subfield solutions would miss this
four-dimensional non-subfield nullspace; the actual matrix calculation
and all81 combinations are retained. A separate negative control retains
repeated factors: gcd(T6-1,1+T+T²)=(T-1)² has degree2, not1.

All81 nullspace elements are checked. The78 outside F3 produce distinct
valid ordered parameters a=(y+1)/y, b=(y-1)/y, with both vertices square.
The verifier confirms1+a+b=0 and1+a85+b85=0 for every parameter.
The first certificate entry is

`y=X²+X³+X9`,

`a=2X5+2X11+X12`,

`b=2+X5+X11+2X12`.

The polynomial identity proved in RESULTS.md makes this a complete
parameterization of B85 for this field: every valid a maps to a
nonconstant kernel element by y=1/(a-1), and conversely all78 such
elements are explicitly checked. Normalizing at each of the three
vertices and identifying the two remaining vertices gives13 distinct
multiplicative edge orbits. The entire13-orbit collection forms a single
Frobenius orbit of length13. The verifier checks this partition directly
by field arithmetic; no discrete logarithm or all-field scan is used.

The k85 frequency orbit has length13, is disjoint from the constant and
affine frequencies, and therefore gives13 additional trace functions.
The sparse incidence kernel has dimension **at least27**, compared with14
for the full square-set incidence kernel. Its exact dimension is not
computed. The explicit witness Tr(u85) takes values (1,1,0) on the genuine
square edge with

`a'=1+X+X³+X4`, `b'=1+2X+2X³+2X4`.

The nonzero sum2 proves nonaffinity. Seed-translate vanishing follows
from the checked field identity and trace linearity, rather than from
enumerating all797161 translates.

## Verification boundary

The ordinary arithmetic implementation is independent of the earlier
bitplane gcd search, but certificate generation and verification in this
module share arithmetic routines. Separate independent review must check
the coordinate calculations and mathematical reduction. Mutation tests
reject reducible field data, changed seed coordinates, deleted or duplicated
parameters, a false kernel basis, a false trace witness, and altered
frequency/orbit-cover receipts. They do not constitute formal verification.

The result refutes an odd-degree connectedness sufficiency conjecture.
It does not refute existence of some good seed for every m, certify all
bad frequencies at m13, or establish historical novelty. The complete
B85 coverage is only for this one frequency and its Frobenius orbit.

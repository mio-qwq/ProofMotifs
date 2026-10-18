"""Exact minimal exceptional-degree certificates for PM-QUESTION-0002.

Standalone standard-library arithmetic: no project imports, field tables,
primitive-X assumption, logarithms, row-code test, or all-frequency claim.
Rabin certifies the quotient fields; an exact normal-basis determinant,
three quadratic characters and maximal-subgroup exclusions certify each seed.
Only degrees 5,6,7,8,10,16 are needed by the accompanying counting criterion.
"""
import argparse
import json
from pathlib import Path

DEGREES = [5, 6, 7, 8, 10, 16]
SCOPE = {"degrees": DEGREES, "fixed_direct_witnesses": True,
         "field_enumeration": False, "primitive_X_or_discrete_logs_required": False,
         "row_code_or_all_frequency_claim": False,
         "infinite_existence_from_computation_claim": False}
CASES = [
    (5, [1, 2, 0, 0, 0, 1], [1, 1]),
    (6, [2, 1, 0, 0, 0, 0, 1], [0, 0, 2, 1, 0, 1]),
    (7, [1, 0, 2, 0, 0, 0, 0, 1], [1, 2, 1]),
    (8, [2, 0, 0, 1, 0, 0, 0, 0, 1], [1, 1, 1, 1]),
    (10, [2, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1], [1, 1, 2, 1]),
    (16, [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
     [1, 0, 2, 1, 2, 1, 2, 0, 2, 2, 1, 2, 2, 2, 0, 2]),
]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def prime_factorization(n):
    """Complete trial division, including multiplicities; n <= (3^16-1)/2."""
    factors, p = [], 2
    while p*p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 1
    if n > 1:
        factors.append(n)
    return factors


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while b:
        while a and len(a) >= len(b):
            scalar, shift = a[-1]*b[-1] % 3, len(a)-len(b)
            for j, v in enumerate(b):
                a[shift+j] = (a[shift+j]-scalar*v) % 3
            a = trim(a)
        a, b = b, a
    return [v*a[-1] % 3 for v in a] if a else []


class Field:
    def __init__(self, modulus):
        require(isinstance(modulus, list) and len(modulus) >= 3
                and modulus[-1] == 1
                and all(type(c) is int and c in (0, 1, 2) for c in modulus),
                "invalid modulus")
        self.modulus, self.m = modulus, len(modulus)-1
        self.q, self.N = 3**self.m, (3**self.m-1)//2
        self.weights = [3**j for j in range(self.m)]

    def coordinates(self, a):
        require(type(a) is int and 0 <= a < self.q, "invalid field coordinate integer")
        return [a//w % 3 for w in self.weights]

    def encode(self, a):
        return sum(v*w for v, w in zip(a, self.weights))

    def add(self, a, b):
        return self.encode([(a//w+b//w) % 3 for w in self.weights])

    def neg(self, a):
        return self.encode([-v % 3 for v in self.coordinates(a)])

    def mul(self, a, b):
        aa, bb = self.coordinates(a), self.coordinates(b)
        out = [0]*(2*self.m-1)
        for i, v in enumerate(aa):
            for j, w in enumerate(bb):
                out[i+j] = (out[i+j]+v*w) % 3
        for i in range(2*self.m-2, self.m-1, -1):
            c = out[i]
            for j, v in enumerate(self.modulus):
                out[i-self.m+j] = (out[i-self.m+j]-c*v) % 3
        return self.encode(out[:self.m])

    def power(self, a, exponent):
        result = 1
        while exponent:
            if exponent & 1:
                result = self.mul(result, a)
            a = self.mul(a, a)
            exponent >>= 1
        return result

    def rabin(self):
        require(self.power(3, self.q) == 3, "Rabin full Frobenius check")
        tests = []
        for p in sorted(set(prime_factorization(self.m))):
            value = self.add(self.power(3, 3**(self.m//p)), self.neg(3))
            g = pgcd(self.modulus, self.coordinates(value))
            require(g == [1], "Rabin proper-degree gcd")
            tests.append({"prime_divisor_m": p, "remainder": value, "gcd": g})
        return {"X_pow_q": 3, "proper_degree_gcd_checks": tests}

    def normality(self, y):
        conjugates = [self.power(y, 3**j) for j in range(self.m)]
        matrix = [self.coordinates(z) for z in conjugates]
        rank, det = 0, 1
        for col in range(self.m):
            pivot = next((i for i in range(rank, self.m) if matrix[i][col]), None)
            if pivot is None:
                continue
            if pivot != rank:
                matrix[pivot], matrix[rank] = matrix[rank], matrix[pivot]
                det = -det % 3
            scalar = matrix[rank][col]
            det = det*scalar % 3
            matrix[rank] = [v*scalar % 3 for v in matrix[rank]]
            for i in range(rank+1, self.m):
                scalar = matrix[i][col]
                matrix[i] = [(u-scalar*v) % 3 for u, v in zip(matrix[i], matrix[rank])]
            rank += 1
        return {"conjugates": conjugates, "rank": rank,
                "determinant": det if rank == self.m else 0}

    def witness(self, y):
        self.coordinates(y)
        require(y not in (0, 1, 2), "excluded parameter")
        characters = [self.power(self.add(y, c), self.N) for c in (2, 0, 1)]
        require(characters[0] in (1, 2) and len(set(characters)) == 1,
                "three-character filter")
        normal = self.normality(y)
        require(normal["rank"] == self.m, "parameter is not normal")
        inv = self.power(y, self.q-2)
        a, b = self.add(1, inv), self.add(1, self.neg(inv))
        require(self.mul(a, y) == self.add(y, 1)
                and self.mul(b, y) == self.add(y, 2), "rational-image identity")
        require(len({1, a, b}) == 3 and self.add(self.add(1, a), b) == 0,
                "degenerate or non-zero-sum seed")
        powers = [self.power(a, self.N), self.power(b, self.N)]
        require(powers == [1, 1], "seed entries not squares")
        factors = prime_factorization(self.N)
        tests = [{"prime_divisor_N": p, "a_power": self.power(a, self.N//p),
                  "b_power": self.power(b, self.N//p)} for p in sorted(set(factors))]
        require(all(t["a_power"] != 1 or t["b_power"] != 1 for t in tests),
                "seed lies in a maximal proper subgroup")
        return {"m": self.m, "q": self.q, "N": self.N, "modulus": self.modulus,
            "Rabin": self.rabin(), "y": y, "y_coefficients": self.coordinates(y),
            "a": a, "b": b, "a_coefficients": self.coordinates(a), "b_coefficients": self.coordinates(b),
            "character_powers_y_minus_1_y_y_plus_1": characters, "normality": normal,
            "subgroup_certificate": {"a_b_pow_N": powers,
                "N_factorization_with_multiplicity": factors,
                "maximal_subgroup_exclusions": tests, "joint_generation": True,
                "a_generates_S": all(t["a_power"] != 1 for t in tests),
                "b_generates_S": all(t["b_power"] != 1 for t in tests)}}


def build_report():
    rows = []
    for m, modulus, y_coordinates in CASES:
        f = Field(modulus)
        require(f.m == m, "chosen modulus degree mismatch")
        rows.append(f.witness(f.encode(y_coordinates)))
    return {"schema": 1, "task": "PM-CYCLE12-D-minimal", "scope": SCOPE, "witnesses": rows}


def verify_report(report):
    require(report["schema"] == 1 and report["task"] == "PM-CYCLE12-D-minimal"
            and report["scope"] == SCOPE, "schema or scope mismatch")
    require([row["m"] for row in report["witnesses"]] == DEGREES, "wrong exceptional degrees")
    receipts = []
    for row in report["witnesses"]:
        require(row["m"] in DEGREES, "unsupported degree")
        f = Field(row["modulus"])
        require(f.m == row["m"], "field degree mismatch")
        expected = f.witness(row["y"])
        require(row == expected, "stored witness certificate mismatch")
        receipts.append({"m": f.m, "y": row["y"], "normal_rank": f.m,
            "normal_determinant": row["normality"]["determinant"],
            "character_powers": row["character_powers_y_minus_1_y_y_plus_1"],
            "joint_generation": True, "a_generates_S": row["subgroup_certificate"]["a_generates_S"]})
    return {"verified": True, "scope": SCOPE, "witnesses": receipts}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", type=Path)
    args = parser.parse_args()
    if args.check:
        result = verify_report(json.loads(args.check.read_text()))
    else:
        result = build_report()
        verify_report(result)
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()

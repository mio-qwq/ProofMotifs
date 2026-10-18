"""Independent coordinate certificate for a normal quartic bad parameter.

No ProofMotifs modules, logarithm arithmetic, or external packages are used.
Integers encode eight ascending base-three coefficients.  The field modulus
is X^8 + X^3 + 2.  A complete primitive-X cycle certifies the field.
"""
import itertools
import json
from math import gcd

M, Q, N = 8, 3**8, (3**8 - 1) // 2
WEIGHTS = [3**j for j in range(M)]


def coefficients(value):
    return [(value // w) % 3 for w in WEIGHTS]


def encode(cs):
    return sum(c * w for c, w in zip(cs, WEIGHTS))


def add(a, b):
    return encode([(x + y) % 3 for x, y in zip(coefficients(a), coefficients(b))])


def mul(a, b):
    aa, bb = coefficients(a), coefficients(b)
    out = [0] * 15
    for i in range(8):
        for j in range(8):
            out[i+j] = (out[i+j] + aa[i] * bb[j]) % 3
    for i in range(14, 7, -1):
        # X^8 = 1 + 2 X^3.
        out[i-8] = (out[i-8] + out[i]) % 3
        out[i-5] = (out[i-5] + 2 * out[i]) % 3
    return encode(out[:8])


def power(a, exponent):
    value = 1
    while exponent:
        if exponent & 1:
            value = mul(value, a)
        a = mul(a, a)
        exponent //= 2
    return value


def trace(a):
    result, x = 0, a
    for _ in range(M):
        result = add(result, x)
        x = power(x, 3)
    assert result in (0, 1, 2)
    return result


def determinant(rows):
    a = [coefficients(v) for v in rows]
    det = 1
    for j in range(M):
        pivot = next((i for i in range(j, M) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[pivot], a[j] = a[j], a[pivot]
            det = -det % 3
        p = a[j][j]
        det = det * p % 3
        a[j] = [(p * v) % 3 for v in a[j]]
        for i in range(j + 1, M):
            c = a[i][j]
            a[i] = [(x-c*y) % 3 for x, y in zip(a[i], a[j])]
    return det


def main():
    xs, x = [], 1
    for _ in range(Q - 1):
        xs.append(x)
        x = mul(x, 3)
    assert x == 1 and len(set(xs)) == Q-1 and 0 not in xs
    gamma = mul(3, 3)
    y, a, b = 4863, 4783, 2761
    assert mul(a, y) == add(y, 1)
    assert mul(b, y) == add(y, 2)
    assert add(add(1, a), b) == 0
    assert len({1, a, b}) == 3
    assert power(a, N) == power(b, N) == 1
    assert power(gamma, 76) == a and power(gamma, 2368) == b
    support_index = gcd(gcd(76, 2368), N)
    assert support_index == 4
    conjugates = [power(y, 3**j) for j in range(M)]
    det = determinant(conjugates)
    assert det != 0
    character_arguments = [add(y, 2), y, add(y, 1)]
    characters = [power(z, N) for z in character_arguments]
    assert len(set(characters)) == 1 and characters[0] != 0
    positions, k = [0, 2, 4, 6], 820
    four = [conjugates[i] for i in positions]
    quadratic_value = 0
    for u, v in itertools.combinations(four, 2):
        quadratic_value = add(quadratic_value, mul(u, v))
    assert quadratic_value == 2
    assert power(a, k) == power(b, k) == 1
    assert add(add(1, power(a, k)), power(b, k)) == 0
    orbit, current = [], k
    while current not in orbit:
        orbit.append(current)
        current = 3 * current % N
    affine = {0} | {3**j % N for j in range(M)}
    assert orbit == [820, 2460] and not affine.intersection(orbit)
    omitted_seed = [0, 2, 1672]
    omitted_edge = [power(gamma, i) for i in omitted_seed]
    assert omitted_edge == [1, 81, 164]
    assert add(add(*omitted_edge[:2]), omitted_edge[2]) == 0
    omitted_trace = [trace(power(u, k)) for u in omitted_edge]
    assert omitted_trace == [2, 1, 2] and sum(omitted_trace) % 3 == 2
    sparse_trace = [trace(power(u, k)) for u in [1, a, b]]
    assert sparse_trace == [2, 2, 2]
    report = {
        "field_modulus": [2, 0, 0, 1, 0, 0, 0, 0, 1],
        "primitive_X_cycle_length": len(xs), "gamma": gamma,
        "y": y, "a": a, "b": b,
        "y_coefficients": coefficients(y),
        "a_coefficients": coefficients(a), "b_coefficients": coefficients(b),
        "normal_conjugates": conjugates, "normal_determinant": det,
        "square_filter_characters": characters,
        "seed_exponents": [0, 76, 2368], "connectivity_index": support_index,
        "quartic_positions": positions, "quartic_frequency": k,
        "quadratic_value": quadratic_value,
        "extra_frequency_orbit": orbit,
        "sparse_trace_values": sparse_trace,
        "omitted_seed": omitted_seed, "omitted_edge": omitted_edge,
        "omitted_trace_values": omitted_trace, "omitted_trace_sum": 2,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

"""Independent exact F8 replay: convolution, brute inverses, rank, interpolation.

Does not import the primary construction implementation. Standard library only.
"""
from itertools import product
import json


def mul(a, b):
    value = 0
    for i in range(3):
        for j in range(3):
            if (a >> i) & (b >> j) & 1:
                value ^= 1 << (i + j)
    for degree in range(4, 2, -1):
        if value >> degree & 1:
            value ^= 11 << (degree - 3)
    return value


def power(a, n):
    value = 1
    for _ in range(n):
        value = mul(value, a)
    return value


def inverse(a):
    return next(b for b in range(1, 8) if mul(a, b) == 1)


def span_rank(rows):
    basis = {}
    for row in rows:
        reduced = row[:]
        for pivot, vector in sorted(basis.items()):
            coefficient = reduced[pivot]
            reduced = [x ^ mul(coefficient, y) for x, y in zip(reduced, vector)]
        if any(reduced):
            pivot = next(i for i, x in enumerate(reduced) if x)
            coefficient = inverse(reduced[pivot])
            basis[pivot] = [mul(coefficient, x) for x in reduced]
    return len(basis)


def report():
    monomials = [(i, j) for i in range(4) for j in range(4) if i + j <= 3]
    good = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1)]
    bad = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)]

    def evaluation(holes):
        return [[mul(power(x, i), power(y, j)) for i, j in monomials]
                for x, y in holes]

    ranks = [span_rank(evaluation(good)), span_rank(evaluation(bad))]
    assert ranks == [5, 4]
    weights = []
    for i in range(5):
        denominator = 1
        for j in range(5):
            if i != j:
                denominator = mul(denominator, i ^ j)
        weights.append(inverse(denominator))
    assert weights == [2, 6, 5, 7, 6]
    moments = []
    for n in range(5):
        value = 0
        for i in range(5):
            value ^= mul(weights[i], power(i, n))
        moments.append(value)
    assert moments == [0, 0, 0, 0, 1]

    # Solve five indicator interpolation systems, rather than using the
    # primary script's displayed Lagrange formula.
    matrix = evaluation(good)
    coefficients = []
    for target in range(5):
        augmented = [row[:] + [int(i == target)] for i, row in enumerate(matrix)]
        pivots = []
        for column in range(len(monomials)):
            found = next((r for r in range(len(pivots), 5) if augmented[r][column]), None)
            if found is None:
                continue
            row = len(pivots)
            augmented[row], augmented[found] = augmented[found], augmented[row]
            scale = inverse(augmented[row][column])
            augmented[row] = [mul(scale, x) for x in augmented[row]]
            for other in range(5):
                if other != row:
                    scale = augmented[other][column]
                    augmented[other] = [x ^ mul(scale, y)
                                        for x, y in zip(augmented[other], augmented[row])]
            pivots.append(column)
        solution = [0] * len(monomials)
        for row, column in enumerate(pivots):
            solution[column] = augmented[row][-1]
        coefficients.append(solution)

    def evaluate(polynomial, point):
        value = 0
        for coefficient, (i, j) in zip(polynomial, monomials):
            value ^= mul(coefficient, mul(power(point[0], i), power(point[1], j)))
        return value

    identity = [[int(i == j) for j in range(5)] for i in range(5)]
    assert [[evaluate(c, point) for c in coefficients] for point in good] == identity

    def gram(points):
        result = [[0] * 5 for _ in range(5)]
        for point in points:
            values = [evaluate(c, point) for c in coefficients]
            for i in range(5):
                for j in range(5):
                    result[i][j] ^= mul(values[i], values[j])
        return result

    universe = list(product(range(8), repeat=2))
    assert gram([point for point in universe if point not in good]) == identity
    lines = set()
    for slope, intercept in product(range(8), repeat=2):
        lines.add(tuple((x, mul(slope, x) ^ intercept) for x in range(8)))
    for x in range(8):
        lines.add(tuple((x, y) for y in range(8)))
    assert len(lines) == 72
    assert all(gram(line) == [[0] * 5 for _ in range(5)] for line in lines)
    return {'independent_field_arithmetic': 'bit convolution plus brute inverse',
            'ranks': ranks, 'barycentric_weights': weights, 'moments': moments,
            'independently_interpolated_line_grams': len(lines), 'punctured_gram': 'I5'}


if __name__ == '__main__':
    print(json.dumps(report(), indent=2, sort_keys=True))

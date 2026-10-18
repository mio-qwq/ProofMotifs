"""Two punctured subspaces: an exact coordinate model for a subgroup family.

All arithmetic is coordinatewise over F3. No extension-field tables, project
finite-field class, or GF(729) construction is used. The full automorphism
group order is derived from the proved wreath product, not enumerated. Only
the eight-point component in dimension two is exhaustively enumerated.
"""
from itertools import combinations, permutations, product
import json
from math import factorial


def add_vector(a: int, b: int, dimension: int) -> int:
    return sum(((a//3**j+b//3**j) % 3)*3**j for j in range(dimension))


def negative_vector(a: int, dimension: int) -> int:
    return sum((-(a//3**j) % 3)*3**j for j in range(dimension))


def rank3(rows: list[list[int]], width: int) -> int:
    basis: dict[int, list[int]] = {}
    for raw in rows:
        if len(raw) != width or any(x not in (0, 1, 2) for x in raw):
            raise ValueError('require a rectangular matrix over F3')
        row = list(raw)
        for pivot in sorted(basis):
            factor = row[pivot]
            if factor:
                row = [(x-factor*y) % 3 for x, y in zip(row, basis[pivot])]
        pivot = next((j for j, x in enumerate(row) if x), None)
        if pivot is not None:
            if row[pivot] == 2:
                row = [(2*x) % 3 for x in row]
            basis[pivot] = row
    return len(basis)


def component_hypergraph(dimension: int) -> tuple[tuple[int, ...], tuple[tuple[int, int, int], ...]]:
    if not isinstance(dimension, int) or dimension < 1:
        raise ValueError('dimension must be a positive integer')
    vertices = tuple(range(1, 3**dimension))
    edges = []
    for u, v in combinations(vertices, 2):
        w = negative_vector(add_vector(u, v, dimension), dimension)
        if w > v:
            edges.append((u, v, w))
    return vertices, tuple(edges)


def components(vertices: tuple, edges: tuple) -> list[list]:
    adjacent = {x: set() for x in vertices}
    for edge in edges:
        for x in edge:
            adjacent[x].update(y for y in edge if y != x)
    unseen = set(vertices)
    answer = []
    while unseen:
        stack = [min(unseen)]
        reached = set(stack)
        while stack:
            x = stack.pop()
            for y in adjacent[x]-reached:
                reached.add(y)
                stack.append(y)
        unseen -= reached
        answer.append(sorted(reached))
    return answer


def gl_order(dimension: int) -> int:
    q = 3**dimension
    answer = 1
    for j in range(dimension):
        answer *= q-3**j
    return answer


def enumerate_dimension_two_component() -> dict:
    vertices, edges = component_hypergraph(2)
    edge_set = set(edges)
    automorphisms = set()
    examined = 0
    for images in permutations(vertices):
        examined += 1
        mapping = dict(zip(vertices, images))
        if all(tuple(sorted(mapping[x] for x in edge)) in edge_set for edge in edges):
            automorphisms.add(images)
    linear_actions = set()
    for columns in product(range(1, 9), repeat=2):
        matrix = [[columns[j]//3**i % 3 for j in range(2)] for i in range(2)]
        if rank3(matrix, 2) != 2:
            continue
        image = []
        for x in vertices:
            a, b = x % 3, x//3
            value = 0
            for coefficient, column in ((a, columns[0]), (b, columns[1])):
                for _ in range(coefficient):
                    value = add_vector(value, column, 2)
            image.append(value)
        linear_actions.add(tuple(image))
    if automorphisms != linear_actions:
        raise AssertionError('component automorphisms differ from GL(2,3) actions')
    return dict(vertex_count=8, edge_count=8,
                all_vertex_permutations_examined=examined,
                automorphism_count=len(automorphisms),
                gl_action_count=len(linear_actions),
                full_group_computation='one component only; no full sixteen-point group enumeration')


def obstruction_report(dimension: int, enumerate_component: bool = False) -> dict:
    local_vertices, local_edges = component_hypergraph(dimension)
    s = 3**dimension
    vertices = tuple((component, x) for component in (0, 1) for x in local_vertices)
    edges = tuple(tuple((component, x) for x in edge)
                  for component in (0, 1) for edge in local_edges)
    index = {x: j for j, x in enumerate(vertices)}
    rows = []
    for edge in edges:
        row = [0]*len(vertices)
        for x in edge:
            row[index[x]] = 1
        rows.append(row)
    rank = rank3(rows, len(vertices))
    affine = [[1]*len(vertices)]
    for component in (0, 1):
        for j in range(dimension):
            affine.append([(x//3**j) % 3 if c == component else 0
                           for c, x in vertices])
    extra = [component for component, x in vertices]
    order_two_mode = [1 if component == 0 else 2 for component, x in vertices]
    if any(extra[j] != 2*(1-value) % 3 for j, value in enumerate(order_two_mode)):
        raise AssertionError('the component indicator differs from (1-tau)/2')
    extra_edge_sums = [sum(extra[index[x]] for x in edge) % 3 for edge in edges]
    if any(extra_edge_sums):
        raise AssertionError('component constant fails a line relation')
    affine_rank = rank3(affine, len(vertices))
    augmented_rank = rank3([*affine, extra], len(vertices))
    if (len(vertices)-rank != 2*dimension+2 or affine_rank != 2*dimension+1
            or augmented_rank != 2*dimension+2):
        raise AssertionError('computed incidence kernel differs from the structural theorem')
    component_sizes = sorted(map(len, components(vertices, edges)))
    expected_sizes = [s-1, s-1] if dimension >= 2 else [1]*4
    if component_sizes != expected_sizes:
        raise AssertionError('unexpected connected components')
    full_group_order = (2*gl_order(dimension)**2 if dimension >= 2 else factorial(4))
    report = dict(component_dimension=dimension, subfield_size=s,
                  ambient_dimension=2*dimension, ambient_field_order=s*s,
                  multiplicative_subgroup_index=(s+1)//2,
                  vertex_count=len(vertices), edge_count=len(edges),
                  incidence_rank=rank, incidence_kernel_dimension=len(vertices)-rank,
                  ambient_affine_dimension=affine_rank,
                  extra_component_constant=extra,
                  order_two_mode=order_two_mode,
                  order_two_mode_cyclic_exponent=s-1,
                  nonaffine_augmented_dimension=augmented_rank,
                  exact_extra_line_equations_checked=len(edges),
                  connected_component_sizes=component_sizes,
                  component_gl_order=gl_order(dimension),
                  full_automorphism_order=full_group_order,
                  full_group_order_method=('proved wreath-product formula, not enumerated'
                                           if dimension >= 2 else
                                           'four vertices with no edges: S4'),
                  scalar_frobenius_subgroup_order=2*(s-1)*(2*dimension),
                  arithmetic='exact direct-sum vector coordinates over F3; no extension-field tables')
    if enumerate_component:
        if dimension != 2:
            raise ValueError('component permutation enumeration is restricted to dimension two')
        report['component_enumeration'] = enumerate_dimension_two_component()
    return report


def main() -> None:
    print(json.dumps(dict(schema=1, randomized=False,
                          family='two independent punctured subspaces',
                          reports=[obstruction_report(1), obstruction_report(2, True),
                                   obstruction_report(3)]), sort_keys=True, indent=2))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Classical dynamic evaluation, explicit acyclic arithmetic/zero-query DAG.

Outputs are literal discrete labels, NEVER encodings of field registers.
Primehood is promised. No field ordering, field-to-integer conversion, hidden
oracle, arbitrary Python execution or callback is part of this grammar.
"""
import json
from factor_readout import checked_input, trim, add, neg, mul, mod, gcd, divmod_poly


def inverse(a, f, p):
    r0, r1, s0, s1 = f, a, [], [1]
    while r1:
        q, r = divmod_poly(r0, r1, p)
        r0, r1 = r1, r
        s0, s1 = s1, add(s0, neg(mul(q, s1, p), p), p)
    if len(r0) != 1:
        raise ValueError('unit inverse required')
    return mod([x*pow(r0[0], -1, p) % p for x in s0], f, p)


def validate(program):
    if not isinstance(program, list) or not program:
        raise ValueError('nonempty instruction DAG required')
    for i, node in enumerate(program):
        if not isinstance(node, dict):
            raise ValueError('instruction object required')
        op = node.get('op')
        if op not in ('const', 'add', 'sub', 'mul', 'inv', 'test', 'return'):
            raise ValueError('unsupported field/control operation')
        if op == 'return':
            if type(node.get('label')) is not str:
                raise ValueError('literal discrete string required')
            continue
        targets = ['zero', 'nonzero'] if op == 'test' else ['next']
        for key in targets:
            target = node.get(key)
            if type(target) is not int or not i < target < len(program):
                raise ValueError('forward DAG target required')
        if op == 'const':
            if type(node.get('value')) is not int:
                raise ValueError('integer field constant required')
        else:
            args = ['a', 'b'] if op in ('add', 'sub', 'mul') else ['a']
            if any(type(node.get(key)) is not str for key in args):
                raise ValueError('register-name operand required')
        if op != 'test' and type(node.get('dest')) is not str:
            raise ValueError('register-name destination required')


def execute(p, f, program, inputs):
    """Return SPLIT at first mixed test, else COMMON discrete output.

    Definedness of the scalar algorithm on all components is a theorem
    hypothesis; undefined zero inverses/registers are rejected explicitly.
    """
    f = checked_input(p, f)
    validate(program)
    n = len(f)-1
    if not isinstance(inputs, dict):
        raise ValueError('named quotient inputs required')
    registers = {}
    for name, a in inputs.items():
        if (type(name) is not str or not isinstance(a, list) or len(a) > n or
                any(type(x) is not int for x in a)):
            raise ValueError('degree<n integer input with string name required')
        registers[name] = trim(a, p)
    pc, visited = 0, []
    while True:
        node = program[pc]
        op = node['op']
        visited.append(pc)
        if op == 'return':
            return {'status': 'COMMON', 'label': node['label'], 'visited': visited,
                    'meaning': 'all component executions have this discrete label'}
        try:
            a = registers[node['a']] if op != 'const' else None
            b = registers[node['b']] if op in ('add', 'sub', 'mul') else None
        except KeyError as exc:
            raise ValueError('uninitialized register: invalid scalar procedure') from exc
        if op in ('inv', 'test'):
            g = gcd(f, a, p)
            if 1 < len(g) < len(f):
                return {'status': 'SPLIT', 'factor': g, 'tested': a,
                        'instruction': pc, 'operation': op, 'visited': visited}
            if op == 'inv':
                if g != [1]:
                    raise ValueError('undefined scalar inverse in every component')
                value = inverse(a, f, p)
            else:
                pc = node['zero'] if g == f else node['nonzero']
                continue
        elif op == 'const':
            value = trim([node['value']], p)
        elif op == 'add':
            value = add(a, b, p)
        elif op == 'sub':
            value = add(a, neg(b, p), p)
        else:
            value = mod(mul(a, b, p), f, p)
        registers[node['dest']] = value
        pc = node['next']


def demo():
    program = [
        {'op': 'const', 'value': 1, 'dest': 'one', 'next': 1},
        {'op': 'sub', 'a': 'x', 'b': 'one', 'dest': 'difference', 'next': 2},
        {'op': 'test', 'a': 'difference', 'zero': 3, 'nonzero': 4},
        {'op': 'return', 'label': 'zero'},
        {'op': 'return', 'label': 'nonzero'}]
    return {'contract': 'supplied program; not discovery of a distinguishing invariant',
            'mixed': execute(7, [2, 4, 1], program, {'x': [0, 1]}),
            'same': execute(7, [6, 2, 1], program, {'x': [0, 1]}),
            'raw_field_output_control': 'return-register is outside the discrete grammar'}


if __name__ == '__main__':
    print(json.dumps(demo(), indent=2, sort_keys=True))

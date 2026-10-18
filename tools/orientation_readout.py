#!/usr/bin/env python3
"""Source142/Ronyai-style conditional even split, no roots supplied.

Input p promised odd prime; F checked squarefree and totally split using
Frobenius. A full 2-primary generator is supplied AND checked, not discovered.
Arithmetic stays in Fp[X,Y]/(F(X),F(Y)); no coordinate roots are enumerated.
"""
import json
from factor_readout import checked_input, fixed_basis, mod, gcd, divmod_poly


class Tensor:
    def __init__(self, p, f):
        self.p, self.f, self.n = p, f, len(f)-1
        self.one = [1]+[0]*(self.n**2-1)

    def add(self, a, b):
        return [(x+y) % self.p for x, y in zip(a, b)]

    def neg(self, a):
        return [-x % self.p for x in a]

    def scale(self, a, c):
        return [c*x % self.p for x in a]

    def scalar(self, c):
        return self.scale(self.one, c)

    def multiply(self, a, b):
        n, p, f = self.n, self.p, self.f
        width = 2*n-1
        c = [[0]*width for _ in range(width)]
        for ij, x in enumerate(a):
            if not x:
                continue
            i, j = divmod(ij, n)
            for kl, y in enumerate(b):
                if y:
                    k, l = divmod(kl, n)
                    c[i+k][j+l] = (c[i+k][j+l]+x*y) % p
        for i in range(width-1, n-1, -1):
            for j in range(width):
                for k in range(n):
                    c[i-n+k][j] = (c[i-n+k][j]-c[i][j]*f[k]) % p
        for j in range(width-1, n-1, -1):
            for i in range(n):
                for k in range(n):
                    c[i][j-n+k] = (c[i][j-n+k]-c[i][j]*f[k]) % p
        return [c[i][j] for i in range(n) for j in range(n)]

    def power(self, a, exponent):
        if type(exponent) is not int or exponent < 0:
            raise ValueError('nonnegative integer tensor exponent required')
        out = self.one[:]
        while exponent:
            if exponent & 1:
                out = self.multiply(out, a)
            a = self.multiply(a, a)
            exponent >>= 1
        return out

    def swap(self, a):
        return [a[j*self.n+i] for i in range(self.n) for j in range(self.n)]

    def partial_trace(self, a):
        # Trace of multiplication, not a normalized trace or evaluation oracle.
        traces = []
        for j in range(self.n):
            total = 0
            for k in range(self.n):
                v = mod([0]*(j+k)+[1], self.f, self.p)
                total += v[k] if k < len(v) else 0
            traces.append(total % self.p)
        return mod([sum(a[i*self.n+j]*traces[j] for j in range(self.n)) % self.p
                    for i in range(self.n)], self.f, self.p)


def setup(p, f):
    f = checked_input(p, f)
    n = len(f)-1
    if p == 2 or n < 2 or p <= n or n % 2:
        raise ValueError('odd prime p > even N >= 2 required')
    if len(fixed_basis(p, f)) != n:
        raise ValueError('totally split polynomial required')
    return Tensor(p, f)


def verify_orientation(p, f, e):
    r = setup(p, f)
    if (not isinstance(e, list) or len(e) != r.n**2 or
            any(type(x) is not int for x in e)):
        raise ValueError('N by N integer tensor coefficient list required')
    e = [x % p for x in e]
    delta = [0]*(r.n**2)
    delta[r.n], delta[1] = 1, p-1
    off = r.power(delta, p-1)
    if r.multiply(e, e) != e or r.add(e, r.swap(e)) != off:
        raise ValueError('idempotent orientation/transpose certificate failed')
    c = r.partial_trace(e)
    if len(c) < 2:
        raise ArithmeticError('even tournament row-count theorem violated')
    for a in range(r.n):
        h = gcd(r.f, [(c[0] if c else 0)-a]+c[1:], p)
        if 1 < len(h) < len(r.f):
            return {'p': p, 'modulus': r.f, 'orientation': e,
                    'partial_trace': c, 'label': a, 'factor': h,
                    'primary_generator_discovery': 'NOT performed',
                    'primehood': 'input promise'}
    raise ArithmeticError('bounded scalar-label theorem violated')


def construct(p, f, u):
    r = setup(p, f)
    if type(u) is not int or not 0 < u < p:
        raise ValueError('canonical supplied primary generator required')
    t, s = p-1, 0
    while t % 2 == 0:
        t //= 2
        s += 1
    if pow(u, 1 << s, p) != 1 or pow(u, 1 << (s-1), p) == 1:
        raise ValueError('supplied element lacks full 2-primary order')
    delta = [0]*(r.n**2)
    delta[r.n], delta[1] = 1, p-1
    off = r.power(delta, p-1)
    z = r.power(delta, t)
    parts = [(off, 0)]
    max_parts = 1
    for j in range(s):
        exponent = 1 << (s-1-j)
        zpower = r.power(z, exponent)
        new_parts = []
        for mask, ell in parts:
            difference = r.add(zpower, r.scalar(-pow(u, ell*exponent, p)))
            difference = r.multiply(mask, difference)
            zero = r.add(mask, r.neg(r.power(difference, p-1)))
            one = r.add(mask, r.neg(zero))
            if any(zero):
                new_parts.append((zero, ell))
            if any(one):
                new_parts.append((one, ell+(1 << j)))
        parts = new_parts
        max_parts = max(max_parts, len(parts))
        if len(parts) > r.n*(r.n-1):
            raise ArithmeticError('disjoint nonempty mask bound violated')
    orientation = [0]*(r.n**2)
    for mask, ell in parts:
        if ell < (1 << (s-1)):
            orientation = r.add(orientation, mask)
    result = verify_orientation(p, f, orientation)
    result.update({'supplied_primary_generator': u, 'digit_levels': s,
                   'maximum_nonempty_masks': max_parts})
    return result


def demo():
    # The solver receives coefficients, not the roots used to design this test.
    # The supplied u=28 has order32, checked by the constructor.
    p, f = 97, [24, -50, 35, -10, 1]
    out = construct(p, f, 28)
    q, rem = divmod_poly(f, out['factor'], p)
    assert not rem and len(q) > 1
    return out


if __name__ == '__main__':
    print(json.dumps(demo(), indent=2, sort_keys=True))

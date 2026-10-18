"""Independent coordinate arithmetic for the m=3,4 obstructions and m=8 boundary.

No ProofMotifs imports, no power/log arithmetic, no shared normality checker.
"""
import json


def audit(mod, quartic_case=False):
    m = len(mod) - 1
    q = 3 ** m
    def vec(a):
        return [(a // 3**j) % 3 for j in range(m)]
    def enc(a):
        return sum(c * 3**j for j, c in enumerate(a))
    def add(a, b):
        return enc([(x+y) % 3 for x, y in zip(vec(a), vec(b))])
    def neg(a):
        return enc([(-x) % 3 for x in vec(a)])
    def mul(a, b):
        av, bv = vec(a), vec(b)
        c = [0] * (2*m-1)
        for i in range(m):
            for j in range(m):
                c[i+j] = (c[i+j] + av[i]*bv[j]) % 3
        for d in range(2*m-2, m-1, -1):
            z = c[d]
            for j in range(m+1):
                c[d-m+j] = (c[d-m+j] - z*mod[j]) % 3
        return enc(c[:m])
    def powr(a, e):
        r = 1
        while e:
            if e & 1:
                r = mul(r, a)
            a = mul(a, a)
            e >>= 1
        return r
    def pgcd(a,b):
        def trim(a):
            a = a[:]
            while a and a[-1] == 0:
                a.pop()
            return a
        a,b = trim(a),trim(b)
        while b:
            while a and len(a)>=len(b):
                shift = len(a)-len(b)
                c = a[-1]*b[-1] % 3
                for j,v in enumerate(b):
                    a[shift+j] = (a[shift+j]-c*v) % 3
                a = trim(a)
            a,b = b,a
        return [(v*a[-1]) % 3 for v in a] if a else []
    if quartic_case:
        # Rabin for degree eight needs only the proper-degree divisor four.
        assert m == 8 and powr(3,q) == 3
        assert pgcd(mod,vec(add(powr(3,81),neg(3)))) == [1]
        assert powr(3,q-1) == 1
        assert all(powr(3,(q-1)//p) != 1 for p in (2,5,41))
    else:
        # Direct no-zero-divisor check certifies the two small quotients.
        assert all(mul(a,b) for a in range(1,q) for b in range(1,q))
    def chi(a):
        if not a:
            return 0
        c = powr(a, (q-1)//2)
        assert c in (1,2)
        return 1 if c == 1 else -1
    def rank(rows):
        rows = [r[:] for r in rows]
        k = 0
        for col in range(m):
            piv = next((i for i in range(k,m) if rows[i][col]), None)
            if piv is None:
                continue
            rows[k], rows[piv] = rows[piv], rows[k]
            z = rows[k][col]
            rows[k] = [(z*v) % 3 for v in rows[k]]
            for i in range(m):
                if i != k:
                    z = rows[i][col]
                    rows[i] = [(u-z*v) % 3 for u,v in zip(rows[i], rows[k])]
            k += 1
        return k
    if quartic_case:
        y,a,b = 4863,4783,2761
        assert mul(a,y) == add(y,1)
        assert mul(b,y) == add(y,2)
        assert add(add(1,a),b) == 0 and len({1,a,b}) == 3
        conjugates = [powr(y,3**j) for j in range(m)]
        assert rank([vec(c) for c in conjugates]) == 8
        signs = [chi(add(y,c)) for c in (2,0,1)]
        assert len(set(signs)) == 1 and signs[0]
        gamma = mul(3,3)
        assert powr(gamma,76) == a and powr(gamma,2368) == b
        assert chi(a) == chi(b) == 1
        from math import gcd
        index = gcd(gcd(76,2368),(q-1)//2)
        assert index == 4
        k = 820
        assert powr(a,k) == powr(b,k) == 1
        quadratic = 0
        four = [conjugates[j] for j in (0,2,4,6)]
        for i in range(4):
            for j in range(i+1,4):
                quadratic = add(quadratic,mul(four[i],four[j]))
        assert quadratic == 2
        def trace(c):
            result = 0
            for j in range(m):
                result = add(result,powr(c,3**j))
            assert result in (0,1,2)
            return result
        edge = [1,81,164]
        assert all(chi(u) == 1 for u in edge)
        assert add(add(edge[0],edge[1]),edge[2]) == 0
        values = [trace(powr(u,k)) for u in edge]
        assert values == [2,1,2] and sum(values) % 3 == 2
        rows = [vec(c) for c in conjugates]
        det = 1
        for j in range(m):
            piv = next(i for i in range(j,m) if rows[i][j])
            if piv != j:
                rows[piv],rows[j] = rows[j],rows[piv]
                det = -det % 3
            z = rows[j][j]
            det = det*z % 3
            rows[j] = [(v*z) % 3 for v in rows[j]]
            for i in range(j+1,m):
                z = rows[i][j]
                rows[i] = [(u-z*v) % 3 for u,v in zip(rows[i],rows[j])]
        assert det == 2
        return {'m':m,'modulus':mod,'y':y,'a':a,'b':b,
                'Rabin_and_primitive_X_checks':True,
                'normal_rank':8,'normal_determinant':det,
                'normal_conjugates':conjugates,'characters':signs,
                'seed':[0,76,2368],'component_index':index,
                'component_kernel_lower_bound':36,
                'quartic_frequency':k,'quartic_Q':quadratic,
                'separating_edge':edge,'trace_values':values,'trace_sum':2}
    normals, patterns, intersections, histogram = [], [], [], {}
    alt_zero = []
    for y in range(q):
        cs = [powr(y,3**j) for j in range(m)]
        r = rank([vec(c) for c in cs])
        if r == m:
            normals.append(y)
        signs = [chi(add(y,c)) for c in (2,0,1)]
        if signs[0] and len(set(signs)) == 1:
            patterns.append(y)
            histogram[r] = histogram.get(r,0) + 1
            if r == m:
                intersections.append(y)
            if m == 4:
                alt = add(add(cs[0],neg(cs[1])), add(cs[2],neg(cs[3])))
                if alt == 0:
                    alt_zero.append(y)
                assert alt == 0 or cs[0] == cs[2]
    return {'m':m, 'modulus':mod, 'normal_count':len(normals),
            'pattern_count':len(patterns), 'intersection':intersections,
            'pattern_rank_histogram':histogram, 'pattern_elements':patterns,
            'pattern_alternating_trace_zero':alt_zero}


if __name__ == '__main__':
    reports = [audit([1,2,0,1]), audit([2,1,0,0,1])]
    assert all(not r['intersection'] for r in reports)
    reports.append(audit([2,0,0,1,0,0,0,0,1],quartic_case=True))
    print(json.dumps(reports, indent=2, sort_keys=True))

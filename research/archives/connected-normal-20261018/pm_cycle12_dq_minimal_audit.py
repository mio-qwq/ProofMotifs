"""Independent, no-search polynomial/list audit of six minimal witnesses.

Only Python's standard library is imported. No project or witness-generation
code, discrete logarithm table or primitive-X assumption is used.
"""
import hashlib
import json

INPUT = '/tmp/pm_cycle12_d_minimal.json'
DEGREES = (5, 6, 7, 8, 10, 16)


def trim(a):
    a = [x % 3 for x in a]
    while a and not a[-1]:
        a.pop()
    return a


def subtract(a, b):
    return trim([(a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def plus(a, b):
    return subtract(a, [-x for x in b])


def product(a, b):
    if not a or not b:
        return []
    out = [0] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return trim(out)


def divide(a, b):
    a, b = trim(a), trim(b)
    assert b
    quotient = [0] * max(0,len(a)-len(b)+1)
    while len(a) >= len(b):
        shift = len(a)-len(b)
        c = a[-1]*b[-1] % 3
        quotient[shift] = c
        for j in range(len(b)):
            a[shift+j] -= c*b[j]
        a = trim(a)
    return trim(quotient), a


def gcd_poly(a, b):
    a, b = trim(a), trim(b)
    while b:
        a, b = b, divide(a,b)[1]
    return trim([a[-1]*x for x in a]) if a else []


def times_mod(a,b,f):
    return divide(product(a,b),f)[1]


def power_mod(a,e,f):
    ans = [1]
    for bit in bin(e)[2:]:
        ans = times_mod(ans,ans,f)
        if bit == '1':
            ans = times_mod(ans,a,f)
    return ans


def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p,0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n,0)+1
    return out


def decode(n,m):
    return trim([(n//3**j)%3 for j in range(m)])


def encode(a):
    return sum((x % 3)*3**j for j,x in enumerate(a))


def determinant(columns,m):
    rows = [[columns[j][i] if i < len(columns[j]) else 0 for j in range(m)]
            for i in range(m)]
    det = 1
    for j in range(m):
        pivot = next((i for i in range(j,m) if rows[i][j]),None)
        if pivot is None:
            return 0
        if pivot != j:
            rows[j],rows[pivot] = rows[pivot],rows[j]
            det = -det % 3
        v = rows[j][j]
        det = det*v % 3
        rows[j] = [(v*x)%3 for x in rows[j]]
        for i in range(j+1,m):
            c = rows[i][j]
            rows[i] = [(a-c*b)%3 for a,b in zip(rows[i],rows[j])]
    return det


def audit(m,f,y,a,b):
    f,y,a,b = trim(f),trim(y),trim(a),trim(b)
    assert len(f) == m+1 and f[-1] == 1
    q,N = 3**m,(3**m-1)//2
    assert N < 2**25
    x = [0,1]
    frob_x = [x]
    for _ in range(m):
        frob_x.append(power_mod(frob_x[-1],3,f))
    assert frob_x[m] == x
    rabin = []
    for p in factor(m):
        g = gcd_poly(f,subtract(frob_x[m//p],x))
        assert g == [1]
        rabin.append({'prime_divisor_of_degree':p,'gcd':g})
    conjugates = [y]
    for _ in range(m-1):
        conjugates.append(power_mod(conjugates[-1],3,f))
    det = determinant(conjugates,m)
    assert det
    ym,yp = subtract(y,[1]),plus(y,[1])
    chars = [power_mod(z,N,f) for z in (ym,y,yp)]
    assert chars[0] == chars[1] == chars[2] and chars[0] in ([1],[2])
    assert times_mod(a,y,f) == yp
    assert times_mod(b,y,f) == ym
    assert plus(plus([1],a),b) == []
    assert len({tuple([1]),tuple(a),tuple(b)}) == 3
    assert power_mod(a,N,f) == power_mod(b,N,f) == [1]
    facN = factor(N)
    rebuild = 1
    for p,e in facN.items():
        rebuild *= p**e
    assert rebuild == N
    exclusions = []
    for p in facN:
        ap,bp = power_mod(a,N//p,f),power_mod(b,N//p,f)
        assert ap != [1] or bp != [1]
        exclusions.append({'prime':p,'exponent_N_over_p':N//p,
                           'a_power_encoded':encode(ap),'b_power_encoded':encode(bp),
                           'at_least_one_not_one':True})
    return {'m':m,'q':q,'N':N,'modulus_ascending':f,
            'rabin_final_x_power_equals_x':True,'rabin_proper_divisor_gcds':rabin,
            'y_encoded':encode(y),'a_encoded':encode(a),'b_encoded':encode(b),
            'normal_conjugates_encoded':[encode(z) for z in conjugates],
            'normal_determinant':det,'normal_rank':m,
            'equal_nonzero_characters':[encode(c) for c in chars],
            'ratio_identities_and_distinct_seed':True,'a_b_square_power_checks':True,
            'N_trial_factorization':[[p,e] for p,e in facN.items()],
            'maximal_subgroup_exclusions':exclusions,
            'connected_generation_certified':True}


def main():
    with open(INPUT,'rb') as stream:
        raw = stream.read()
    data = json.loads(raw)
    # The schema adapter is filled only after inspecting the supplied JSON;
    # the arithmetic above is independent of its generation algorithm.
    rows = data['witnesses']
    assert tuple(row['m'] for row in rows) == DEGREES
    out = []
    for row in rows:
        m = row['m']
        checked = audit(m,row['modulus'],decode(row['y'],m),
                        decode(row['a'],m),decode(row['b'],m))
        # Independently recomputed values must match every supplied numerical
        # certificate field, not merely satisfy the desired qualitative claims.
        assert row['q'] == checked['q'] and row['N'] == checked['N']
        assert row['normality']['conjugates'] == checked['normal_conjugates_encoded']
        assert row['normality']['rank'] == checked['normal_rank']
        assert row['normality']['determinant'] == checked['normal_determinant']
        assert row['character_powers_y_minus_1_y_y_plus_1'] == checked['equal_nonzero_characters']
        for name in ('y','a','b'):
            assert row[name+'_coefficients'] == [(row[name]//3**j)%3 for j in range(m)]
        cert = row['subgroup_certificate']
        assert cert['a_b_pow_N'] == [1,1]
        assert cert['joint_generation'] is True
        expected_factors = [p for p,e in checked['N_trial_factorization'] for _ in range(e)]
        assert cert['N_factorization_with_multiplicity'] == expected_factors
        excludes = checked['maximal_subgroup_exclusions']
        assert cert['a_generates_S'] == all(x['a_power_encoded'] != 1 for x in excludes)
        assert cert['b_generates_S'] == all(x['b_power_encoded'] != 1 for x in excludes)
        assert cert['maximal_subgroup_exclusions'] == [
            {'prime_divisor_N':x['prime'],'a_power':x['a_power_encoded'],
             'b_power':x['b_power_encoded']} for x in excludes]
        assert row['Rabin']['X_pow_q'] == 3
        expected_rabin = []
        for p in factor(m):
            remainder = subtract(power_mod([0,1],3**(m//p),row['modulus']),[0,1])
            expected_rabin.append({'prime_divisor_m':p,'gcd':[1],
                                   'remainder':encode(remainder)})
        assert row['Rabin']['proper_degree_gcd_checks'] == expected_rabin
        checked['all_supplied_numerical_fields_match'] = True
        out.append(checked)
    print(json.dumps({'task':'PM-CYCLE12-DQ-MINIMAL-AUDIT',
                      'input_sha256':hashlib.sha256(raw).hexdigest(),
                      'scope_degrees':list(DEGREES),'search_performed':False,
                      'arithmetic':'ordinary polynomial/list arithmetic over F3; standard library only',
                      'all_checks_passed':True,'certificates':out},sort_keys=True,indent=2))


if __name__ == '__main__':
    main()

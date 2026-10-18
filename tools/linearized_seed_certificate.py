"""Exact degree-13 forbidden-frequency certificate; no full field table.

Arithmetic is ordinary coefficient-list F3 arithmetic, with no project imports.
The certificate proves a sparse kernel lower bound, not its exact dimension.
"""
import json
import argparse
from pathlib import Path
from itertools import product
from math import isqrt

M=13
Q=3**M
N=(Q-1)//2

def require(condition, message):
    if not condition:
        raise ValueError(message)

def trim(a):
    a=list(a)
    while a and a[-1]==0:
        a.pop()
    return a

def add(a,b):
    return trim([((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0))%3
                 for i in range(max(len(a),len(b)))])

def neg(a):
    return [(-v)%3 for v in a]

def divrem(a,b):
    a=trim(a)
    quotient=[0]*max(0,len(a)-len(b)+1)
    while a and len(a)>=len(b):
        shift=len(a)-len(b)
        scalar=a[-1]*b[-1]%3
        quotient[shift]=scalar
        for i,v in enumerate(b):
            a[i+shift]=(a[i+shift]-scalar*v)%3
        a=trim(a)
    return trim(quotient),a

def mulraw(a,b):
    if not a or not b:
        return []
    c=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):
            c[i+j]=(c[i+j]+v*w)%3
    return trim(c)

def mul(a,b,f):
    return divrem(mulraw(a,b),f)[1]

def power(a,e,f):
    out=[1]
    while e:
        if e&1:
            out=mul(out,a,f)
        a=mul(a,a,f)
        e//=2
    return out

def pgcd(a,b):
    while b:
        a,b=b,divrem(a,b)[1]
    return [(v*a[-1])%3 for v in a] if a else []

def irreducible(f):
    x=[0,1]
    if pgcd(f,add(power(x,3,f),neg(x)))!=[1]:
        return False
    return power(x,Q,f)==x

def choose_modulus():
    for j in range(1,M):
        for c,d in product((1,2),repeat=2):
            f=[d]+[0]*(M-1)+[1]
            f[j]=c
            if irreducible(f):
                return f
    raise RuntimeError('no tested sparse modulus')

def nullspace(matrix):
    a=[row[:] for row in matrix]
    pivots=[]
    row=0
    for col in range(M):
        pivot=next((i for i in range(row,M) if a[i][col]),None)
        if pivot is None:
            continue
        a[row],a[pivot]=a[pivot],a[row]
        scalar=a[row][col]
        a[row]=[v*scalar%3 for v in a[row]]
        for i in range(M):
            if i!=row and a[i][col]:
                scalar=a[i][col]
                a[i]=[(v-scalar*w)%3 for v,w in zip(a[i],a[row])]
        pivots.append(col)
        row+=1
    basis=[]
    for free in range(M):
        if free in pivots:
            continue
        v=[0]*M
        v[free]=1
        for i,col in enumerate(pivots):
            v[col]=(-a[i][free])%3
        basis.append(trim(v))
    return basis

def trace(a,f):
    out=[]
    for _ in range(M):
        out=add(out,a)
        a=power(a,3,f)
    require(len(out)<=1, 'trace escaped prime field')
    return out[0] if out else 0

def solve():
    factors=[p for p in range(2,isqrt(N)+1) if N%p==0]
    assert not factors
    f=choose_modulus()
    x=[0,1]
    assert power(x,Q-1,f)==[1]
    assert power(x,N,f)==[2]
    assert power(x,2,f)!=[1]
    def linear(y):
        return add(add(y,power(y,3,f)),power(y,81,f))
    cols=[linear([0]*i+[1]) for i in range(M)]
    matrix=[[(cols[j][i] if i<len(cols[j]) else 0) for j in range(M)] for i in range(M)]
    basis=nullspace(matrix)
    assert len(basis)==4
    h=[2]+[0]*12+[1]
    p=[1,1,0,0,1]
    symbolic_gcd=pgcd(h,p)
    assert len(symbolic_gcd)==5
    candidates=[]
    for coefficients in product(range(3),repeat=len(basis)):
        y=[]
        for scalar,v in zip(coefficients,basis):
            y=add(y,[scalar*x%3 for x in v])
        assert linear(y)==[]
        if len(y)<=1:
            continue
        inv=power(y,Q-2,f)
        a=mul(add(y,[1]),inv,f)
        b=mul(add(y,[2]),inv,f)
        assert add(add([1],a),b)==[]
        if power(a,N,f)==[1] and power(b,N,f)==[1]:
            assert len({tuple([1]),tuple(a),tuple(b)})==3
            assert add(add([1],power(a,85,f)),power(b,85,f))==[]
            candidates.append({'y':y,'a':a,'b':b})
    separator=None
    for integer in range(3,500):
        a=[]
        v=integer
        while v:
            a.append(v%3)
            v//=3
        b=neg(add([1],a))
        if a==[1] or b==[1] or a==b or not b:
            continue
        if power(a,N,f)==[1] and power(b,N,f)==[1]:
            values=[trace([1],f),trace(power(a,85,f),f),trace(power(b,85,f),f)]
            if sum(values)%3:
                separator={'a':a,'b':b,'trace_values':values,'trace_sum':sum(values)%3}
                break
    orbit=[]
    k=85
    while k not in orbit:
        orbit.append(k)
        k=k*3%N
    assert len(orbit)==M and 1 not in orbit and 0 not in orbit
    report={'schema':1,'task':'PM-CYCLE10-B','m':M,'q':Q,'N':N,'N_prime_trial_division_bound':isqrt(N),
      'modulus':f,'irreducible_rabin':True,'primitive_x':True,
      'primitive_x_checks':{'x_pow_2N':power(x,2*N,f),'x_pow_N':power(x,N,f),'x_pow_2':power(x,2,f)},
      'linearized_operator_exponents':[1,3,81],
      'frobenius_symbol_gcd':symbolic_gcd,'nullspace_basis':basis,
      'kernel_dimension':len(basis),'kernel_elements_checked':3**len(basis),'valid_square_seeds':candidates,
      'frequency':85,'frequency_orbit':orbit,'trace_separator':separator}
    representatives=sorted({canonical_seed(c['a'],c['b'],f) for c in candidates})
    report['fixed_frequency_orbit_representatives']=[list(map(list,r)) for r in representatives]
    report['fixed_frequency_orbit_count']=len(representatives)
    current=representatives[0]
    frobenius=[]
    while current not in frobenius:
        frobenius.append(current)
        current=canonical_seed(power(list(current[0]),3,f),power(list(current[1]),3,f),f)
    report['seed_frobenius_orbit_length']=len(frobenius)
    report['all_fixed_frequency_seed_orbits_one_frobenius_orbit']=set(frobenius)==set(representatives)
    return report

def canonical_seed(a,b,f):
    """The three choices of vertex normalized to1, with the other pair unordered."""
    vertices=[[1],a,b]
    normalized=[]
    for i,v in enumerate(vertices):
        inv=power(v,Q-2,f)
        pair=[tuple(mul(w,inv,f)) for j,w in enumerate(vertices) if j!=i]
        normalized.append(tuple(sorted(pair)))
    return min(normalized)

def verify_report(report):
    require(isinstance(report,dict) and report.get('schema')==1,'unknown certificate schema')
    require((report.get('m'),report.get('q'),report.get('N'),report.get('frequency'))==(M,Q,N,85),
            'wrong target parameters')
    require(not any(N%p==0 for p in range(2,isqrt(N)+1)),'subgroup order is not prime')
    require(report.get('N_prime_trial_division_bound')==isqrt(N),'wrong prime bound')
    def polynomial(value, max_degree=M-1):
        require(isinstance(value,list) and len(value)<=max_degree+1
                and all(type(c) is int and c in (0,1,2) for c in value)
                and (not value or value[-1]!=0),'invalid coefficient polynomial')
        return value
    f=polynomial(report['modulus'],M)
    require(len(f)==M+1 and f[-1]==1 and irreducible(f),'field modulus fails Rabin test')
    require(report.get('irreducible_rabin') is True,'missing irreducibility receipt')
    x=[0,1]
    primitive_checks={'x_pow_2N':power(x,2*N,f),'x_pow_N':power(x,N,f),'x_pow_2':power(x,2,f)}
    require(primitive_checks['x_pow_2N']==[1] and primitive_checks['x_pow_N']!=[1]
            and primitive_checks['x_pow_2']!=[1],'primitive order checks fail')
    require(report.get('primitive_x') is True and report.get('primitive_x_checks')==primitive_checks,
            'primitive order receipt differs')
    require(report.get('linearized_operator_exponents')==[1,3,81],'wrong linearized exponents')
    def linear(y):
        return add(add(y,power(y,3,f)),power(y,81,f))
    cols=[linear([0]*i+[1]) for i in range(M)]
    matrix=[[(cols[j][i] if i<len(cols[j]) else 0) for j in range(M)] for i in range(M)]
    expected_basis=nullspace(matrix)
    basis=[polynomial(v) for v in report['nullspace_basis']]
    require(basis==expected_basis and len(basis)==4,'wrong complete nullspace basis')
    require(report.get('kernel_dimension')==4 and report.get('kernel_elements_checked')==81,
            'wrong linearized nullspace size')
    h=[2]+[0]*12+[1]
    require(report.get('frobenius_symbol_gcd')==pgcd(h,[1,1,0,0,1])==[1,1,0,0,1],
            'wrong Frobenius-symbol gcd')
    ys=[]
    for coefficients in product(range(3),repeat=4):
        y=[]
        for c,v in zip(coefficients,basis):
            y=add(y,[c*w%3 for w in v])
        require(not linear(y),'nullspace combination fails equation')
        ys.append(tuple(y))
    require(len(set(ys))==81,'dependent nullspace basis')
    expected_ys={y for y in ys if len(y)>1}
    candidates=report['valid_square_seeds']
    require(isinstance(candidates,list) and len(candidates)==78,'wrong fixed-frequency seed count')
    actual_ys=set()
    for candidate in candidates:
        y,a,b=(polynomial(candidate[key]) for key in ('y','a','b'))
        actual_ys.add(tuple(y))
        require(tuple(y) in expected_ys,'candidate not a nonconstant kernel parameter')
        require(mul(y,a,f)==add(y,[1]) and mul(y,b,f)==add(y,[2]),'parameter ratios fail')
        require(len({tuple([1]),tuple(a),tuple(b)})==3 and a and b,'degenerate seed')
        require(add(add([1],a),b)==[],'seed is not zero sum')
        require(power(a,N,f)==power(b,N,f)==[1],'seed vertex is not square')
        require(add(add([1],power(a,85,f)),power(b,85,f))==[],'extra frequency equation fails')
    require(actual_ys==expected_ys,'missing or duplicate kernel parameter')
    orbit=[]
    k=85
    while k not in orbit:
        orbit.append(k)
        k=k*3%N
    affine=[]
    k=1
    while k not in affine:
        affine.append(k)
        k=k*3%N
    require(report.get('frequency_orbit')==orbit and len(orbit)==13
            and not set(orbit)&(set(affine)|{0}),'extra orbit meets affine frequencies')
    separator=report['trace_separator']
    a,b=(polynomial(separator[key]) for key in ('a','b'))
    require(len({tuple([1]),tuple(a),tuple(b)})==3 and a and b,'degenerate trace separator')
    require(add(add([1],a),b)==[] and power(a,N,f)==power(b,N,f)==[1],
            'separator is not a real square edge')
    values=[trace([1],f),trace(power(a,85,f),f),trace(power(b,85,f),f)]
    require(separator.get('trace_values')==values and separator.get('trace_sum')==sum(values)%3
            and sum(values)%3!=0,'trace separator does not violate equation')
    representatives=sorted({canonical_seed(c['a'],c['b'],f) for c in candidates})
    require(report.get('fixed_frequency_orbit_representatives')==[list(map(list,r)) for r in representatives]
            and len(representatives)==report.get('fixed_frequency_orbit_count')==13,
            'wrong fixed-frequency multiplicative orbit partition')
    current=representatives[0]
    frobenius=[]
    while current not in frobenius:
        frobenius.append(current)
        current=canonical_seed(power(list(current[0]),3,f),power(list(current[1]),3,f),f)
    require(report.get('seed_frobenius_orbit_length')==len(frobenius)==13
            and set(frobenius)==set(representatives)
            and report.get('all_fixed_frequency_seed_orbits_one_frobenius_orbit') is True,
            'fixed-frequency seeds are not the recorded Frobenius orbit')
    return {'verified':True,'linearized_kernel_dimension':4,'fixed_frequency_parameters':78,
            'fixed_frequency_seed_orbits':13,'seed_frobenius_orbit_length':13,
            'sparse_kernel_dimension_lower_bound':27,'full_kernel_dimension':14,
            'trace_separator_sum':sum(values)%3,
            'all_field_seed_orbits_scanned':False,'exact_sparse_kernel_dimension_claimed':False}

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',help='write deterministic certificate JSON')
    parser.add_argument('--verify',help='verify an existing JSON certificate')
    args=parser.parse_args()
    require(not(args.output and args.verify),'choose generation or verification')
    if args.verify:
        print(json.dumps(verify_report(json.loads(Path(args.verify).read_text())),sort_keys=True))
    else:
        report=solve()
        verify_report(report)
        output=json.dumps(report,indent=2,sort_keys=True)+'\n'
        if args.output:
            Path(args.output).write_text(output)
            print(json.dumps({'output':args.output,'verification':verify_report(report)},sort_keys=True))
        else:
            print(output,end='')

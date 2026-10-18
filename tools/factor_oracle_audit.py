"""Independent code-audit oracles. Roots/factors occur only in the oracle."""
import importlib.util
import itertools
from pathlib import Path
import random
import sys

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0,str(REPO/'tools'))
import factor_readout as M
import orientation_readout as O

sp = importlib.util.spec_from_file_location('independent_c',str(Path(__file__).with_name('factor_independent_c.py')))
C = importlib.util.module_from_spec(sp)
sp.loader.exec_module(C)

checks = 0
for p,maxn in ((2,6),(3,4),(5,3)):
    for n in range(1,maxn+1):
        for cs in itertools.product(range(p),repeat=n):
            f = tuple(cs)+(1,)
            der = C.trim(i*f[i]%p for i in range(1,len(f)))
            if len(C.gcd(f,der,p)) != 1:
                continue
            fs = C.factors(f,p)
            r = len(fs)
            es = [C.crt_idempotent(fs,[int(i==j) for i in range(r)],p)
                  for j in range(r)]
            assert len(M.fixed_basis(p,list(f))) == C.fixed_dim(f,p)
            for vals in itertools.product(range(p),repeat=r):
                b = ()
                for v,e in zip(vals,es):
                    b = C.add(b,tuple(v*x%p for x in e),p)
                labels = sorted(set(vals))
                out = M.readout(p,list(f),[{'poly':list(b),'labels':labels}])
                expected = []
                for v in labels:
                    h = (1,)
                    for a,g in zip(vals,fs):
                        if a==v:
                            h = C.mul(h,g,p)
                    expected.append(h)
                assert set(map(tuple,out['blocks'])) == set(expected)
                assert out['observable_algebra_dimension'] == len(labels)
                assert out['closure_product_offers'] <= n
                assert (out['status']=='COMPLETE') == (len(labels)==r)
                checks += 1
print('PASS independent CRT-value oracle:',checks,'general finite-label production readouts')


def at(a,x,p):
    z = 0
    for c in reversed(a):
        z = (z*x+c)%p
    return z


def generator(p):
    s,t = 0,p-1
    while t%2==0:
        s,t = s+1,t//2
    return next(u for u in range(1,p)
                if pow(u,1<<s,p)==1 and pow(u,1<<(s-1),p)!=1)


cases = []
for p in (3,5,7):
    for n in range(2,min(4,p-1)+1,2):
        cases += [(p,rs) for rs in itertools.combinations(range(p),n)]
rng = random.Random(729143)
for p in (11,13,17,19,29,31,37,41,73,97,257):
    for n in (2,4,6):
        for _ in range(3):
            cases.append((p,tuple(sorted(rng.sample(range(p),n)))))
for p,roots in cases:
    f = (1,)
    for x in roots:
        f = C.mul(f,(-x%p,1),p)
    out = O.construct(p,list(f),generator(p))
    n = len(roots)
    def value(a,x,y):
        return sum(a[i*n+j]*pow(x,i,p)*pow(y,j,p)
                   for i in range(n) for j in range(n))%p
    vals = [[value(out['orientation'],x,y) for y in roots] for x in roots]
    assert all(vals[i][i]==0 for i in range(n))
    assert all(vals[i][j] in (0,1) and vals[i][j]+vals[j][i]==1
               for i in range(n) for j in range(i+1,n))
    scores = [sum(row) for row in vals]
    assert [at(out['partial_trace'],x,p) for x in roots] == scores
    assert len(set(scores))>1
    assert 1<len(out['factor'])<len(f)
    assert not C.divmodp(f,tuple(out['factor']),p)[1]
print('PASS independent point-value oracle:',len(cases),
      'root-free constructor cases, varied 2-valuations, N2/4/6')

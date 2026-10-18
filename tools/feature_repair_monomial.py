#!/usr/bin/env python3
"""PM-REPAIR-B. Dependency-free, exact rational representation repair.

Every answer is independently checked by multiplication against the original
evaluation matrices. No floating-point optimizer or guessed square is used.
Run: python3 /tmp/pm_repair_b.py
"""
from fractions import Fraction as Q
from itertools import combinations
from functools import lru_cache
import hashlib
import json
from pathlib import Path


def dot(a, b):
    return sum((x*y for x,y in zip(a,b)), Q(0))


def rref(matrix, width=None):
    a = [[Q(x) for x in row] for row in matrix]
    n = len(a[0]) if a else (width or 0)
    row, pivots = 0, []
    for col in range(n):
        pivot = next((i for i in range(row,len(a)) if a[i][col]),None)
        if pivot is None:
            continue
        a[row],a[pivot] = a[pivot],a[row]
        d = a[row][col]
        a[row] = [x/d for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                c = a[i][col]
                a[i] = [x-c*y for x,y in zip(a[i],a[row])]
        pivots.append(col)
        row += 1
        if row == len(a):
            break
    return a,pivots


def nullspace(a, n):
    rr,pivots = rref(a,n)
    free = [j for j in range(n) if j not in pivots]
    out=[]
    for f in free:
        v=[Q(0)]*n
        v[f]=Q(1)
        for i,p in enumerate(pivots):
            v[p]=-rr[i][f]
        out.append(v)
    return out


def unique_solve(a,b,n):
    """Return unique solution of a*x=b, or None (inconsistent or nonunique)."""
    rr,pivots=rref([list(row)+[rhs] for row,rhs in zip(a,b)], n+1)
    if n in pivots or len(pivots)!=n:
        return None
    x=[Q(0)]*n
    for i,p in enumerate(pivots):
        x[p]=rr[i][-1]
    assert all(dot(row,x)==rhs for row,rhs in zip(a,b))
    return x


def exact_oracle(features, target):
    """Rows are points, columns are features. Return ('primal',c) or ('dual',z)."""
    n=len(features)
    p=len(features[0]) if n else 0
    target=set(target)
    off=[i for i in range(n) if i not in target]
    if not off:
        return 'primal',[Q(0)]*p
    _,cols=rref(features,p)
    a=[[Q(row[j]) for j in cols] for row in features]
    r=len(cols)
    drows=[a[i] for i in sorted(target)]
    # Kernel basis in coefficient space, represented by its column vectors.
    nbasis=nullspace(drows,r)
    q=[[dot(a[i],v) for v in nbasis] for i in off]
    k=len(nbasis)
    for inds in combinations(range(len(off)),k):
        b=unique_solve([q[j] for j in inds],[Q(1)]*k,k)
        if b is None or any(dot(row,b)<1 for row in q):
            continue
        reduced=[sum((nbasis[j][i]*b[j] for j in range(k)),Q(0)) for i in range(r)]
        c=[Q(0)]*p
        for j,v in zip(cols,reduced):
            c[j]=v
        verify_primal(features,target,c)
        return 'primal',c
    # Caratheodory's theorem makes this finite dual search complete.
    for size in range(1,min(k+1,len(off))+1):
        for inds in combinations(range(len(off)),size):
            equations=[[q[j][h] for j in inds] for h in range(k)]
            equations.append([Q(1)]*size)
            y=unique_solve(equations,[Q(0)]*k+[Q(1)],size)
            if y is None or any(v<=0 for v in y):
                continue
            z=[Q(0)]*n
            for j,v in zip(inds,y):
                z[off[j]]=v
            # Select independent target rows; their columns solve lambda uniquely.
            dt=sorted(target)
            _,basis_indices=rref([[a[i][h] for i in dt] for h in range(r)],len(dt))
            chosen=[dt[j] for j in basis_indices]
            rhs=[-sum((z[i]*a[i][h] for i in off),Q(0)) for h in range(r)]
            lam=unique_solve([[a[i][h] for i in chosen] for h in range(r)],rhs,len(chosen))
            assert lam is not None
            for i,v in zip(chosen,lam):
                z[i]=v
            verify_dual(features,target,z)
            return 'dual',z
    raise AssertionError('neither alternative found: implementation error')


def verify_primal(features,target,c):
    for i,row in enumerate(features):
        v=dot(row,c)
        assert v==0 if i in target else v>=1


def verify_dual(features,target,z):
    off=[i for i in range(len(features)) if i not in target]
    assert all(z[i]>=0 for i in off)
    assert sum((z[i] for i in off),Q(0))==1
    assert all(sum((z[i]*features[i][j] for i in range(len(features))),Q(0))==0
               for j in range(len(features[0])))


class Repair:
    def __init__(self,omega,target,base,blocks,cost):
        self.omega,self.target,self.base,self.blocks,self.cost=omega,set(target),base,blocks,cost
        self.calls=0
        self.cache={}

    def feature_exponents(self,mask):
        return sorted(set(self.base).union(*(self.blocks[j] for j in range(len(self.blocks)) if mask>>j&1)))

    def matrix(self,mask):
        exps=self.feature_exponents(mask)
        return [[Q(t**e) for e in exps] for t in self.omega]

    def oracle(self,mask):
        if mask not in self.cache:
            self.calls+=1
            self.cache[mask]=exact_oracle(self.matrix(mask),self.target)
        return self.cache[mask]

    def objective(self,mask):
        return (sum(self.cost[j] for j in range(len(self.blocks)) if mask>>j&1),mask.bit_count(),mask)

    def killmask(self,z):
        return sum((1<<j) for j,exps in enumerate(self.blocks)
                   if any(sum((z[i]*Q(t**e) for i,t in enumerate(self.omega)),Q(0))
                          for e in exps))

    def benders(self):
        cuts=[]
        while True:
            candidates=(m for m in range(1<<len(self.blocks)) if all(m&c['killmask'] for c in cuts))
            mask=min(candidates,key=self.objective,default=None)
            if mask is None:
                return {'feasible':False,'cuts':cuts,'calls':self.calls}
            kind,cert=self.oracle(mask)
            if kind=='primal':
                # All cuts are independently checked, and the final point is a
                # minimum-cost master solution. This is an exact lower bound.
                assert all(mask&c['killmask'] for c in cuts)
                assert all(self.objective(m)>=self.objective(mask) for m in range(1<<len(self.blocks))
                           if all(m&c['killmask'] for c in cuts))
                return {'feasible':True,'mask':mask,'exponents':self.feature_exponents(mask),
                        'coefficients':cert,'values':[dot(row,cert) for row in self.matrix(mask)],
                        'objective':self.objective(mask),'cuts':cuts,'calls':self.calls}
            kill=self.killmask(cert)
            assert not(mask&kill)
            # Recheck the claimed cut against the original, unsimplified blocks.
            assert kill==self.killmask(cert)
            cuts.append({'mask':mask,'killmask':kill,'z':cert})
            if kill==0:
                return {'feasible':False,'cuts':cuts,'calls':self.calls}

    def baseline(self):
        before=self.calls
        for mask in sorted(range(1<<len(self.blocks)),key=self.objective):
            kind,cert=self.oracle(mask)
            if kind=='primal':
                return {'feasible':True,'mask':mask,'objective':self.objective(mask),'calls':self.calls-before}
        return {'feasible':False,'calls':self.calls-before}


def dumpable(x):
    if isinstance(x,Q):
        return str(x)
    if isinstance(x,dict):
        return {str(k):dumpable(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):
        return [dumpable(v) for v in x]
    return x


def main():
    freeze=Path(__file__).resolve().parents[1]/'research/experiments/feature-repair-monomial-panel.json'
    frozen_bytes=open(freeze,'rb').read()
    assert hashlib.sha256(frozen_bytes).hexdigest()=='476a983f7b806a7ff1cb4dd0a71ad3fc758f10541e85faeb1697480f2cd68192'
    frozen=json.loads(frozen_bytes)
    omega=list(range(-6,7))
    target=[i for i,t in enumerate(omega) if abs(t) in (1,3,5)]
    base=[0,1]
    blocks=[sorted({2*(j+1),2*((3*j+4)%11+1),2*j+3}) for j in range(10)]
    cost=[1+((7*j+3)%5) for j in range(10)]
    master=Repair(omega,target,base,blocks,cost)
    answer=master.benders()
    reference=Repair(omega,target,base,blocks,cost).baseline()
    assert answer['feasible']==reference['feasible']
    assert answer.get('objective')==reference.get('objective')
    out={'freeze_sha256':hashlib.sha256(frozen_bytes).hexdigest(),
         'classification':frozen['classification'],'omega':omega,'target_indices':target,
         'blocks':blocks,'costs':cost,'benders':answer,'exhaustive_baseline':reference}
    if answer['feasible']:
        deleted=sorted(e for e in answer['exponents'] if e>0 and e%2==0)[:3]
        negative_blocks=[[e for e in block if e not in deleted] for block in blocks]
        negative=Repair(omega,target,base,negative_blocks,cost).benders()
        negative_reference=Repair(omega,target,base,negative_blocks,cost).baseline()
        assert negative['feasible']==negative_reference['feasible']
        assert negative.get('objective')==negative_reference.get('objective')
        out['negative_control']={'deleted_even_exponents':deleted,'benders':negative,
                                 'exhaustive_baseline':negative_reference}
    # Pure univariate odd-feature control: no positive even feature remains.
    odd_blocks=[[e for e in block if e%2] for block in blocks]
    odd=Repair(omega,target,base,odd_blocks,cost).benders()
    assert not odd['feasible']
    out['odd_only_negative_control']=odd
    print(json.dumps(dumpable(out),indent=2,sort_keys=True))


if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Independent certificate replay: no imports from the discovery code.

Also directly audits the coordinator's signed-grid degree family for r=1..4
and ambient dimension p=6, marked dimension r=2.
"""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path


def total(values):
    return sum(values,Fraction(0))


def verify_case(data,blocks,costs):
    omega=data['omega']
    target=set(data['target_indices'])
    answer=data['answer']
    cuts=answer['cuts']
    for cut in cuts:
        z=[Fraction(v) for v in cut['z']]
        off=[i for i in range(len(omega)) if i not in target]
        assert all(z[i]>=0 for i in off)
        assert total(z[i] for i in off)==1
        base=[0,1]
        selected=set(base)
        for j,block in enumerate(blocks):
            if cut['mask']&(1<<j):
                selected.update(block)
        for e in selected:
            assert total(z[i]*omega[i]**e for i in range(len(omega)))==0
        kill=0
        for j,block in enumerate(blocks):
            if any(total(z[i]*omega[i]**e for i in range(len(omega)))!=0 for e in block):
                kill|=1<<j
        assert kill==cut['killmask']
        assert not kill&cut['mask']
    if not answer['feasible']:
        assert any(cut['killmask']==0 for cut in cuts)
        return {'feasible':False,'dual_cuts_verified':len(cuts)}
    mask=answer['mask']
    exponents=answer['exponents']
    coefficients=[Fraction(v) for v in answer['coefficients']]
    available={0,1}
    for j,block in enumerate(blocks):
        if mask&(1<<j):
            available.update(block)
    assert set(exponents)==available
    for i,t in enumerate(omega):
        value=total(c*t**e for e,c in zip(exponents,coefficients))
        assert value==Fraction(answer['values'][i])
        if i in target:
            assert value==0
        else:
            assert value>=1
    objective=lambda m:(sum(costs[j] for j in range(len(costs)) if m&(1<<j)),m.bit_count(),m)
    assert all(mask&cut['killmask'] for cut in cuts)
    assert tuple(answer['objective'])==objective(mask)
    # A stand-alone lower-bound proof from valid cuts, with no LP/oracle calls.
    for other in range(1<<len(blocks)):
        if objective(other)<objective(mask):
            assert any(not(other&cut['killmask']) for cut in cuts)
    # Independent special-family lower bound: symmetrization plus sparse-root
    # counting requires at least six distinct nonconstant even monomials.
    def even_count(m):
        return len({e for j,block in enumerate(blocks) if m&(1<<j)
                    for e in block if e>0 and e%2==0})
    necessary=min((objective(m) for m in range(1<<len(blocks)) if even_count(m)>=6),default=None)
    assert necessary==objective(mask)
    return {'feasible':True,'objective':objective(mask),'dual_cuts_verified':len(cuts),
            'independent_six_even_features_lower_bound':necessary}


def monomial(point,exponent):
    value=1
    for x,e in zip(point,exponent):
        value*=x**e
    return value


def tensor_degree_audit(p,r):
    assert 1<=r<=p
    points=list(product((-1,0,1),repeat=p))
    coeff={-1:1,0:-2,1:1}
    signed=[]
    for x in points:
        if any(x[j]!=0 for j in range(r,p)):
            continue
        z=1
        for j in range(r):
            z*=coeff[x[j]]
        signed.append((x,z))
    off=[x for x in points if all(x[j]!=0 for j in range(r))]
    assert all(z==1 for x,z in signed if all(x[j]!=0 for j in range(r)))
    assert sum(z for x,z in signed if all(x[j]!=0 for j in range(r)))==2**r
    low_degree=0
    moments=[]
    for e in product((0,1,2),repeat=p):
        if sum(e)<2*r:
            moment=sum(z*monomial(x,e) for x,z in signed)
            assert moment==0
            low_degree+=1
        # Stronger exact statement about the entire reduced monomial dictionary.
        moment=sum(z*monomial(x,e) for x,z in signed)
        expected=2**r if tuple(e)==(2,)*r+(0,)*(p-r) else 0
        assert moment==expected
        if moment:
            moments.append((e,moment))
    for x in points:
        positive=monomial(x,(2,)*r+(0,)*(p-r))
        assert positive in (0,1)
        assert (positive==0)==any(x[j]==0 for j in range(r))
    a=(1,)*p
    b=(-1,)+(1,)*(p-1)
    signed_exponent=(1,)*r+(0,)*(p-r)
    assert monomial(a,signed_exponent)==1
    assert monomial(b,signed_exponent)==-1
    assert a in off and b in off
    return {'p':p,'r':r,'points':len(points),'low_degree_monomials_annihilated':low_degree,
            'sharp_nonnegative_degree':2*r,'signed_degree':r,'bad_signed_product_length':2,
            'only_nonzero_reduced_moment':moments}


def main():
    d=json.load(open(Path(__file__).resolve().parents[1]/'research/experiments/feature-repair-monomial-report.json'))
    blocks=d['blocks']
    common={'omega':d['omega'],'target_indices':d['target_indices']}
    result={}
    result['designed_original']=verify_case(dict(common,answer=d['benders']),blocks,d['costs'])
    removed=set(d['negative_control']['deleted_even_exponents'])
    newblocks=[[e for e in block if e not in removed] for block in blocks]
    result['designed_restricted']=verify_case(dict(common,answer=d['negative_control']['benders']),newblocks,d['costs'])
    oddblocks=[[e for e in block if e%2] for block in blocks]
    result['odd_only']=verify_case(dict(common,answer=d['odd_only_negative_control']),oddblocks,d['costs'])
    result['coordinator_family_audit']=[tensor_degree_audit(r,r) for r in range(1,5)]+[tensor_degree_audit(6,2)]
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()

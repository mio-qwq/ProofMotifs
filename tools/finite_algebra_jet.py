#!/usr/bin/env python3
"""Bounded constant-field rational-matrix algebra generation; exact controls.

Field p is None for Q or a PROMISED prime; no primality test is performed.
All costs count explicit dimension budget and expanded polynomial degrees.
Budget exhaustion proves only D+1 independent words, never infinitude.
"""
from fractions import Fraction
from itertools import product
from copy import deepcopy
import json


class K:
    def __init__(self, p=None):
        if p is not None and (type(p) is not int or p < 2):
            raise ValueError('Expected Q or a promised prime')
        self.p = p
    def c(self, x):
        if not isinstance(x, (int, Fraction)):
            raise ValueError("closure coefficients must be constant field scalars")
        q = Fraction(x)
        return q if self.p is None else q.numerator * pow(q.denominator, -1, self.p) % self.p
    def add(self, a, b): return a+b if self.p is None else (a+b) % self.p
    def mul(self, a, b): return a*b if self.p is None else a*b % self.p
    def neg(self, a): return -a if self.p is None else -a % self.p
    def inv(self, a): return 1/a if self.p is None else pow(a, -1, self.p)


def trim(a):
    a = list(a)
    while len(a)>1 and a[-1] == 0: a.pop()
    return tuple(a or [0])


def padd(a,b,k):
    return trim([k.add(a[i] if i<len(a) else k.c(0), b[i] if i<len(b) else k.c(0)) for i in range(max(len(a),len(b)))])


def pscale(a,c,k): return trim([k.mul(x,c) for x in a])


def pmul(a,b,k):
    c=[k.c(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]=k.add(c[i+j], k.mul(x,y))
    return trim(c)


def ppow(a,e,k):
    out=(k.c(1),)
    for _ in range(e): out=pmul(out,a,k)
    return out


def ident(n,k): return tuple(tuple((k.c(int(i==j)),) for j in range(n)) for i in range(n))


def mmul(A,B,k):
    n=len(A)
    return tuple(tuple(sum_poly([pmul(A[i][h],B[h][j],k) for h in range(n)],k) for j in range(n)) for i in range(n))


def sum_poly(polys,k):
    out=(k.c(0),)
    for p in polys: out=padd(out,p,k)
    return out


class TupleModel:
    def __init__(self, numerators, delta=(1,), p=None):
        self.k=K(p)
        self.delta=trim([self.k.c(x) for x in delta])
        if self.delta[0]==0: raise ValueError("delta(0) must be nonzero")
        self.n=len(numerators[0]) if numerators else 1
        if self.n < 1: raise ValueError('Positive matrix dimension required')
        self.P=[]
        for A in numerators:
            if len(A)!=self.n or any(len(row)!=self.n for row in A): raise ValueError("matrix shape")
            self.P.append(tuple(tuple(trim([self.k.c(x) for x in entry]) for entry in row) for row in A))
        self.b=max([len(self.delta)-1]+[len(q)-1 for A in self.P for row in A for q in row])

    def word(self,w):
        A=ident(self.n,self.k)
        for a in w:
            if type(a) is not int or not 0<=a<len(self.P): raise ValueError("word alphabet")
            A=mmul(A,self.P[a],self.k)
        return A,len(w)


def flatten_cleared(M, elements):
    """Common denominator delta^L; coordinates are over K, never K(t)."""
    L=max((ell for A,ell in elements),default=0)
    scaled=[]
    for A,ell in elements:
        q=ppow(M.delta,L-ell,M.k)
        scaled.append([pmul(entry,q,M.k) for row in A for entry in row])
    degree=max((len(q)-1 for A in scaled for q in A),default=0)
    return [[q[j] if j<len(q) else M.k.c(0) for q in A for j in range(degree+1)] for A in scaled]


def constant_coordinates(M,basis,target):
    """Solve coefficient equations for a target in a K-span."""
    vectors=flatten_cleared(M,basis+[target]); m=len(basis); k=M.k
    equations=[[vectors[j][i] for j in range(m)]+[vectors[-1][i]] for i in range(len(vectors[-1]))]
    row=0; pivots=[]
    for col in range(m):
        pivot=next((i for i in range(row,len(equations)) if equations[i][col]),None)
        if pivot is None: continue
        equations[row],equations[pivot]=equations[pivot],equations[row]
        inv=k.inv(equations[row][col]); equations[row]=[k.mul(inv,x) for x in equations[row]]
        for i in range(len(equations)):
            if i!=row and equations[i][col]:
                c=equations[i][col]
                equations[i]=[k.add(x,k.neg(k.mul(c,y))) for x,y in zip(equations[i],equations[row])]
        pivots.append(col); row+=1
    if any(not any(e[:m]) and e[m] for e in equations): return None
    answer=[k.c(0)]*m
    for i,j in enumerate(pivots): answer[j]=equations[i][m]
    return answer


def generate(M,D):
    if type(D) is not int or D<1: raise ValueError("positive explicit dimension budget required")
    words=[()]; basis=[M.word(())]; head=0; offers=1
    while head<len(basis):
        A,ell=basis[head]
        for i,P in enumerate(M.P):
            offers+=1
            target=(mmul(A,P,M.k),ell+1)
            if constant_coordinates(M,basis,target) is None:
                words.append(words[head]+(i,)); basis.append(target)
                if len(basis)>D:
                    return {"status":"rank_budget_exceeded","words":words,"independent_words":len(words),"offers":offers,"D":D}
        head+=1
    C=[]
    for A,ell in basis:
        C.append([constant_coordinates(M,basis,(mmul(A,P,M.k),ell+1)) for P in M.P])
    d=len(basis)
    return {"status":"closed","words":words,"initial":constant_coordinates(M,basis,M.word(())),"C":C,"d":d,"D":D,"b":M.b,"E":1+(d-1)*M.b,"offers":offers}


def independent_rank(vectors,k):
    """Checker-only row elimination, separate from coordinate solver."""
    rows=[v[:] for v in vectors]; rank=0
    for col in range(len(rows[0]) if rows else 0):
        p=next((i for i in range(rank,len(rows)) if rows[i][col]),None)
        if p is None: continue
        rows[rank],rows[p]=rows[p],rows[rank]
        inv=k.inv(rows[rank][col]); rows[rank]=[k.mul(inv,x) for x in rows[rank]]
        for i in range(rank+1,len(rows)):
            z=rows[i][col]
            rows[i]=[k.add(x,k.neg(k.mul(z,y))) for x,y in zip(rows[i],rows[rank])]
        rank+=1
    return rank


def verify(M,c):
    try:
        if type(c['D']) is not int or c['D'] < 1: raise ValueError('dimension budget')
        words=c["words"]; basis=[M.word(w) for w in words]; d=len(words); k=M.k
        if independent_rank(flatten_cleared(M,basis),k)!=d: raise ValueError("dependent words")
        if c["status"]=="rank_budget_exceeded":
            if d!=c["D"]+1: raise ValueError("invalid exceeded budget")
            return True,"verified D+1 independent words, not infinitude"
        if c["status"]!="closed" or d!=c["d"] or d>c["D"]: raise ValueError("status/dimension")
        if any(len(w)>d-1 for w in words): raise ValueError("word length")
        if c["b"]!=M.b or c["E"]!=1+(d-1)*M.b: raise ValueError("jet bound")
        def identity(target,coeffs):
            if not isinstance(coeffs,list) or len(coeffs)!=d: raise ValueError("coefficient shape")
            scalars=[k.c(x) for x in coeffs]
            vectors=flatten_cleared(M,basis+[target])
            for j,x in enumerate(vectors[-1]):
                total=k.c(0)
                for i,z in enumerate(scalars): total=k.add(total,k.mul(z,vectors[i][j]))
                if total!=x: raise ValueError("coefficient identity")
        identity(M.word(()),c["initial"])
        if len(c["C"])!=d: raise ValueError("closure height")
        for j,(A,ell) in enumerate(basis):
            if len(c["C"][j])!=len(M.P): raise ValueError("closure alphabet")
            for i,P in enumerate(M.P): identity((mmul(A,P,k),ell+1),c["C"][j][i])
        return True,"accepted"
    except (ValueError,TypeError,IndexError,KeyError,ZeroDivisionError) as e:
        return False,str(e)


def jets(M,elements,E):
    k=M.k; out=[]
    for A,ell in elements:
        denom=ppow(M.delta,ell,k); inv0=k.inv(denom[0]); row=[]
        for matrixrow in A:
            for q in matrixrow:
                coefficients=[]
                for j in range(E):
                    x=q[j] if j<len(q) else k.c(0)
                    for h in range(1,min(j,len(denom)-1)+1): x=k.add(x,k.neg(k.mul(denom[h],coefficients[j-h])))
                    coefficients.append(k.mul(x,inv0))
                row.extend(coefficients)
        out.append(row)
    return out


def checked(M,D):
    c=generate(M,D); assert verify(M,c)[0],verify(M,c)
    if c["status"]=="closed":
        B=[M.word(w) for w in c["words"]]
        assert independent_rank(jets(M,B,c["E"]),M.k)==c["d"]
        # Independent finite full-word control, not used by generation.
        allwords=[w for length in range(c["d"]+1) for w in product(range(len(M.P)),repeat=length)]
        assert independent_rank(flatten_cleared(M,[M.word(w) for w in allwords]),M.k)==c["d"]
    return c


def main():
    report={}
    report["scalar_t"]=[]
    for D in (1,2,4,8):
        M=TupleModel([[[(0,1)]]]); c=checked(M,D)
        assert c["status"]=="rank_budget_exceeded"
        report["scalar_t"].append({"D":D,"status":c["status"],"independent_words":len(c["words"]),"max_word_length":max(map(len,c["words"]))})
    idempotent=TupleModel([[[(1,),(0,1)],[(0,),(0,)]]])
    ci=checked(idempotent,2); assert ci["d"]==2 and ci["E"]==2
    report["polynomial_idempotent"]={"d":ci["d"],"b":ci["b"],"E":ci["E"],"words":ci["words"]}
    joint=TupleModel([[[(0,),(0,1)],[(0,),(0,)]],[[(0,),(0,)],[(1,),(0,)]]])
    cj=checked(joint,5)
    assert cj['status']=='rank_budget_exceeded' and cj['independent_words']==6
    report['joint_nilpotents']={'each_generator_square_zero': True,
                               'D': 5, 'independent_words': 6,
                               'status': cj['status']}
    Mpower=17
    delayed=TupleModel([[[(0,),tuple([0]*Mpower+[1])],[(0,),(0,)]]])
    cd=checked(delayed,2); B=[delayed.word(w) for w in cd["words"]]
    ranks=[independent_rank(jets(delayed,B,E),delayed.k) for E in range(1,Mpower+2)]
    assert cd["d"]==2 and cd["E"]==Mpower+1 and ranks==[1]*Mpower+[2]
    report["delayed_nilpotent"]={"M":Mpower,"d":cd["d"],"required_E":cd["E"],"jet_ranks_E_1_through_M_plus_1":ranks}
    rational=TupleModel([[[(1,-1),(0,1)],[(0,),(0,)]]],(1,-1))
    cr=checked(rational,2); assert cr["d"]==2
    report["delta_1_minus_t"]={"d":cr["d"],"b":cr["b"],"E":cr["E"]}
    # S E12 S^-1 and S E21 S^-1, S=I+t/(1-t) E12.
    conjugate=TupleModel([[[(0,),(1,-2,1)],[(0,),(0,)]],[[(0,1,-1),(0,0,-1)],[(1,-2,1),(0,-1,1)]]],(1,-2,1))
    cc=checked(conjugate,4); assert cc["d"]==4
    report["rational_conjugate_M2"]={"d":cc["d"],"b":cc["b"],"E":cc["E"],"words":cc["words"]}
    too_small=checked(conjugate,3)
    assert too_small["status"]=="rank_budget_exceeded" and len(too_small["words"])==4
    report["finite_algebra_budget_too_small"]={"true_dimension":4,"D":3,"status":too_small["status"],"independent_words":4}
    distribution={}
    for bits in product((0,1),repeat=8):
        nums=[[[tuple([bits[offset+2*i+j]]) for j in range(2)] for i in range(2)] for offset in (0,4)]
        M=TupleModel(nums,p=2); c=checked(M,4); assert c["status"]=="closed"
        distribution[c["d"]]=distribution.get(c["d"],0)+1
    polycontrols=0
    for p in (2,3):
        for coeff in product(range(p),repeat=3):
            M=TupleModel([[[(1,),coeff],[(0,),(0,)]]],p=p)
            c=checked(M,2); assert c["d"]==2; polycontrols+=1
        for nums,delta,D in [(conjugate.P,conjugate.delta,4),(rational.P,rational.delta,2),(delayed.P,delayed.delta,2)]:
            M=TupleModel(nums,delta,p); c=checked(M,D); assert c["status"]=="closed"
    report["finite_field_controls"]={"all_F2_constant_2x2_two_generator_tuples":256,"dimension_distribution":distribution,"all_degree_at_most_2_idempotent_offdiagonals_F2_F3":polycontrols,"rational_and_delayed_controls_F2_F3":6}
    malformed={}
    for label,change in [("t_dependent_scalar",lambda c:c["C"][1][0].__setitem__(1,[0,1])),("wrong_constant",lambda c:c["C"][1][0].__setitem__(1,Fraction(2))),("false_jet_order",lambda c:c.__setitem__("E",1))]:
        c=deepcopy(ci); change(c); ok,why=verify(idempotent,c); assert not ok
        malformed[label]=why
    scalar=TupleModel([[[(0,1)]]])
    fake={"status":"closed","words":[()],"initial":[1],"C":[[[[0,1]]]],"d":1,"D":1,"b":1,"E":1}
    ok,why=verify(scalar,fake); assert not ok
    malformed["fake_K_t_closure_of_scalar_t"]=why
    report["malformed_rejected"]=malformed
    invalid_delta=False
    try: TupleModel([[[(1,)]]],(0,1))
    except ValueError: invalid_delta=True
    assert invalid_delta
    report["delta_zero_at_origin_rejected"]=True
    report["status"]="ALL EXACT FINITE-ALGEBRA CHECKS PASSED"
    print(json.dumps(report,indent=2))


if __name__=="__main__": main()

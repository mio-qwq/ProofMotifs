"""Independent coordinate-multiplication check of the F729 trace separator.
No imports from other project modules; reduces X^6=1+2X directly."""
import json
pows=[3**j for j in range(6)]
def add(a,b): return sum(((a//p+b//p)%3)*p for p in pows)
def mul(a,b):
 A=[a//p%3 for p in pows];B=[b//p%3 for p in pows];C=[0]*11
 for i in range(6):
  for j in range(6): C[i+j]=(C[i+j]+A[i]*B[j])%3
 for i in range(10,5,-1):
  c=C[i];C[i]=0
  C[i-6]=(C[i-6]+c)%3;C[i-5]=(C[i-5]+2*c)%3
 return sum(C[j]*pows[j] for j in range(6))
def power(a,n):
 out=1
 while n:
  if n&1:out=mul(out,a)
  a=mul(a,a);n//=2
 return out
def trace(a):
 out=0
 for j in range(6):out=add(out,power(a,3**j))
 assert out in (0,1,2)
 return out
A=[power(3,j) for j in range(728)]
assert len(set(A))==728 and power(3,728)==1
S=[power(9,j) for j in range(364)]
assert len(set(S))==364
seed=[1,power(9,25),power(9,311)]
omitted=[1,power(9,5),power(9,255)]
f=lambda u:trace(power(u,34))
assert add(add(*seed[:2]),seed[2])==0
assert add(add(*omitted[:2]),omitted[2])==0
assert all(sum(f(mul(t,x)) for x in seed)%3==0 for t in S)
assert sum(f(x) for x in omitted)%3==1
mode=[34*3**j%364 for j in range(6)]
affine=[0]+[3**j for j in range(6)]
assert len(set(mode))==6 and set(mode).isdisjoint(affine)
print(json.dumps({'field_modulus':[2,1,0,0,0,0,1],'primitive_cycle':728,'square_generator':9,'square_order':364,'seed':seed,'omitted_edge':omitted,'omitted_trace_values':[f(x) for x in omitted],'seed_trace_values':[f(x) for x in seed],'all_seed_translates_checked':364,'mode':mode,'affine_spectrum':affine},indent=2))

"""Independent PM-CYCLE10-E arithmetic, no project imports."""
import itertools,json,math
def trim(a):
 a=[x%3 for x in a]
 while a and not a[-1]:a.pop()
 return a
def rem(a,b):
 a=trim(a);b=trim(b)
 while a and len(a)>=len(b):
  z=a[-1]*pow(b[-1],-1,3)%3;k=len(a)-len(b)
  for j,c in enumerate(b):a[k+j]=(a[k+j]-z*c)%3
  a=trim(a)
 return a
def gcd(a,b):
 while b:a,b=b,rem(a,b)
 return [x*pow(a[-1],-1,3)%3 for x in a]
def mulpoly(a,b,f):
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%3
 return rem(c,f)
def ppow(a,n,f):
 b=[1]
 while n:
  if n&1:b=mulpoly(a,b,f)
  a=mulpoly(a,a,f);n//=2
 return b
g=gcd([2]+[0]*12+[1],[1,1,0,0,1])
assert len(g)==5
def irreducible13(f):
 if len(gcd(f,[0,2,0,1]))!=1:return False
 return ppow([0,1],3**13,f)==[0,1]
mod=None
for j in range(1,13):
 for c,e in itertools.product((1,2),repeat=2):
  f=[c]+[0]*12+[1];f[j]=e
  if irreducible13(f):mod=f;break
 if mod:break
assert mod
m=13;q=3**m;N=(q-1)//2
pows=[3**i for i in range(m)]
def encode(a):return sum(x*p for x,p in zip(a,pows))
def digits(a):return [a//p%3 for p in pows]
def add(a,b):return encode([(x+y)%3 for x,y in zip(digits(a),digits(b))])
def neg(a):return encode([-x%3 for x in digits(a)])
def mult(a,b):return encode(mulpoly(trim(digits(a)),trim(digits(b)),mod)) if a and b else 0
def power(a,n):
 b=1
 while n:
  if n&1:b=mult(a,b)
  a=mult(a,a);n//=2
 return b
def L(y):return add(add(y,power(y,3)),power(y,81))
cols=[digits(L(p)) for p in pows]
mat=[[cols[j][i] for j in range(m)] for i in range(m)]
piv=[];r=0
for c in range(m):
 sel=next((i for i in range(r,m) if mat[i][c]),None)
 if sel is None:continue
 mat[r],mat[sel]=mat[sel],mat[r]
 z=pow(mat[r][c],-1,3);mat[r]=[x*z%3 for x in mat[r]]
 for i in range(m):
  if i!=r:
   z=mat[i][c];mat[i]=[(x-z*y)%3 for x,y in zip(mat[i],mat[r])]
 piv.append(c);r+=1
free=[j for j in range(m) if j not in piv];basis=[]
for j in free:
 v=[0]*m;v[j]=1
 for i,c in enumerate(piv):v[c]=-mat[i][j]%3
 basis.append(encode(v))
assert len(basis)==4
kernel=[];passing=[]
def chi(x):return power(x,N) if x else 0
for cs in itertools.product(range(3),repeat=4):
 y=0
 for c,b in zip(cs,basis):
  for _ in range(c):y=add(y,b)
 assert L(y)==0;kernel.append(y)
 if y in (0,1,2):continue
 if len({chi(y),chi(add(y,1)),chi(add(y,2))})!=1:continue
 inv=power(y,q-2);a=add(1,inv);b=add(1,neg(inv))
 assert add(add(1,a),b)==0 and chi(a)==chi(b)==1
 assert add(add(1,power(a,85)),power(b,85))==0
 # Since 13 is prime, any nonprime-field a generates the whole field.
 assert power(a,3)!=a
 passing.append({'y':y,'a':a,'b':b,'gcd_orders_bound':math.gcd(85,N)})
assert len(set(kernel))==81
# Independent trial-division primality proof, then nonidentity squares have order N.
assert all(N%d for d in range(2,math.isqrt(N)+1))
assert len(passing)==78
y=3**2+3**3+3**9
a=2*3**5+2*3**11+3**12
b=2+3**5+3**11+2*3**12
assert y==19719 and {'y':y,'a':a,'b':b,'gcd_orders_bound':1} in passing
assert mult(y,add(a,2))==1
assert len({1,a,b})==3 and power(a,N)==power(b,N)==1
assert a!=1 and b!=1
mode=[85*3**j%N for j in range(13)]
affine=[0]+[3**j%N for j in range(13)]
assert len(set(mode))==13 and set(mode).isdisjoint(affine)
def trace(x):
 z=0
 for _ in range(13):z=add(z,x);x=power(x,3)
 assert z in (0,1,2)
 return z
aa=1+3+3**3+3**4
bb=1+2*3+2*3**3+2*3**4
assert add(add(1,aa),bb)==0 and len({1,aa,bb})==3
assert chi(aa)==chi(bb)==1
tracevals=[trace(power(t,85)) for t in (1,aa,bb)]
assert tracevals==[1,1,0] and sum(tracevals)%3==2
assert [trace(power(t,85)) for t in (1,a,b)]==[1,1,1]
print(json.dumps({'task':'PM-CYCLE10-E','field_modulus':mod,'rabin_irreducible':True,'square_order_prime':N,'linear_gcd':g,'kernel_basis':basis,'kernel_dimension':4,'kernel_size':81,'square_filtered_count':len(passing),'selected':{'y':y,'a':a,'b':b},'extra_frobenius_orbit':mode,'affine_frobenius_orbit':affine,'kernel_lower_bound':27,'omitted_edge': [1,aa,bb],'omitted_trace_values':tracevals,'omitted_trace_sum':sum(tracevals)%3},indent=2))

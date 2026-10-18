"""Independent coefficient-list gcd, bounded-census and trace checks.

No imports from other project modules. Optional positional argument selects
an SC-013 report; by default check the repository's saved report. Run without
Python's -O flag, because independent arithmetic checks use assertions.
"""
import argparse
from pathlib import Path
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('report', nargs='?', type=Path,
                    default=Path(__file__).resolve().parents[1] / 'research/experiments/single-orbit-report.json')
args = parser.parse_args()
import json, math

def trim(a):
 a=[x%3 for x in a]
 while a and not a[-1]:a.pop()
 return a

def subtract(a,b):
 return trim([(a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])

def remainder(a,b):
 a=trim(a);b=trim(b)
 assert b
 while len(a)>=len(b):
  c=a[-1]*pow(b[-1],-1,3)%3
  k=len(a)-len(b)
  for j,v in enumerate(b):a[k+j]=(a[k+j]-c*v)%3
  a=trim(a)
 return a

def gcd(a,b):
 while b:a,b=b,remainder(a,b)
 return [(c*pow(a[-1],-1,3))%3 for c in a]

def plus(a,b):return subtract(a,[-x for x in b])

f=[2,1,0,0,0,0,1];q=729;N=364
# Ordinary coefficient-list long division, independently coded, no project imports.
a=[1];powers=[]
for i in range(q-1):
 powers.append(a)
 a=remainder([0]+a,f)
assert a==[1]
assert len({tuple(a) for a in powers})==q-1
h=[2]+[0]*(N-1)+[1]
rows=[]
for seed in [(0,25,311),(0,5,255)]:
 s=[]
 for e in seed:s=plus(s,powers[(2*e)%(q-1)])
 assert not s
 p=[0]*(max(seed)+1)
 for e in seed:p[e]=1
 d=gcd(h,p)
 rows.append({'seed':seed,'index':math.gcd(seed[1],seed[2],N),'gcd_degree':len(d)-1,'gcd_coefficients_ascending':d})
assert rows[0]['index']==1 and rows[0]['gcd_degree']==13
assert rows[1]['gcd_degree']==7
result={'engine':'independent ordinary coefficient-list polynomial division; no project/B imports','field_modulus':f,'primitive_x_full_cycle':len(powers),'rows':rows,'complete_censuses':[]}
# Independently check trace separator and the exact finite census reported in SC-013.
vals=[]
for e in range(N):
 value=[]
 for j in range(6):value=plus(value,powers[(2*e*34*3**j)%728])
 assert not value or len(value)==1
 vals.append(value[0] if value else 0)
assert all(sum(vals[(t+e)%N] for e in [0,25,311])%3==0 for t in range(N))
assert [vals[e] for e in [0,5,255]]==[0,0,1]
enc=lambda a:sum(c*3**i for i,c in enumerate(a))
assert [enc(powers[2*e%728]) for e in [0,25,311]]==[1,118,235]
assert [enc(powers[2*e%728]) for e in [0,5,255]]==[1,567,407]
report=json.loads(args.report.read_text())['report']
for field in report['fields']:
 m=field['m']
 if m>6:continue
 q=3**m;n=(q-1)//2;mod=field['field_modulus'];ps=[];a=[1]
 for k in range(q-1):ps.append(a);a=remainder([0]+a,mod)
 assert a==[1] and len(set(map(tuple,ps)))==q-1
 sq=ps[::2];log={tuple(v):i for i,v in enumerate(sq)};patterns=set()
 for i,u in enumerate(sq):
  v=subtract([-1],u)
  if tuple(v) not in log:continue
  j=log[tuple(v)];tr=(0,i,j)
  if len(set(tr))<3:continue
  patterns.add(min(tuple(sorted((e-t)%n for e in tr)) for t in tr))
 assert sorted(patterns)==[tuple(row['seed']) for row in field['orbits']]
 for row in field['orbits']:
  seed=row['seed'];p=[0]*(max(seed)+1)
  for e in seed:p[e]=1
  assert len(gcd([2]+[0]*(n-1)+[1],p))-1==row['gcd_degree']
  assert math.gcd(seed[1],seed[2],n)==row['connectivity_index']
 result['complete_censuses'].append({'m':m,'orbits':len(patterns)})
result['trace_witness']={'seed_translates_checked':364,'seed_violations':0,'omitted_edge_values':[0,0,1]}
print(json.dumps(result,indent=2))

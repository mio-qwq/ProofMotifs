"""Independent exact toy checks for PM-FACTOR-C; no external packages."""
from itertools import product, combinations_with_replacement


def trim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b, p):
    return trim(((a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)) % p
                for i in range(max(len(a), len(b))))


def neg(a, p):
    return trim((-x) % p for x in a)


def mul(a, b, p):
    c = [0] * max(0, len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j] + x*y) % p
    return trim(c)


def divmodp(a, b, p):
    a = list(trim(a))
    assert b
    q = [0] * max(0, len(a)-len(b)+1)
    inv = pow(b[-1], -1, p)
    while len(a) >= len(b):
        k = len(a)-len(b)
        c = a[-1]*inv % p
        q[k] = c
        for j, v in enumerate(b):
            a[k+j] = (a[k+j]-c*v) % p
        a = list(trim(a))
    return trim(q), trim(a)


def gcd(a, b, p):
    while b:
        a, b = b, divmodp(a, b, p)[1]
    return trim(x*pow(a[-1], -1, p) % p for x in a) if a else ()


def mm(a, b, f, p):
    return divmodp(mul(a, b, p), f, p)[1]


def mpow(a, k, f, p):
    b = (1,)
    while k:
        if k & 1:
            b = mm(b, a, f, p)
        a = mm(a, a, f, p)
        k //= 2
    return b


def rank(rows, p):
    rows = [list(r) for r in rows]
    if not rows:
        return 0
    r = 0
    for j in range(len(rows[0])):
        v = next((i for i in range(r, len(rows)) if rows[i][j]), None)
        if v is None:
            continue
        rows[r], rows[v] = rows[v], rows[r]
        z = pow(rows[r][j], -1, p)
        rows[r] = [x*z % p for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][j]:
                z = rows[i][j]
                rows[i] = [(x-z*y) % p for x,y in zip(rows[i], rows[r])]
        r += 1
        if r == len(rows):
            break
    return r


def pad(a, n):
    return list(a) + [0]*(n-len(a))


def fixed_dim(f, p):
    n = len(f)-1
    rows = []
    for j in range(n):
        v = (0,)*j + (1,)
        rows.append(pad(add(mpow(v,p,f,p),neg(v,p),p),n))
    return n-rank(rows,p)


def closure_dim(es, f, p):
    n = len(f)-1
    basis = [(1,)]
    for e in es:
        offers = basis + [mm(e,b,f,p) for b in basis]
        basis = []
        for b in offers:
            if rank([pad(v,n) for v in basis+[b]],p) > len(basis):
                basis.append(b)
    return len(basis)


def leaves(es, f, p):
    out = [f]
    for e in es:
        new = []
        for h in out:
            for a in (0,1):
                d = gcd(h,add(e,(-a % p,),p),p)
                if len(d)>1:
                    new.append(d)
        out = new
    return out


def factors(f,p):
    h = f
    out = []
    for d in range(1, (len(f)-1)//2+1):
        for cs in product(range(p),repeat=d):
            g = tuple(cs)+(1,)
            while len(h)>d and not divmodp(h,g,p)[1]:
                out.append(g)
                h = divmodp(h,g,p)[0]
    if len(h)>1:
        out.append(h)
    return out


def crt_idempotent(fs, bits, p):
    f = (1,)
    for h in fs:
        f = mul(f,h,p)
    e = ()
    # Each quotient's inverse is obtained by exhaustive search only in this
    # bounded checker, never used as a complexity claim.
    for h, bit in zip(fs,bits):
        if not bit:
            continue
        q = divmodp(f,h,p)[0]
        d = len(h)-1
        inv = next(tuple(cs) for cs in product(range(p),repeat=d)
                   if divmodp(mul(q,cs,p),h,p)[1] == (1,))
        e = add(e,mul(q,inv,p),p)
    return divmodp(e,f,p)[1]


checked = 0
family_checks = 0
for p,maxn in ((2,6),(3,4),(5,3)):
    for n in range(1,maxn+1):
        for cs in product(range(p),repeat=n):
            f = tuple(cs)+(1,)
            der = trim(i*f[i] % p for i in range(1,len(f)))
            if len(gcd(f,der,p)) != 1:
                continue
            fs = factors(f,p)
            r = len(fs)
            assert r == fixed_dim(f,p)
            bits = list(product((0,1),repeat=r))
            idem = [crt_idempotent(fs,b,p) for b in bits]
            assert all(mm(e,e,f,p) == e for e in idem)
            # All families of size 0, 1, 2, including repeated entries.
            fams = [()] + [(i,) for i in range(len(idem))]
            fams += list(combinations_with_replacement(range(len(idem)),2))
            for inds in fams:
                es = [idem[i] for i in inds]
                codes = {tuple(bits[i][j] for i in inds) for j in range(r)}
                dim = closure_dim(es,f,p)
                ls = leaves(es,f,p)
                assert dim == len(codes) == len(ls)
                assert (dim == r) == (set(ls)==set(fs))
                family_checks += 1
            t = (r-1).bit_length()
            es = [crt_idempotent(fs,[(j>>k)&1 for j in range(r)],p)
                  for k in range(t)]
            assert closure_dim(es,f,p)==r
            assert set(leaves(es,f,p))==set(fs)
            checked += 1

# Nonreduced failure: fixed algebra complete, yet its only leaf is reducible.
p = 5
f = (0,0,1)
assert fixed_dim(f,p)==closure_dim([],f,p)==1
assert leaves([],f,p)==[f]
assert mm((0,1),(0,1),f,p)==()
assert mpow((0,1),p-1,f,p)==()
print(f"PASS: {checked} squarefree inputs; {family_checks} binary families")
print("PASS: nonreduced f=X^2 has complete empty family but reducible leaf X^2")
print("PASS: nilpotent X != 0 yet X^(p-1)=0 in F5[X]/X^2")

# Missing full-primary-generator failure in source02's digit routine.
# p=19, q=3, s=2; 7 has order 3, not 9. a=8 is a cube, with 2^3=8.
p,q,s = 19,3,2
u,a = 7,8
assert pow(2,q,p)==a and pow(u,q,p)==1 and u != 1
t = 2
aq = pow(a,t*pow(t,-1,q**s),p)
assert aq==11
base = pow(u,q**(s-1),p)
digit_targets = [pow(aq,q**(s-j-1),p) for j in range(s)]
assert base==1 and digit_targets==[1,11]
print("PASS: weakened order-3 u=7 fails source02 digit step j=1 for cube a=8 over F19")

# The auxiliary residue test supplies transitive Frobenius, not just a q-space.
# Dropping that test: all other elementary aux-prime conditions hold here.
p,q,ell = 73,3,37
assert ell % (12*q)==1 and ell not in (2,3,p,q)
H = {pow(a,q,ell) for a in range(1,ell)}
remaining = set(range(1,ell))
cosets = []
while remaining:
    a = min(remaining)
    c = {a*h % ell for h in H}
    cosets.append(c)
    remaining -= c
action = [next(j for j,c in enumerate(cosets) if p*min(cs)%ell in c)
          for cs in cosets]
assert len(cosets)==q and pow(p,(ell-1)//q,ell)==1
assert action == list(range(q))
print("PASS: p=73,q=3,ell=37 without residue test gives U_q=F73^3, not a field")

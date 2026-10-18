# PM-CYCLE8-E2 independent audit: two punctured axes

Reviewer: /root/weil_completion_review, actual scoped AI agent.
Date: 2026-10-18. Scope: candidate supplied by coordinator; independent
adversarial derivation. No shared files edited and no Git writes/pushes.

## Verdict

ACCEPT every stated result for e>=2. One important scope clarification:
the e=1 exception belongs to the two-axis hypergraph and its connected-
component argument, not to either single-axis kernel or automorphism result.
For one punctured one-dimensional axis those conclusions still hold trivially.
No human or Lean verification or historical novelty is claimed.

## 1. Field construction and multiplicative subgroup

Put s=3^e and choose a nonzero nonsquare a in F_s. Such a exists because
F_s* has even order. The polynomial X^2-a is irreducible over F_s, and
adjoining a root beta produces K=F_(s^2). Every element of K has a unique
form u+beta*v with u,v in F_s, and beta notin F_s. Its conjugate is -beta,
so beta^s=-beta.

The sets U=F_s and W=beta*F_s are complementary e-dimensional F3-vector
subspaces of K. Their punctured union
H=U* union W*
is a subgroup of K*: products of two U* elements remain U*, a mixed product
lies in W*, and (beta*u)(beta*v)=a*u*v lies in U*. It contains1, is finite
and closed under multiplication, hence is a subgroup; inverses can also be
checked explicitly. Its two pieces are disjoint. Consequently
|H|=2(s-1), and [K*:H]=(s+1)/2.

Equivalently H is the unique subgroup of that order, or the solutions of
x^(2(s-1))=1. On its two axes,
x^(s-1)=1 on U*, and x^(s-1)=-1 on W*.
This also shows directly why the order-two multiplicative character records
which component a vertex belongs to.

## 2. Hypergraph decomposition and connectivity

A triple from H which uses both axes has two entries from one and one entry
from the other. Its projection onto the latter nonzero axis is nonzero, so
it cannot sum to zero. Thus all edges lie inside one axis. Inside an axis,
the distinct zero-sum triples are exactly the affine F3-lines avoiding0.

Within P=F3^e\{0}, distinct x,y lie together in an edge exactly when y!=-x.
Indeed their forced third point is -x-y, which is nonzero in that case and
cannot equal either endpoint unless x=y (characteristic3 is used here).
For e>=2, an opposite pair x,-x has a common neighbor z chosen outside
{0,x,-x}. Hence the adjacency graph is connected. The two punctured axes
are therefore exactly the hypergraph's two connected components.

## 3. Complete punctured-axis kernel proof

Let f:P->F3 vanish in sum on each edge. Any zero-sum triple with repetitions
is diagonal in characteristic3, and then its f equation is automatic.

For any relation u+v=w+z in P, choose a outside the at most four values
{0,-u,-w,z-u}; this is possible since |V|=s>=9. Put
b=-u-a, c=-w-a, d=u+a-z.
All are nonzero. The four triples
(u,a,b), (w,a,c), (b,z,d), (c,v,d)
have sum zero. Their f equations yield
f(u)-f(w)=f(c)-f(b)=f(z)-f(v),
so f(u)+f(v)=f(w)+f(z). No further exclusions are needed for repeated entries.

The difference set P-P is all V: for a given nonzero x choose b outside
{0,-x}, and use (b+x)-b=x. Define L(x)=f(b+x)-f(b). Equality of two difference
representations is a two-sum relation, so L is well-defined. It gives
L(0)=0 and L(-x)=-L(x).
Choose b outside {0,-x,-x-y}, possible because s>=9. Telescoping the three
values f(b),f(b+x),f(b+x+y) yields
L(x+y)=L(x)+L(y).
This choice also works when some forbidden values coincide; alternatively
zero arguments and opposite arguments can be treated directly. Thus L is
F3-linear and f(u)=L(u)+c on P.

Conversely every affine restriction has zero edge sum. Restrictions are
independent: an affine function which vanishes at every nonzero point must
have constant0, by comparing x and -x, and then its linear part vanishes
on all of V. Hence the kernel dimension is e+1.
A separate actual scoped reviewer, /punctured_kernel_audit, independently
accepted this argument and the automorphism argument below.

## 4. Automorphisms of one component

For any permutation sigma of P preserving its edges, each coordinate of
sigma belongs to the preceding kernel. Coordinatewise affine extension
gives F(x)=A(x)+t, with A F3-linear, restricting to sigma on P.
If A were singular its image would have at most3^(e-1)<3^e-1 points, which
contradicts bijectivity on P. Thus A is invertible. Since F is now an affine
permutation of V,
F(P)=V\{t}.
But this equals P=V\{0}, so t=0. Conversely all invertible F3-linear maps
preserve P and zero sums. Therefore Aut(P)=GL(e,3).

No theorem concerning arbitrary affine-space automorphisms is being silently
assumed. The supplied derivation proves the needed special case directly.
The object and its rigidity are classical; this does not establish novelty
relative to Pavone or any other finite-geometry classification.

## 5. Two-axis automorphisms and ambient stabilizer

Because the two connected components are isomorphic and indivisible under
an automorphism, their full group is
Aut(H)=GL(e,3) wr S2=(GL(e,3) x GL(e,3)) semidirect S2.
Every such action extends to a linear map of U directsum W, by choosing
independent linear maps on the two axes and optionally exchanging them.
Conversely an ambient linear map stabilizing H restricts to a hypergraph
automorphism. The restriction is faithful because H spans K. Thus this
hypergraph automorphism group is exactly the ambient F3-linear stabilizer.

For e=2, |GL(2,3)|=(9-1)(9-3)=48, giving
|Aut(H)|=2*48^2=4608.
The obvious field-semilinear subgroup consists of x->h*x^(3^j), h inH,
0<=j<2e. It has size |H|*2e=4e(s-1), equal to64 for e=2.
Its parameters act distinctly: equality at1 fixes h, and H spans K, so
agreement of the two Frobenius powers on H implies agreement on K.

## 6. Kernel obstruction and its precise meaning

The edge equations on the disconnected axes are independent, so the full
kernel dimension is2(e+1)=2e+2. Ambient affine functions restrict injectively
to H and have dimension2e+1. Injectivity follows by comparing x and-x on
one axis to kill the constant, and then using both axes to kill the linear
part. In componentwise affine descriptions, the only missing condition for
an ambient affine restriction is equality of the two component constants.

The indicator which equals1 on U* and0 on W* satisfies every edge equation
but cannot be an ambient affine restriction: constancy on U* forces its
ambient constant to be1, while constancy on W* forces it to be0.
It has the explicit multiplicative expression
f(x)=(1+x^(s-1))/2 on H.
This gives the entire one-dimensional excess over the ambient affine kernel.

Thus minimal affine-kernel dimension is indeed NOT necessary for equality
of hypergraph automorphisms with the ambient linear stabilizer. It remains
a sufficient reconstruction criterion. This family does not contradict
the square-subgroup theorem: for e>=2 its subgroup index is(s+1)/2>=5,
rather than2.

## 7. Small case and limits

When e=1, each punctured axis has2 vertices and no edges; the full H has4
isolated vertices, so Aut(H)=S4 of order24, while its ambient linear
stabilizer has order8. The statement about exactly two connected components
is false there, correctly motivating the hypothesis e>=2. The single-axis
kernel dimension remains2=e+1 and its automorphism group isS2=GL(1,3).

The classification is valid for every integer e>=2, without unproved
asymptotics or reliance on finite enumeration. It has not been independently
formalized. Its classical finite-geometry nature and direct proof should
be preserved in all claims; no first-discovery assertion is justified.

Concrete next step: retain this as a precise obstruction/counterexample to
necessity of the minimal-kernel criterion, record the explicit order-two
character responsible, and use it as a negative control for SC-010 rather
than treating it as a new broad classification method.

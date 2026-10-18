# PM-CYCLE11-D: scoped normal-character basecases

Only degrees 4, 5, 8 were searched. No repository files were edited.

Commands actually run successfully:

```
python /tmp/pm_cycle11_d_small_normal.py
python /tmp/pm_cycle11_d_independent.py
```

The first script uses the existing CompactField field power-cycle certificate
but a separately implemented Gaussian rank routine. The second script imports
no project modules and implements ordinary F3 coefficient-list polynomial
arithmetic, Rabin irreducibility, primitive order, character powers, and a
second column-elimination rank routine. This is independent arithmetic
verification, not proof-assistant formalization or human review.

## Degree four is impossible

Let F=F81. Exactly eighteen y satisfy
chi(y-1)=chi(y)=chi(y+1) nonzero. There are 32 normal elements, and none
of these eighteen is normal. Their conjugate ranks are: rank one, two
elements; rank two, eight elements; rank three, eight elements.

This has a field-independent polynomial certificate, beyond a field table.
All polynomials below belong to F3[Y]. Put

G=gcd(Y^81-Y, (Y-1)^40-Y^40, (Y+1)^40-Y^40).

Ordinary Euclidean arithmetic gives

G=Y^18+Y^10+2Y^6+2Y^4+2=G6*G12,
G6=Y^6+Y^4+Y^2+1,
G12=Y^12+2Y^10+2Y^4+Y^2+2.

There are no extraneous zero-character solutions: if one of y-1,y,y+1
is zero, they cannot all have equal fortieth powers. The gcd with
Y^81-Y ensures these eighteen roots are simple and split in F81.

The factor G6 divides Y^9-Y, so those six roots lie in F9 and have
conjugate rank at most two. The other factor divides

L(Y)=Y^27-Y^9+Y^3-Y,

as checked by exact polynomial division. If sigma(y)=y^3, this says
(sigma-1)(sigma^2+1)y=0, a nonzero relation among four Frobenius
conjugates. Hence the remaining twelve roots have rank at most three.
No qualifying y can be normal. In particular a proposed normal-pattern
existence theorem must exclude degree four.

## Degree five witness

Field modulus X^5+2X+1, primitive X, gamma=X^2.
The first witness in ascending base-three coordinate order is y=4=1+X.
Its conjugates are [4,28,165,180,228], with independent coordinate rank
five. The three quadratic characters are all -1.

Set a=(y+1)/y=211, b=(y-1)/y=151. Then a,b are squares, 1+a+b=0,
and their gamma-exponents give seed [0,89,87]. The connectivity index
gcd(89,87,121) equals one. Selected-seed ternary bitplane polynomial
gcd gives kernel dimension six, so this selected seed is good.

## Degree eight witness

Field modulus X^8+X^3+2, primitive X, gamma=X^2.
First witness y=40=1+X+X^2+X^3. Its conjugates are
[40,922,2525,612,4143,4914,5444,1811], with rank eight.
Again all three characters are -1.

Set a=1721, b=1224. Their gamma-exponents give seed [0,771,35].
The connectivity index gcd(771,35,3280) equals one. Selected-seed
ternary bitplane polynomial gcd gives kernel dimension nine, so this
selected seed is good.

The degree-five scan stopped after five field elements (including zero);
the degree-eight scan stopped after 41. Counts before stopping are not
total existence counts. The independent script checks the selected
witnesses directly without repeating those two searches. Only the
degree-four scan was complete. These finite checks do not prove that
all normal-character seeds are connected or good.

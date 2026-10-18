"""Exact finite checks of the square-set Freiman completion gadgets.

This checks finite instances, including genuine small-field failures.  It is
not a proof of a character-sum estimate or of an infinite classification.  The
field arithmetic is the repository's existing exact ``Field`` implementation.

For u+v=w+z in the nonzero square set S, choose a and put
b=-u-a, c=-w-a, d=u+a-z.  The four zero-sum triples
(u,a,b), (w,a,c), (b,z,d), (c,v,d) imply the pair-sum equation
f(u)+f(v)=f(w)+f(z).  Repeated vertices are allowed in this auxiliary gadget:
a repeated zero-sum triple in characteristic three has all entries equal, so
its corresponding F_3-valued equation is automatic.
"""

from collections import Counter
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cancellation import Field


def bit_elements(mask: int):
    """Yield encoded field elements in increasing order."""
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def nontrivial_pair_relation(u: int, v: int, w: int, z: int) -> bool:
    return sorted((u, v)) != sorted((w, z))


def bound_holds(count: int, q: int, constant: int, radical: int,
                denominator: int) -> bool:
    """Exact check: count >= (q-constant-radical*sqrt(q))/denominator."""
    remainder = q - constant - denominator * count
    return remainder <= 0 or remainder * remainder <= radical * radical * q


class CompletionGeometry:
    def __init__(self, field: Field):
        if field.p != 3:
            raise ValueError("characteristic three required")
        self.f = field
        self.squares = tuple(sorted({field.mul[t][t] for t in range(1, field.q)}))
        self.square_set = set(self.squares)
        self.square_mask = sum(1 << s for s in self.squares)
        # shift_masks[t] contains exactly a with a+t in S, including a=0
        # when appropriate.  Intersect with square_mask when a itself is needed.
        self.shift_masks = tuple(
            sum(1 << a for a in range(field.q) if field.add[a][t] in self.square_set)
            for t in range(field.q))
        self.reflected_masks = tuple(
            sum(1 << a for a in range(field.q)
                if field.neg[field.add[t][a]] in self.square_set)
            for t in range(field.q))

    def check_relation(self, u: int, v: int, w: int, z: int) -> None:
        if any(t not in self.square_set for t in (u, v, w, z)):
            raise ValueError("all four relation entries must be nonzero squares")
        if self.f.add[u][v] != self.f.add[w][z]:
            raise ValueError("the pair-sum relation does not hold")

    def completion_mask(self, u: int, v: int, w: int, z: int) -> int:
        self.check_relation(u, v, w, z)
        shift = self.f.add[u][self.f.neg[z]]
        return (self.square_mask & self.reflected_masks[u]
                & self.reflected_masks[w] & self.shift_masks[shift])

    def roots(self, u: int, w: int, z: int) -> tuple[int, int, int, int]:
        return (0, self.f.neg[u], self.f.neg[w],
                self.f.add[z][self.f.neg[u]])

    def gadget(self, u: int, v: int, w: int, z: int, a: int):
        self.check_relation(u, v, w, z)
        f = self.f
        b = f.neg[f.add[u][a]]
        c = f.neg[f.add[w][a]]
        d = f.add[f.add[u][a]][f.neg[z]]
        return ((u, a, b), (w, a, c), (b, z, d), (c, v, d))

    def relations(self, normalized: bool = False):
        """Every ordered nontrivial relation, or its square-scaling u=1 slice.

        Every nonzero square u has a square inverse.  Multiplication by that
        inverse sends u to 1 and is a bijection on S and gadget completions.
        Thus the normalized slice represents every ordered relation exactly
        |S| times when all square scalings are restored.
        """
        f = self.f
        first = (1,) if normalized else self.squares
        for u in first:
            for v in self.squares:
                total = f.add[u][v]
                for w in self.squares:
                    z = f.add[total][f.neg[w]]
                    if z in self.square_set and nontrivial_pair_relation(u, v, w, z):
                        yield (u, v, w, z)

    def relation_report(self, normalized: bool = False) -> dict:
        f = self.f
        histogram = Counter()
        instances = 0
        first_failure = None
        for relation in self.relations(normalized):
            u, v, w, z = relation
            # This also checks all six potential root collisions in the exact
            # tested family, independently of the completion-count predicate.
            if len(set(self.roots(u, w, z))) != 4:
                raise AssertionError(("root collision", relation))
            mask = self.completion_mask(*relation)
            count = mask.bit_count()
            histogram[count] += 1
            if not count and first_failure is None:
                first_failure = list(relation)
            if not bound_holds(count, f.q, 38, 11, 16):
                raise AssertionError(("four-form bound failed", relation, count))
            for a in bit_elements(mask):
                for triple in self.gadget(*relation, a):
                    if any(t not in self.square_set for t in triple):
                        raise AssertionError(("nonsquare in gadget", relation, a))
                    if f.add[f.add[triple[0]][triple[1]]][triple[2]]:
                        raise AssertionError(("gadget sum is nonzero", relation, a))
                    if len(set(triple)) < 3 and len(set(triple)) != 1:
                        raise AssertionError(("invalid repeated triple", triple))
                instances += 1
        examined = sum(histogram.values())
        return {
            "scope": "u=1 square-scaling representatives" if normalized
                     else "all ordered nontrivial square pair-sum relations",
            "relations_examined": examined,
            "ordered_relations_represented": examined * (len(self.squares) if normalized else 1),
            "completion_count_histogram": dict(sorted(histogram.items())),
            "minimum_completions": min(histogram) if histogram else None,
            "failed_relations": histogram[0],
            "first_failure": first_failure,
            "complete_gadget_instances_checked": instances,
            "distinct_roots_checked_for_every_examined_relation": True,
            "character_lower_bound_checked_for_every_examined_relation": True,
        }

    def triple_report(self) -> dict:
        """Check all b,b+x,b+x+y intersections with x,y,x+y nonzero."""
        f = self.f
        histogram = Counter()
        first_failure = None
        for x in range(1, f.q):
            for y in range(1, f.q):
                total = f.add[x][y]
                if total == 0:
                    continue
                mask = self.square_mask & self.shift_masks[x] & self.shift_masks[total]
                count = mask.bit_count()
                histogram[count] += 1
                if not count and first_failure is None:
                    first_failure = [x, y]
                if not bound_holds(count, f.q, 15, 2, 8):
                    raise AssertionError(("three-form bound failed", x, y, count))
        return {
            "nondegenerate_ordered_increment_pairs": sum(histogram.values()),
            "intersection_count_histogram": dict(sorted(histogram.items())),
            "minimum_intersection": min(histogram),
            "empty_intersections": histogram[0],
            "first_failure": first_failure,
            "character_lower_bound_checked_for_every_pair": True,
        }


def character_expansion(geometry: CompletionGeometry, relation) -> dict:
    """Directly verify the four-indicator expansion and its root correction.

    The product of 1+chi at a root can be nonzero although the corresponding
    square-membership indicator is zero.  The four root corrections are each
    at most eight, so their total is at most 32.
    """
    u, v, w, z = relation
    geometry.check_relation(*relation)
    f = geometry.f

    def chi(x):
        return 0 if x == 0 else (1 if x in geometry.square_set else -1)

    raw_sum = 0
    correction = 0
    roots = set(geometry.roots(u, w, z))
    for a in range(f.q):
        forms = (a, f.neg[f.add[u][a]], f.neg[f.add[w][a]],
                 f.add[f.add[u][a]][f.neg[z]])
        term = 1
        for value in forms:
            term *= 1 + chi(value)
        raw_sum += term
        if a in roots:
            correction += term
    count = geometry.completion_mask(*relation).bit_count()
    if raw_sum - correction != 16 * count:
        raise AssertionError("indicator expansion does not reproduce the exact count")
    return {"raw_indicator_sum": raw_sum, "root_correction": correction,
            "completion_count": count}


def main() -> None:
    fields = (Field(3, (0, 1)), Field(3, (1, 0, 1)),
              Field(3, (1, 2, 0, 1)), Field(3, (2, 0, 1, 0, 1)),
              Field(3, (1, 2, 0, 0, 0, 1)))
    reports = []
    for f in fields:
        geometry = CompletionGeometry(f)
        reports.append({"q": f.q, "modulus": list(f.modulus),
                        "nonzero_squares": len(geometry.squares),
                        "four_form_completions": geometry.relation_report(f.q == 243),
                        "three_form_intersections": geometry.triple_report()})
    print(json.dumps({"schema": 1, "arithmetic": "exact repository finite-field tables",
                      "randomized": False,
                      "scope": "finite certificates; no infinite theorem inferred",
                      "fields": reports}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

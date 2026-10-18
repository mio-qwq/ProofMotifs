"""Independent exact audit checks. No third-party dependencies or file output.

The oracle is Fourier--Motzkin elimination with tracked rational Farkas
multipliers, intentionally different from a closest-convex-hull oracle.
"""
from fractions import Fraction as F
from itertools import product
import json


def dot(a, b):
    return sum((F(x) * F(y) for x, y in zip(a, b)), F(0))


def certificate_oracle(rows, target):
    rows = [tuple(map(F, row)) for row in rows]
    n = len(rows[0])
    dset = set(target)
    initial = []
    for s in range(n):
        col = tuple(row[s] for row in rows)
        signs = (1, -1) if s in dset else (1,)
        for sign in signs:
            z = tuple(F(sign if i == s else 0) for i in range(n))
            initial.append((tuple(sign * x for x in col),
                            F(0 if s in dset else 1), z))

    def fm(ineqs, k):
        if k == 0:
            for a, b, z in ineqs:
                if b > 0:
                    return None, tuple(v / b for v in z)
            return (), None
        lower = [q for q in ineqs if q[0][-1] > 0]
        upper = [q for q in ineqs if q[0][-1] < 0]
        projected = [(a[:-1], b, z) for a, b, z in ineqs if a[-1] == 0]
        for ap, bp, zp in lower:
            for an, bn, zn in upper:
                fp, fn = F(1) / ap[-1], -F(1) / an[-1]
                projected.append((tuple(fp*x + fn*y for x, y in zip(ap[:-1], an[:-1])),
                                  fp*bp + fn*bn,
                                  tuple(fp*x + fn*y for x, y in zip(zp, zn))))
        x, z = fm(projected, k - 1)
        if z is not None:
            return None, z
        lo = [(b - dot(a[:-1], x)) / a[-1] for a, b, _ in lower]
        hi = [(b - dot(a[:-1], x)) / a[-1] for a, b, _ in upper]
        last = max(lo) if lo else min(hi) if hi else F(0)
        assert not hi or last <= min(hi)
        return x + (last,), None

    c, z = fm(initial, len(rows))
    if c is not None:
        w = tuple(dot(c, [row[s] for row in rows]) for s in range(n))
        assert all(w[s] == 0 if s in dset else w[s] >= 1 for s in range(n))
        return {"feasible": True, "coefficient": c, "weight": w}
    assert all(dot(row, z) == 0 for row in rows)
    assert all(z[s] >= 0 for s in range(n) if s not in dset)
    assert sum(z[s] for s in range(n) if s not in dset) == 1
    return {"feasible": False, "trade": z}


def repair(base, blocks, target, costs):
    masks = list(product((0, 1), repeat=len(blocks)))
    cuts, trace = [], []
    while True:
        allowed = [x for x in masks if all(any(x[j] for j in cut) for cut in cuts)]
        if not allowed:
            return {"feasible": False, "cuts": cuts, "trace": trace}
        x = min(allowed, key=lambda a: (dot(a, costs), sum(a), a))
        rows = base + [r for j, block in enumerate(blocks) if x[j] for r in block]
        result = certificate_oracle(rows, target)
        trace.append({"mask": x, **result})
        if result["feasible"]:
            return {"feasible": True, "mask": x, "cost": dot(x, costs),
                    "cuts": cuts, "trace": trace}
        z = result["trade"]
        cut = tuple(j for j, block in enumerate(blocks) if any(dot(r, z) != 0 for r in block))
        assert not any(x[j] for j in cut)
        cuts.append(cut)
        assert len(trace) <= len(masks)


def serial(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [serial(v) for v in x]
    return x


def main():
    base = [(1, 1, 1)]
    signed = [(0, 1, -1)]
    rays = [(-1, 1, 0), (-1, 0, 1)]
    assert all(any(dot(r, v) for r in signed) for v in rays)
    assert dot(signed[0], (-2, 1, 1)) == 0
    signed_result = certificate_oracle(base + signed, (0,))
    assert not signed_result["feasible"]
    adaptive = repair(base, [signed, [(0, 1, 1)]], (0,), (1, 2))
    assert adaptive["feasible"] and adaptive["cost"] == 2

    onehot_base = [(1, 0, 1, 0), (0, 1, 0, 1)]
    onehot_added = [(1, 0, 0, 1), (0, 1, 1, 0)]
    onehot_rays = [(-1, 0, 1, 0), (0, -1, 0, 1)]
    assert all(any(dot(r, v) for r in onehot_added) for v in onehot_rays)
    assert all(dot(r, (-1, -1, 1, 1)) == 0 for r in onehot_base + onehot_added)
    onehot_result = certificate_oracle(onehot_base + onehot_added, (0, 1))
    assert not onehot_result["feasible"]

    # Independent exhaustive check of the weighted-set-cover subcase.
    sets = [{0, 1}, {1, 2}, {2}]
    scblocks = [[tuple([0] + [int(u in s) for u in range(3)])] for s in sets]
    scbase = [(1, 1, 1, 1)]
    for mask in product((0, 1), repeat=3):
        chosen = set().union(*(sets[j] for j, b in enumerate(mask) if b))
        rows = scbase + [r for j, b in enumerate(mask) if b for r in scblocks[j]]
        assert certificate_oracle(rows, (0,))["feasible"] == (chosen == set(range(3)))
    sc = repair(scbase, scblocks, (0,), (2, 3, 1))
    assert sc["feasible"] and sc["cost"] == 3 and sc["mask"] == (1, 0, 1)

    # A fixed numerical coefficient bound is not innocuous.
    small = certificate_oracle([(1, 1), (0, F(1, 1024))], (0,))
    assert small["feasible"] and small["coefficient"][1] >= 1024

    # Direct evaluations, not the factorized proof, for the designed grid family.
    grids = []
    for r in range(1, 5):
        points = list(product((-1, 0, 1), repeat=r))
        q = [(-2)**sum(t == 0 for t in s) for s in points]
        moments = []
        for powers in product((0, 1, 2), repeat=r):
            val = 0
            for s, coeff in zip(points, q):
                term = coeff
                for t, power in zip(s, powers):
                    term *= t**power
                val += term
            assert val == (2**r if powers == (2,)*r else 0)
            moments.append(val)
        assert sum(c for s, c in zip(points, q) if 0 not in s) == 2**r
        grids.append({"dimension": r, "points": len(points), "moments": len(moments),
                      "top_moment": 2**r, "other_moments_zero": True})

    print(json.dumps(serial({"signed_ray_failure": signed_result,
                            "onehot_ray_failure": onehot_result,
                            "adaptive_repair": adaptive,
                            "setcover_masks_checked": 8, "setcover_repair": sc,
                            "coefficient_scale": small, "grid_family": grids}), indent=2))


if __name__ == "__main__":
    main()

"""Read-only independent audit of frozen feature-repair panels and report.

Uses target-equality nullspace elimination followed by tracked exact
Fourier--Motzkin, not the implementation's orthogonal projection/KKT oracle.
"""
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
from feature_repair_boundary import dot, serial


def echelon(rows, n):
    a = [list(map(F, row)) for row in rows]
    pivots, k = [], 0
    for j in range(n):
        candidates = [i for i in range(k, len(a)) if a[i][j] != 0]
        if not candidates:
            continue
        i = candidates[0]
        a[i], a[k] = a[k], a[i]
        divisor = a[k][j]
        a[k] = [v / divisor for v in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j]:
                mul = a[i][j]
                a[i] = [v - mul*w for v, w in zip(a[i], a[k])]
        pivots.append(j)
        k += 1
    return a, pivots


def independent_oracle(rows, target):
    rows = [tuple(map(F, r)) for r in rows]
    n, r = len(rows[0]), len(rows)
    target = sorted(target)
    off = [i for i in range(n) if i not in target]
    eqs = [[row[j] for row in rows] for j in target]
    reduced, pivots = echelon(eqs, r)
    basis = []
    for j in range(r):
        if j not in pivots:
            v = [F(int(i == j)) for i in range(r)]
            for k, pivot in enumerate(pivots):
                v[pivot] = -reduced[k][j]
            basis.append(v)
    inequalities = []
    for j in off:
        col = [row[j] for row in rows]
        inequalities.append((tuple(dot(v, col) for v in basis), F(1),
                             tuple(F(int(i == j)) for i in range(n))))

    def fm(ineqs, k):
        if k == 0:
            bad = next((q for q in ineqs if q[1] > 0), None)
            return (None, tuple(v/bad[1] for v in bad[2])) if bad else ((), None)
        pos = [q for q in ineqs if q[0][-1] > 0]
        neg = [q for q in ineqs if q[0][-1] < 0]
        projected = [(a[:-1], b, z) for a, b, z in ineqs if a[-1] == 0]
        for ap, bp, zp in pos:
            for an, bn, zn in neg:
                u, v = F(1)/ap[-1], -F(1)/an[-1]
                projected.append((tuple(u*x+v*y for x, y in zip(ap[:-1], an[:-1])),
                                  u*bp+v*bn, tuple(u*x+v*y for x, y in zip(zp, zn))))
        x, z = fm(projected, k-1)
        if z is not None:
            return None, z
        lower = [(b-dot(a[:-1], x))/a[-1] for a, b, _ in pos]
        upper = [(b-dot(a[:-1], x))/a[-1] for a, b, _ in neg]
        last = max(lower) if lower else min(upper) if upper else F(0)
        assert not upper or last <= min(upper)
        return x+(last,), None

    t, outside = fm(inequalities, len(basis))
    if t is not None:
        c = [sum((v[i]*scale for v, scale in zip(basis, t)), F(0)) for i in range(r)]
        w = [dot(c, [row[j] for row in rows]) for j in range(n)]
        assert all(w[j] == 0 if j in target else w[j] >= 1 for j in range(n))
        return {"kind": "selector", "coefficients": c, "weights": w}
    equations = [[row[j] for j in target] + [-dot(row, outside)] for row in rows]
    solved, pc = echelon(equations, len(target))
    assert all(any(row[:-1]) or not row[-1] for row in solved)
    z = list(outside)
    for k, pivot in enumerate(pc):
        z[target[pivot]] = solved[k][-1]
    assert all(dot(row, z) == 0 for row in rows)
    assert all(z[j] >= 0 for j in off) and sum(z[j] for j in off) == 1
    return {"kind": "trade", "trade": z}


def matrix(instance, mask):
    return instance["base_rows"] + [row for j, b in enumerate(instance["blocks"])
                                    if mask & (1 << j) for row in b["rows"]]


def cost(instance, mask):
    return sum((F(b["cost"]) for j, b in enumerate(instance["blocks"]) if mask & (1 << j)), F(0))


def check_certificate(instance, mask, cert):
    a, target = matrix(instance, mask), set(instance["target_indices"])
    n = len(instance["omega"])
    if cert["kind"] == "trade":
        z = list(map(F, cert["trade"]))
        assert len(z) == n
        assert all(dot(row, z) == 0 for row in a)
        assert all(z[j] >= 0 for j in range(n) if j not in target)
        assert sum(z[j] for j in range(n) if j not in target) == 1
    else:
        c = list(map(F, cert["coefficients"]))
        assert len(c) == len(a)
        w = [dot(c, [row[j] for row in a]) for j in range(n)]
        assert list(map(F, cert["weights"])) == w
        assert all(w[j] == 0 if j in target else w[j] >= 1 for j in range(n))
        assert all(v.denominator == 1 for v in w)


def grid_instance(drop_top=False):
    pts = list(product((-1, 0, 1), repeat=2))
    exps = list(product((0, 1, 2), repeat=2))
    base, blocks = [], []
    for e in exps:
        row = [s[0]**e[0]*s[1]**e[1] for s in pts]
        if sum(e) <= 1:
            base.append(row)
        elif not (drop_top and e == (2, 2)):
            blocks.append({"name": "monomial_"+str(e[0])+str(e[1]),
                           "rows": [row], "cost": 5 if e == (2, 2) else 1})
    return {"id": "coordinate-zero-union"+("-without-top" if drop_top else ""),
            "omega": pts, "target_indices": [j for j, s in enumerate(pts) if 0 in s],
            "base_rows": base, "blocks": blocks}


def main():
    repo = Path(__file__).resolve().parents[1]
    panel = json.loads((repo/"research/experiments/feature-repair-panel.json").read_text())
    report = json.loads((repo/"research/experiments/feature-repair-report.json").read_text())
    instances = panel["panels"] + [grid_instance(), grid_instance(True)]
    results = []
    for instance, entry in zip(instances, report["panels"]):
        assert instance["id"] == entry["id"]
        adaptive = entry["adaptive"]
        masks = sorted(range(1 << len(instance["blocks"])), key=lambda x: (cost(instance, x), x))
        cuts, checked = [], 0
        for history in adaptive.get("history", []):
            expected = next(mask for mask in masks if all(mask & cut for cut in cuts))
            assert history["mask"] == expected
            assert F(history["cost"]) == cost(instance, expected)
            check_certificate(instance, expected, history["trade"])
            z = list(map(F, history["trade"]["trade"]))
            detection = sum(1 << j for j, b in enumerate(instance["blocks"])
                            if any(dot(row, z) != 0 for row in b["rows"]))
            assert detection == history["mandatory_cut_mask"] and not expected & detection
            cuts.append(detection)
            checked += 1
        final_mask = adaptive.get("mask", adaptive.get("full_mask"))
        check_certificate(instance, final_mask, adaptive["certificate"])
        checked += 1
        if adaptive["status"] == "optimal":
            assert final_mask == next(mask for mask in masks if all(mask & cut for cut in cuts))
            assert F(adaptive["cost"]) == cost(instance, final_mask)
            assert adaptive["selected"] == [b["name"] for j, b in enumerate(instance["blocks"])
                                            if final_mask & (1 << j)]
        else:
            assert final_mask == (1 << len(instance["blocks"]))-1
        # Every mask, not just the reported optimum, gets an independent oracle.
        feasible_masks = []
        for mask in masks:
            own = independent_oracle(matrix(instance, mask), instance["target_indices"])
            if own["kind"] == "selector":
                feasible_masks.append(mask)
        optimum = feasible_masks[0] if feasible_masks else None
        assert (optimum is not None) == (adaptive["status"] == "optimal")
        if optimum is not None:
            assert optimum == adaptive["mask"] and cost(instance, optimum) == F(adaptive["cost"])
            assert optimum == entry["exhaustive"]["mask"]
            assert cost(instance, optimum) == F(entry["exhaustive"]["cost"])
        else:
            assert entry["exhaustive"]["status"] == "dictionary_impossible"
        results.append({"id": instance["id"], "all_masks_checked": len(masks),
                        "feasible_masks": len(feasible_masks), "reported_certificates_replayed": checked,
                        "adaptive_cuts_replayed": len(cuts), "independent_optimal_mask": optimum,
                        "independent_optimal_cost": None if optimum is None else cost(instance, optimum)})
    assert len(instances) == len(report["panels"]) == 5
    print(json.dumps(serial({"oracle": "target nullspace + tracked exact Fourier-Motzkin",
                             "panels": results, "total_masks_checked": sum(x["all_masks_checked"] for x in results),
                             "all_assertions_passed": True}), indent=2))


if __name__ == "__main__":
    main()

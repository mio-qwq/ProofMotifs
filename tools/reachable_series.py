#!/usr/bin/env python3
"""PM-SUCCINCT-B: exact independent synthesis / certificate verification controls.

Standard-library only. No repository imports, hidden oracle, numerical arithmetic,
or invocation of the synthesis algorithm from the verifier.
"""
from fractions import Fraction
from itertools import product
from copy import deepcopy
from math import isqrt
import json
import random


class Field:
    def __init__(self, p=None):
        if p is not None:
            if not isinstance(p, int) or p < 2 or any(p % t == 0 for t in range(2, isqrt(p) + 1)):
                raise ValueError("modulus must be prime")
        self.p = p

    def c(self, x):
        q = Fraction(x)
        if self.p is None:
            return q
        if q.denominator % self.p == 0:
            raise ValueError("undefined rational specialization")
        return q.numerator * pow(q.denominator, -1, self.p) % self.p

    def add(self, a, b):
        return (a + b) if self.p is None else (a + b) % self.p

    def mul(self, a, b):
        return (a * b) if self.p is None else (a * b) % self.p

    def neg(self, a):
        return -a if self.p is None else -a % self.p

    def inv(self, a):
        if a == 0:
            raise ZeroDivisionError
        return 1 / a if self.p is None else pow(a, -1, self.p)

    @property
    def label(self):
        return "Q" if self.p is None else "F" + str(self.p)


class Model:
    def __init__(self, lam, mats, gamma, p=None):
        self.k = Field(p)
        self.r = len(lam)
        if self.r < 1 or len(gamma) != self.r or any(not isinstance(a, str) or len(a) != 1 for a in mats):
            raise ValueError("invalid dimension/alphabet")
        if any(len(A) != self.r or any(len(row) != self.r for row in A) for A in mats.values()):
            raise ValueError("matrix dimension")
        self.lam = [self.k.c(x) for x in lam]
        self.mats = {a: [[self.k.c(x) for x in row] for row in A] for a, A in mats.items()}
        self.gamma = [self.k.c(x) for x in gamma]


def row_times(v, A, k):
    out = [k.c(0) for _ in v]
    for i, vi in enumerate(v):
        if vi:
            for j, aij in enumerate(A[i]):
                if aij:
                    out[j] = k.add(out[j], k.mul(vi, aij))
    return out


def dot(v, z, k):
    ans = k.c(0)
    for x, y in zip(v, z):
        ans = k.add(ans, k.mul(x, y))
    return ans


class IncrementalSpan:
    """Synthesis-only triangular span, with expressions in original rows."""
    def __init__(self, k, r):
        self.k, self.r = k, r
        self.original, self.echelon, self.expr, self.pivots = [], [], [], []

    def reduce(self, v):
        k = self.k
        rem = v[:]
        coords = [k.c(0) for _ in self.original]
        for e, ex, p in zip(self.echelon, self.expr, self.pivots):
            t = rem[p]
            if t:
                rem = [k.add(x, k.neg(k.mul(t, y))) for x, y in zip(rem, e)]
                coords = [k.add(x, k.mul(t, y)) for x, y in zip(coords, ex)]
        return rem, coords

    def offer(self, v):
        k = self.k
        rem, coords = self.reduce(v)
        if not any(rem):
            return False
        p = next(i for i, x in enumerate(rem) if x)
        t = k.inv(rem[p])
        for ex in self.expr:
            ex.append(k.c(0))
        self.original.append(v[:])
        self.echelon.append([k.mul(t, x) for x in rem])
        self.expr.append([k.neg(k.mul(t, x)) for x in coords] + [t])
        self.pivots.append(p)
        return True

    def coordinates(self, v):
        rem, coords = self.reduce(v)
        if any(rem):
            raise ValueError("not in span")
        return coords


def synthesize(M):
    k = M.k
    span = IncrementalSpan(k, M.r)
    words = []
    offers = 1
    if span.offer(M.lam):
        words.append("")
    head = 0
    while head < len(words):
        v, w = span.original[head], words[head]
        for a, A in M.mats.items():
            offers += 1
            if span.offer(row_times(v, A, k)):
                words.append(w + a)
        head += 1
    B = span.original
    outputs = [dot(b, M.gamma, k) for b in B]
    cert = {
        "version": "PM-SUCCINCT-B-1", "field": k.label,
        "rows": deepcopy(B), "words": words,
        "initial": span.coordinates(M.lam),
        "closure": {a: [span.coordinates(row_times(b, A, k)) for b in B] for a, A in M.mats.items()},
        "outputs": outputs,
        "decision": "nonzero" if any(outputs) else "zero",
    }
    if any(outputs):
        j = next(i for i, x in enumerate(outputs) if x)
        cert["witness"] = {"word": words[j], "coefficient": outputs[j]}
    return cert, {"row_offers": offers, "rank": len(B)}


def verify(M, cert):
    """Independent checker: direct identities + fresh full Gaussian rank.

    Does NOT use IncrementalSpan, synthesize, row_times, or dot. Independence
    here is implementation separation; same Python/field primitives remain trusted.
    """
    k, r = M.k, M.r

    def require(ok, why):
        if not ok:
            raise ValueError(why)

    def total(terms):
        ans = k.c(0)
        for x in terms:
            ans = k.add(ans, x)
        return ans

    def vector(v, size):
        require(isinstance(v, list) and len(v) == size, "vector shape")
        return [k.c(x) for x in v]

    def replay(w):
        require(isinstance(w, str) and all(a in M.mats for a in w), "witness alphabet")
        v = M.lam[:]
        for a in w:
            v = [total(k.mul(v[i], M.mats[a][i][j]) for i in range(r)) for j in range(r)]
        return v

    try:
        require(cert["version"] == "PM-SUCCINCT-B-1" and cert["field"] == k.label, "version/field")
        require(isinstance(cert["rows"], list), "rows type")
        m = len(cert["rows"])
        require(m <= r, "oversize basis")
        B = [vector(v, r) for v in cert["rows"]]
        require(isinstance(cert["words"], list) and len(cert["words"]) == m, "word count")
        for b, w in zip(B, cert["words"]):
            require(len(w) <= max(0, m - 1), "long basis word")
            require(replay(w) == b, "basis word provenance")
        # Full elimination, distinct from incremental synthesis.
        E = deepcopy(B)
        rank = 0
        for col in range(r):
            pivot = next((i for i in range(rank, m) if E[i][col]), None)
            if pivot is None:
                continue
            E[rank], E[pivot] = E[pivot], E[rank]
            z = k.inv(E[rank][col])
            E[rank] = [k.mul(z, x) for x in E[rank]]
            for i in range(m):
                if i != rank:
                    z = E[i][col]
                    E[i] = [k.add(E[i][j], k.neg(k.mul(z, E[rank][j]))) for j in range(r)]
            rank += 1
        require(rank == m, "dependent basis")
        alpha = vector(cert["initial"], m)
        require(all(total(k.mul(alpha[t], B[t][j]) for t in range(m)) == M.lam[j] for j in range(r)), "initial containment")
        require(isinstance(cert["closure"], dict) and set(cert["closure"]) == set(M.mats), "closure alphabet")
        for a, A in M.mats.items():
            require(isinstance(cert["closure"][a], list) and len(cert["closure"][a]) == m, "closure height")
            C = [vector(v, m) for v in cert["closure"][a]]
            for i in range(m):
                for j in range(r):
                    left = total(k.mul(B[i][t], A[t][j]) for t in range(r))
                    right = total(k.mul(C[i][t], B[t][j]) for t in range(m))
                    require(left == right, "closure identity")
        outputs = vector(cert["outputs"], m)
        require(outputs == [total(k.mul(B[i][j], M.gamma[j]) for j in range(r)) for i in range(m)], "output identity")
        require(cert["decision"] in ("zero", "nonzero"), "decision tag")
        if cert["decision"] == "zero":
            require(not any(outputs), "annihilation")
        else:
            require(any(outputs), "missing nonzero output")
            w = cert["witness"]["word"]
            require(isinstance(w, str) and len(w) <= r - 1, "witness length")
            value = total(k.mul(x, y) for x, y in zip(replay(w), M.gamma))
            require(value != 0 and value == k.c(cert["witness"]["coefficient"]), "witness coefficient")
        return True, "accepted"
    except (ValueError, TypeError, KeyError, IndexError, ZeroDivisionError) as e:
        return False, str(e)


def expand_all_words(M, depth):
    """Full explicit coefficient table; no reachable-space pruning or certificate."""
    k, r = M.k, M.r
    state_polys = [{"": M.lam[i]} for i in range(r)]
    out = {}
    for length in range(depth + 1):
        for w in map("".join, product(M.mats, repeat=length)):
            val = k.c(0)
            for i in range(r):
                val = k.add(val, k.mul(state_polys[i].get(w, k.c(0)), M.gamma[i]))
            out[w] = val
        if length == depth:
            break
        new = [{} for _ in range(r)]
        for i in range(r):
            for w, coefficient in state_polys[i].items():
                for a, A in M.mats.items():
                    for j in range(r):
                        wa = w + a
                        new[j][wa] = k.add(new[j].get(wa, k.c(0)), k.mul(coefficient, A[i][j]))
        state_polys = new
    return out


def explicit_paths(M, w):
    k = M.k
    contributions = []
    for states in product(range(M.r), repeat=len(w) + 1):
        z = M.lam[states[0]]
        for i, a in enumerate(w):
            z = k.mul(z, M.mats[a][states[i]][states[i + 1]])
        z = k.mul(z, M.gamma[states[-1]])
        if z:
            contributions.append((states, z))
    return contributions


def shift_family(D, p=None):
    r = D + 1
    S = [[0] * r for _ in range(r)]
    for i in range(D):
        S[i][i + 1] = 1
    return Model([1] + [0] * D, {"x": S, "y": S}, [0] * D + [1], p)


def main():
    report = {}
    tested, coefficients = 0, 0
    rng = random.Random(1162026)
    counts = {"zero": 0, "nonzero": 0}
    for p in (None, 2, 3, 5):
        for r in range(1, 5):
            for trial in range(24):
                vals = lambda: rng.randrange(-2, 3)
                lam, gamma = [vals() for _ in range(r)], [vals() for _ in range(r)]
                mats = {a: [[vals() for _ in range(r)] for _ in range(r)] for a in "xy"}
                if p is None and trial % 3 == 0:
                    lam = [Fraction(x, 3) for x in lam]
                    mats["x"] = [[Fraction(x, 2) for x in row] for row in mats["x"]]
                M = Model(lam, mats, gamma, p)
                c, _ = synthesize(M)
                assert verify(M, c)[0], verify(M, c)
                expanded = expand_all_words(M, r + 1)
                bounded_nonzero = any(v for w, v in expanded.items() if len(w) <= r - 1)
                assert bounded_nonzero == (c["decision"] == "nonzero")
                if c["decision"] == "zero":
                    assert not any(expanded.values())
                else:
                    assert expanded[c["witness"]["word"]] == c["witness"]["coefficient"]
                counts[c["decision"]] += 1
                tested += 1
                coefficients += len(expanded)
    report["small_expansion"] = {"models": tested, "word_coefficients": coefficients, "fields": ["Q", "F2", "F3", "F5"], "dimensions": [1, 2, 3, 4], "max_depth": "r+1", **counts}

    exhaustive_counts = {"zero": 0, "nonzero": 0}
    for bits in product((0, 1), repeat=12):
        M = Model(list(bits[:2]), {"x": [list(bits[4:6]), list(bits[6:8])], "y": [list(bits[8:10]), list(bits[10:12])]}, list(bits[2:4]), 2)
        c, _ = synthesize(M)
        assert verify(M, c)[0]
        table = expand_all_words(M, 3)
        assert any(v for w, v in table.items() if len(w) <= 1) == (c["decision"] == "nonzero")
        if c["decision"] == "zero":
            assert not any(table.values())
        else:
            assert table[c["witness"]["word"]] == c["witness"]["coefficient"]
        exhaustive_counts[c["decision"]] += 1
    report["all_binary_two_state_two_letter_inputs"] = {"models": 4096, "word_coefficients": 4096 * 15, "through_length": 3, **exhaustive_counts}

    # A genuine two-path cancellation for xy; all other words also vanish.
    cancel = Model([1, 0, 0, 0], {"x": [[0, 1, -1, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "y": [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 0]]}, [0, 0, 0, 1])
    cz, sz = synthesize(cancel)
    assert verify(cancel, cz)[0] and cz["decision"] == "zero"
    paths = explicit_paths(cancel, "xy")
    assert [v for _, v in paths] == [1, -1]
    expanded = expand_all_words(cancel, 6)
    assert not any(expanded.values())
    report["cancellation"] = {"rank": sz["rank"], "basis_words": cz["words"], "xy_nonzero_path_contributions": [str(v) for _, v in paths], "full_zero_coefficients_through_length_6": len(expanded)}

    # Rank drops under specialization; characteristic zero cannot be inferred.
    special = lambda p: Model([1, 0], {"x": [[0, 2], [0, 0]]}, [0, 1], p)
    specialization = {}
    for p in (None, 2, 3):
        M = special(p)
        c, s = synthesize(M)
        assert verify(M, c)[0]
        specialization[M.k.label] = {"rank": s["rank"], "decision": c["decision"], "witness": c.get("witness", {}).get("word")}
    assert specialization == {"Q": {"rank": 2, "decision": "nonzero", "witness": "x"}, "F2": {"rank": 1, "decision": "zero", "witness": None}, "F3": {"rank": 2, "decision": "nonzero", "witness": "x"}}
    report["specialization"] = specialization

    corruptions = {}
    def reject(name, M, c):
        ok, why = verify(M, c)
        assert not ok, name
        corruptions[name] = why

    c = deepcopy(cz); c["closure"]["x"][0][0] += 1; reject("wrong_closure_scalar", cancel, c)
    c = deepcopy(cz); del c["closure"]["y"]; reject("omitted_letter", cancel, c)
    c = deepcopy(cz); c["initial"] = [0] * len(c["rows"]); reject("false_initial_containment", cancel, c)
    c = deepcopy(cz); c["rows"][1][1] += 1; reject("forged_reachable_row", cancel, c)
    c = deepcopy(cz); c["closure"]["y"].pop(); reject("missing_closure_row", cancel, c)
    c = deepcopy(cz); c["outputs"][0] = 1; reject("forged_output", cancel, c)
    c = deepcopy(cz); c["field"] = "F2"; reject("field_mismatch", cancel, c)
    c, _ = synthesize(special(None)); c["field"] = "F2"; reject("rational_basis_reused_after_rank_drop", special(2), c)
    # Most important adversarial challenge: all listed rows annihilate gamma,
    # but the proposed subspace omits a reachable escape direction.
    escape = shift_family(2)
    fake = {"version": "PM-SUCCINCT-B-1", "field": "Q", "rows": [[Fraction(1), Fraction(0), Fraction(0)]], "words": [""], "initial": [1], "closure": {"x": [[0]], "y": [[0]]}, "outputs": [0], "decision": "zero"}
    reject("annihilating_rows_but_not_closed", escape, fake)
    good, _ = synthesize(escape)
    assert good["witness"]["word"] == "xx"
    c = deepcopy(good); c["witness"]["word"] = "x"; reject("false_nonzero_witness", escape, c)
    # Replay alone is not enough to claim a basis / exact reachable rank.
    c = deepcopy(cz)
    c["rows"] = [cancel.lam[:], cancel.lam[:]]
    c["words"] = ["", ""]
    reject("dependent_rows", cancel, c)
    report["malformed_certificates_rejected"] = corruptions

    # Formal coefficients are not captured by scalar-value oracles.
    commutator = Model([1, 0, 0, 0], {"x": [[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, -1], [0, 0, 0, 0]], "y": [[0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]]}, [0, 0, 0, 1], 3)
    cc, _ = synthesize(commutator)
    table = expand_all_words(commutator, 4)
    assert verify(commutator, cc)[0] and table["xy"] == 1 and table["yx"] == 2
    scalar_values = []
    for x, y in product(range(3), repeat=2):
        value = 0
        for w, coefficient in table.items():
            monomial = 1
            for a in w:
                monomial = monomial * {"x": x, "y": y}[a] % 3
            value = (value + coefficient * monomial) % 3
        scalar_values.append(value)
    assert scalar_values == [0] * 9
    report["scalar_black_box_boundary"] = {"polynomial": "xy-yx over F3", "nonzero_formal_coefficients": {w: v for w, v in table.items() if v}, "all_9_scalar_values": scalar_values, "decision": cc["decision"]}

    # 2^96 distinct degree-96 words, each coefficient 1; no expansion here.
    D = 96
    huge = shift_family(D, 2)
    ch, sh = synthesize(huge)
    assert verify(huge, ch)[0] and sh["rank"] == D + 1
    assert ch["witness"]["word"] == "x" * D and ch["witness"]["coefficient"] == 1
    assert len(ch["witness"]["word"]) == huge.r - 1
    # Small members validate the family formula by full expansion.
    family_controls = []
    for d in range(8):
        M = shift_family(d, 2)
        table = expand_all_words(M, d + 1)
        nz = {w: v for w, v in table.items() if v}
        assert len(nz) == 2 ** d and all(len(w) == d and v == 1 for w, v in nz.items())
        family_controls.append({"degree": d, "nonzero_words": len(nz), "all_words_checked": len(table)})
    report["implicit_exponential_word_family"] = {"degree": D, "states": huge.r, "alphabet": 2, "field": "F2", "nonzero_degree_D_words": str(2 ** D), "input_matrix_entries": 2 * huge.r ** 2, "basis_rows": sh["rank"], "row_offers": sh["row_offers"], "closure_scalars": 2 * sh["rank"] ** 2, "witness_length": D, "witness_coefficient": 1, "full_large_expansion_performed": False, "small_full_expansion_controls": family_controls}

    edge = []
    for M in [Model([0, 0], {"x": [[1, 2], [3, 4]]}, [1, 1]), Model([1], {}, [0]), Model([1], {}, [2]), Model([1], {"x": [[1]]}, [1], 2)]:
        c, s = synthesize(M)
        assert verify(M, c)[0]
        edge.append({"field": M.k.label, "rank": s["rank"], "decision": c["decision"], "witness": c.get("witness", {}).get("word")})
    denominator_rejected = False
    try:
        Model([Fraction(1, 2)], {}, [1], 2)
    except ValueError:
        denominator_rejected = True
    assert denominator_rejected
    report["edge_cases"] = {"cases": edge, "undefined_denominator_specialization_rejected": denominator_rejected}
    report["status"] = "ALL EXACT CHECKS PASSED"
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()

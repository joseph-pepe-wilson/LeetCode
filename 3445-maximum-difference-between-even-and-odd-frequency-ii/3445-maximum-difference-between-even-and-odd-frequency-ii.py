class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        res = float('-inf')
        for a in '01234':
            for b in '01234':
                if a == b: continue
                n, p, pa, pb = len(s), [0], [0], [0]
                for c in s:
                    p.append(p[-1] + (1 if c == a else -1 if c == b else 0))
                    pa.append(pa[-1] + (c == a))
                    pb.append(pb[-1] + (c == b))
                mn = [[float('inf')] * 2 for _ in range(2)]
                i = 0
                for j in range(n + 1):
                    while j - i >= k and pa[j] > pa[i] and pb[j] > pb[i]:
                        mn[pa[i]%2][pb[i]%2] = min(mn[pa[i]%2][pb[i]%2], p[i])
                        i += 1
                    res = max(res, p[j] - mn[1 - (pa[j]%2)][pb[j]%2])
        return res
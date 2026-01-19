from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], t: int) -> int:
        n, m = len(mat), len(mat[0])
        prf = [[0] * (m + 1) for _ in range(n + 1)]

        # Build prefix sum matrix
        for i in range(n):
            for j in range(m):
                prf[i][j] = (
                    mat[i][j]
                    + prf[i][j - 1]
                    + prf[i - 1][j]
                    - prf[i - 1][j - 1]
                )

        def sqr(lo: int, hi: int) -> int:
            if hi <= lo:
                return lo

            k = (hi + lo + 1) // 2 - 1
            for i in range(n - k):
                prf1, prfk = prf[i - 1], prf[i + k]
                for j in range(m - k):
                    if (
                        prfk[j + k]
                        - prfk[j - 1]
                        - prf1[j + k]
                        + prf1[j - 1]
                        <= t
                    ):
                        return sqr(k + 1, hi)

            return sqr(lo, k)

        return sqr(0, min(n, m))
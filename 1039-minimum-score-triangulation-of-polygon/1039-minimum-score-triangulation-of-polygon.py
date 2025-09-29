class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        # dp[i][j] will store the minimum score to triangulate polygon from vertex i to j
        dp = [[0] * n for _ in range(n)]

        # Fill dp table for all sub-polygons of length >= 3
        for length in range(3, n + 1):  # length of sub-polygon
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = float('inf')
                for k in range(i + 1, j):
                    score = values[i] * values[k] * values[j] + dp[i][k] + dp[k][j]
                    dp[i][j] = min(dp[i][j], score)

        return dp[0][n - 1]
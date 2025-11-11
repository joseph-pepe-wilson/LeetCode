class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize a 2D DP array with dimensions (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')

            # Traverse dp array in reverse to avoid overwriting needed values
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])

        return dp[m][n]
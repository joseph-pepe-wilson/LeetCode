class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        powers = []
        i = 1
        while (val := i**x) <= n:
            powers.append(val)
            i += 1

        # dp[i][j] = number of ways to sum up to j using first i powers
        dp = [0] * (n + 1)
        dp[0] = 1  # base case: one way to sum to 0 (empty set)

        for power in powers:
            for total in range(n, power - 1, -1):
                dp[total] = (dp[total] + dp[total - power]) % MOD

        return dp[n]

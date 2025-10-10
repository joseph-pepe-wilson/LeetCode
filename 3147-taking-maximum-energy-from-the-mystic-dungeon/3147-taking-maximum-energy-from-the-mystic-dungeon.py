class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        dp = energy[:]  # dp[i] will store the total energy starting from i with k jumps

        # Traverse backwards to accumulate energy from future reachable magicians
        for i in range(n - 1, -1, -1):
            next_i = i + k
            if next_i < n:
                dp[i] += dp[next_i]

        return max(dp)
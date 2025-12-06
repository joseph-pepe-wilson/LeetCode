class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        from collections import deque
        
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)

        dp[0] = 1
        prefix[0] = 1

        maxdq = deque()
        mindq = deque()

        left = 0

        for right in range(n):
            # Maintain max deque
            while maxdq and nums[maxdq[-1]] <= nums[right]:
                maxdq.pop()
            maxdq.append(right)

            # Maintain min deque
            while mindq and nums[mindq[-1]] >= nums[right]:
                mindq.pop()
            mindq.append(right)

            # Shrink window until valid
            while nums[maxdq[0]] - nums[mindq[0]] > k:
                left += 1
                if maxdq[0] < left:
                    maxdq.popleft()
                if mindq[0] < left:
                    mindq.popleft()

            # dp[right+1] = sum(dp[left .. right])
            dp[right + 1] = (prefix[right] - prefix[left - 1] if left > 0 else prefix[right]) % MOD

            prefix[right + 1] = (prefix[right] + dp[right + 1]) % MOD

        return dp[n] % MOD
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % MOD

        left, right = 0, n - 1
        result = 0
        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + powers[right - left]) % MOD
                left += 1
            else:
                right -= 1

        return result

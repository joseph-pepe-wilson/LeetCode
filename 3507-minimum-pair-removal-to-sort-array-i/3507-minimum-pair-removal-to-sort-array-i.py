class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        #Solution1 (Brute Force)
        ans = 0
        while sorted(nums) != nums:
            min_sum = float("inf")
            idx = 1
            for i in range(len(nums) - 1, 0, -1):
                sum = nums[i] + nums[i - 1]
                if sum <= min_sum:
                    idx = i
                    min_sum = sum
            nums[idx - 1] = nums[idx - 1] + nums[idx]
            nums.pop(idx)
            ans += 1
        return ans
        
                
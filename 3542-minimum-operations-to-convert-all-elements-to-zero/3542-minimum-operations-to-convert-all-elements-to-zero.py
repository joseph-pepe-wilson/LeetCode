class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def helper(left: int, right: int, base: int) -> int:
            if left > right:
                return 0
            # Find minimum in the current segment
            min_val = min(nums[left:right+1])
            # Cost of reducing all elements to min_val
            cost = min_val - base
            i = left
            while i <= right:
                if nums[i] == min_val:
                    i += 1
                else:
                    j = i
                    while j <= right and nums[j] != min_val:
                        j += 1
                    cost += helper(i, j - 1, min_val)
                    i = j
            return min(cost, right - left + 1)

        return helper(0, len(nums) - 1, 0)
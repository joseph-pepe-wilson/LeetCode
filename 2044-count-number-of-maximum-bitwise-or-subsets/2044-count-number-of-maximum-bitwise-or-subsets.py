class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num

        self.count = 0

        def dfs(index, current_or):
            if index == len(nums):
                if current_or == max_or:
                    self.count += 1
                return
            # Include nums[index]
            dfs(index + 1, current_or | nums[index])
            # Exclude nums[index]
            dfs(index + 1, current_or)

        dfs(0, 0)
        return self.count

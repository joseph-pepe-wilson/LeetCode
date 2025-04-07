from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = set()
        dp.add(0)
        
        for num in nums:
            new_dp = dp.copy()
            for t in dp:
                if t + num == target:
                    return True
                new_dp.add(t + num)
            dp = new_dp
        
        return target in dp

from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        if target == 0:
            return 0
        
        prefix = 0
        seen = {0: -1}  # prefix sum modulo p → index
        res = len(nums)
        
        for i, num in enumerate(nums):
            prefix = (prefix + num) % p
            # We want prefix[j] == (prefix - target) % p
            need = (prefix - target) % p
            if need in seen:
                res = min(res, i - seen[need])
            # update hashmap
            seen[prefix] = i
        
        return res if res < len(nums) else -1
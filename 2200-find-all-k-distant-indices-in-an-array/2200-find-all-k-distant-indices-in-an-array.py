from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices = [i for i, val in enumerate(nums) if val == key]
        result = set()
        
        for idx in key_indices:
            start = max(0, idx - k)
            end = min(len(nums) - 1, idx + k)
            for i in range(start, end + 1):
                result.add(i)
        
        return sorted(result)

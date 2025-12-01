from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        total = sum(batteries)
        low, high = 0, total // n
        
        while low < high:
            mid = (low + high + 1) // 2  # bias upward
            if sum(min(b, mid) for b in batteries) >= n * mid:
                low = mid
            else:
                high = mid - 1
        return low 
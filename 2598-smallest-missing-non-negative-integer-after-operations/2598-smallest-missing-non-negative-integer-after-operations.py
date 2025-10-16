from collections import Counter
from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        # Count how many numbers fall into each modulo class
        count_mod = Counter(num % value for num in nums)
        
        mex = 0
        while True:
            mod_class = mex % value
            if count_mod[mod_class] > 0:
                count_mod[mod_class] -= 1
                mex += 1
            else:
                return mex
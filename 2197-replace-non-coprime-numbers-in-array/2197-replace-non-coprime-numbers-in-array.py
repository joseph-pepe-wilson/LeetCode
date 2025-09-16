from math import gcd
from typing import List

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def lcm(a: int, b: int) -> int:
            return a * b // gcd(a, b)

        stack = []
        for num in nums:
            stack.append(num)
            # Keep merging while the top two elements are non-coprime
            while len(stack) >= 2 and gcd(stack[-1], stack[-2]) > 1:
                b = stack.pop()
                a = stack.pop()
                stack.append(lcm(a, b))
        return stack

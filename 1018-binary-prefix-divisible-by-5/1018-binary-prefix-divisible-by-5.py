class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        num = 0
        for bit in nums:
            num = (num << 1) | bit  # Shift left and add current bit
            result.append(num % 5 == 0)
        return result
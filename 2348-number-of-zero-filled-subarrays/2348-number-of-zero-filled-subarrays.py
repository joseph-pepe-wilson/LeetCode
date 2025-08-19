class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        length = 0
        
        for num in nums:
            if num == 0:
                length += 1
                count += length
            else:
                length = 0
        
        return count

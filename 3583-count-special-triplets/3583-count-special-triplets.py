class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        
        from collections import Counter
        
        right = Counter(nums)  # counts of all elements to the right of j
        left = Counter()       # counts of elements to the left of j
        
        ans = 0
        
        for j, val in enumerate(nums):
            right[val] -= 1  # j is no longer in the right side
            
            target = val * 2
            
            ans = (ans + left[target] * right[target]) % MOD
            
            left[val] += 1   # move j into the left side
        
        return ans
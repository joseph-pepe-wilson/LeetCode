class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        result = set()
        curr = set()
        
        for num in arr:
            # OR the current number with all previous results to extend subarrays
            curr = {num | x for x in curr} | {num}
            result |= curr
        
        return len(result)

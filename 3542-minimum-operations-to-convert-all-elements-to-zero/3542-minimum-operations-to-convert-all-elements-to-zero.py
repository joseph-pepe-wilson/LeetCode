class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Initialize stack to keep track of previous values in a "monotonic non-decreasing" way
        stack = [-1]
        # Counter for the required operations
        operations = 0
        
        for num in nums:
            # Remove previous numbers that are greater than current num from stack
            while num < stack[-1]:
                stack.pop()
            # Only increment operations for non-zero numbers strictly greater than previous top
            if num > stack[-1]:
                operations += 1 if num > 0 else 0
                stack.append(num)
        
        return operations

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        flip_count = 0
        operations = 0
        flip_state = [0] * n  # To manage flips within the sliding window

        for i in range(n):
            flip_count ^= flip_state[i]
            
            # If the current element is 0
            if (nums[i] ^ flip_count) == 0:
                if i + 2 >= n:  # If we can't flip 3 elements, return -1
                    return -1
                
                # Perform a flip starting from index `i`
                flip_count ^= 1
                operations += 1
                
                # Mark the end of the flip's effect
                if i + 3 < n:
                    flip_state[i + 3] ^= 1

        return operations

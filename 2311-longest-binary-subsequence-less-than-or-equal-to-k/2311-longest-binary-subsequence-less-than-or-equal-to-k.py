class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count = 0
        value = 0
        power = 1
        
        # Traverse from the end (least significant bit)
        for bit in reversed(s):
            if bit == '0':
                count += 1  # Always safe to include 0
            else:
                if value + power <= k:
                    value += power
                    count += 1
                else:
                    pass  # Skip this '1' since it exceeds k
            power <<= 1  # Increase power of 2
        
            # Early break if power exceeds k (no further bits can be safely added)
            if power > k:
                break
        
        # Count remaining leading zeros (can safely be added to front)
        zeros = s[:len(s) - count].count('0')
        return count + zeros

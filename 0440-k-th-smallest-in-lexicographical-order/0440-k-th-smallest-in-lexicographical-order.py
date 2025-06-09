class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current = 1
        k -= 1  # Because we count from 1

        while k > 0:
            # Count numbers in the current subtree
            step = 0
            first, last = current, current + 1
            while first <= n:
                step += min(n + 1, last) - first
                first *= 10
                last *= 10
            
            # If `k` is greater than the count of this subtree, move to the next lexicographical number
            if step <= k:
                k -= step
                current += 1
            else:
                # Move deeper in the tree
                k -= 1
                current *= 10
        
        return current

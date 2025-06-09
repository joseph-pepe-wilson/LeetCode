from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 1
        
        for _ in range(n):
            result.append(current)
            
            # Try to go deeper in the tree (multiply by 10)
            if current * 10 <= n:
                current *= 10
            else:
                # If we can't go deeper, move to the next number
                while current % 10 == 9 or current + 1 > n:
                    current //= 10
                current += 1
                
        return result

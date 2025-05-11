from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0  # Count consecutive odd numbers
        for num in arr:
            if num % 2 == 1:  # Check if the number is odd
                count += 1
                if count == 3:  # If we have found three consecutive odd numbers
                    return True
            else:
                count = 0  # Reset the count if an even number is encountered
        return False

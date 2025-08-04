from collections import defaultdict
from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_count = defaultdict(int)
        left = 0
        max_fruits = 0

        for right in range(len(fruits)):
            fruit_count[fruits[right]] += 1

            # If we have more than 2 types of fruits, shrink the window from the left
            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            # Update the maximum number of fruits collected
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        
        digit_sum_groups = defaultdict(int)
        
        # Count the frequency of numbers belonging to each digit sum group
        for num in range(1, n + 1):
            digit_sum = sum(int(digit) for digit in str(num))
            digit_sum_groups[digit_sum] += 1
        
        max_size = max(digit_sum_groups.values())  # Find the largest group size
        return sum(1 for size in digit_sum_groups.values() if size == max_size)  # Count the number of groups with max size

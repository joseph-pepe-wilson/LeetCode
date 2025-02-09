from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        good_pair_count = 0
        diff_count = defaultdict(int)

        for i in range(n):
            expected_value = nums[i] - i
            good_pair_count += diff_count[expected_value]
            diff_count[expected_value] += 1

        total_pairs = n * (n - 1) // 2
        bad_pair_count = total_pairs - good_pair_count
                
        return bad_pair_count
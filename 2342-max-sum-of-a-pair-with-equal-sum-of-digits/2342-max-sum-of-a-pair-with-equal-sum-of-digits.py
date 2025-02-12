class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum_dict = {}
        max_sum = -1

        for i in nums:
            digit_sum = sum(int(j) for j in str(i))
            if digit_sum in digit_sum_dict:
                max_sum = max(max_sum, digit_sum_dict[digit_sum] + i)
                digit_sum_dict[digit_sum] = max(digit_sum_dict[digit_sum], i)
            else:
                digit_sum_dict[digit_sum] = i

        return max_sum
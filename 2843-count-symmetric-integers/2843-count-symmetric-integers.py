class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(num: int) -> bool:
            num_str = str(num)
            length = len(num_str)
            if length % 2 != 0:
                return False  # Must have an even number of digits
            half = length // 2
            return sum(map(int, num_str[:half])) == sum(map(int, num_str[half:]))

        return sum(1 for num in range(low, high + 1) if is_symmetric(num))

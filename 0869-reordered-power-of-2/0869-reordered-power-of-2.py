class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        from collections import Counter

        def count_digits(x):
            return Counter(str(x))

        target = count_digits(n)

        for i in range(31):  # 2^0 to 2^30 are all <= 10^9
            if count_digits(1 << i) == target:
                return True
        return False

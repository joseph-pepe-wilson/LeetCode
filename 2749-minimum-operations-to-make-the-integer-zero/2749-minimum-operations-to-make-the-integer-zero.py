class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            target = num1 - k * num2
            if target < k:
                continue
            if bin(target).count('1') <= k:
                return k
        return -1

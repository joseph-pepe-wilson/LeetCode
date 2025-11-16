class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        result = 0

        for char in s:
            if char == '1':
                count += 1
                result = (result + count) % MOD
            else:
                count = 0

        return result
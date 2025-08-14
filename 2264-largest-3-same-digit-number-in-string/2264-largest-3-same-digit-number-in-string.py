class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num) - 2):
            substr = num[i:i+3]
            if substr[0] == substr[1] == substr[2]:
                if substr > max_good:
                    max_good = substr
        return max_good

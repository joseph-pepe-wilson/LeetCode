class Solution:
    def clearDigits(self, s: str) -> str:
        while any(char.isdigit() for char in s):
            for i , char in enumerate(s):
                if char.isdigit():

                    for j in range(i - 1, -1, -1):
                        if not s[j].isdigit():
                            s = s[:j] + s[j + 1:i] + s[i + 1:]
                            break
                    break
        return s
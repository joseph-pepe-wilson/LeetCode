class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            new_s = []
            for i in range(len(s) - 1):
                sum_mod = (int(s[i]) + int(s[i + 1])) % 10
                new_s.append(str(sum_mod))
            s = ''.join(new_s)
        return s[0] == s[1]
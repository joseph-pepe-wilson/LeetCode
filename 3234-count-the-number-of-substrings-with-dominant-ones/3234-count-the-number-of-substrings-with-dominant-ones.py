class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        zeros = [-1]
        res = 0
        for i, c in enumerate(s):
            if s[i] == "0":
                zeros.append(i)

            p = len(zeros) - 1
            cnt = 0
            j = i
            while 0 <= p and cnt * cnt <= i:
                k = zeros[p]
                p -= 1
                ones = i - k - cnt
                res += max(0, min(j - k, ones - cnt * cnt + 1))
                j = k
                cnt += 1

        return res
        
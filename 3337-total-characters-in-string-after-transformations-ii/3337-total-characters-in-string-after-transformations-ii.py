class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9 + 7
        vector = [[0] * 26 for _ in range(26)]
        for c in range(26):
            num = nums[c]
            for j in range(1, num + 1):
                next_c = (c + j) % 26
                vector[c][next_c] += 1

        def matrix_multi(x, y):
            res = [[0] * 26 for _ in range(26)]
            for i in range(26):
                for j in range(26):
                    if x[i][j] == 0:
                        continue
                    for l in range(26):
                        res[i][l] = (res[i][l] + x[i][j] * y[j][l]) % mod
            return res

        def matrix_pol(m, n):
            total = [[1 if i == j else 0 for j in range(26)] for i in range(26)]
            while n > 0:
                if n % 2 == 1:
                    total = matrix_multi(total, m)
                m = matrix_multi(m, m)
                n //= 2
            return total
        compute = matrix_pol(vector, t)

        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - ord('a')] += 1
            
        new_cnt =[0] * 26
        for i in range(26):
            for j in range(26):
                new_cnt[j] = (new_cnt[j] + cnt[i] * compute[i][j]) % mod
                         
        result = 0
        for x in new_cnt:
            result = (result + x) % mod
        return result
class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        def pali(num, base):
            s = ""
            while num > 0:
                s = str(num % base) + s
                num //= base
            return s == s[::-1]

        ct = 0
        ans = 0
        st = 1
        
        while ct < n:
            for op in range(2):  
                for i in range(st, st * 10):
                    if ct >= n:
                        break

                    x = i // 10 if op == 0 else i
                    cb = i
                    temp = x

                    while temp > 0:
                        cb = cb * 10 + (temp % 10)
                        temp //= 10

                    if pali(cb, k):
                        ct += 1
                        ans += cb

            st *= 10

        return ans

        

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        
        n, m = len(str1), len(str2)
        L = n + m - 1
        res = [None] * L
        free = [True] * L
        
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    c = str2[j]
                    if res[pos] is None:
                        res[pos] = c
                        free[pos] = False
                    elif res[pos] != c:
                        return ""
                        
        for i in range(L):
            if res[i] is None:
                res[i] = 'a'
                
        for i in range(n):
            if str1[i] == 'F':
                eq = True
                
                for j in range(m):
                    if res[i+j] != str2[j]:
                        eq = False
                        break
                        
                if eq:
                    cand = -1
                    for j in range(m):
                        pos = i + j
                        if free[pos]:
                            cand = pos
                    if cand == -1:
                        return ""
                    res[cand] = 'b'
                    free[cand] = False
                    
        return "".join(res)
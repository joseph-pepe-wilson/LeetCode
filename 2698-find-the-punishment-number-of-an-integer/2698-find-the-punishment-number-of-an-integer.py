class Solution:
    def punishmentNumber(self, n: int) -> int:
        f = lambda v,t:v and any(v==t or f(v//q,t-v%q) for q in (10,100,1000))
        return sum(i*i*f(i*i,i) for i in range(1,n+1))
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        
        ans = 1          # every single day counts
        streak = 1       # current descent streak length
        
        for i in range(1, n):
            if prices[i] == prices[i-1] - 1:
                streak += 1
            else:
                streak = 1
            ans += streak
        
        return ans
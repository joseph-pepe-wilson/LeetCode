class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        res = 0

        for i in range(n):
            for j in range(i + 1, n):
                xl1, yb1 = bottomLeft[i]
                xr1, yt1 = topRight[i]
                xl2, yb2 = bottomLeft[j]
                xr2, yt2 = topRight[j]
                
                if (xl2 < xr1 and xl1 < xr2) and (yb2 < yt1 and yb1 < yt2):
                    l = max(xl2, xl1)
                    r = min(xr1, xr2)
                    t = min(yt2, yt1)
                    d = max(yb2, yb1)
                    
                    res = max(res, min(r - l, t - d) ** 2)
            
        return res
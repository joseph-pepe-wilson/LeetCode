class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def area(a, b, c, d): 
            lx, rx, ty, dy = cols, 0, rows, 0
            for i in range(a, b + 1):
                for j in range(c, d + 1):
                    if grid[i][j]:
                        lx = min(lx, j)
                        rx = max(rx, j)
                        ty = min(ty, i)
                        dy = max(dy, i)
            return (rx - lx + 1) * (dy - ty + 1)

        ans = int(10**9)

        for i in range(rows):
            for j in range(cols):
                ans = min(ans,
                          area(0, i, 0, cols-1) + area(i+1, rows-1, 0, j) + area(i+1, rows-1, j+1, cols-1),
                          area(0, i, 0, j) + area(0, i, j+1, cols-1) + area(i+1, rows-1, 0, cols-1),
                          area(0, rows-1, 0, j) + area(0, i, j+1, cols-1) + area(i+1, rows-1, j+1, cols-1),
                          area(0, rows-1, j+1, cols-1) + area(0, i, 0, j) + area(i+1, rows-1, 0, j)
                          )

        for i in range(rows):
            for j in range(i, rows):
                ans = min(ans,
                          area(0, i, 0, cols-1) + area(i+1, j, 0, cols-1) + area(j+1, rows-1, 0, cols-1))

        for i in range(cols):
            for j in range(i, cols):
                ans = min(ans, 
                           area(0, rows-1, 0, i) + area(0, rows-1, i+1, j) + area(0, rows-1, j+1, cols-1))

        return ans
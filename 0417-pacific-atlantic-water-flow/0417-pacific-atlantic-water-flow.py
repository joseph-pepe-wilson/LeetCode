from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])
        pacific_reachable = [[False] * n for _ in range(m)]
        atlantic_reachable = [[False] * n for _ in range(m)]

        def dfs(r, c, reachable):
            reachable[r][c] = True
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < m and 0 <= nc < n and
                    not reachable[nr][nc] and
                    heights[nr][nc] >= heights[r][c]):
                    dfs(nr, nc, reachable)

        # Start DFS from Pacific Ocean borders
        for i in range(m):
            dfs(i, 0, pacific_reachable)       # Left edge
            dfs(i, n - 1, atlantic_reachable)  # Right edge
        for j in range(n):
            dfs(0, j, pacific_reachable)       # Top edge
            dfs(m - 1, j, atlantic_reachable)  # Bottom edge

        result = []
        for r in range(m):
            for c in range(n):
                if pacific_reachable[r][c] and atlantic_reachable[r][c]:
                    result.append([r, c])
        return result
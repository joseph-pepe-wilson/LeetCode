from heapq import heappush, heappop
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18

        # dist[r][c][t] = min cost to reach (r,c) using t teleports
        dist = [[[INF] * (k + 1) for _ in range(n)] for _ in range(m)]
        dist[0][0][0] = 0

        # Min-heap: (cost, r, c, usedTeleports)
        pq = [(0, 0, 0, 0)]

        # Sort all cells by value for teleport optimization
        cells = []
        for i in range(m):
            for j in range(n):
                cells.append((grid[i][j], i, j))
        cells.sort()

        # For each teleport count, track how many teleport targets processed
        teleport_ptr = [0] * (k + 1)

        while pq:
            cost, r, c, t = heappop(pq)

            if cost > dist[r][c][t]:
                continue

            # Reached destination
            if r == m - 1 and c == n - 1:
                return cost

            # -------- Normal moves --------
            if r + 1 < m:
                nc = cost + grid[r + 1][c]
                if nc < dist[r + 1][c][t]:
                    dist[r + 1][c][t] = nc
                    heappush(pq, (nc, r + 1, c, t))

            if c + 1 < n:
                nc = cost + grid[r][c + 1]
                if nc < dist[r][c + 1][t]:
                    dist[r][c + 1][t] = nc
                    heappush(pq, (nc, r, c + 1, t))

            # -------- Teleport --------
            if t < k:
                ptr = teleport_ptr[t]
                while ptr < len(cells) and cells[ptr][0] <= grid[r][c]:
                    _, x, y = cells[ptr]
                    if cost < dist[x][y][t + 1]:
                        dist[x][y][t + 1] = cost
                        heappush(pq, (cost, x, y, t + 1))
                    ptr += 1
                teleport_ptr[t] = ptr

        return -1
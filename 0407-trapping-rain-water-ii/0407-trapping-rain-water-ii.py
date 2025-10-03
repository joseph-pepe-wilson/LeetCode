import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []

        # Step 1: Push all boundary cells into the heap
        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

        # Step 2: Process cells from the heap
        trapped_water = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while heap:
            height, x, y = heapq.heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    neighbor_height = heightMap[nx][ny]
                    trapped_water += max(0, height - neighbor_height)
                    heapq.heappush(heap, (max(height, neighbor_height), nx, ny))

        return trapped_water
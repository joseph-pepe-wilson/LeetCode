from heapq import heappop, heappush
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        pq = [(0, 0, 0, 1)]  # (current_time, row, col, next_move_time)
        seen = {}

        while pq:
            time, r, c, next_move_time = heappop(pq)
            
            if (r, c) in seen and seen[(r, c)] <= time:
                continue
            seen[(r, c)] = time
            
            if r == n - 1 and c == m - 1:
                return time

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < m:
                    wait_time = max(moveTime[nr][nc] - time, 0)
                    new_time = time + wait_time + next_move_time
                    new_move_time = 1 if next_move_time == 2 else 2
                    heappush(pq, (new_time, nr, nc, new_move_time))
        
        return -1  # Should never reach here


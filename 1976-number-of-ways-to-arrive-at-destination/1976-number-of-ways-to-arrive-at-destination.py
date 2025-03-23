import heapq
from collections import defaultdict, deque

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Build the graph
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Use Dijkstra's algorithm
        min_heap = [(0, 0)]  # (time, intersection)
        shortest_time = [float('inf')] * n
        shortest_time[0] = 0
        ways = [0] * n
        ways[0] = 1
        
        while min_heap:
            current_time, u = heapq.heappop(min_heap)
            
            # If the current time is greater than the shortest time, skip
            if current_time > shortest_time[u]:
                continue
            
            for v, time in graph[u]:
                new_time = current_time + time
                if new_time < shortest_time[v]:
                    shortest_time[v] = new_time
                    ways[v] = ways[u]
                    heapq.heappush(min_heap, (new_time, v))
                elif new_time == shortest_time[v]:
                    ways[v] = (ways[v] + ways[u]) % MOD
        
        return ways[n - 1]
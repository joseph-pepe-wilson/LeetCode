from collections import deque, defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        in_degree = [0] * n

        # Construct the graph and compute in-degrees
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1

        # Topological sorting using Kahn's algorithm
        queue = deque([node for node in range(n) if in_degree[node] == 0])
        dp = [[0] * 26 for _ in range(n)]
        visited_count = 0
        max_color_value = 0

        while queue:
            node = queue.popleft()
            visited_count += 1
            color_index = ord(colors[node]) - ord('a')
            dp[node][color_index] += 1
            max_color_value = max(max_color_value, dp[node][color_index])

            for neighbor in graph[node]:
                for i in range(26):
                    dp[neighbor][i] = max(dp[neighbor][i], dp[node][i])
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return max_color_value if visited_count == n else -1  # Check if there's a cycle

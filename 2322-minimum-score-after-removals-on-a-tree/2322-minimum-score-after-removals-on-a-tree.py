class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        from collections import defaultdict

        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Stores the XOR sum of subtree rooted at each node
        subtree_xor = [0] * n
        # Store the in and out times for ancestor checking
        in_time = [0] * n
        out_time = [0] * n
        time = 0

        # DFS to calculate subtree XORs and in/out times
        def dfs(node, parent):
            nonlocal time
            in_time[node] = time
            time += 1
            xor_val = nums[node]
            for nei in graph[node]:
                if nei != parent:
                    xor_val ^= dfs(nei, node)
            subtree_xor[node] = xor_val
            out_time[node] = time
            time += 1
            return xor_val

        total_xor = dfs(0, -1)

        # Helper to check if u is ancestor of v
        def is_ancestor(u, v):
            return in_time[u] < in_time[v] and out_time[v] < out_time[u]

        min_score = float('inf')
        # Try all pairs of edges as (child1, child2)
        for i in range(1, n):
            for j in range(1, n):
                if i == j:
                    continue
                # Determine components based on ancestor relationship
                if is_ancestor(i, j):
                    a = subtree_xor[j]
                    b = subtree_xor[i] ^ subtree_xor[j]
                    c = total_xor ^ subtree_xor[i]
                elif is_ancestor(j, i):
                    a = subtree_xor[i]
                    b = subtree_xor[j] ^ subtree_xor[i]
                    c = total_xor ^ subtree_xor[j]
                else:
                    a = subtree_xor[i]
                    b = subtree_xor[j]
                    c = total_xor ^ subtree_xor[i] ^ subtree_xor[j]
                min_score = min(min_score, max(a, b, c) - min(a, b, c))
        
        return min_score
   
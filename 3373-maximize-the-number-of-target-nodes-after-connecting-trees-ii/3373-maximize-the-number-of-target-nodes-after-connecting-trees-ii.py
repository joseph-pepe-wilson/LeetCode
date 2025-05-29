class Solution:
    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
        from collections import deque
        n = len(edges1) + 1
        m = len(edges2) + 1

        #Adjacency lists
        adj1 = [[] for _ in range(n)]
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        adj2 = [[] for _ in range(m)]
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)

        #Depth parity (0 for even, 1 for odd) with BFS
        def compute_parity(adj: list[list[int]], size: int) -> list[int]:
            parity = [-1] * size
            dq = deque([0])
            parity[0] = 0
            while dq:
                u = dq.popleft()
                for w in adj[u]:
                    if parity[w] == -1:
                        parity[w] = parity[u] ^ 1
                        dq.append(w)
            return parity

        p1 = compute_parity(adj1, n)
        p2 = compute_parity(adj2, m)

        #Count how many nodes in each tree have even vs. odd depth
        cnt1_even = p1.count(0)
        cnt1_odd  = n - cnt1_even
        cnt2_even = p2.count(0)
        cnt2_odd  = m - cnt2_even

        #Pick v to maximize # of nodes
        best2 = max(cnt2_even, cnt2_odd)
        ans = []
        for i in range(n):
            same_parity_count = cnt1_even if p1[i] == 0 else cnt1_odd
            ans.append(same_parity_count + best2)

        return ans
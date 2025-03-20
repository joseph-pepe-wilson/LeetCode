from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weights = [131071] * n  # Max 17-bit integer

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y, w):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] >= self.rank[rootY]:
                self.parent[rootY] = rootX
                self.rank[rootX] += self.rank[rootY]
            else:
                self.parent[rootX] = rootY
                self.rank[rootY] += self.rank[rootX]
        # Update the weight of the connected component
        self.weights[rootX] = self.weights[rootY] = self.weights[rootX] & self.weights[rootY] & w

    def path_weight(self, node):
        return self.weights[self.find(node)]

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        uf = UnionFind(n)

        # Build uf with edges
        for u, v, w in edges:
            uf.union(u, v, w)

        result = []
        for s, t in query:
            if uf.find(s) == uf.find(t):
                result.append(uf.path_weight(s))
            else:
                result.append(-1)

        return result
class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent = list(range(c + 1))

        def find(x):
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px

        for u, v in connections:
            union(u, v)

        components = defaultdict(list)
        for i in range(1, c + 1):
            heapq.heappush(components[find(i)], i)

        online_check = [1] * (c + 1)
        res = []

        for t, x in queries:
            if t == 1:
                if online_check[x]:
                    res.append(x)
                else:
                    comp = components[find(x)]
                    while comp and not online_check[comp[0]]:
                        heapq.heappop(comp)
                    res.append(comp[0] if comp else -1)
            else:
                online_check[x] = 0
        return res
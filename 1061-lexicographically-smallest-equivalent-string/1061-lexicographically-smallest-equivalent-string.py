class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}

        def find(c):
            if parent[c] != c:
                parent[c] = find(parent[c])
            return parent[c]

        def union(c1, c2):
            p1, p2 = find(c1), find(c2)
            if p1 != p2:
                if p1 < p2:
                    parent[p2] = p1
                else:
                    parent[p1] = p2

        for c1, c2 in zip(s1, s2):
            union(c1, c2)

        return "".join(find(c) for c in baseStr)

from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        def add_op(s):
            s = list(s)
            for i in range(1, len(s), 2):
                s[i] = str((int(s[i]) + a) % 10)
            return ''.join(s)

        def rotate_op(s):
            return s[-b:] + s[:-b]

        visited = set()
        queue = deque([s])
        smallest = s

        while queue:
            curr = queue.popleft()
            if curr in visited:
                continue
            visited.add(curr)
            smallest = min(smallest, curr)

            added = add_op(curr)
            rotated = rotate_op(curr)

            if added not in visited:
                queue.append(added)
            if rotated not in visited:
                queue.append(rotated)

        return smallest
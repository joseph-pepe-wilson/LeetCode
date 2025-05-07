class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        m, n, dx, dy = len(moveTime), len(moveTime[0]), 1, 0

        heap = [(0, 0, 0)]

        unseen = set(product(range(m), range(n)))
        unseen.remove(((0, 0)))

        while heap:
            time, x, y = heappop(heap)
            if (x, y) == (m - 1, n - 1): return time

            for _ in range(4):

                dx, dy = dy, -dx
                X, Y = x + dx, y + dy

                if (X, Y) in unseen:
                    t = max(time, moveTime[X][Y]) + 1
                    heappush(heap, (t, X, Y))
                    unseen.remove((X, Y))
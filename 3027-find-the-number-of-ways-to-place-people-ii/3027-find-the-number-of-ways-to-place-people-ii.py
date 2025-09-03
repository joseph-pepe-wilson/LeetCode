class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        count = 0

        for i in range(n):
            ax, ay = points[i]  # Alice's position
            for j in range(n):
                if i == j:
                    continue
                bx, by = points[j]  # Bob's position

                # Alice must be upper-left, Bob must be lower-right
                if ax <= bx and ay >= by:
                    valid = True
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        x, y = points[k]
                        if ax <= x <= bx and by <= y <= ay:
                            valid = False
                            break
                    if valid:
                        count += 1

        return count

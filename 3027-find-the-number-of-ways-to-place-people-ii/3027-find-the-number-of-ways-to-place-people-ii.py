class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p : (p[0], -p[1]))
        count = 0
        for i, (xi, yi) in enumerate(points):
            b = float('-inf')
            for xj, yj in points[i + 1 : ]:
                if yi >= yj > b:
                    count += 1
                    b = yj
        return count
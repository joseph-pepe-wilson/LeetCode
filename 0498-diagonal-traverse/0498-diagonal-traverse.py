class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        diagonals = {}

        # Group elements by the sum of their indices (i + j)
        for i in range(m):
            for j in range(n):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])

        # Traverse diagonals in order
        for k in range(m + n - 1):
            if k % 2 == 0:
                # Reverse even-indexed diagonals
                result.extend(reversed(diagonals[k]))
            else:
                result.extend(diagonals[k])

        return result

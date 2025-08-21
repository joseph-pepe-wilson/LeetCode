class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        # Preprocess each row to store number of consecutive ones ending at each cell
        for i in range(m):
            for j in range(1, n):
                if mat[i][j]:
                    mat[i][j] += mat[i][j - 1]

        total = 0
        # For each cell, look upward to count valid submatrices
        for j in range(n):
            for i in range(m):
                min_width = mat[i][j]
                for k in range(i, -1, -1):
                    min_width = min(min_width, mat[k][j])
                    if min_width == 0:
                        break
                    total += min_width
        return total

class Solution:
    def sortMatrix(self, grid):
        n = len(grid)

        # Helper to get and set diagonal starting from (row, col)
        def get_diagonal(row, col):
            i, j = row, col
            diagonal = []
            while i < n and j < n:
                diagonal.append(grid[i][j])
                i += 1
                j += 1
            return diagonal

        def set_diagonal(row, col, diagonal):
            i, j = row, col
            idx = 0
            while i < n and j < n:
                grid[i][j] = diagonal[idx]
                i += 1
                j += 1
                idx += 1

        # Bottom-left triangle (including the main diagonal) - non-increasing
        for i in range(n):
            diagonal = get_diagonal(i, 0)
            diagonal.sort(reverse=True)
            set_diagonal(i, 0, diagonal)
        for j in range(1, n):
            diagonal = get_diagonal(0, j)
            diagonal.sort()
            set_diagonal(0, j, diagonal)

        return grid

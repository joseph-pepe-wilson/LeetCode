class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize sets with existing digits
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val != '.':
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(r=0, c=0):
            if r == 9: return True
            if c == 9: return backtrack(r + 1, 0)
            if board[r][c] != '.': return backtrack(r, c + 1)

            for num in '123456789':
                box_idx = (r // 3) * 3 + (c // 3)
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_idx]:
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_idx].add(num)

                    if backtrack(r, c + 1): return True

                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_idx].remove(num)

            return False

        backtrack()
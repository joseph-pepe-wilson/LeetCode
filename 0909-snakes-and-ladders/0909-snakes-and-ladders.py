class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coordinates(s: int) -> tuple[int, int]:
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if (quot % 2 == 0) else n - 1 - rem
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (square number, steps)

        while queue:
            square, steps = queue.popleft()
            for i in range(1, 7):
                next_square = square + i
                if next_square > n * n:
                    continue
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square == n * n:
                    return steps + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, steps + 1))

        return -1

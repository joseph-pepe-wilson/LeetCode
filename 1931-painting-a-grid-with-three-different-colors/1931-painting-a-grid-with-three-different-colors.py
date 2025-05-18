class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        def generate_valid_rows(m):
            """ Generate all valid row colorings for the given row size. """
            def dfs(row, last_color):
                if len(row) == m:
                    valid_rows.append(tuple(row))
                    return
                for color in range(3):  # 0: Red, 1: Green, 2: Blue
                    if color != last_color:
                        dfs(row + [color], color)
            
            valid_rows = []
            dfs([], -1)
            return valid_rows
        
        valid_rows = generate_valid_rows(m)
        row_map = {row: i for i, row in enumerate(valid_rows)}
        
        # Compute valid transitions where two rows can be adjacent
        transitions = {row: [] for row in valid_rows}
        for row1 in valid_rows:
            for row2 in valid_rows:
                if all(row1[i] != row2[i] for i in range(m)):  # No column color repetition
                    transitions[row1].append(row2)
        
        # Dynamic Programming: Count ways to fill n columns
        dp = [[0] * len(valid_rows) for _ in range(n)]
        
        for i in range(len(valid_rows)):
            dp[0][i] = 1  # Base case: First column can be any valid row
        
        for col in range(1, n):
            for i, row1 in enumerate(valid_rows):
                dp[col][i] = sum(dp[col - 1][row_map[row2]] for row2 in transitions[row1]) % MOD
        
        return sum(dp[-1]) % MOD

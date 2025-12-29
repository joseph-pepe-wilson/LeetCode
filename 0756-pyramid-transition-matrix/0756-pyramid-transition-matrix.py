class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        adj_list = defaultdict(list)
        for s in allowed:
            adj_list[s[:2]].append(s[2])

        pyramid = [[''] * (i + 1) for i in range(len(bottom))]
        pyramid[-1] = [c for c in bottom]
        
        def dfs(row_idx, col_idx):
            if row_idx <= 0:
                return True
            if row_idx <= col_idx:
                return dfs(row_idx - 1, 0)
            
            key = pyramid[row_idx][col_idx] + pyramid[row_idx][col_idx + 1]
            
            for possible_char in adj_list[key]:
                pyramid[row_idx - 1][col_idx] = possible_char
                if dfs(row_idx, col_idx + 1):
                    return True
            
            return False

        
        return dfs(len(pyramid) - 1, 0)
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        from itertools import combinations
        
        # Get all possible indices to split the word into numFriends parts
        def get_splits(word, numFriends):
            n = len(word)
            indices = list(combinations(range(1, n), numFriends - 1))
            max_str = ""

            for split_points in indices:
                parts = []
                start = 0
                for idx in split_points:
                    parts.append(word[start:idx])
                    start = idx
                parts.append(word[start:])  # Add last segment
                
                max_str = max(max_str, max(parts))  # Track largest lexicographical string
                
            return max_str
        
        return get_splits(word, numFriends)

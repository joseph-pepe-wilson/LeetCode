class Solution:
    def putMarbles(self, weights: list[int], k: int) -> int:
        n = len(weights)
        if k == 1:  # Only one bag, all marbles go in it
            return 0
        
        # Calculate pairwise sums of adjacent marbles
        pair_sums = [weights[i] + weights[i + 1] for i in range(n - 1)]
        
        # Sort the pair sums
        pair_sums.sort()
        
        # To maximize the score, pick the largest (k-1) pair sums & To minimize the score, pick the smallest (k-1) pair sums
        max_score = sum(pair_sums[-(k-1):])
        min_score = sum(pair_sums[:k-1])
        
        return max_score - min_score

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        half = k // 2
        
        # Base profit
        base = sum(strategy[i] * prices[i] for i in range(n))
        
        # Precompute deltas
        delta_first = [-strategy[i] * prices[i] for i in range(n)]
        delta_second = [(1 - strategy[i]) * prices[i] for i in range(n)]
        
        # Initial window gain
        gain = sum(delta_first[:half]) + sum(delta_second[half:k])
        best_gain = gain
        
        # Slide window
        for start in range(1, n - k + 1):
            # Remove outgoing elements
            gain -= delta_first[start - 1]
            gain -= delta_second[start - 1 + half]
            
            # Add incoming elements
            gain += delta_first[start + half - 1]
            gain += delta_second[start + k - 1]
            
            best_gain = max(best_gain, gain)
        
        return base + max(0, best_gain)
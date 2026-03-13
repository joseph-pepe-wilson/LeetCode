import math

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        if mountainHeight == 0: return 0
        
        # 1. Theoretical Seed: Using the global capacity S = sum(1/sqrt(w))
        # This is an "Academic Pivot"—modeling the global system.
        inv_sqrt_sum = sum(1.0 / math.sqrt(w) for w in workerTimes)
        theoretical_t = 0.5 * (mountainHeight / inv_sqrt_sum)**2
        
        # 2. Tightened Search Range
        # Instead of 0 to 1e18, we use a window based on the model.
        # We add a buffer to account for the discrete steps.
        low = int(theoretical_t * 0.5) 
        high = int(theoretical_t * 2.0) + max(workerTimes)
        
        # 3. Discrete Global Function
        def get_total_h(T):
            total = 0
            for w in workerTimes:
                # Solving the quadratic for each worker: w*x(x+1)/2 <= T
                total += int((math.sqrt(1 + 8 * T / w) - 1) / 2)
                if total >= mountainHeight: return True
            return total >= mountainHeight

        # 4. Final Convergence
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if get_total_h(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
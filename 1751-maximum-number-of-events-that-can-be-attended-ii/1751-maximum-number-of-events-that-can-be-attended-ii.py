from functools import lru_cache
from bisect import bisect_right

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        
        # Extract start times for binary search
        start_days = [e[0] for e in events]

        @lru_cache(None)
        def dp(i, remaining):
            if i == n or remaining == 0:
                return 0

            # Option 1: Skip this event
            not_take = dp(i + 1, remaining)

            # Option 2: Take this event
            # Find the next event that starts after current ends
            next_i = bisect_right(start_days, events[i][1])
            take = events[i][2] + dp(next_i, remaining - 1)

            return max(take, not_take)

        return dp(0, k)
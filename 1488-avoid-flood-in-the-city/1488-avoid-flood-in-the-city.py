from typing import List
from collections import defaultdict
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        lake_to_day = dict()  # Tracks the last day a lake was filled
        dry_days = SortedList()  # Sorted list of indices where we can dry a lake

        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.add(i)
                ans[i] = 1  # Placeholder, will be updated if needed
            else:
                if lake in lake_to_day:
                    # Find the earliest dry day after the last rain on this lake
                    prev_day = lake_to_day[lake]
                    idx = dry_days.bisect_right(prev_day)
                    if idx == len(dry_days):
                        return []  # No dry day available to prevent flood
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake  # Dry this lake on that day
                    dry_days.remove(dry_day)
                lake_to_day[lake] = i  # Update last rain day for this lake

        return ans
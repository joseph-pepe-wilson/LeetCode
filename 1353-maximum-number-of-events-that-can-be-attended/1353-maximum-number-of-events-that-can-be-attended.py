from heapq import heappush, heappop
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # Sort events by start day
        events.sort()
        total_days = max(end for _, end in events)
        event_index = 0
        attended = 0
        min_heap = []

        for day in range(1, total_days + 1):
            # Add all events starting today
            while event_index < len(events) and events[event_index][0] == day:
                heappush(min_heap, events[event_index][1])
                event_index += 1

            # Remove events that have already expired
            while min_heap and min_heap[0] < day:
                heappop(min_heap)

            # Attend the event that ends earliest
            if min_heap:
                heappop(min_heap)
                attended += 1

        return attended

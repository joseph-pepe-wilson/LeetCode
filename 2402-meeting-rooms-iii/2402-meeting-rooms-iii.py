import heapq
from collections import defaultdict

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()  # Sort meetings by start time

        available = list(range(n))  # All rooms initially available
        heapq.heapify(available)

        busy = []  # (end_time, room_number)
        room_meeting_count = [0] * n

        for start, end in meetings:
            duration = end - start

            # Free up rooms that have completed meetings before current start
            while busy and busy[0][0] <= start:
                freed_end, freed_room = heapq.heappop(busy)
                heapq.heappush(available, freed_room)

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
            else:
                # No room available, delay meeting until earliest room gets free
                freed_end, freed_room = heapq.heappop(busy)
                heapq.heappush(busy, (freed_end + duration, freed_room))
                room = freed_room

            room_meeting_count[room] += 1

        # Find the room with the most meetings; in case of tie, pick lowest room number
        max_meetings = max(room_meeting_count)
        for room_number, count in enumerate(room_meeting_count):
            if count == max_meetings:
                return room_number

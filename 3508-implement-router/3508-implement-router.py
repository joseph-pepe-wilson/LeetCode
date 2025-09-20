from collections import deque, defaultdict
from bisect import bisect_left, bisect_right
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.queue = deque()  # FIFO queue of packets
        self.packetSet = set()  # To detect duplicates
        self.destMap = defaultdict(list)  # destination -> sorted list of timestamps

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.packetSet:
            return False

        # If memory limit exceeded, remove oldest packet
        if len(self.queue) >= self.memoryLimit:
            old_source, old_dest, old_time = self.queue.popleft()
            self.packetSet.remove((old_source, old_dest, old_time))
            # Remove timestamp from destMap[old_dest]
            idx = bisect_left(self.destMap[old_dest], old_time)
            if idx < len(self.destMap[old_dest]) and self.destMap[old_dest][idx] == old_time:
                self.destMap[old_dest].pop(idx)

        # Add new packet
        self.queue.append((source, destination, timestamp))
        self.packetSet.add(key)
        self.destMap[destination].append(timestamp)  # timestamps are added in order
        return True

    def forwardPacket(self) -> List[int]:
        if not self.queue:
            return []
        source, destination, timestamp = self.queue.popleft()
        self.packetSet.remove((source, destination, timestamp))
        # Remove timestamp from destMap[destination]
        idx = bisect_left(self.destMap[destination], timestamp)
        if idx < len(self.destMap[destination]) and self.destMap[destination][idx] == timestamp:
            self.destMap[destination].pop(idx)
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.destMap[destination]
        left = bisect_left(timestamps, startTime)
        right = bisect_right(timestamps, endTime)
        return right - left

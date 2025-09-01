from typing import List
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            return (p + 1) / (t + 1) - p / t
        
        max_heap = []
        for p, t in classes:
            heapq.heappush(max_heap, (-gain(p, t), p, t))
        
        for _ in range(extraStudents):
            g, p, t = heapq.heappop(max_heap)
            p += 1
            t += 1
            heapq.heappush(max_heap, (-gain(p, t), p, t))
        
        total_ratio = 0
        n = len(classes)
        while max_heap:
            g, p, t = heapq.heappop(max_heap)
            total_ratio += p / t
        
        return total_ratio / n

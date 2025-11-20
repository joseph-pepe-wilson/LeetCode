from typing import List

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        # Sort intervals by end ascending, and start descending for tie-breaking
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        res = []
        
        for start, end in intervals:
            # Count how many elements in res are within [start, end]
            count = 0
            for x in res:
                if start <= x <= end:
                    count += 1
            
            # If fewer than 2 elements are in the interval, add the largest possible ones
            for i in range(2 - count):
                res.append(end - i)
        
        return len(res)
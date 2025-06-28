from typing import List
import heapq

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Attach original indices to values
        indexed = list(enumerate(nums))
        # Get the k elements with largest values (with indices) using a heap
        largest = heapq.nlargest(k, indexed, key=lambda x: x[1])
        # Sort by original index to maintain relative order
        largest.sort(key=lambda x: x[0])
        # Extract the values
        return [x[1] for x in largest]

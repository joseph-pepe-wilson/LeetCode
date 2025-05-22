import heapq
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort(key = lambda x: x[1], reverse = True)
        q = []
        for i in range(len(nums) - 1):
            nums[i] -= nums[i + 1]
        n = len(nums) - 1
        while n >- 1 and not nums[n]:
              n -= 1
        qi = 0
        while qi < len(queries) and queries[qi][1] >= n:
            heapq.heappush(q, queries[qi][0])
            qi += 1
        c = 0
        while q:
            m = heapq.heappop(q)
            if m > n:
                continue
            nums[n] -= 1
            if m:
                nums[m-1] += 1
            c += 1
            while n >= 0 and nums[n] <= 0:        
                nums[n-1] += nums[n]
                n -= 1
            if n == -1:
                break
            while qi < len(queries) and queries[qi][1] >= n:
                heapq.heappush(q, queries[qi][0])
                qi += 1
        return len(queries) - c if n == -1 else -1
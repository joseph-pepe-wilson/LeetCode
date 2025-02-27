class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index = {x: i for i, x  in enumerate(arr)}
        longest = {}
        ans = 0

        for k in range(len(arr)):
            for j in range(k):
                i = index.get(arr[k] - arr[j])
                if i is not None and i < j:
                    curr = longest.get((i, j), 2) + 1
                    longest[j, k] = curr
                    ans = max(ans, curr)

        return ans if ans >= 3 else 0
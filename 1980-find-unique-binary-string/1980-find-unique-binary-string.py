class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        seen = set(nums)

        def dfs(s):
            if len(s) == n:
                return s if s not in seen else None
            res = dfs(s + '0')
            if res:
                return res
            return dfs(s + '1')

        return dfs('')
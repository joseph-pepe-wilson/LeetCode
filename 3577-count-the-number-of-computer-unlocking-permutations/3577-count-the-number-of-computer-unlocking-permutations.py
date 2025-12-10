class Solution:
    def countPermutations(self, complexity):
        mod = 1000000007
        n = len(complexity)

        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0

        ans = 1
        for i in range(1, n):
            ans = (ans * i) % mod

        return ans
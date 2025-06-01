class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(num: int) -> int:
            res = num * (num - 1) // 2 if num >= 0 else 0
            return res
        
        return max((comb(n + 2) - 3 * comb(n - limit + 1) + 3 * comb(n - 2 * limit) - comb(n - 3 * limit - 1)), 0)
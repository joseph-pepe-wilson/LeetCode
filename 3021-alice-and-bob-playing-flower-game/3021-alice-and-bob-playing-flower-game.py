class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        odds_n, evens_n = (n + 1) // 2, n // 2
        odds_m, evens_m = (m + 1) // 2, m // 2
        return odds_n * evens_m + evens_n * odds_m

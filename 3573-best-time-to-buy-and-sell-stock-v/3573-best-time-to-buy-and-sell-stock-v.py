class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        def makeTransaction(dp: List[int])-> List[int]:
            update = [0] * n
            nrml, shrt = -prices[0], prices[0]

            for idx, price in (enumerate(prices[1:])):
                update[idx + 1] = max(update[idx], nrml + price, shrt - price)
                nrml, shrt = max(nrml, dp[idx] - price), max(shrt, dp[idx] + price)
            return update


        n = len(prices)
        dp = [0] * n

        for _ in range(k):
            dp = makeTransaction(dp)
        return dp[-1]        
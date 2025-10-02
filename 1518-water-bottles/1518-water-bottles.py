class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty = numBottles

        while empty >= numExchange:
            # Exchange numExchange empty bottles for 1 full bottle
            new_bottles = empty // numExchange
            total_drunk += new_bottles
            # Update empty bottles: used for exchange + newly drunk
            empty = empty % numExchange + new_bottles

        return total_drunk
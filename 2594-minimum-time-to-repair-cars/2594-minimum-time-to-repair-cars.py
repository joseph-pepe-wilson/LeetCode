class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def canRepairInTime(time):
            total_cars = 0
            for rank in ranks:
                total_cars += int((time // rank) ** 0.5)
            return total_cars >= cars

        left, right = 1, max(ranks) * cars * cars
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid
            else:
                left = mid + 1

        return left

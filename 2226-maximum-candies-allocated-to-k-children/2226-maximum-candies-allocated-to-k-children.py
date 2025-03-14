class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canDistribute(mid):
            # Check if we can distribute k piles of size `mid` candies
            count = 0
            for candy in candies:
                count += candy // mid
                if count >= k:
                    return True
            return False

        left, right = 1, max(candies)  # Set the binary search range
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if canDistribute(mid):
                result = mid  # Update result, try for a larger `mid`
                left = mid + 1
            else:
                right = mid - 1

        return result

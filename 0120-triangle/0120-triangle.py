class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second-last row and move upward
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update each element to be the sum of itself and the min of the two adjacent numbers below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        # The top element now contains the minimum path sum
        return triangle[0][0]
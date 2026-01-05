class Solution:
    def maxMatrixSum(self, matrix):
        count = 0
        min = 100000000
        sum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] < 0:
                    count += 1
                sum += abs(matrix[i][j])
                min = min if min < abs(matrix[i][j]) else abs(matrix[i][j])
        if count % 2 == 0:
            return sum
        return sum - (2 * min)
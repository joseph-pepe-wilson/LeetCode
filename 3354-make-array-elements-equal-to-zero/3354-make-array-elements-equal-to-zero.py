class Solution:
    def countValidSelections(self, nums):
        def simulate(start, dir):
            n = len(nums)
            arr = nums[:]  # make a copy
            curr = start
            direction = dir  # +1 (right) or -1 (left)
            steps = 0  # ensure termination
            while 0 <= curr < n and steps < n * 200:
                if arr[curr] == 0:
                    curr += direction
                elif arr[curr] > 0:
                    arr[curr] -= 1
                    direction *= -1  # reverse direction
                    curr += direction
                steps += 1
            return all(x == 0 for x in arr)

        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if simulate(i, -1):  # try left
                    count += 1
                if simulate(i, 1):   # try right
                    count += 1
        return count

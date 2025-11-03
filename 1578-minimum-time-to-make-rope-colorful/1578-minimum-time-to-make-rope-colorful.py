class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_time = 0
        prev_time = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i] == colors[i - 1]:
                # Remove the balloon with the smaller time
                total_time += min(prev_time, neededTime[i])
                # Keep the balloon with the larger time for future comparison
                prev_time = max(prev_time, neededTime[i])
            else:
                prev_time = neededTime[i]

        return total_time
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        last = [-1] * 32  # Track last seen index for each bit

        for i in reversed(range(n)):
            for bit in range(32):
                if (nums[i] >> bit) & 1:
                    last[bit] = i
            # Find the farthest index we need to go to get max OR
            farthest = i
            for bit in range(32):
                if last[bit] != -1:
                    farthest = max(farthest, last[bit])
            answer[i] = farthest - i + 1

        return answer

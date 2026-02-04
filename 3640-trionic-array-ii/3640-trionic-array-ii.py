class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)

        # 1. Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        # 2. Segments
        seg = []
        i = 0
        while i < n - 1:
            j = i
            if nums[j + 1] > nums[j]:
                while j + 1 < n and nums[j + 1] > nums[j]:
                    j += 1
                seg.append((i, j, 1))
            elif nums[j + 1] < nums[j]:
                while j + 1 < n and nums[j + 1] < nums[j]:
                    j += 1
                seg.append((i, j, -1))
            else:
                seg.append((i, i + 1, 0))
                i += 1
                continue
            i = j
        
        res = float('-inf')

        # 3. Interpret segments
        for i in range(len(seg) - 2):
            l1, r1, grad1 = seg[i]
            l2, r2, grad2 = seg[i + 1]
            l3, r3, grad3 = seg[i + 2]

            if not (grad1 == grad3 == 1 and grad2 == -1):
                continue
            
            total = prefix[r2 + 1] - prefix[l2]
            # Maximise sum of 1st and 3rd segment
            total += max(prefix[r1] - prefix[k] for k in range(l1, r1))
            total += max(prefix[k + 1] - prefix[l3 + 1] for k in range(l3 + 1, r3 + 1))
            res = max(res, total)
            
        
        return res


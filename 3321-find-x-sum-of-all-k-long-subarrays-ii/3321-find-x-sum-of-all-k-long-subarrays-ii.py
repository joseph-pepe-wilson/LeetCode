from collections import Counter
from sortedcontainers import SortedList

class Solution:
    def findXSum(self, nums, k, x):
        freq = Counter()
        top = SortedList()
        rest = SortedList()
        top_sum = 0
        ans = []

        # Helper sets for fast lookup
        top_set = set()
        rest_set = set()

        def balance():
            nonlocal top_sum
            # Fill top from rest
            while len(top) < x and rest:
                f, v = rest.pop()
                rest_set.remove((f, v))
                top.add((f, v))
                top_set.add((f, v))
                top_sum += f * v
            # Trim top to x
            while len(top) > x:
                f, v = top.pop(0)
                top_set.remove((f, v))
                top_sum -= f * v
                rest.add((f, v))
                rest_set.add((f, v))
            # Swap if needed
            while rest and top and rest[-1] > top[0]:
                f1, v1 = rest.pop()
                rest_set.remove((f1, v1))
                f2, v2 = top.pop(0)
                top_set.remove((f2, v2))
                top_sum += f1 * v1 - f2 * v2
                top.add((f1, v1))
                top_set.add((f1, v1))
                rest.add((f2, v2))
                rest_set.add((f2, v2))

        def add(num):
            nonlocal top_sum
            old = (freq[num], num)
            if old in top_set:
                top.remove(old)
                top_set.remove(old)
                top_sum -= old[0] * old[1]
            elif old in rest_set:
                rest.remove(old)
                rest_set.remove(old)
            freq[num] += 1
            new = (freq[num], num)
            rest.add(new)
            rest_set.add(new)
            balance()

        def remove(num):
            nonlocal top_sum
            old = (freq[num], num)
            if old in top_set:
                top.remove(old)
                top_set.remove(old)
                top_sum -= old[0] * old[1]
            elif old in rest_set:
                rest.remove(old)
                rest_set.remove(old)
            freq[num] -= 1
            if freq[num] > 0:
                new = (freq[num], num)
                rest.add(new)
                rest_set.add(new)
            else:
                del freq[num]
            balance()

        for i in range(k):
            add(nums[i])
        ans.append(top_sum)

        for i in range(k, len(nums)):
            remove(nums[i - k])
            add(nums[i])
            ans.append(top_sum)

        return ans
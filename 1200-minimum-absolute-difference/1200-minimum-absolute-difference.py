class Solution:
    def minimumAbsDifference(self, A):
        A.sort()
        D = [A[i + 1] - A[i] for i in range(len(A) - 1)]
        target = min(D)
        return [[A[i], A[i + 1]] for i, d in enumerate(D) if d == target]
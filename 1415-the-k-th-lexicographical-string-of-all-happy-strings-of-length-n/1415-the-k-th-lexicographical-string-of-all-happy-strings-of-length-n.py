class Solution:
    def __init__(self):
        self.ans = ""

    def solve(self, length, k, n, chars, s):
        if length == n:
            k[0] -= 1
            if k[0] == 0:
                self.ans = s
            return
        for i in chars:
            if length == 0 or s[-1] != i:
                self.solve(length + 1, k, n, chars, s + i)
                if k[0] == 0:
                    return  # Stop recursion early

    def getHappyString(self, n: int, k: int) -> str:
        self.ans = ""
        self.solve(0, [k], n, ['a', 'b', 'c'], "")
        return self.ans
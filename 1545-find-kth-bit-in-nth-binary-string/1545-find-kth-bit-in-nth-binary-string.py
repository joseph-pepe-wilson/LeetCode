class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        # start = ["0"]
        # for i in range(1,n):
        #     s = start[-1]
        #     e = ""
        #     for j in s:
        #         e += str(int(not int(j)))
        #     target = s + "1" + e[::-1]
        #     start.append(target)
        # print(start)
        # return start[-1][k-1]
        if n == 1:
            return '0'
        l = 2 ** n - 1
        mid = l // 2 + 1
        if k == mid:
            return '1'
        if k < mid:
            return self.findKthBit(n - 1, k)
        return '1' if self.findKthBit(n - 1, l - k + 1) == '0' else '0'
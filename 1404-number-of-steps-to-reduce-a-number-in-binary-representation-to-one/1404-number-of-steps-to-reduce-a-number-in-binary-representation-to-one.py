class Solution:
    def numSteps(self, s: str) -> int:
        integer = int(s, 2)
        count = 0
        if  s == "1":
            return 0
        while integer > 1:
            if integer % 2 != 0:
                integer = integer + 1
                count = count + 1 
            integer = integer // 2
            count = count + 1 
        return count
            
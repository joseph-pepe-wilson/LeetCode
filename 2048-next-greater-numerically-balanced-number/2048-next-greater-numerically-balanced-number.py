class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x: int) -> bool:
            s = str(x)
            from collections import Counter
            c = Counter(s)
            for digit, count in c.items():
                if int(digit) != count:
                    return False
            return True
        
        current = n + 1
        while True:
            if is_balanced(current):
                return current
            current += 1

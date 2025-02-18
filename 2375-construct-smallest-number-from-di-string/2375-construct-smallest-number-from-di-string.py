class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        num = []
        stack = []

        # Traverse the pattern and construct the number
        for i in range(n + 1):
            stack.append(i + 1)
            if i == n or pattern[i] == 'I':
                while stack:
                    num.append(stack.pop())

        # Convert list of digits to string and return
        return ''.join(map(str, num))
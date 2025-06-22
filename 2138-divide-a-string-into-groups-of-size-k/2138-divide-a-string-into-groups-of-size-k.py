from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        # If the length of s is not divisible by k, pad with fill
        remainder = len(s) % k
        if remainder != 0:
            s += fill * (k - remainder)
        
        # Split the string into chunks of size k
        return [s[i:i+k] for i in range(0, len(s), k)]

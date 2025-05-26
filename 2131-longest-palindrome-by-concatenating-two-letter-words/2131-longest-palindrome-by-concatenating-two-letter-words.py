from collections import Counter
from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        length = 0
        central = False

        for word, freq in count.items():
            reversed_word = word[::-1]

            if word == reversed_word:  # Case of symmetric pairs like "gg", "cc"
                if freq % 2 == 0:
                    length += freq * 2
                else:
                    length += (freq - 1) * 2
                    central = True
            elif reversed_word in count:  # Case of matching pairs like "lc" and "cl"
                length += min(freq, count[reversed_word]) * 4
                count[word] = 0  # To avoid duplicate counting
                count[reversed_word] = 0

        if central:
            length += 2  # Adding a central element if available

        return length

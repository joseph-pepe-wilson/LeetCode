class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')
        parity_seen = set()
        vowel_count = 0

        for ch in s:
            if ch in vowels:
                vowel_count += 1
            parity_seen.add(vowel_count % 2)

        return 1 in parity_seen  # Alice wins if odd parity is seen

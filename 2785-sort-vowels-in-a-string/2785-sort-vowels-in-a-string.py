class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        s_list = list(s)

        # Collect vowels and their positions
        vowel_positions = []
        vowel_chars = []

        for i, ch in enumerate(s_list):
            if ch in vowels:
                vowel_positions.append(i)
                vowel_chars.append(ch)

        # Sort vowels by ASCII value
        vowel_chars.sort()

        # Place sorted vowels back into their original positions
        for pos, ch in zip(vowel_positions, vowel_chars):
            s_list[pos] = ch

        return ''.join(s_list)

from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(word: str) -> str:
            vowels = set('aeiou')
            return ''.join('*' if c in vowels else c for c in word.lower())

        exact_words = set(wordlist)
        cap_map = {}
        vowel_map = {}

        for word in wordlist:
            lower = word.lower()
            devow = devowel(word)
            if lower not in cap_map:
                cap_map[lower] = word
            if devow not in vowel_map:
                vowel_map[devow] = word

        result = []
        for query in queries:
            if query in exact_words:
                result.append(query)
            elif query.lower() in cap_map:
                result.append(cap_map[query.lower()])
            elif devowel(query) in vowel_map:
                result.append(vowel_map[devowel(query)])
            else:
                result.append("")
        return result

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        for word in words[1:]:
            if sorted(word) != sorted(res[-1]):
                res.append(word)
        return res

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merge_str = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            merge_str.append(word1[i])
            merge_str.append(word2[j])
            i += 1
            j += 1

        #for remaining characters
        while i < len(word1):
            merge_str.append(word1[i])
            i += 1
        while j < len(word2):
            merge_str.append(word2[j])
            j += 1
        
        return ''.join(merge_str)
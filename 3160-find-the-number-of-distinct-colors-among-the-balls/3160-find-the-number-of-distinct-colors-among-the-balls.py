class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
 
        clerd = {} # saves ball -> color
        freq = {} # freq of each color
        result = []
        for x , y in queries:
            if x in clerd:
                old_color = clerd[x]
                freq[old_color] -= 1
                if freq[old_color] == 0:
                    del freq[old_color]

            clerd[x] = y
            freq[y] = freq.get(y , 0) + 1
            result.append(len(freq))

        return result
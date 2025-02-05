class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        dif = [(a, b) for a, b in zip(s1, s2) if a != b] # Find all positions where the characters are different

        if len(dif) == 2 and dif[0] == dif[1][::-1]:
            return True
        else:
            return False # Check if we have exactly two differences and they are swappable
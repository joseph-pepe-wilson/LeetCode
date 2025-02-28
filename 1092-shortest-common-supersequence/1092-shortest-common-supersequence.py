class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Function to compute the Longest Common Subsequence (LCS)
        def lcs(x, y):
            m, n = len(x), len(y)
            dp = [[""] * (n + 1) for _ in range(m + 1)]
            for i in range(1, m + 1):
                for j in range(1, n +1):
                    if x[i - 1] == y[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + x[i - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key = len)
            return dp[m][n]

        # Find the LCS of str1 and str2
        common = lcs(str1, str2)
        
        # Construct the shortest common supersequence
        i = j = 0
        result = []
        for c in common:
            while i < len(str1) and str1[i] != c:
                result.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != c:
                result.append(str2[j])
                j += 1
            result.append(c)
            i += 1
            j += 1
        # Add remaining characters
        result.extend(str1[i:])
        result.extend(str2[j:])
        
        return "".join(result)
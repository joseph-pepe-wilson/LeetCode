class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Step 1: Extract powers of 2 from binary representation of n
        powers = []
        for i in range(31):  # since 2^30 > 10^9
            if (n >> i) & 1:
                powers.append(1 << i)
        
        # Step 2: Precompute prefix products modulo MOD
        prefix = [1] * (len(powers) + 1)
        for i in range(len(powers)):
            prefix[i + 1] = (prefix[i] * powers[i]) % MOD
        
        # Step 3: Answer each query using prefix products
        answers = []
        for left, right in queries:
            product = (prefix[right + 1] * pow(prefix[left], MOD - 2, MOD)) % MOD
            answers.append(product)
        
        return answers

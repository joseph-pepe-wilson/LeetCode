class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        # Precompute squares for speed
        squares = {i*i: i for i in range(1, n+1)}
        
        for a in range(1, n+1):
            for b in range(1, n+1):
                s = a*a + b*b
                if s in squares and squares[s] <= n:
                    count += 1
        return count
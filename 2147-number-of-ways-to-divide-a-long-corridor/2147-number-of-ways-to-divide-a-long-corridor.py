class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        
        # Collect indices of all seats
        seats = [i for i, c in enumerate(corridor) if c == 'S']
        
        # If no seats or odd number of seats → impossible
        if len(seats) == 0 or len(seats) % 2 == 1:
            return 0
        
        ways = 1
        
        # For every boundary between consecutive seat-pairs
        for i in range(2, len(seats), 2):
            # seats[i-1] is the end of previous pair
            # seats[i] is the start of next pair
            gap = seats[i] - seats[i-1]
            ways = (ways * gap) % MOD
        
        return ways
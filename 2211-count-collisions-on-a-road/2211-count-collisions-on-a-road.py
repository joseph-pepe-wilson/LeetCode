class Solution:
    def countCollisions(self, directions: str) -> int:
        # Remove cars that never collide
        directions = directions.lstrip('L').rstrip('R')
        
        # Count all moving cars inside the collision zone
        return sum(c != 'S' for c in directions)
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n

        # Traverse left to right, applying rightward forces
        force = 0
        for i in range(n):
            if dominoes[i] == 'R':
                force = n  # Large force to propagate
            elif dominoes[i] == 'L':
                force = 0  # No rightward force beyond here
            else:
                force = max(force - 1, 0)  # Gradual decay of force
            forces[i] += force

        # Traverse right to left, applying leftward forces
        force = 0
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)
            forces[i] -= force

        # Construct the final state
        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return "".join(result)

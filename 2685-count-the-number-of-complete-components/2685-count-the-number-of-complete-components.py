from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build the graph using adjacency lists
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        
        # Find connected components using DFS
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)
        
        visited = set()
        connected_components = []
        
        for i in range(n):
            if i not in visited:
                component = []
                dfs(i, component)
                connected_components.append(component)
        
        # Check if a component is complete
        def is_complete(component):
            size = len(component)
            for node in component:
                if len(graph[node]) != size - 1:  # Each node must connect to all other nodes
                    return False
            return True
        
        # Count complete components
        count = 0
        for component in connected_components:
            if is_complete(component):
                count += 1
        
        return count
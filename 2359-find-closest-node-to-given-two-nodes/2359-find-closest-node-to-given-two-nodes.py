from typing import List

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def find_distances(start: int) -> List[int]:
            n = len(edges)
            distances = [-1] * n
            distance = 0
            current = start
            
            while current != -1 and distances[current] == -1:
                distances[current] = distance
                distance += 1
                current = edges[current]
            
            return distances
        
        dist1 = find_distances(node1)
        dist2 = find_distances(node2)
        
        min_max_distance = float('inf')
        result_node = -1
        
        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:  
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_max_distance:
                    min_max_distance = max_dist
                    result_node = i
        
        return result_node

from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bobArrivalTimes = {i: float('inf') for i in range(len(amount))}
        self.findBobPath(bob, 0, -1, graph, bobArrivalTimes)
        
        return self.findMaxProfitForAlice(graph, amount, bobArrivalTimes)
    
    def findBobPath(self, node, time, parent, graph, bobArrivalTimes):
        bobArrivalTimes[node] = time
        if node == 0:
            return True
        
        for neighbor in graph[node]:
            if neighbor != parent and self.findBobPath(neighbor, time + 1, node, graph, bobArrivalTimes):
                return True
        
        bobArrivalTimes[node] = float('inf')
        return False

    def findMaxProfitForAlice(self, graph, amount, bobArrivalTimes):
        self.maxProfit = float('-inf')
        self.exploreAlicePaths(0, 0, 0, -1, graph, amount, bobArrivalTimes)
        return self.maxProfit

    def exploreAlicePaths(self, node, time, currentProfit, parent, graph, amount, bobArrivalTimes):
        nodeProfit = amount[node] if time < bobArrivalTimes[node] else amount[node] // 2 if time == bobArrivalTimes[node] else 0
        totalProfit = currentProfit + nodeProfit
        
        if len(graph[node]) == 1 and node != 0:
            self.maxProfit = max(self.maxProfit, totalProfit)
            return
        
        for neighbor in graph[node]:
            if neighbor != parent:
                self.exploreAlicePaths(neighbor, time + 1, totalProfit, node, graph, amount, bobArrivalTimes)
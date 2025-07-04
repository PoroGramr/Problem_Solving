from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times:
            graph[time[0]].append((time[2], time[1]))
        
        costs = {}
        pq = []
        heapq.heappush(pq, (0,k))

        while pq:
            curCost, curNode = heapq.heappop(pq)
            if curNode not in costs:
                costs[curNode] = curCost
                for cost, nextNode in graph[curNode]:
                    nextCost = curCost + cost
                    heapq.heappush(pq, (nextCost, nextNode))
        
        for node in range(1, n + 1):
            if node not in costs:
                return - 1
        
        return max(costs.values())

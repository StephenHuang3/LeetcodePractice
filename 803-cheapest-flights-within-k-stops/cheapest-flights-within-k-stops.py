from collections import deque
import math


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        cost = [float("inf")] * n
        cost[src] = 0

        for i in range(k + 1):
            print(cost)
            new_cost = cost.copy()
            for start, end, price in flights:
                if new_cost[end] > cost[start] + price:
                    new_cost[end] = cost[start] + price
            cost = new_cost

        print(cost)
        return cost[dst] if cost[dst] != float("inf") else -1

        # 2->4->1->0
        # 1.   1. 5
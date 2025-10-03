from collections import deque
import math


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        cost = [float("inf")] * n
        cost[src] = 0


        for i in range(k + 1):
            prev = cost.copy()
            changed = False
            for start, end, price in flights:
                if prev[start] != float("inf") and cost[end] > prev[start] + price:
                    cost[end] = prev[start] + price
                    changed = True

            if not changed:
                break


        if cost[dst] == float("inf"):
            return -1
        return cost[dst]

       
import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            heapq.heappush(h, [math.sqrt(x*x + y*y), [x,y]])

        res = []
        for i in range(k):
            dis, point = heapq.heappop(h)
            res.append(point)

        return res
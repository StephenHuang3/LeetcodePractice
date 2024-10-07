import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            dis = math.sqrt(x*x + y*y)
            if len(h) < k:
                heapq.heappush(h, (-dis, (x, y)))
            else:
                heapq.heappushpop(h,(-dis, (x, y)))

        return [point[1] for point in h]
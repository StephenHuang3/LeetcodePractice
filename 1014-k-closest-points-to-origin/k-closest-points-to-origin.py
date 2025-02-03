class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        res = []

        for i in range(len(points)):
            dis = math.sqrt((points[i][0]**2 + points[i][1]**2))
            heapq.heappush(h, (-dis, points[i][0], points[i][1]))
            if len(h) > k:
                heapq.heappop(h)

        for i in range(len(h)):
            res.append([h[i][1], h[i][2]])

        return res
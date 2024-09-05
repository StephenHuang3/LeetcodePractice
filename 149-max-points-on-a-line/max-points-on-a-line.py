class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # y = mx + b
        if len(points) <= 1:
            return len(points)

        maxcount = 0
        for i in range(len(points)):
            slopes = {}
            for j in range(len(points)):
                if j == i:
                    continue
                # (y2 - y1) / (x2 - x1)
                if (points[j][0] == points[i][0]):
                    slopes['und'] = slopes.get('und', 0) + 1
                    maxcount = max(slopes['und'], maxcount)
                else:
                    m = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0])
                    slopes[m] = slopes.get(m, 0) + 1
                    maxcount = max(slopes[m], maxcount)

        return maxcount + 1

                
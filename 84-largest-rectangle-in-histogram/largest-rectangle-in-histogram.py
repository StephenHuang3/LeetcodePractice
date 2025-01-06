class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = [(heights[0], 0)]
        n = len(heights)
        area = heights[0]

        for r in range(1, n):
            last_idx = r
            while stk and stk[-1][0] > heights[r]:
                hei, idx = stk.pop()
                last_idx = idx
                area = max(area, (r - idx) * hei)

            stk.append(([heights[r], last_idx]))

        while stk:
            hei, idx = stk.pop()
            area = max(area, (n - idx) * hei)
        
        return area
                



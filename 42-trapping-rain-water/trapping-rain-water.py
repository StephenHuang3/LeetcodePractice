class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = height[0]
        maxr = height[len(height) - 1]
        total = 0
        l = 0
        r = len(height) - 1

        while l < r:
            if maxl <= maxr:
                l += 1
                total += max(0, maxl - height[l])
                maxl = max(maxl, height[l])

            else:
                r -= 1
                total += max(0, maxr - height[r])
                maxr = max(maxr, height[r])

        return total
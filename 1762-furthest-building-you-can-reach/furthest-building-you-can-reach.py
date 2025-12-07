import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        hp = []
        
        for i in range(n - 1):
            if heights[i] >= heights[i + 1]:
                continue
            heapq.heappush(hp, heights[i + 1] - heights[i])
            if len(hp) > ladders:
                popped = heapq.heappop(hp)
                bricks -= popped
                if bricks < 0:
                    return i

        return n - 1
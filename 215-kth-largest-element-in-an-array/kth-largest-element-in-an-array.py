import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num * -1)

        for i in range(k - 1):
            heapq.heappop(heap)

        return heapq.heappop(heap) * -1
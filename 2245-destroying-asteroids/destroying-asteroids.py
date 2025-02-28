import heapq


class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        wait_heap = []
        for asteroid in asteroids:
            while wait_heap and wait_heap[0] <= mass:
                mass += heapq.heappop(wait_heap)
            if asteroid <= mass:
                mass += asteroid
            else:
                heapq.heappush(wait_heap, asteroid)

        while wait_heap and wait_heap[0] <= mass:
            mass += heapq.heappop(wait_heap)
        
        return not wait_heap
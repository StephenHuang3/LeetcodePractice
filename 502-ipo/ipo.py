import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        c = 0
        for i in range(len(capital)):
            heapq.heappush(heap, [profits[i] * -1, capital[i]])
        exp = []
        while c < k and len(heap) > 0:
            prof, req = heapq.heappop(heap)
            if w >= req:
                
                w += prof * -1
                for i in range(len(exp)):
                    heapq.heappush(heap, [exp[i][0],exp[i][1]])
                exp = []
                c += 1
            else:
                exp.append([prof, req])
            # print(c < k)
            # print(len(heap) > 0)

        return w

        
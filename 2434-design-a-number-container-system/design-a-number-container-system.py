import heapq


class NumberContainers:

    def __init__(self):
        self.idx_to_num = {}
        self.num_heap = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.idx_to_num and self.idx_to_num[index] == number:
            return
        self.idx_to_num[index] = number
        heapq.heappush(self.num_heap[number], index)
        
    def find(self, number: int) -> int:
        heapp = self.num_heap[number]
        while heapp and self.idx_to_num[heapp[0]] != number:
            heapq.heappop(heapp)

        if heapp:
            return heapp[0]
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
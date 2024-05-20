class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = [1 for i in range(len(ratings))]

        for i in range(0, len(ratings) - 1, 1):
            if ratings[i] < ratings[i + 1]:
                arr[i + 1] = arr[i] + 1
        
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                arr[i - 1] = max(arr[i - 1], arr[i] + 1)

        return sum(arr)
class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        max_keep = 0
        n = len(beans)
        total =0 

        for i, amount in enumerate(beans):
            total += amount
            width = n - i
            max_keep = max(max_keep, width * amount)

        return total - max_keep
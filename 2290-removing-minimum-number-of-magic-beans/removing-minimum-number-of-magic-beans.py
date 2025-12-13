class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        min_remove = float("inf")
        alr_removed = 0
        n = len(beans)
        prefix = [0] * n
        prefix[0] = beans[0]

        for i in range(1, n):
            prefix[i] = prefix[i - 1] + beans[i]

        def get_sum(i):
            if i - 1 >= 0:
                return prefix[-1] - prefix[i - 1]
            else:
                return prefix[-1]

        for i in range(len(beans)):
            cur_height = beans[i]
            rect_amount = cur_height * (n - i)
            rmv_req = alr_removed + get_sum(i) - rect_amount
            min_remove = min(min_remove, rmv_req)
            alr_removed += cur_height
            if alr_removed >= min_remove:
                break

        return min_remove

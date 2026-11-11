class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        if need1 > need2 or (need1 == need2 and cost2 < cost1):
            need1, need2 = need2, need1
            cost1, cost2 = cost2, cost1

        if costBoth <= cost1 and costBoth <= cost2:
            return max(need1, need2) * costBoth
        elif costBoth >= cost1 + cost2:
            return need1 * cost1 + need2 * cost2
        elif costBoth <= cost1:
            return costBoth * need1 + (need2 - need1) * cost2
        elif costBoth <= cost2:
            return costBoth * need2
        else:
            return costBoth * need1 + (need2 - need1) * cost2


        
        # arr = [[0 for i in range(need1 + 1)] for j in range(need2 + 1)]

        # minc = min(cost1, costBoth)
        # minr = min(cost2, costBoth)

        # for c in range(1, need1 + 1):
        #     arr[0][c] = arr[0][c - 1] + minc

        # for r in range(1, need2 + 1):
        #     arr[r][0] = arr[r - 1][0] + minr

        # for c in range(1, need1 + 1):
        #     for r in range(1, need2 + 1):
        #         arr[r][c] = min(arr[r-1][c-1] + costBoth, arr[r-1][c] + cost2, arr[r][c - 1] + cost1)

        # # print(arr)

        # return arr[-1][-1]

        

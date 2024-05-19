class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        # l = 0
        # length, r = len(citations)

        # while l <= r:
        #     m = (l + r) / 2
        #     if citations[m] > length - m:
        #         if m + 1 < length and citations[m - 1] >= length - m - 1:

        length = len(citations)
        curmax = 0
        for i in range(len(citations)):
            curmax = max(curmax, min(citations[i], i + 1))
            # print(citations[i])
            # print(i + 1)
            # print("___")

        return curmax


# 1 3 5 7 8 9
# N
# 6 5 4 3 2 1

# 3 1 1
# 1 2 3
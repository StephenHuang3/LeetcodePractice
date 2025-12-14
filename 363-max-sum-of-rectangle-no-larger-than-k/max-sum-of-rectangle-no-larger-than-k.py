import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        if R > C:
            matrix = list(zip(*matrix))
            R, C = C, R

        max_sum = float("-inf")

        for left in range(C):
            row_sum = [0] * R
            for right in range(left, C):
                for i in range(R):
                    row_sum[i] += matrix[i][right]

                prefix = 0
                prefixes = [0]

                for s in row_sum:
                    prefix += s
                    idx = bisect.bisect_left(prefixes, prefix - k)
                    if idx < len(prefixes):
                        max_sum = max(max_sum, prefix - prefixes[idx])

                    insort(prefixes, prefix)

        return max_sum
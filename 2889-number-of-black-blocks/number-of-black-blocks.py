from collections import defaultdict


class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        ret = [0] * 5
        coord = defaultdict(int)
        for r, c in coordinates:
            if r != m - 1 and c != n - 1:
                coord[(r, c)] += 1
            if r - 1 >= 0 and c - 1 >= 0:
                coord[(r - 1, c - 1)] += 1
            if r - 1 >= 0 and c != n - 1:
                coord[(r - 1, c)] += 1
            if c - 1 >= 0 and r != m - 1:
                coord[(r, c - 1)] += 1

        for key, val in coord.items():
            ret[val] += 1

        ret[0] = (m - 1) * (n - 1) - sum(ret)

        return ret
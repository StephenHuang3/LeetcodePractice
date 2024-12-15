class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def backtrack(pos, comb, total):
            nonlocal n
            if pos >= n or target < total:
                return

            if target == total:
                res.append(comb[:])
                return

            comb.append(candidates[pos])
            backtrack(pos, comb, total + candidates[pos])
            comb.pop()
            backtrack(pos + 1, comb, total)

            return res

        return backtrack(0, [], 0)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        N = len(candidates)
        comb = []
        def back_track(pos, total):
            if total >= target:
                # print("right comb",comb)
                # print("total", total)
                if total == target:
                    res.append(list(comb))
                return

            for i in range(pos, N, 1):
                comb.append(candidates[i])
                back_track(i, total + candidates[i])
                comb.pop()
        
        back_track(0, 0)
        return res

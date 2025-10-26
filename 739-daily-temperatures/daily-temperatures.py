class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = [] #[temp, idx]
        for i, temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                ans[stk[-1][1]] = i - stk[-1][1]
                stk.pop()
            stk.append([temp, i])

        return ans
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        cur = []
        open = 0
        close= 0
        def backtrack():
            nonlocal open
            nonlocal close
            
            if open + close == n + n:
                res.append("".join(cur))
                return
            if open < n:
                cur.append("(")
                open += 1
                backtrack()
                cur.pop()
                open -= 1
            # print("reach )")
            if close < n and close < open:
                cur.append(")")
                close += 1
                backtrack()
                cur.pop()
                close -= 1

        backtrack()

        return res

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = [-1]
        max_len = 0

        for i, c in enumerate(s):
            if c == "(":
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                max_len = max(max_len, i - stk[-1])

        return max_len

        #  ) ) ) ) ) ( ( ( ( (
        # -1-2-3-4-5-4-3-2-1 0    
        # ( ( ( ( )( ( ) ) ) () ()
        # -1-2-3-2-1 0 1 0 -1-2-3

        # 2

        #    (  ( ( ( ) ( ( )
        # -1 0  1 2     5 6
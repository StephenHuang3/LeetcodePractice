class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        brac = set(['(', ')'])
        ret = []
        stk = []
        rmv_close = set()
        for i, c in enumerate(s):
            if c in brac:
                if c == '(':
                    stk.append(i)
                else:
                    if stk:
                        stk.pop()
                    else:
                        rmv_close.add(i)

        rmv_close.update(stk)

        for i, c in enumerate(s):
            if i not in rmv_close:
                ret.append(c)

        return "".join(ret)

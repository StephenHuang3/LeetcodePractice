class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        brac = set(['(', ')'])
        ret = []
        stk = []
        for i, c in enumerate(s):
            if c in brac:
                if c == '(':
                    stk.append(('(', i))
                    ret.append(('(', i))
                else:
                    if stk:
                        stk.pop()
                        ret.append(')')
            else:
                ret.append(c)

        pos = set([i[1] for i in stk])

        ret2 = []
        for i in range(len(ret)):
            if isinstance(ret[i], str):
                ret2.append(ret[i])
            elif ret[i][1] in pos:
                continue
            else:
                ret2.append(ret[i][0])

        return "".join(ret2)
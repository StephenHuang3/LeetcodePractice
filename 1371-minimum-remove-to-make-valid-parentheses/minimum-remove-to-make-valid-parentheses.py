class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = []
        remove_set = set()

        for i in range(len(s)):
            if s[i] == "(":
                stk.append(i)
            if s[i] == ")":
                if len(stk) == 0:
                    remove_set.add(i)
                else:
                    stk.pop()
        
        while stk:
            remove_set.add(stk.pop())

        res = ""

        for i in range(len(s)):
            if i in remove_set:
                continue
            else:
                res += s[i]

        return res
        
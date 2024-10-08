class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for brac in s:
            if brac in "([{":
                stk.append(brac)

            if len(stk) == 0:
                return False
            elif brac == ")":
                if stk.pop() != "(":
                    return False
            elif brac == "]":
                if stk.pop() != "[":
                    return False
            elif brac == "}":
                if stk.pop() != "{":
                    return False

        return len(stk) == 0
        
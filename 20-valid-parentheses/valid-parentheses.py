class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        open = set()
        open.add("(")
        open.add("[")
        open.add("{")

        for bra in s:
            print(bra)
            print(bra in open)
            if bra in open:
                stk.append(bra)
            else:
                if len(stk) == 0:
                    print("len 0", bra)
                    return False
                popped = stk.pop()
                if bra == ")" and popped != "(":
                    return False
                elif bra == "}" and popped != "{":
                    return False
                elif bra == "]" and popped != "[":
                    return False

        # print(len(stk))
        return True if len(stk) == 0 else False

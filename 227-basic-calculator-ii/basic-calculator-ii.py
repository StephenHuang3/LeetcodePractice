class Solution:
    def calculate(self, s: str) -> int:
        def cal(op1, op2, operand):
            if operand == "+":
                return op1 + op2
            if operand == "-":
                return op1 - op2
            if operand == "*":
                return op1 * op2
            if operand == "/":
                return op1 // op2

        stk = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i] == "/" or s[i] == "*":
                stk.append(s[i])
                i += 1

                while s[i] == " ":
                    i += 1

                c = 1
                while i + c < len(s) and s[i + c].isnumeric():
                    c += 1

                op2 = int(s[i: i + c])
                operand = stk.pop()
                op1 = stk.pop()
                stk.append(cal(op1, op2, operand))
                i = c + i - 1
            elif s[i].isnumeric():
                c = 1
                while i + c < len(s) and s[i + c].isnumeric():
                    c += 1
                stk.append(int(s[i: i + c]))
                i = c + i - 1
            else:
                stk.append(s[i])
            i += 1

        print(stk)
        if len(stk) == 1:
            return stk[0]

        i = 0
        stk2 = []
        while i < len(stk):
            if isinstance(stk[i], int):
                stk2.append(stk[i])
            else:
                operand = stk[i]
                i += 1
                op2 = stk[i]
                op1 = stk2.pop()
                stk2.append(cal(op1, op2, operand))

            i += 1

        return stk2[0]



        
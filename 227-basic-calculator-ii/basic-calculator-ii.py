class Solution:
    def calculate(self, s: str) -> int:
        num, PreSign, stk=0, '+', []
        for c in s + '+':
            if c == ' ':
                continue
            elif c.isnumeric():
                num = num * 10 + int(c)
            elif c in "+-*/":
                if PreSign == "+":
                    stk.append(num)
                if PreSign == "-":
                    stk.append(-num)
                if PreSign == "*":
                    op1 = stk.pop()
                    stk.append(op1 * num)
                if PreSign == "/":
                    op1 = stk.pop()
                    stk.append(math.trunc(op1/num))

                num = 0
                PreSign = c

        return sum(stk)
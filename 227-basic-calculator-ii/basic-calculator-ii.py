class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = ""
        prev_operator = '+'

        for i in range(len(s) + 1):
            ch = s[i] if i < len(s) else '\0'

            if ch.isdigit():
                num += ch
            elif ch != " " or i == len(s):
                match prev_operator:
                    case "+":
                        stack.append(int(num))
                    case "-":
                        stack.append(-1 * int(num))
                    case "*":
                        op1 = stack.pop()
                        stack.append(op1 * int(num))
                    case "/":
                        op1 = stack.pop()
                        stack.append(int(op1 / int(num)))

                    
                prev_operator = ch
                num = ""

        return sum(stack)

        
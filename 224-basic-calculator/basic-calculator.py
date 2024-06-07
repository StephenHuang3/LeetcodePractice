class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        current_num = 0
        operator = 1
        n = len(s)
        result = 0
        for i, char in enumerate(s):
            if char.isdigit():
                current_num = (current_num*10) + int(char)
            if char in "+-()" or i==n-1:
                if operator == 1:
                    result+=current_num
                elif operator == -1:
                    result-=current_num
                if char == '(':
                    stack.append(result)
                    stack.append(operator)
                    operator = 1
                    result=0
                elif char == ')':
                    sign = stack.pop()
                    first_arg = stack.pop()
                    result = first_arg + result * sign

                current_num = 0
                if char == '+':
                    operator = 1
                elif char == '-':
                    operator = -1

        return result
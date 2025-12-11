class Solution:
    def calculate(self, s: str) -> int:
        stk = []
        cur_val = 0
        result = 0
        sign = 1

        for c in s:
            # print("c", cur_val, result, stk)
            if c == ' ':
                continue
            elif c.isnumeric():
                cur_val = cur_val * 10 + int(c)
            elif c in "()":
                if c == "(":
                    result = result + cur_val * sign
                    stk.append(result)
                    stk.append(sign)
                    result = 0
                else:
                    # print(stk)
                    # print('result', result)
                    result += cur_val * sign
                    # print("curval", cur_val)
                    # print(result)
                    old_sign = stk.pop()
                    old_result = stk.pop()
                    # print("oldsign", old_sign)
                    # print("oldresult", old_result)
                    result = old_result + old_sign * result

                cur_val = 0
                sign = 1
                
            elif c in "+-":
                if c == "+":
                    # print("+ before", result)
                    result += cur_val * sign
                    sign = 1
                    # print("+", cur_val)
                    # print("+", result)
                elif c == "-":
                    result += cur_val * sign
                    sign = -1

                cur_val = 0

        print(result, cur_val)
        return result + cur_val * sign
#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stk = []

        for e in tokens:
            if e == "+":
                num2 = stk.pop()
                num1 = stk.pop()
                stk.append(num1 + num2);
            
            elif e == "-":
                num2 = stk.pop()
                num1 = stk.pop()
                stk.append(num1 - num2);
            
            elif e == "*":
                num2 = stk.pop()
                num1 = stk.pop()
                stk.append(int(num1 * num2));
            
            elif e == "/":
                num2 = stk.pop()
                num1 = stk.pop()
                stk.append(int(num1 / num2));
            
            else:
                stk.append(int(e));

        return stk.pop();
            
        
# @lc code=end


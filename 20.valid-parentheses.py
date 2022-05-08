#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stk = []

        for brack in s:
            if brack in ['(', '[', '{']:
                stk.append(brack)

            elif brack == ')':
                if len(stk) == 0:
                    return False
                elif stk.pop() != '(':
                    return False

            elif brack == '}':
                if len(stk) == 0:
                    return False
                elif stk.pop() != '{':
                    return False
            
            elif brack == ']':
                if len(stk) == 0:
                    return False
                elif stk.pop() != '[':
                    return False
                
        if len(stk) == 0:
            return True
        
        return False
        
# @lc code=end


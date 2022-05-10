#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ppos = 0;

        for i in range(len(s)):
            if ppos >= len(p):
                return False
            if s[i] == p[ppos] or p[ppos] == '.':
                ppos += 1
                continue
            if p[ppos] == '*' and p[ppos - 1] == '.':
                return True
            if p[ppos] == '*' and p[ppos - 1] != s[i]:
                ppos += 1
                if p[ppos] == s[i]:
                    continue
                elif ppos < len(p):
                    ppos += 1
                    continue
                else:
                    return False
        

        return True

        
# @lc code=end


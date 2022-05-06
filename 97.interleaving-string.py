#
# @lc app=leetcode id=97 lang=python
#
# [97] Interleaving String
#

# @lc code=start
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        c1 = 0
        c2 = 0
        doable = True

        for i in range(len(s3)):
            if (c1 < len(s1) and s3[i] == s1[c1]):
                c1 += 1
                continue
            if (c2 < len(s2) and s3[i] == s2[c2]):
                c2 += 1
                continue
            if (s3[i] != s1[c1] and s3[i] != s2[c2]):
                doable = False

        return doable
        
# @lc code=end


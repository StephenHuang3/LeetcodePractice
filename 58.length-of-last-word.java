/*
 * @lc app=leetcode id=58 lang=java
 *
 * [58] Length of Last Word
 */

// @lc code=start
import java.util.Arrays;
class Solution {
    public int lengthOfLastWord(String s) {
        String[] letters = s.split(" ");
        return letters[letters.length - 1].length();
    }
}
// @lc code=end


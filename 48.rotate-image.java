/*
 * @lc app=leetcode id=48 lang=java
 *
 * [48] Rotate Image
 */

// @lc code=start
class Solution {
    public void rotate(int[][] matrix) {

        int len = matrix.length;

        for(int i = 0; i < len; i++){
            for(int j = 0; j < i + 1; j++){
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }

        for(int i = 0; i < len; i++){
            for(int j = 0; j < len/2; j++){
                int temp2 = matrix[i][len - j - 1];
                matrix[i][len - j - 1] = matrix[i][j];
                matrix[i][j] = temp2;

            }
        }
        
    }
}
// @lc code=end


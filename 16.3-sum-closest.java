/*
 * @lc app=leetcode id=16 lang=java
 *
 * [16] 3Sum Closest
 */

// @lc code=start
class Solution {
    public int threeSumClosest(int[] nums, int target) {

        int len = nums.length;
        int min = 2147483647;
        Arrays.sort(nums);

        for(int i = 0; i < len; i++){
            for(int j = 0; j < len; j++){
                for(int k = 0; k < len; k++){
                    if(i == j || j == k || k == i) continue;

                    if(Math.abs(nums[i] + nums[j] + nums[k] - target) < min){
                        min = nums[i] + nums[j] + nums[k];
                    }

                }
            }
        }
        return min;
        
    }
}
// @lc code=end


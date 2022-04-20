import java.util.List;

/*
 * @lc app=leetcode id=442 lang=java
 *
 * [442] Find All Duplicates in an Array
 */

// @lc code=start
class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        int len = nums.length;

        int[] rep = new int[len + 1];
        
        for(int i = 0; i < len; i++){
            rep[nums[i]]++;
        }

        int count = 0;

        for(int i = 0; i < len + 1; i++){
            if(rep[i] > 1) count ++;
        }

        List<Integer> list=new ArrayList<Integer>();

        for(int i = 0; i < len + 1; i++){
            if(rep[i] > 1){
                list.add(i);
            }
        }
        
        return list;
    }
}
// @lc code=end


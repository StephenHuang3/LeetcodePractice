class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        found = set()
        nums.sort()

        for i in range(len(nums) - 2):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum == target:
                    if (nums[i], nums[l], nums[r]) not in found:
                        res.append([nums[i], nums[l], nums[r]])
                        found.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                    while nums[r]==nums[r+1] and l<r:
                        r-=1
                    # print("num l r", nums[l], nums[r])
                elif cur_sum < target:
                    l += 1
                else:
                    r -= 1

        return res
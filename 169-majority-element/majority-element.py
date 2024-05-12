class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hp = {}
        for i in range(len(nums)):
            if nums[i] in hp:
                hp[nums[i]] += 1
            else:
                hp[nums[i]] = 1

        for num, count in hp.items():
            if count > (len(nums)/2):
                return num
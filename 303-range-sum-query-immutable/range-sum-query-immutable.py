class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.prefix_sum = [0]
        for num in nums:
            self.prefix_sum.append(num + self.prefix_sum[-1])
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
        
# 1  2  3  4  5
# 1  3  6 10 15


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.k = floor(sqrt(len(nums)))
        self.buckets = []

        for i in range(0, len(nums), self.k):
            bucket_sum = sum(nums[i:i + self.k])
            self.buckets.append(bucket_sum)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.buckets[(index // self.k)] += diff
        

    def sumRange(self, left: int, right: int) -> int:
        jl = left // self.k
        jr = right // self.k

        if jl == jr:
            return sum(self.nums[left:right + 1])

        return sum(self.buckets[jl + 1: jr]) + sum(self.nums[left:((jl + 1) * self.k)]) + sum(self.nums[jr * self.k:right + 1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
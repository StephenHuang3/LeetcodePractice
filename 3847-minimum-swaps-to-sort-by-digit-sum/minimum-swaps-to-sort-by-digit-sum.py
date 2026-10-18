class Solution:
    def digsum(self, num: int):
        total = 0
        while num != 0:
            total += num % 10
            num = num // 10

        return total

    def minSwaps(self, nums: List[int]) -> int:
        num2pos = {}
        cycles = 0
        arr = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            dsum = self.digsum(nums[i])
            arr[i] = (dsum, nums[i])

        arr.sort()
        for i in range(len(nums)):
            num2pos[nums[i]] = i
        arr2 = [num2pos[i[1]] for i in arr]
        # print(arr)
        # print(arr2)

        seen = set()
        for i in range(len(nums)):
            if len(seen) == len(nums):
                break
            if arr2[i] in seen:
                continue
            
            seen.add(arr2[i])
            cur = arr2[i]
            while True:
                cur = arr2[cur]
                if cur in seen:
                    break
                else:
                    seen.add(cur)

            cycles += 1


        return len(nums) - cycles

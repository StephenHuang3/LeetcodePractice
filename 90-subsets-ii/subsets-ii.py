class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # res = []
        # cur = []
        # def backtrack(pos):
        #     # base case
        #     if pos == len(nums):
        #         res.append(cur.copy())
        #         return

        #     cur.append(nums[pos])
        #     backtrack(pos + 1)
        #     cur.pop()

        #     if pos + 1 < len(nums) and nums[pos] == nums[pos + 1]:
        #         pos += 1

        #     backtrack(pos + 1)

        # backtrack(0)
        # return res

        def f(index, t):
            ans.append(list(t))
            
            for i in range(index, len(nums)):
                if i != index and nums[i] == nums[i - 1]:
                    continue
                t.append(nums[i])
                print("index", index)
                print(i)
                print(t)
                f(i + 1, t)
                t.pop()

        ans = []
        nums.sort()
        f(0, [])
        return ans
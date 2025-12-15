class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        s = Counter()

        for num in nums:
            ns = Counter()
            for ss, v in s.items():
                if ss < k:
                    continue
                ns[ss & num] += v
            ns[num] += 1
            ans += ns[k]
            print(ns[k])
            s = ns
        
        return ans
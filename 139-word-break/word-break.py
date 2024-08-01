class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)

        for i in range(len(s)):
            for word in wordDict:
                # print("word")
                # print(word)
                # print("s[i:i + len(word)")
                # print(s[i:i + len(word)])
                if i + len(word) <= len(s) and s[i:i + len(word)] == word and (dp[i - 1] or i - 1 < 0):
                    # print("word")
                    # print(word)
                    # print("s[i:i + len(word)")
                    # print(s[i:i + len(word)])
                    dp[i + len(word) - 1] = True

        # print(dp)
        return dp[-1]
        
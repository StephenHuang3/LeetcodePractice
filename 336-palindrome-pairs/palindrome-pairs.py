class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        backward, res = {}, []
        for i, word in enumerate(words):
            backward[word[::-1]] = i

        for i, word in enumerate(words):
        # j goes 0..len(word) inclusive of both empty prefix/suffix
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]

                # Case 1: prefix is palindrome, need reversed(suffix)
                if prefix == prefix[::-1] and suffix in backward:
                    k = backward[suffix]
                    if k != i:
                        res.append([k, i])

                # Case 2: suffix is palindrome, need reversed(prefix)
                # avoid duplicating the empty-suffix case by requiring j < len(word)
                if j < len(word) and suffix == suffix[::-1] and prefix in backward:
                    k = backward[prefix]
                    if k != i:
                        res.append([i, k])
        return res
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        hp1 = {}
        hp2 = {}
        count = 0

        for word in words1:
            hp1[word] = hp1.get(word, 0) + 1

        for word in words2:
            hp2[word] = hp2.get(word, 0) + 1

        # print(hp1)
        # print(hp2)

        for word, freq in hp1.items():
            if freq == hp2.get(word, 0) == 1:
                count += 1

        return count
        
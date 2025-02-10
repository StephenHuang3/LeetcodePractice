class MagicDictionary:

    def __init__(self):
        self.myDict = defaultdict(set)
        

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            n = len(word)
            self.myDict[n].add(word)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        if n not in self.myDict: return False

        def findDiff(w1, w2):
            count = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    count += 1
                if count > 1:
                    return 2

            return count
        
        for word in self.myDict[n]:
            if findDiff(word, searchWord) == 1:
                return True

        return False
        


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
class MagicDictionary:

    def __init__(self):
        self.hp = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                key = word[0:i] + '*' + word[i + 1:]
                if key not in self.hp:
                    self.hp[key] = [False, word[i]]
                else:
                    self.hp[key] = [True, word[i]]

        print(self.hp)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            key = searchWord[0:i] + '*' + searchWord[i + 1:]
            if key in self.hp and (self.hp[key][0] or self.hp[key][1] != searchWord[i]):
                print("key", key)
                return True
        return False
        
# {'*': [True, 'l'], 'h*': [False, 'e'], 'he*': [False, 'l'], 'hel*': [False, 'l'], 'hell*': [False, 'o'], 'l*': [False, 'e'], 'le*': [False, 'e'], 'lee*': [False, 't'], 'leet*': [False, 'c'], 'leetc*': [False, 'o'], 'leetco*': [False, 'd'], 'leetcod*': [False, 'e']}

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
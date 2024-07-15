class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        check = {i:0 for i in wordList}
        if endWord not in check:
            return 0
        def oneChange(new, old) -> bool:
            c = 0
            for i in range(len(new)):
                if new[i] != old[i]:
                    c += 1

            return c == 1

        q = collections.deque()
        q.append(beginWord)
        step = 0
        
        while q:
            length = len(q)
            # print(q)
            for i in range(length):
                checkWord = q.popleft()
                if checkWord == endWord:
                    return step + 1
                if step != 0 and check[checkWord] != 0:
                    wordList.remove(checkWord)
                for word in wordList:
                    if oneChange(checkWord, word) and check[word] == 0:
                        check[word] = 1
                        q.append(word)
            
            step += 1

        return 0
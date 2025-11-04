from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hp = defaultdict(list)
        seen = set()
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                hp[key].append(word)

        q = collections.deque()
        q.append((beginWord, 1))
        seen.add(beginWord)
        
        while q:
            word, dis = q.popleft()
            if word == endWord:
                return dis

            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                for connection_word in hp[key]:
                    if connection_word not in seen:
                        seen.add(connection_word)
                        q.append((connection_word, dis + 1))

        return 0

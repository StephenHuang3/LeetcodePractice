from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = set()
        seen.add(beginWord)
        pattern_to_word = defaultdict(list)

        for word in wordList:
            for i in range(len(beginWord)):
                pattern = word[:i] + "*" + word[i + 1:]
                pattern_to_word[pattern].append(word)

        level = 1
        q = deque()
        q.append(beginWord)
        while q:
            length = len(q)
            for i in range(length):
                word = q.popleft()
                seen.add(word)
                if word == endWord:
                    return level
                for i in range(len(beginWord)):
                    pattern = word[:i] + "*" + word[i + 1:]
                    for cand in pattern_to_word[pattern]:
                        if cand not in seen:
                            q.append(cand)
            level += 1

        return 0
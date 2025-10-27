from collections import deque

import collections

class ANode:
    def __init__(self, letter):
        self.letter = letter
        self.children = {}
        self.end = False          # any word ends here?
        self.out = []             # list of matched patterns (optional: store lengths/ids)
        self.fail = None

class AhoC:
    def __init__(self, wordDict):
        self.root = ANode("*")
        self.root.fail = self.root

        # Build trie
        for w in wordDict:
            cur = self.root
            for ch in w:
                if ch not in cur.children:
                    cur.children[ch] = ANode(ch)
                cur = cur.children[ch]
            cur.end = True
            cur.out.append(w)     # store the word (or len(w)/id)

        # Build failure links (BFS)
        q = collections.deque()

        # depth-1: fail -> root
        for ch, node in self.root.children.items():
            node.fail = self.root
            q.append(node)

        while q:
            u = q.popleft()
            for ch, v in u.children.items():
                q.append(v)
                f = u.fail
                # walk failure links until we can follow ch or we reach root
                while f is not self.root and ch not in f.children:
                    f = f.fail
                v.fail = f.children[ch] if ch in f.children else self.root
                # inherit outputs from failure state
                v.end |= v.fail.end
                if v.fail.out:
                    v.out += v.fail.out

    def step(self, state, ch):
        """Follow char ch from node 'state', using fail links on mismatch."""
        while state is not self.root and ch not in state.children:
            state = state.fail
        return state.children.get(ch, self.root)

    def find_all(self, s):
        """Return list of (end_index, matched_word)."""
        res = []
        state = self.root
        for i, ch in enumerate(s):
            state = self.step(state, ch)
            if state.out:
                for w in state.out:
                    res.append((i, w))
        return res




class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        aho = AhoC(wordDict)
        dp[0] = True

        matches = aho.find_all(s)

        for i, w in matches:
            dp[i + 1] |= dp[i + 1 - len(w)]

        # print(matches)
        # print(dp)
        return dp[-1]


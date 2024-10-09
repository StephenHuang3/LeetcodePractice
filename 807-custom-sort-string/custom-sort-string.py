class Solution:
    def customSortString(self, order: str, s: str) -> str:
        hp = {}
        for i in range(len(order)):
            hp[order[i]] = i

        new = []
        
        for i in range(len(s)):
            new.append([s[i], hp.get(s[i], 27)])

        new.sort(key = lambda i: i[1])

        res = [i[0] for i in new]
        return "".join(res)
class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kv = {}
        for key, val in knowledge:
            kv[key] = val

        res = []
        c = 0
        while c < len(s):
            if s[c] == "(":
                c += 1
                cur = []
                while s[c] != ")":
                    print(s[c])
                    cur.append(s[c])
                    c += 1

                c += 1
                res.append(kv.get("".join(cur), "?"))
            else:
                res.append(s[c])
                c += 1

        return "".join(res)
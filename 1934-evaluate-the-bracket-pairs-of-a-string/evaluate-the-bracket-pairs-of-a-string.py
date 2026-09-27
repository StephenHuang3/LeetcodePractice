class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        kv = {}
        for key, val in knowledge:
            kv[key] = val

        res = []
        c = 0
        while c < len(s):
            if s[c] == "(":
                b= c + 1
                c += 1
                e = b
                while s[c] != ")":
                    e += 1
                    c += 1

                c += 1
                res.append(kv.get(s[b:e], "?"))
            else:
                res.append(s[c])
                c += 1

        return "".join(res)
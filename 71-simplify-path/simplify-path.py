class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        res = []

        for dir in arr:
            if dir == ".":
                continue
            elif dir == "..":
                if len(res) >= 1:
                    res.pop()
            elif dir == "":
                continue
            else:
                res.append(dir)

        return "/" + "/".join(res)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        hp = {}
        res = []
        hp['2'] = ['a', 'b', 'c']
        hp['3'] = ['d','e','f']
        hp['4'] = ['g','h','i']
        hp['5'] = ['j','k','l']
        hp['6'] = ['m','n','o']
        hp['7'] = ['p','q','r','s']
        hp['8'] = ['t','u','v']
        hp['9'] = ['w','x','y','z']

        def findAll(digits, cur):
            if len(digits) == 0:
                res.append(cur)
                return
            for l in hp[digits[0]]:
                findAll(digits[1:], cur + l)

        findAll(digits, "")
        return res
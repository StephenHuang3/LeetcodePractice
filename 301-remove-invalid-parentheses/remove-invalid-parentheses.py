class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ropen = 0
        rclose = 0

        stk = 0
        for c in s:
            if c == "(":
                stk += 1
            elif c == ")":
                if stk == 0:
                    rclose += 1
                else:
                    stk -= 1

        ropen += stk

        if ropen + rclose == 0:
            return [s]

        res = []
        sample = ""
        seen = set()

        def back(pos, ropen, rclose, balance):
            nonlocal sample
            # print("sm pos ro rc b", sample, pos, ropen, rclose, balance)
            if pos == len(s):
                if balance == 0 and ropen == 0 and rclose == 0 and sample not in seen:
                    res.append(sample)
                    seen.add(sample)
                return
            if s[pos] == "(":
                if ropen == 0:
                    if len(s) - pos >= ropen + rclose:
                        sample += "("
                        back(pos + 1, ropen, rclose, balance + 1)
                        sample = sample[:-1]
                else:
                    back(pos + 1, ropen - 1, rclose, balance)
                    if len(s) - pos >= ropen + rclose:
                        sample += "("
                        back(pos + 1, ropen, rclose, balance + 1)
                        sample = sample[:-1]

            if s[pos] == ")":
                if rclose == 0:
                    if balance > 0:
                        if len(s) - pos >= ropen + rclose:
                            sample += ")"
                            back(pos + 1, ropen, rclose, balance -1)
                            sample = sample[:-1]
                    else:
                        return
                else:
                    back(pos + 1, ropen, rclose - 1, balance)
                    if balance > 0:
                        if len(s) - pos >= ropen + rclose:
                            sample += ")"
                            back(pos + 1, ropen, rclose, balance - 1)
                            sample = sample[:-1]
            else:
                if len(s) - pos >= ropen + rclose:
                    sample += s[pos]
                    back(pos + 1, ropen, rclose, balance)
                    sample = sample[:-1]

        
        back(0, ropen, rclose, 0)
        return res
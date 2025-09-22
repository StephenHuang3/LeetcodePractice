class Solution:
    def myAtoi(self, s: str) -> int:
        c = 0
        news = []
        while c < len(s):
            if s[c] == ' ':
                c += 1
                continue
            break

        if c == len(s):
            return 0
            
        neg = False
        if s[c] == '-':
            neg = True
            c += 1
        elif s[c] == '+':
            c += 1

        while c < len(s):
            if s[c] == '0':
                c += 1
                continue
            break

        while c < len(s):
            if ord('9') >= ord(s[c]) >= ord('0'):
                news.append(s[c])
                c += 1
            else:
                break

        if len(news) == 0:
            return 0

        print(news)
        str_int = "".join(news)
        ret_int = int(str_int) * -1 if neg else int(str_int)
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if ret_int > INT_MAX:
            return INT_MAX
        elif ret_int < INT_MIN:
            return INT_MIN
        return ret_int
class Solution:
    def decodeString(self, s: str) -> str:
        cnt = 0
        dec_str = []
        cnt_stk = []
        dec_str_stk = []
        brac_cnt = 0

        for c in s:
            if c.isnumeric():
                cnt = cnt * 10 + int(c)
            elif c.isalpha():
                dec_str.append(c)
            elif c == '[':
                if cnt != 0:
                    cnt_stk.append([brac_cnt, cnt])
                cnt = 0
                if dec_str:
                    dec_str_stk.append([brac_cnt, dec_str])
                dec_str = []
                brac_cnt += 1
            else: # c == ']':
                brac_cnt -= 1
                if cnt_stk[-1][0] == brac_cnt:
                    _, cnt = cnt_stk.pop()


                dec_str += dec_str * (cnt - 1)
                while dec_str_stk and dec_str_stk[-1][0] == brac_cnt:
                    _, dec = dec_str_stk.pop()
                    dec_str = dec + dec_str
                
                cnt = 0

            # print("added",c)
            # print("cnt", cnt)
            # print("dec_str", dec_str)
            # print("cnt_stk", cnt_stk)
            # print("dec_str_stk", dec_str_stk)

        return "".join(dec_str)

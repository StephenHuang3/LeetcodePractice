class Solution:
    def bestClosingTime(self, customers: str) -> int:
        y_total = 0
        n_total = 0
        

        for c in customers:
            if c == 'Y':
                y_total += 1
            elif c == 'N':
                n_total += 1

        min_close = 0
        min_penalty = y_total
        cur_y = y_total
        cur_n = n_total

        for i in range(len(customers)):
            if customers[i] == 'Y':
                cur_y -= 1
            elif customers[i] == 'N':
                cur_n -= 1
            cur_penalty = cur_y + (n_total - cur_n)
            if cur_penalty < min_penalty:
                min_penalty = cur_penalty
                min_close = i + 1

        return min_close
        
class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n != 1:
            if n in visit:
                return False
            visit.add(n)
            print(visit)
            dsum = 0
            while n != 0:
                dsum += ( n % 10) * (n % 10)
                n = n // 10
            n = dsum


        return True
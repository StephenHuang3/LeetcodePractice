class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        if n == 1:
            return x
        
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n

        odd_power = 1
        even_power = x
        while n > 1:
            if n % 2 == 1:
                odd_power *= even_power
                n = n - 1

            even_power *= even_power
            n = n // 2

        return even_power * odd_power
        
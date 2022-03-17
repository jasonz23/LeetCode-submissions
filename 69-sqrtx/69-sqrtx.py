class Solution:
    def mySqrt(self, x: int) -> int:
        a = 0
        while True:
            if a * a ==  x:
                return a
            if (a*a < x < (a+1)*(a+1)):
                return a
            a += 1
        
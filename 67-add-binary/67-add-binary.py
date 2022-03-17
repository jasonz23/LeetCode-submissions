class Solution:
    def addBinary(self, a: str, b: str) -> str:
        tota = 0
        totb = 0
        a = a[::-1]
        b = b[::-1]
        for num in range(len(a)):
            tota += int(a[num]) * (2 ** num)
        for num in range(len(b)):
            totb +=int(b[num]) * (2 ** num)

        tot = tota + totb
        return bin(tot)[2:]
                
                
            
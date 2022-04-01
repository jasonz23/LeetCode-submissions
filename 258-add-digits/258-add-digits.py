class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        sum = 0
        a = str(num)
        b = len(str(num)) -1
        while b >= 0:
            sum += int(a[b])
            b -= 1
        
        return self.addDigits(sum)
            
        
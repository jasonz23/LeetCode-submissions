class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strings = [str(digit) for digit in digits]
        num = "".join(strings)
        
        num = num[::-1]
        print(num)
        number  = 0
        index = 0
        for string in num:
            number += int(string) * (10 ** index)
            print(number)
            index += 1
        number += 1
        string_n = str(number)
        ints = []
        for s in string_n:
            ints.append(int(s))
        return ints
            
        
        
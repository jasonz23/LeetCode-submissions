class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0
        for i1, a in enumerate(s):
            if i1 + 1 > len(s) -1:
                if a != " ":
                    l += 1
                return l
            if a == " " and s[i1 +1] != " ":
                 l =0
            if a != " ":
                l += 1
        return l
            
            
        
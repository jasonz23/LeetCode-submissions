class Solution:
    def longestPalindrome(self, s: str) -> str:
        st = ""
        if len(s) == 0 or len(s) == 1:
            return s
        for i in range(len(s) - 1):
            j = len(s)
            while j > i:
                if s[i:j] == s[i:j][::-1] and (j-i > len(st)):
                    if len(s[i:j] ) > len(st):

                        st = (s[i:j])
                if j - i < len(st):
                    break
                j -= 1
                
        return st

                
        
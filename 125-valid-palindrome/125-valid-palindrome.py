import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub("[^a-zA-Z0-9]+", "", s)
        s = s.lower()
        sb = s[::-1]
        print(sb)
        return s == sb
        
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0:
            return word2
        if len(word2) == 0:
            return word1
        string = ""
        
        string += word1[0]
        string += word2[0]
        return string + self.mergeAlternately(word1[1:],word2[1:])
        
        
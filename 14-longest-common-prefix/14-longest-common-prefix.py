class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        string = ""
        for s in zip(*strs):
            mylist = list(dict.fromkeys(s))
            if len(mylist) == 1:
                string += s[0]
            else:
                break
        return string
            
        
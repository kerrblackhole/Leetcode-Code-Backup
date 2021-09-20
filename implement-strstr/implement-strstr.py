class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        elif needle not in haystack:
            return -1
        else:
            out = 0
            while haystack[out:out+len(needle)] != needle:
                out +=1
            return out
        
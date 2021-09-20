class Solution:
    def isValid(self, s: str) -> bool:
        out = False
        while True:
            if '{}' in s:
                s = s.replace('{}','')
            elif '()' in s:
                s = s.replace('()','')
            elif '[]' in s:
                s = s.replace('[]','')
            else:
                break
        if len(s) == 0:
            out = True
        return out
        
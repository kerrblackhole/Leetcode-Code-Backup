class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        out = 0
        for i in range(-1,-len(s)-1,-1):
            if s[i] != ' ':
                out += 1
            elif out > 0:
                break
        return out
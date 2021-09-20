class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        out = False
        for i in range(len(s)):
            s = s[1:] + s[0]
            if s == goal:
                out = True
                break
        return out
        
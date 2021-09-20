class Solution:
    def checkRecord(self, s: str) -> bool:
        out = True
        x = 0
        for i in range(len(s)):
            if s[i] == 'A':
                x += 1
            if x == 2:
                out = False
                break
            if i < len(s)-2:
                if s[i:i+3] == 'LLL':
                    out = False
                    break
        return out
class Solution:
    def maxScore(self, s: str) -> int:
        outs = []
        for i in range(len(s)-1):
            out = 0
            for j in s[0:i+1]:
                if j == '0':
                    out += 1
            for j in s[i+1:len(s)]:
                if j == '1':
                    out += 1
            outs.append(out)
        return max(outs)
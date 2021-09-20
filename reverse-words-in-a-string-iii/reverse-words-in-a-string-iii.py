class Solution:
    def reverseWords(self, s: str) -> str:
        s += ' '
        out = ''
        slis = []
        for i in s:
            if i != ' ':
                slis.append(i)
            if i == ' ':
                for j in range(len(slis)):
                    out += slis[-j-1]
                out += ' '
                slis = []
        return out[:-1]
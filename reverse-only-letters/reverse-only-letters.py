class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ind = []
        tanda = []
        for i in range(len(s)-1,-1,-1):
            if not((s[i] >= 'a' and s[i] <= 'z') or (s[i] >= 'A' and s[i] <= 'Z')):
                ind.append(i)
                tanda.append(s[i])
                s = s[0:i] + s[i+1:len(s)]
        s = s[::-1]
        for i in range(-1,-len(ind)-1,-1):
            s = s[0:ind[i]] + tanda[i] + s[ind[i]:len(s)]
        return s
        
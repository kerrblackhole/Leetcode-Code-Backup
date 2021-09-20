class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a','i','u','e','o','A','I','U','E','O']
        strs = []
        for i in s:
            strs.append(i)
        vowlis = []
        inlis = []
        out = ''
        for i in range(-1,-len(s)-1,-1):
            if strs[i] in vowel:
                vowlis.append(s[i])
                inlis.append(i)
        inlis.sort()
        for i in range(len(vowlis)):
            strs[inlis[i]] = vowlis[i]
        for i in strs:
            out +=i
        return out
            
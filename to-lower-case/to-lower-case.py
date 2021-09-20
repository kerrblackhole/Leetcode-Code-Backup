class Solution:
    def toLowerCase(self, s: str) -> str:
        up = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in range(len(s)):
            if s[i] in up:
                x = low[up.index(s[i])]
                s = s[:i] + x + s[i+1:]
        return s
        

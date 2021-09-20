class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        count = 1
        out = []
        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                count +=1
            if s[i-1] != s[i]:
                if count >2:
                    out.append([i-count,i-1])
                count = 1
        if count >2:
            out.append([len(s)-count,len(s)-1])
        return out
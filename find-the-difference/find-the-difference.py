class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s += t
        lis = []
        for i in s:
            lis.append(i)
        lis.sort()
        out = lis[-1]
        for i in range(0,len(lis)-1,2):
            if lis[i] != lis[i+1]:
                out = lis[i]
                break
        return out
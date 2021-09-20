class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = []
        l2 = []
        out = False
        for i in s:
            l1.append(i)
        l1.sort()
        for j in t:
            l2.append(j)
        l2.sort()
        if l1 == l2:
            out = True
        return out
class Solution:
    def maxPower(self, s: str) -> int:
        sst = []
        for i in s:
            sst.append(i)
        out = [0]
        for i in range(1,len(sst)):
            if sst[i] == sst[i-1]:
                out[-1] += 1
            else:
                out.append(0)
        return max(out)+1
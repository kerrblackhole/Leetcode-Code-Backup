class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xbin = bin(x)
        ybin = bin(y)
        pan = max(len(xbin),len(ybin))-2
        xb = xbin[2:].zfill(pan)
        yb = ybin[2:].zfill(pan)
        out = 0
        for i in range(pan):
            if xb[i] != yb[i]:
                out += 1
        return out
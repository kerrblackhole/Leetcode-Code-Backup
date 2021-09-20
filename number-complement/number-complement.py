class Solution:
    def findComplement(self, num: int) -> int:
        nbin = bin(num)[2:]
        out = 0
        for i in range(len(nbin)):
            out += (1-int(nbin[-i-1])) * (2 ** i)
        return out
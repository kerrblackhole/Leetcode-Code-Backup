class Solution:
    def reverseBits(self, n: int) -> int:
        xbin = bin(n)[2:].zfill(32)
        out = 0
        for i in range(32):
            out += int(xbin[i]) * (2**i)
        return out
        
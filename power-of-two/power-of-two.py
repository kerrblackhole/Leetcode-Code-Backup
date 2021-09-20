class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = str(bin(n))[2:]
        out = False
        if n>0:
            if x[0] == '1' and x[1:] == '0'*(len(x)-1):
                out = True
        return out
            
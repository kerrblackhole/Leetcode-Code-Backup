class Solution:
    def trailingZeroes(self, n: int) -> int:
        x = 1
        out = 0
        while 5 ** x <= n:
            c = n // 5 ** x
            out += c
            x +=1
        return out
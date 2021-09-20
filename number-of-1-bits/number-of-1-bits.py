class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 1
        while n > 1:
            rem = n % 2
            if rem == 1:
                out += 1
            n = n // 2
        if n ==0:
            out -= 1
        return out
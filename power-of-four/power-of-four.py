class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x = False
        if n == 1:
            x = True
        while n>3:
            n /= 4
            if n == 1:
                x = True
                break
            if int(n) != n:
                break
        return x
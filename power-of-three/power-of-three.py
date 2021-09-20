class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        x = False
        if n == 1:
            x = True
        while n>2:
            n /= 3
            if n == 1:
                x = True
                break
            if int(n) != n:
                break
        return x
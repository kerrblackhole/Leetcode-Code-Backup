class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        x = False
        num = num ** (0.5)
        if int(num) == num:
            x = True
        return x
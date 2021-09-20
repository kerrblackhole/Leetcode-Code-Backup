class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        nb = text.count('b')
        na = text.count('a')
        nl = text.count('l')
        no = text.count('o')
        nn = text.count('n')
        return min(nb,na,nl // 2,no // 2,nn)
        
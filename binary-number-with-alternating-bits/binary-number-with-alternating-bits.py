class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        out = True
        xbin = ''
        while n>1:
            rem = n % 2
            xbin += str(rem)
            n = n // 2
            try:
                if xbin[-1] == xbin[-2]:
                    out = False
                    break
            except:
                pass
        if len(xbin) > 0:
            if xbin[-1] == '1':
                out = False
        return out
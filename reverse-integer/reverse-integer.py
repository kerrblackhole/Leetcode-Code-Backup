class Solution:
    def reverse(self, x: int) -> int:
        out = ''
        while x%10 == 0 and x != 0:
            x = int(x/10)
        strx = str(abs(x))
        for i in range(len(strx)-1,-1,-1):
            out += strx[i]
        if x<0:
            out = '-' + out
        if x<-(2**(31)) or int(out)<-(2**(31)) or x>= 2**(31) or int(out)>=2**(31):
            return 0
        else:
            return int(out)
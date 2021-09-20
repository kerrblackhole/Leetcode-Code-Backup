class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        nlis = []
        cek = 0
        out = False
        for i in range(1,int(num**0.5)+1):
            x = num / i
            if int(x) == x:
                if x != i:
                    nlis.append(i)
                    nlis.append(int(x))
                else:
                    nlis.append(i)
        for i in nlis:
            cek += i
        if num == cek / 2:
            out = True
        return out
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        outl = []
        out = 0
        for i in ops:
            try:
                outl.append(int(i))
                out += int(i)
            except:
                pass
            if i == 'C':
                out -= outl[-1]
                del outl[-1]
            if i == 'D':
                out += 2*outl[-1]
                outl.append(2*outl[-1])
            if i == '+':
                out += outl[-1] + outl[-2]
                outl.append(outl[-1] + outl[-2])
        return out
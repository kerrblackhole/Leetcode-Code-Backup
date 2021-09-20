class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        out = ''
        outl = [0 for i in range(len(num1)+len(num2))]
        for i in range(-1,-len(num2)-1,-1):
            for j in range(-1,-len(num1)-1,-1):
                outl[i+j+1] += int(num2[i]) * int(num1[j])
        for i in range(-1,-len(outl),-1):
            outl[i-1] += outl[i] // 10
            out = str(outl[i] % 10) + out
        if outl[0] != 0:
            out = str(outl[0]) + out
        if num1 == '0' or num2 == '0':
            out = '0'
        return out
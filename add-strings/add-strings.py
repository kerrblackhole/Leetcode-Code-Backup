class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        pan = max(len(num1),len(num2))
        n1 = num1.zfill(pan)
        n2 = num2.zfill(pan)
        carry = 0
        out = ''
        for i in range(pan):
            add = int(n1[-i-1])+int(n2[-i-1])+carry
            carry = 0
            if add > 9:
                carry =1
            out = str(add % 10) +out
        if carry == 1:
            out = str(carry) + out
        return out
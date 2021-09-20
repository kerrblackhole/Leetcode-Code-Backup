class Solution:
    def addDigits(self, num: int) -> int:
        while num >9:
            snum = str(num)
            num = 0
            for i in snum:
                num += int(i)
        return num
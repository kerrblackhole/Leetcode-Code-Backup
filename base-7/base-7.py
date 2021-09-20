class Solution:
    def convertToBase7(self, num: int) -> str:
        numab = abs(num)
        x = ''
        while numab > 6:
            y = numab % 7
            x = str(y) + x
            numab = int((numab-y)/7)
        x = str(numab) + x
        if num < 0:
            x = '-' + x
        return x
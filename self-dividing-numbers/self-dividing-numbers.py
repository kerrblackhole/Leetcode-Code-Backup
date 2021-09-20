class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        out = []
        for i in range(left, right+1):
            x = True
            for j in str(i):
                if int(j) == 0:
                    x = False
                else:
                    if i % int(j) != 0:
                        x = False
                        break
            if x == True:
                out.append(i)
        return out
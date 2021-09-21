class Solution:
    def intToRoman(self, num: int) -> str:
        out = ''
        Simbol = {1000: ['M',100],
          500: ['D',100],
          100: ['C',10],
          50: ['L',10],
          10: ['X',1],
          5: ['V',1],
          1: ['I',0],
          }
        while num > 0:
            for i in Simbol:
                num -= i
                if num < -Simbol[i][1]:
                    num += i
                    continue
                elif num < 0:
                    num += Simbol[i][1]
                    out += (Simbol[Simbol[i][1]][0] + Simbol[i][0])
                    break
                else:
                    out += Simbol[i][0]
                    break
        return out
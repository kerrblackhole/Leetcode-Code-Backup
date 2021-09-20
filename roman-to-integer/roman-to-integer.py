class Solution:
    def romanToInt(self, s: str) -> int:
        Roman = {"I" : 1,
         "V" : 5,
         "X" : 10,
         "L" : 50,
         "C" : 100,
         "D" : 500,
         "M" : 1000
         }
        init = 0
        for i in range(len(s)-1):
            if Roman[s[i]] < Roman[s[i+1]]:
                init -= Roman[s[i]]
            else:
                init += Roman[s[i]]
        init += Roman[s[len(s)-1]]
        return init
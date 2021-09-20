class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        out = True
        for i in range(len(strx)//2):
            if strx[i] != strx[-i-1]:
                out = False
        return out       
        
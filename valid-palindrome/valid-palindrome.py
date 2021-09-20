class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        x = ''
        y = True
        for i in s:
            if (i>= 'a' and i<= 'z') or (i>= '0' and i<='9'):
                x += i
        for i in range(len(x) // 2):
            if x[i] != x[-i-1]:
                y = False
                break
        return y
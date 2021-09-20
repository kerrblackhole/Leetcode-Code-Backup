class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for x in range(len(s)-1):
            y = s.pop(-1)
            s.insert(x,y)
        return s
            
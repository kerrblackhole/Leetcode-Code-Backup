class Solution:
    def mySqrt(self, x: int) -> int:
        out = 0
        while out*out <= x:
            out +=1
        return out-1
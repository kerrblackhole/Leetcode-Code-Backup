class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        low = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        x = {}
        for i in range(26):
            x[low[i]] = widths[i]
        out = [1,0]
        for i in s:
            out[1] += x[i]
            if out[1] > 100:
                out[0] += 1
                out[1] = x[i]
        if len(s) == 0:
            out[0] = 0
        return out
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        out = 0
        for i in stones:
            if i in jewels:
                out +=1
        return out
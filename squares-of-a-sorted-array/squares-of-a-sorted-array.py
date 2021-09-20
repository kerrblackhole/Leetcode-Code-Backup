class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = [i**2 for i in nums]
        out.sort()
        return out
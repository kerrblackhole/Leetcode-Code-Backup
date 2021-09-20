class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(0,len(nums),2):
            out += [nums[i+1] for j in range(nums[i])]
        return out
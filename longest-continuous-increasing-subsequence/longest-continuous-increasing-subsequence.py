class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        out = 1
        outsem = 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                outsem += 1
            else:
                if outsem > out:
                    out = outsem
                outsem = 1
        return max(out,outsem)
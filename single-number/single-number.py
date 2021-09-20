class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            out = nums[0]
        elif nums[0] != nums[1]:
            out = nums[0]
        elif nums[-2] != nums[-1]:
            out = nums[-1]
        else:
            for i in range(1,len(nums)-1):
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    out = nums[i]
                    break
        return out
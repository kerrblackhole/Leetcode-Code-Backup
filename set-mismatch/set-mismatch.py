class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        out = []
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                out.append(nums[i])
                break
        if nums[0] != 1:
            out.append(1)
        if nums[-1] != len(nums):
            out.append(len(nums))
        else:
            for i in range(0,len(nums)-1):
                if nums[i] +2 == nums[i+1]:
                    out.append(nums[i] +1)
        return out
        
        
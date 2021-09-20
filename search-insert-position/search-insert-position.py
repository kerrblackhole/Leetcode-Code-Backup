class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)
        else:
            out = 0
            while nums[out] < target:
                out +=1
            return out
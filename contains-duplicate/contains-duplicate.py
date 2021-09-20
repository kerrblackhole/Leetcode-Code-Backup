class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        x = False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                x = True
                break
            if x == True:
                break
        return x
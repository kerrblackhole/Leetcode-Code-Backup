class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        out = 0
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                out = nums[i] + nums[i+1] + nums[i+2]
                break
        return out
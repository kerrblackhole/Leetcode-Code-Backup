class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for i in range(k):
            indmin = nums.index(min(nums))
            nums[indmin] *= -1
        out = 0
        for j in nums:
            out += j
        return out
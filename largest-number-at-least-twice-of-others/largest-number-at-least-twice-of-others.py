class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            ind = nums.index(max(nums))
            x = nums.pop(ind)
            y = nums.pop(nums.index(max(nums)))
            if x >= 2*y:
                return ind
            else:
                return -1
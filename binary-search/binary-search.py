class Solution:
    def search(self, nums: List[int], target: int) -> int:
        out = -1
        for i in range(len(nums)):
            if target == nums[i]:
                out = i
                break
        return out       
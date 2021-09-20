class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)-1,-1,-1):
            for j in range(i-1,-1,-1):
                if nums[i]+nums[j]==target:
                    out += [j,i]
        return out
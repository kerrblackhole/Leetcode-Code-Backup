class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        out = []
        for i in range(1, min(nums)):
            out.append(i)
        for i in range(len(nums)-1):
            for j in range(nums[i]+1,nums[i+1]):
                out.append(j)
        for i in range(max(nums)+1,len(nums)+1):
            out.append(i)
        return out
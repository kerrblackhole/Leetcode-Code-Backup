class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        out = []
        nums.insert(0,0)
        for i in range(len(nums)):
            if nums[i] == 0:
                out.append(0)
            else:
                out[-1] += 1
        return max(out)
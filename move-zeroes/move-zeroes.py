class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                x = nums.pop(i)
                nums.insert(c,x)
                c +=1
        
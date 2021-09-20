class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while i%2 != nums[i] % 2:
                x = nums.pop(i)
                nums.append(x)
        return nums
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        y = nums.pop(nums.index(max(nums)))
        uru = [y]
        for i in range(len(nums)):
            x = nums.pop(nums.index(max(nums)))
            if uru[-1] != x:
                uru.append(x)
            if len(uru) == 3:
                break
        if len(uru) == 3:
            y = uru[-1]
        return y
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        out = True
        cek = nums[0:2]
        for i in range(2,len(nums)):
            if (cek[-1] - cek[-2])*(nums[i] - cek[-1]) < 0:
                out = False
                break
            if nums[i] != cek[-1]:
                cek.append(nums[i])
        return out
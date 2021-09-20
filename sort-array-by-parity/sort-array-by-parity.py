class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        cek = []
        for i in range(len(nums)-1,-1,-1):
            if nums[i] % 2 == 0:
                x = nums.pop(i)
                cek.append(x)
        return cek + nums
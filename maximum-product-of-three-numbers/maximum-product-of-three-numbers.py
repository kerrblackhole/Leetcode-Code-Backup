class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        temp = []
        hasil = 1
        for i in range(3):
            pop = nums.pop(nums.index(max(nums)))
            hasil *= pop
            temp.append(pop)
        hasil1 = temp[0]
        nums += temp
        for i in range(2):
            pop = nums.pop(nums.index(min(nums)))
            hasil1 *= pop
        return(max(hasil,hasil1))
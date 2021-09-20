class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            y = nums.pop(nums.index(max(nums)))
        return y
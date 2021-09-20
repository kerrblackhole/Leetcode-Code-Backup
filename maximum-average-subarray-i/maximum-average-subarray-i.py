class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        jum = 0
        for i in range(k):
            jum += nums[i]
        jum1 = jum
        for i in range(1,len(nums)-k+1):
            jum1 = jum1-nums[i-1]+nums[i+k-1]
            if jum1 > jum:
                jum = jum1
        return(jum/k)
        
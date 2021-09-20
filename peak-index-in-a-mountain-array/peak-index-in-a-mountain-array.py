class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        out = 0
        for i in range(1,len(arr)-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                out = i
                break
        return out
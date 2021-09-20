class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        out = True
        indmax = arr.index(max(arr))
        if indmax == 0 or indmax == len(arr)-1:
            out = False
        elif len(arr) < 2:
            out = False
        else:
            for i in range(indmax-1):
                if arr[i] >= arr[i+1]:
                    out = False
                    break
            for i in range(indmax,len(arr)-1):
                if arr[i] <= arr[i+1]:
                    out = False
                    break
        return out
                
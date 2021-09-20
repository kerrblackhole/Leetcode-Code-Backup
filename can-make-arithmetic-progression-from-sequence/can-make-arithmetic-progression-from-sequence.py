class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        beda = arr[1] - arr[0]
        out = True
        for i in range(1,len(arr)-1):
            if arr[i+1] - arr[i] != beda:
                out = False
                break
        return out
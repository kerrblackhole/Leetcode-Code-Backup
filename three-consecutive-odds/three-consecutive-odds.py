class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        out = False
        for i in range(len(arr)-2):
            if arr[i] % 2 ==0:
                continue
            else:
                if arr[i+1] % 2 ==1 and arr[i+2] % 2 ==1:
                    out = True
                    break
        return out
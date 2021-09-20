class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        try:
            arr.remove(0)
        except:
            pass
        out = False
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if arr[i] > 0 and arr[j] > 2*arr[i]:
                    break
                if arr[i] < 0 and arr[j] > 0.5*arr[i]:
                    break
                if arr[j] == 2*arr[i] or arr[j] == 0.5*arr[i]:
                    out = True
                    break
            if out == True:
                break
        return out
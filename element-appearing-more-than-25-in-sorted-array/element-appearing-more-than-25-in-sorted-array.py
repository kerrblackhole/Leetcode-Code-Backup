class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        cek = len(arr)//4+1
        jum = 1
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                jum += 1
                if jum == cek:
                    break
            else:
                jum = 1
        if len(arr) == 1:
            return arr[0]
        else:
            return arr[i-1]
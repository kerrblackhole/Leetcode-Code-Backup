class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        nar = []
        for i in range(len(arr)):
            if arr[i] == 0:
                nar.append(i)
        for i in range(-1,-len(nar)-1,-1):
            arr.insert(nar[i],0)
            del arr[-1]
        return arr
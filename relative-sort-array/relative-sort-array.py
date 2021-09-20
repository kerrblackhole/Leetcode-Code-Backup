class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out = []
        for i in arr2:
            while i in arr1:
                x = arr1.pop(arr1.index(i))
                out.append(x)
        arr1.sort()
        return out + arr1
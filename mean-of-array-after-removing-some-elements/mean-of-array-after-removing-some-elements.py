class Solution:
    def trimMean(self, arr: List[int]) -> float:
        hapus = int(len(arr)/20)
        out = 0
        for i in range(hapus):
            arr.remove(max(arr))
            arr.remove(min(arr))
        for j in arr:
            out += j
        return out / len(arr)
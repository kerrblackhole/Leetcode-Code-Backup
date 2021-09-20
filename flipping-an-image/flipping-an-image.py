class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        out = []
        for vec in image:
            veco = []
            for i in range(len(vec)):
                veco.append(-vec[-i-1]+1)
            out.append(veco)
        return out
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        out = []
        while len(matrix) > 0:
            for i in range(4):
                if i == 0:
                    for i in matrix[0]:
                        out.append(i)
                    del matrix[0]
                elif i == 1:
                    for i in range(len(matrix)):
                        y = matrix[i].pop(-1)
                        out.append(y)
                    while [] in matrix:
                        matrix.remove([])
                elif i == 2:
                    for i in range(-1,-len(matrix[-1])-1,-1):
                        out.append(matrix[-1][i])
                    del matrix[-1]
                elif i == 3:
                    for i in range(-1,-len(matrix)-1,-1):
                        z = matrix[i].pop(0)
                        out.append(z)
                    while [] in matrix:
                        matrix.remove([])
                if len(matrix) == 0:
                    break
        return out
        
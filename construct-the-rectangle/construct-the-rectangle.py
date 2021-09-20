class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        out = [0,0]
        for i in range(int((area**0.5)+1),0,-1):
            x = area / i
            if int(x) == x:
                out[0] = int(x)
                out[1] = i
                break
        if out[1] > out[0]:
            y = out.pop(0)
            out.append(y)
        return out
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        pan = max(len(num),len(str(k)))
        out = [0 for i in range(pan+1)]
        for i in range(pan-len(num)):
            num.insert(0,0)
        sk = str(k).zfill(pan)
        for i in range(-1,-pan-1,-1):
            jum = out[i] + num[i] + int(sk[i])
            if jum > 9:
                out[i] = jum %10
                out[i-1] += 1
            else:
                out[i] = jum
        if out[0] == 0:
            del out[0]
        return out
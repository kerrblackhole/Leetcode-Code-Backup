class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pan = max(len(a),len(b))
        ab = a.zfill(pan)
        bb = b.zfill(pan)
        out = ''
        carry = 0
        for i in range(-1,-pan-1,-1):
            jum = carry + int(ab[i]) + int(bb[i])
            if jum > 1:
                out = str(jum%2) + out
                carry = 1
            else:
                out = str(jum) + out
                carry = 0
        if carry == 1:
            out = '1' + out
        return out
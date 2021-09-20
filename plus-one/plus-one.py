class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        outstr = ''
        for i in digits:
            outstr += str(i)
        outint = int(outstr)+1
        outlist = [x for x in str(outint)]
        return outlist
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = [[1]]
        init = [1,1]
        for i in range(numRows-1):
            out += [init]
            newlist = []
            for j in range(len(init)-1):
                jum = init[j]+init[j+1]
                newlist += [jum]
            init = newlist.copy()
            init.insert(0,1)
            init.insert(len(init),1)
        return out
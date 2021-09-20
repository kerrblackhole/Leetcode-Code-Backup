class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        init = [1,1]
        if rowIndex == 0:
            init = [1]
        else:
            for i in range(rowIndex-1):
                newlist = []
                for j in range(len(init)-1):
                    jum = init[j]+init[j+1]
                    newlist.append(jum)
                init = newlist.copy()
                init.insert(0,1)
                init.insert(len(init),1)
        return init
        
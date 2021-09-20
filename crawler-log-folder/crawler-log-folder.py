class Solution:
    def minOperations(self, logs: List[str]) -> int:
        fol = []
        for i in logs:
            if i == '../':
                try:
                    del fol[-1]
                except:
                    pass
            elif i == './':
                pass
            else:
                fol.append(i[:-1])
        return len(fol)
        
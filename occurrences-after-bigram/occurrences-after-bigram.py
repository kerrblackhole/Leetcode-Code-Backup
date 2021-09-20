class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        lis = text.split(' ')
        out = []
        for i in range(len(lis)-2):
            if lis[i] == first and lis[i+1] == second:
                out.append(lis[i+2])
        return out
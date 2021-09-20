class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        out = ['' for i in range(len(score))]
        for i in range(len(score)):
            maxin = score.index(max(score))
            score[maxin] = -1
            if i == 0:
                out[maxin] = 'Gold Medal'
            elif i == 1:
                out[maxin] = 'Silver Medal'
            elif i == 2:
                out[maxin] = 'Bronze Medal'
            else:
                out[maxin] = str(i+1)
        return out
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        out = [0 for i in range(num_people)]
        init = 0
        while candies > init:
            out[init % num_people] += init+1
            candies -= (init+1)
            init += 1
        out[init % num_people] += candies
        return out
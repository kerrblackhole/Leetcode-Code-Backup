class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        for i in range(len(list1) + len(list2) - 1):
            for j in range(len(list2)):
                if j <= i and (i-j) < len(list1):
                    if list2[j] == list1[i-j]:
                        ans.append(list2[j])
            if len(ans) != 0:
                break
        return ans
        
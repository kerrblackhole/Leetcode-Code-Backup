class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        up = ['q','w','e','r','t','y','u','i','o','p']
        mid = ['a','s','d','f','g','h','j','k','l']
        dow = ['z','x','c','v','b','n','m']
        out = []
        for word in words:
            ind = 0
            for char in word.lower():
                if char in up:
                    ind +=1
                    break
            for char in word.lower():
                if char in mid:
                    ind +=1
                    break
            for char in word.lower():
                if char in dow:
                    ind +=1
                    break
            if ind == 1:
                out.append(word)
        return out
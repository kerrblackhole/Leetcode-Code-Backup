class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cha = [i for i in chars]
        out = 0
        for word in words:
            x = True
            chaa = cha.copy()
            for i in word:
                if i in chaa:
                    chaa.remove(i)
                else:
                    x = False
                    break
            if x == True:
                out += len(word)
        return out
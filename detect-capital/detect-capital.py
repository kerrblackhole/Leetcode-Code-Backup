class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        out = False
        if word.upper() == word:
            out = True
        if word.lower() == word:
            out = True
        if word[0].upper() == word[0] and word[1:].lower() == word[1:]:
            out = True
        return out
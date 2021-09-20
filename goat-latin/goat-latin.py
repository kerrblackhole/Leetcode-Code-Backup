class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        kata = sentence.split()
        vowel = ['a','i','u','e','o']
        for i in range(len(kata)):
            if kata[i][0].lower() not in vowel:
                kata[i] = kata[i][1:] + kata[i][0]
            kata[i] += 'maa' + 'a'*i
        out = ''
        for j in kata:
            out += j + ' '
        return out[:-1]
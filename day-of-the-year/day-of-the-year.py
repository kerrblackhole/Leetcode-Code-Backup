class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[-2:])
        dom = [31,28,31,30,31,30,31,31,30,31,30]
        out = 0
        for i in range(1, month):
            out += dom[i-1]
        out += day
        if year % 4 == 0 and year != 1900 and month > 2:
            out +=1
        return out
class Solution:
    def reformatDate(self, date: str) -> str:
        Bul = {'Jan' : '01',
       'Feb' : '02',      
       'Mar' : '03',
       'Apr' : '04',
       'May' : '05',
       'Jun' : '06',
       'Jul' : '07',
       'Aug' : '08',
       'Sep' : '09',
       'Oct' : '10',
       'Nov' : '11',
       'Dec' : '12',
       }
        year = date[-4:]
        month = Bul[date[-8:-5]]
        day = date[:-11]
        dayz = day.zfill(2)
        return year + '-' + month + '-' + dayz
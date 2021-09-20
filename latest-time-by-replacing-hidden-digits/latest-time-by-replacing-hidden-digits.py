class Solution:
    def maximumTime(self, time: str) -> str:
        out = ''
        for i in [0,1,3,4]:
            if time[i] == '?':
                if i == 0:
                    if time[1] in ['?','0','1','2','3']:
                        out += '2'
                    else:
                        out += '1'
                elif i == 1:
                    if time[0] in ['?','2']:
                        out += '3:'
                    else:
                        out += '9:'
                elif i == 3:
                    out += '5'
                elif i == 4:
                    out += '9'
            else:
                if i == 1:
                    out += time[1:3]
                else:
                    out += time[i]
        return out
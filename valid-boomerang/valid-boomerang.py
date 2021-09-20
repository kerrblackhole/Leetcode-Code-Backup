class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        y12 = points[1][1]-points[0][1]
        x12 = points[1][0]-points[0][0]
        y13 = points[2][1]-points[0][1]
        x13 = points[2][0]-points[0][0]
        out = True
        if (x12==0) and (x13==0):
            out = False
        elif (y12==0) and (y13==0):
            out = False
        elif (y12==0) and (x12==0):
            out = False
        elif (y13==0) and (x13==0):
            out = False
        elif (x12!=0) and (x13!=0):
            m1 = y12/x12
            m2 = y13/x13
            if m1 == m2:
                out = False
        return out
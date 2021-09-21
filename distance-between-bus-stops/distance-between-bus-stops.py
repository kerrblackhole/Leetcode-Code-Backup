class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        out1 = 0
        out2 = 0
        if start > destination:
            z = start
            start = destination
            destination  = z
        for i in range(start):
            out1 += distance[i]
        for i in range(start, destination):
            out2 += distance[i]
        for i in range(destination, len(distance)):
            out1 += distance[i]
        return min(out1,out2)
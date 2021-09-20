class Solution:
    def tribonacci(self, n: int) -> int:
        n1 = 0
        n2 = 1
        n3 = 1
        if n == 0:
            return 0
        elif n in [1,2]:
            return 1
        else:
            for i in range(3,n+1):
                jum = n1+n2+n3
                n1 = n2
                n2 = n3
                n3 = jum
            return n3
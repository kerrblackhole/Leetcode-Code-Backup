class Solution:
    def fib(self, n: int) -> int:
        n1 = 0
        n2 = 1
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            for i in range(2,n+1):
                jum = n1+n2
                n1 = n2
                n2 = jum
            return n2
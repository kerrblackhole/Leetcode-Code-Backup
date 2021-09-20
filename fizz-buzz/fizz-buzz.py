class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1,n+1):
            if i % 3 == 0 or i % 5 ==0:
                outs = 'Fizz'*(i%3==0)+'Buzz'*(i%5==0)
            else:
                outs = str(i)
            out.append(outs)
        return out
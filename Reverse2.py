class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x<0:
            neg = True
            x*=-1
        x = str(x)
        r = x[::-1]
        r = int(r)
        if neg:
            r *= -1
        if r < -2**31 or r > 2**31 - 1:
            return 0
        return r
            

# Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c<0:
            return False
        i = 0
        j = int(c**0.5)
        while i<=j:
            curr_sum = (i*i)+(j*j)
            if curr_sum == c:
                return True
            elif curr_sum<c:
                i+=1
            else:
                j-=1
        return False

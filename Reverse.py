#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x<0:
            neg = True
        x = abs(x)
        r = 0
        while x!= 0:
            rem = x % 10
            r = r*10 + rem
            x = x//10
        if neg:
            r *= -1
        if r < -2**31 or r > 2**31 - 1:
            return 0
        return r
            

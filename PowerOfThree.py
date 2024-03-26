# Given an integer n, return true if it is a power of three. Otherwise, return false.
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        if n==1:
            return True
        
        while n>0:
            r = n%3
            n/=3
            if n==1:
                return True
        return False

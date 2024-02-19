# Given an integer n, return true if it is a power of two. Otherwise, return false. 
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(31):
            if n==2**i:
                return True
        return False
            
        

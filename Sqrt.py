# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        my_dict = {}
        i=0
        while i * i <= x:
            my_dict[i] = i * i
            i += 1

        i = 0
        while i in my_dict and x>=my_dict[i]:
            i+=1
        return i-1

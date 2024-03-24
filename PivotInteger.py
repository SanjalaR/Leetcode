# Given a positive integer n, find the pivot integer x such that:
# The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
# Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

class Solution(object):
    def sums(self, s, e):
        sum=0
        for i in range(s, e+1):
            sum+=i
        return sum
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n+1):
            if self.sums(1, i) == self.sums(i, n):
                return i
        return -1

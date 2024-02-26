# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def sumdig(num):
            if num==0:
                return 0
            if num/10 == 0:
                return num
            sum = 0
            while(num>0):
                sum+=num%10 
                num/=10
            return sumdig(sum)

        return sumdig(num)

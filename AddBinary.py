# Given two binary strings a and b, return their sum as a binary string.
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1 = int(a, 2)
        num2 = int(b, 2)
        num1 = num1+num2        
        return bin(num1).replace("0b", "")

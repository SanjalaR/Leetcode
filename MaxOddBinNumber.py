# Return a string representing the maximum odd binary number that can be created from the given combination.
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c1 = s.count('1')
        c0 = s.count('0')
        return '1'*(c1-1)+'0'*(c0)+'1'

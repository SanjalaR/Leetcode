# Given a roman numeral, convert it to integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        res = 0
        prev = 0
        for i in range(len(s)):
            if rom[s[i]]>prev:
               res += rom[s[i]] - 2*prev
               
            else:
                res += rom[s[i]]
            prev = rom[s[i]]
        return res

# Given a string s consisting of words and spaces, return the length of the last word in the string.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1])

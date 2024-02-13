# Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".
class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for i in words:
            if i==i[::-1]:
                return i
        return ""

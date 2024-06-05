# Given an input string s, reverse the order of the words.
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s_list = s.split()
        s = ' '
        return s.join(s_list[::-1])

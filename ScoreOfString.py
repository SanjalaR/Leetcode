# You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(len(s)):
            if i>0:
                score+=abs(ord(s[i-1]) - ord(s[i]))
        return score
        

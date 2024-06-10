# Given a string s, find the length of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxlen = 0
        j = 0
        while j<len(s):
            if s[j] not in s[i:j]:
                j+=1
                maxlen = max(maxlen, j-i)
            else:
                while s[i]!=s[i]:
                    i+=1
                i+=1
        return maxlen

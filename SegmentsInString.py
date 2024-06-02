# Given a string s, return the number of segments in the string.
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

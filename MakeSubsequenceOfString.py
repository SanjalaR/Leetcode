# Return the minimum number of characters that need to be appended to the end of s so that t becomes a subsequence of s.
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while i!=len(s):
            if j!=len(t) and s[i]==t[j]:
                j+=1
            i+=1
        return len(t)-j
        

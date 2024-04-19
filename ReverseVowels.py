# Given a string s, reverse only all the vowels in the string and return it.
class Solution:
    def reverseVowels(self, s: str) -> str:
        asc = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
        ind = []
        c = []
        for i in range(len(s)):
            if(ord(s[i]) in asc):
                ind.append(i)
                c.append(s[i])
        c[:] = c[::-1]
        l = list(s)
        for i in range(len(ind)):
            l[ind[i]] = c[i]
        
        return "".join(l)

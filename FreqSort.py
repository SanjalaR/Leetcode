# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
class Solution:
    def frequencySort(self, s: str) -> str:
        c = Counter(s)
        res = ''
        c = c.most_common()
        for i in c:
            for j in range(i[1]):
                res+=i[0]
        return res

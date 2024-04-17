# Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        res = []
        for i in words:
            word = set(i.lower())
            if word.issubset(row1) or word.issubset(row2) or word.issubset(row3):
                res.append(i)
        return res

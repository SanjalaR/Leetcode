# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        done = []
        for i in word:
            if i.swapcase() in word and i.lower() not in done:
                count+=1
                done.append(i.lower())
        return count

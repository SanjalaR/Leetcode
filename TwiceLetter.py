# Given a string s consisting of lowercase English letters, return the first letter to appear twice.
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        s = list(s)
        ind1 = None
        ind2 = -1
        tup_list = []
        for i in range(len(s)):
            ind1 = i
            letter = s[i]
            ind = i+1
            new_list = s[ind: ]
            if letter in new_list:
                ind2 = new_list.index(letter) + i 
            if ind2 != -1:
                tup_list.append((ind1, ind2))
        tup_list.sort(key=lambda x:x[1])
        return s[(tup_list[0])[0]]

            

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
# Qotd 5.2.24

class Solution:
    def firstUniqChar(self, s: str) -> int:
        new_list = list(s)
        for i in range(len(new_list)):
            flag = True
            for j in range(len(new_list)):
                if j!=i:
                    if new_list[i] == new_list[j]:
                        flag = False
                        break
            if flag:
                break
        if not flag:
            return -1

        return i

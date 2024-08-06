class Solution:
    def minimumPushes(self, word: str) -> int:
        letter_counts = [0]*26
        for i in word:
            letter_counts[ord(i)-ord('a')]+=1
        sorted_counts = sorted(letter_counts, reverse=True)
        press = 0
        for i,c in enumerate(sorted_counts):
            if c==0:
                break
            press += (i//8+1)*c
        return press

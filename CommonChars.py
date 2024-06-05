# Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = Counter(words[0])
        for word in words[1:]:
            min_freq &= Counter(word)
        return list(min_freq.elements())
                

# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(' ')
        print(sentence)
        for i in range(len(sentence)):
            for j in dictionary:
                if j in sentence[i][:len(j)]:
                    sentence[i] = j

        return ' '.join(sentence)

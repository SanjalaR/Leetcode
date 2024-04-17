'''You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
'''
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            if operations[i]=='+' and len(res)>=2:
                res.append(res[-1]+res[-2])
            elif operations[i]=='D' and len(res)>=1:
                res.append(res[-1]*2)
            elif operations[i]=='C' and len(res)>=1:
                res.pop()
            else:
                score = int(operations[i])
                res.append(score)

        return sum(res)

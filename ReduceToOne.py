'''
Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:

If the current number is even, you have to divide it by 2.

If the current number is odd, you have to add 1 to it.
'''
class Solution:
    def numSteps(self, s: str) -> int:
        s = int(s, 2)
        step = 0
        while s!=1:
            if s%2 == 0:
                s = s//2
                step += 1
            else:
                s += 1
                step += 1
        return step

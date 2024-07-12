# Return the maximum points you can gain after applying the above operations on s.
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        score = 0
        if y>x:
            top = 'ba'
            top_score = y
            bot = 'ab'
            bot_score = x
        else:
            top = 'ab'
            top_score = x
            bot = 'ba'
            bot_score = y
        stack = []
        for i in s:
            if i==top[1] and stack and stack[-1]==top[0]:
                stack.pop()
                score+=top_score
            else:
                stack.append(i)

        stack2 = []
        for i in stack:
            if i==bot[1] and stack2 and stack2[-1]==bot[0]:
                stack2.pop()
                score+=bot_score
            else:
                stack2.append(i)
        return score
        

# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        ind = []
        for i in s:
            if i=='(':
                ind.append(len(stk))
            elif i==')':
                start = ind.pop()
                stk[start:] = stk[start:][::-1]
            else:
                stk.append(i)
        return "".join(stk)

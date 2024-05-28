# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
class Solution:
    def isValid(self, s: str) -> bool:
        op1 = s.count('(')
        cl1 = s.count(')')
        op2 = s.count('{')
        cl2 = s.count('}')
        op3 = s.count('[')
        cl3 = s.count(']')
        if op1 != cl1 or op2 != cl2 or op3 != cl3:
            return False
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')':
                if not stack or '(' != stack.pop():
                    return False
            elif i == '}':
                if not stack or '{' != stack.pop():
                    return False
            elif i == ']':
                if not stack or '[' != stack.pop():
                    return False
        return True
        

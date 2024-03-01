# Given a string s, return true if it is a palindrome, or false otherwise.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(letter for letter in s if letter.isalnum())
        return s==s[::-1]

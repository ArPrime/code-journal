'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_s = ''
        for char in s:
            if char.isalnum():
                formatted_s += char.lower()
        
        length = len(formatted_s)
        i = 0
        j = length - 1
        for i in range(length//2):
            if formatted_s[i] != formatted_s[j]:
                return False
            j -=1
        return True

sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))
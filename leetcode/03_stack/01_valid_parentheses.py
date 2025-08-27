'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true
'''


class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack:
                    return False
                elif mapping[char] != stack.pop():
                    return False
        return not stack

sol = Solution()
s = "(]"
print(sol.isValid(s))
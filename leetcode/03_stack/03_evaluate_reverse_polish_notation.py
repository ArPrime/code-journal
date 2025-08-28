'''
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
'''

from typing import List
import operator

ops = {
    '+': operator.add,
    '-': operator.sub,  
    '*': operator.mul,
    '/': lambda x, y: int(x / y)
}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char in ops:
                result = ops[char](stack[-2], stack[-1])
                del stack[-2:]
                stack.append(result)
            else:
                stack.append(int(char))

        return stack[-1]
    
sol = Solution()
tokens = ["4","13","5","/","+"]
print(sol.evalRPN(tokens))
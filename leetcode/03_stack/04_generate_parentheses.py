'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''

# using stack
# def generateParenthesis(n):
#     result = []
#     # stack 中存储 (当前字符串, 左括号数, 右括号数)
#     stack = [("", 0, 0)]
    
#     while stack:
#         current, open_count, close_count = stack.pop()
        
#         # 如果长度达到 2n，说明生成完毕
#         if len(current) == 2 * n:
#             result.append(current)
#             continue
        
#         # 可以添加左括号
#         if open_count < n:
#             stack.append((current + "(", open_count + 1, close_count))
        
#         # 可以添加右括号
#         if close_count < open_count:
#             stack.append((current + ")", open_count, close_count + 1))
    
#     return result


# using backtrack

from typing import List

class Solution:
    @staticmethod
    def generateParenthesis(n: int) -> List[str]:
        result = []
        def backtrack(current, open_count, close_count):
            if len(current) == n * 2:
                result.append(current)
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            if open_count > close_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result

# 通过实例调用
sol = Solution()
print(sol.generateParenthesis(3))

# 通过类直接调用
print(Solution.generateParenthesis(3))
'''
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        left = 0
        char_idx = {}
        max_length = 0

        for right, char in enumerate(s):
            if char in char_idx and left <= char_idx[char]:
                left = char_idx[char] + 1
            char_idx[char] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length

print(Solution.lengthOfLongestSubstring("abcabcbb"))
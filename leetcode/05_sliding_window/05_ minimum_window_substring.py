'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
'''


from collections import Counter

class Solution:
    @staticmethod
    def minWindow(s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        
        target_count = Counter(t)
        window_count = Counter()
        left = 0
        min_len = float('inf')
        min_start = 0
        required = len(target_count)
        formed = 0

        for right, char in enumerate(s):
            window_count[char] += 1
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left + 1 < min_len:
                    min_len = right -left + 1
                    min_start = left
                char = s[left]
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                left += 1
        
        return '' if min_len == float('inf') else s[min_start:min_start + min_len]
    
print(Solution.minWindow(s = "ADOBECODEBANC", t = "ABC"))
print(Solution.minWindow(s = "ab", t = "a"))
assert Solution.minWindow(s = "ab", t = "a") == 'a'
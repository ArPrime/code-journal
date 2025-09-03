'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''


from collections import Counter

class Solution:
    @staticmethod
    def checkInclusion(s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        target_count = Counter(s1)
        window_size = len(s1)
        window_count = Counter()

        for i in range(window_size):
            window_count[s2[i]] += 1
        if window_count == target_count:
            return True
        
        left = 0
        for i in range(window_size, len(s2)):
            window_count[s2[i]] += 1
            window_count[s2[left]] -= 1
            if window_count == target_count:
                return True
            left += 1
        return False

print(Solution.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
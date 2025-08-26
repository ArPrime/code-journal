'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
'''


from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_str_to_group = defaultdict(list)
        for string in strs:
            sorted_string = tuple(sorted(string))
            sorted_str_to_group[sorted_string].append(string)

        return list(sorted_str_to_group.values())
    
sol = Solution()
test_list = ['abc', 'acb', '', ' ']
print(sol.groupAnagrams(test_list))
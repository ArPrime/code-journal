# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true


def _count_char(string: str) -> dict:
    char_count = {}
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return _count_char(s) == _count_char(t)

sol = Solution()
word_1, word_2 = 'abcd', 'abdc'
print(sol.isAnagram(word_1, word_2))
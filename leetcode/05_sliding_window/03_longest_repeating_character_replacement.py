'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
'''


from collections import defaultdict
class Solution:
    @staticmethod
    def characterReplacement(s: str, k: int) -> int:
        char_count = defaultdict(int)
        left = 0
        max_freq = 0
        max_length = 0

        for right, char in enumerate(s):
            char_count[char] += 1
            max_freq = max(max_freq, char_count[char])

            window_size = right - left + 1
            if window_size - max_freq > k:
                left_char = s[left]
                char_count[left_char] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)

        return max_length

print(Solution.characterReplacement("ABAB", 2))
assert Solution.characterReplacement("ABAB", 2) == 4
assert Solution.characterReplacement("ABAB", 2) == 5
'''
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode



Example 1:

Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]
'''


# basic syntax for the find() method:
# string.find(substring, start, end)


from typing import List

class Solution:
    @staticmethod
    def encode(strs: List[str]) -> str:
        encoded_str = ''
        for word in strs:
            encoded_str += str(len(word)) + '#' + word
        return encoded_str
    
    @staticmethod
    def decode(s: str) -> List[str]:
        i = 0
        decoded_strs = []
        while i < len(s):
            delimiter_index = s.find('#', i)
            word_length = int(s[i : delimiter_index])
            word = s[delimiter_index+1 : delimiter_index+word_length+1]
            decoded_strs.append(word)
            i = delimiter_index + word_length + 1
        return decoded_strs

sol = Solution()
test_strs = ['I', 'love', 'you']
print(sol.encode(test_strs))
print(sol.decode(sol.encode(test_strs)))
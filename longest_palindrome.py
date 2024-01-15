import re
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        for i in range(len(s)):
            char = s[i]
            next_index = i + 1
            counts = s.count(char, next_index)
            for count in range(counts):
                next_index = s.index(char, next_index) + 1
                sub_str = s[i:next_index]

                if(sub_str == sub_str[::-1] and len(result) < next_index - i):
                    result = sub_str
        return result     

import re
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        
        if(len(word1) != len(word2) or set(word1) != set(word2)):
            return False
   
        freq_1 = []
        freq_2 = []
        for char in set(word1):
            freq_1.append(word1.count(char))
            freq_2.append(word2.count(char))
            
        return sorted(freq_1) == sorted(freq_2)

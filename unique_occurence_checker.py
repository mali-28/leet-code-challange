class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = []
        for i in set(arr):
            count = arr.count(i)
            if count in occurences:
                return False
            occurences.append(count)
        return True
        

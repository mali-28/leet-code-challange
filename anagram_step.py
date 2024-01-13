class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count = 0
        a = {}

        #  create a dictionary that have count against character
        for char in s:
            a[char] = a.get(char, 0) + 1
        #  if key and count > 0 exist then decrement in count otherwise current char need to be replaced
        for char in t:
            if a.get(char, 0):
                a[char] -= 1
            else:
                count += 1

        return count

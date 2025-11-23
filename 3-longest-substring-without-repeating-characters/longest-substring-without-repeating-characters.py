class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        char_set = set()
        l = 0
        result = 0

        for r in range(len(s)): # increment the right side of the string
            while s[r] in char_set: # while we have a duplicate 
                char_set.remove(s[l]) # remove terms from the left side of the string until we have no duplicates
                l +=1
            char_set.add(s[r]) # add the new right term
            result = max(result, r - l + 1) # check if the new substring is longer or shorter
        return result
        
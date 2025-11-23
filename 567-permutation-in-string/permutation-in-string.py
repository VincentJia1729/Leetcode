class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False # we want s2 to be the longer string

        s1_count, s2_count = [0] * 26, [0] * 26 # create empty lists 
        # idea is to store the 26 letters of the alphabet

        for i in range(len(s1)): # iterate through the first couple letters in s2 so that 
            # we have the same number of letters in s2 and s1
            s1_count[ord(s1[i]) - ord('a')] += 1 
            s2_count[ord(s2[i]) - ord('a')] += 1

        matches = 0 # idea is we have 26 matches

        for i in range(26): # 0 to 25 hard-coded because we only use the letters of the alphabet
            matches += (1 if s1_count[i] == s2_count[i] else 0) # Python "ternary operator"
            # "a if condition else b"

        l = 0
        for r in range(len(s1), len(s2)): # to iterate over the rest of elements in s2
            if matches == 26: return True

            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]: # it's +1 because we can only add one character at a time
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]: # it's -1 because we can only remove one character at a time
                matches -= 1
            l += 1
        return matches == 26
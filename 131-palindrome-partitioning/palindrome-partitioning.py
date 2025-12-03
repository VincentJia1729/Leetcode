

class Solution:
    def partition(self, s: str) -> List[List[int]]:

        # if we have "aab", how many elements can we select for our first partition
        # we will select from the front
        # we can select "a", "aa", and "aab"
        # 1. In the case we select "a", we have "ab" left over "a | ab". Then we run partition on "ab"
        # 2. In the case we select "aa", we have "b" left over "aa | b". Then we run partition on "b"
        # 3. In the case we select "aab", we have nothing left over. "aab| ".  
        result = [] # we will return result. result will be a list of lists
        partition = [] # this is a temporary list. We will append "partition" to result when we find a series of valid partitions

        def dfs(i): # is is keeping track of how far we are into the string
            # if we reach the end of the string without being stopped, we have found a valid partition
            if i == len(s): 
                result.append(partition.copy())
                return 
    
            for j in range(i, len(s)): # from 0 to len(s)-1 by how "range" works in Python
                if self.is_palindrome(s, i, j): # when i = 0, and j = 0, "is_palindrome" is still True
                    partition.append(s[i:j+1]) # when i = 0, and j = 0, we append a single character, j+1 is to account for noninclusive string slicing
                    dfs(j+1) 
                    partition.pop()
                    
        dfs(0)
        return result

    
    # let's write the helper function first because it's easier to write (and check)
    # l and r are pointer. Indexed from 0 to n-1 where n is len(s)
    def is_palindrome(self, s, l  ,r):
        while l < r: # notice that when l = 0, and r = 0, we return True
            if s[l] != s[r]:
                return False
            l = l + 1
            r = r - 1
        return True



class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        l = 0 # left pointer
        max_length = len(s1)
        count = defaultdict(int)
        
        substring_count = defaultdict(int)
        
        for ch in s1:
            substring_count[ch] += 1
        
        # add current elements of 
        
        for r in range(len(s2)):
        
            count[s2[r]] +=1
        
            while (r - l + 1) > max_length:
                # decrement the left pointer
                count[s2[l]] -= 1
                if count[s2[l]] == 0: # delete keys when goes to 0
                    del count[s2[l]]  # keep dict clean
                l += 1
        
            if count.items() == substring_count.items():
                return True
        return False
        
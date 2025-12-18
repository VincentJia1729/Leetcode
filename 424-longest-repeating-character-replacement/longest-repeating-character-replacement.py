class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        result = 0
        
        l = 0 # start pointers at 0
        
        
        
        for r in range(len(s)):
            # print(r)
            # r starts at 0 
        
            # add 1 to the count of the letter at "r"
            count[s[r]] +=1
        
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1 # move the left pointer up
        
            result = max(result, r - l + 1)
        return result